from flask import Flask, request, url_for, redirect
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
from flask import render_template
import base64
from io import BytesIO
import plotly.express as px



# Inicialize o aplicativo Flask
app = Flask(__name__)

# Conectar ao banco de dados (isso criará um novo arquivo de banco de dados se não existir)
conn = sqlite3.connect('respostas.db')
cursor = conn.cursor()

# Criar a tabela para armazenar as respostas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS respostas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email VARCHAR,
        tempo VARCHAR,
        setor VARCHAR,
        tipo_usuario VARCHAR,
        estrategia1 INTEGER,
        estrategia2 INTEGER,
        estrategia3 INTEGER,
        estrategia4 INTEGER,
        estrategia5 INTEGER,
        estrategia6 INTEGER,
        processo1 INTEGER,
        processo2 INTEGER,
        processo3 INTEGER,
        processo4 INTEGER,
        processo5 INTEGER,
        processo6 INTEGER,
        infra1 INTEGER,
        infra2 INTEGER,
        infra3 INTEGER,
        infra4 INTEGER,
        infra5 INTEGER,
        infra6 INTEGER,
        tec1 INTEGER,
        tec2 INTEGER,
        tec3 INTEGER,
        tec4 INTEGER,
        tec5 INTEGER,
        tec6 INTEGER
    )
''')

# Salvar as alterações e fechar a conexão
conn.commit()
conn.close()

def determine_level(sum_y, sum_x):
    """
    Determina o nível da organização com base nas coordenadas.
    """
    if 0 <= sum_y <= 60 and 0 <= sum_x <= 60:
        return 'Inicial'
    elif 0 <= sum_y <= 60 and 61 <= sum_x <= 120:
        return 'Gerenciado'
    elif 61 <= sum_y <= 120 and 0 <= sum_x <= 60:
        return 'Definido'
    elif 61 <= sum_y <= 120 and 61 <= sum_x <= 120:
        return 'Integrado'

def generate_plot(sum_y, sum_x):
    """
    Gera um gráfico cartesiano e retorna a imagem codificada em base64.
    """
    plt.plot([0, 120], [60, 60], 'k--', linewidth=1)  # Linha horizontal
    plt.plot([60, 60], [0, 120], 'k--', linewidth=1)  # Linha vertical
    plt.scatter(sum_x, sum_y, color='red', marker='o')
    plt.title('Matriz de Prontidão Digital')
    plt.xlim(0, 120)
    plt.ylim(0, 120)
    plt.xlabel('Infraestrutura e Tecnologia')
    plt.ylabel('Estratégia e Processo')
    plt.grid(True)

    # Converter o gráfico em base64
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    plt.close()

    # Codificar em base64 e retornar como string
    encoded_image = base64.b64encode(image_stream.getvalue()).decode('utf-8')

    return encoded_image

def fetch_data_from_database():
    conn = sqlite3.connect('respostas.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM respostas')
    responses = cursor.fetchall()

    conn.close()

    return responses

def calculate_frequencies(responses):
    # Inicialize uma lista de frequências para cada categoria de resposta
    frequencies = [[0] * 11 for _ in range(24)]

    # Itere sobre as respostas e conte as frequências
    for response in responses:
        for i in range(24):
            answer = response[i + 5]  # As respostas começam no índice 5 da tupla
            frequencies[i][answer] += 1

    return frequencies


# Rota para a página principal (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a página admin (admin.html)
@app.route('/admin')
def admin():
    return render_template('admin.html')

# Rota para o arquivo CSS
@app.route('/static/css/style.css')
def style():
    return send_from_directory('static/css', 'style.css')

# Rota para o arquivo JavaScript
@app.route('/static/js/script.js')
def script():
    return send_from_directory('static/js', 'script.js')

# Rota para o Grafico de Distribuição
@app.route('/distribution_chart', methods=['GET'])
def distribution_chart():
    responses = fetch_data_from_database()
    frequencies = calculate_frequencies(responses)

    # Certifique-se de que frequencies seja uma lista bidimensional
    assert all(isinstance(row, list) for row in frequencies), "Frequencies should be a 2D list"

    category_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    labels = [
            'ComunicE1', 'ServNuvemE2', 'AutomSisE3', 'GerPatPropE4', 'TransfDigE5',
            'EspInfraDadE6', 'ColetDadosP7', 'ProcAutomP8', 'ProcPersExP9', 'ProcInfoP10',
            'RealVirtP11', 'ProcAprendP12', 'InfraTiSisI13', 'InfServNuvI14', 'Imp3DAtivI15',
            'PlanImpSegI16', 'InfraIotI17', 'InfraAiI18', 'AutoProcT19', 'TecI4.0T20',
            'TecSegT21', 'CapHumT22', 'AlunDadosT23', 'AccesVelT24'
        ]

    # Converta frequencies para um array numpy
    data = np.array(frequencies)

    data_cum = data.cumsum(axis=1)
    category_colors = plt.colormaps['RdYlGn'](np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.max(np.sum(data, axis=1)))

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color)

        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        ax.bar_label(rects, label_type='center', color=text_color)

    # Adicione a legenda diretamente ao gráfico usando ax.legend
    ax.legend(title='Legenda', bbox_to_anchor=(1, 1), loc='upper left')


    # Converta a imagem para base64
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    plt.close()
    encoded_image = base64.b64encode(image_stream.getvalue()).decode('utf-8')

    # Renderizar a página com o gráfico incorporado
    return render_template('distribution_chart_embedded.html', encoded_image=encoded_image)


# Página com o formulário de questionário
@app.route('/questionario', methods=['GET', 'POST'])
def questionario():
    if request.method == 'POST':
        if request.form.get('generate_all'):
            return redirect(url_for('generate_all_graph'))
        else:
            # Lógica para calcular as somas e determinar o nível da organização vai aqui
            # ...

            # Obtenha os dados do formulário
            email = request.form.get('email')
            tempo = request.form.get('tempo')
            setor = request.form.get('setor')
            tipo_usuario = request.form.get('tipo_usuario')

            # Obtenha as respostas do formulário
            estrategia = [int(request.form[f'estrategia{i}']) for i in range(1, 7)]
            processo = [int(request.form[f'processo{i}']) for i in range(1, 7)]
            infra = [int(request.form[f'infra{i}']) for i in range(1, 7)]
            tec = [int(request.form[f'tec{i}']) for i in range(1, 7)]

            # Conectar ao banco de dados
            conn = sqlite3.connect('respostas.db')
            cursor = conn.cursor()

            # Inserir os dados na tabela respostas
            cursor.execute('''
                INSERT INTO respostas (
                    email, tempo, setor, tipo_usuario,
                    estrategia1, estrategia2, estrategia3, estrategia4, estrategia5, estrategia6,
                    processo1, processo2, processo3, processo4, processo5, processo6,
                    infra1, infra2, infra3, infra4, infra5, infra6,
                    tec1, tec2, tec3, tec4, tec5, tec6
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (email, tempo, setor, tipo_usuario, *estrategia, *processo, *infra, *tec))

            # Salvar as alterações
            conn.commit()

            # Fechar a conexão
            conn.close()

            # Calcule as somas para os eixos x e y
            sum_estrategia = sum(estrategia)
            sum_processo = sum(processo)
            sum_infra = sum(infra)
            sum_tec = sum(tec)

            sum_y = sum_estrategia + sum_processo
            sum_x = sum_infra + sum_tec

            level = determine_level(sum_y, sum_x)
            plot_image = generate_plot(sum_y, sum_x)

            return render_template('result.html', level=level, plot_image=plot_image)

    # Se for um pedido GET, renderize o formulário
    return render_template('questionario.html')

# Rota para o link externo
@app.route('/external_link', methods=['GET', 'POST'])
def external_link():
    # Substitua 'SEU_LINK_EXTERN0' pelo link desejado
    external_file_path = 'inicial.pdf'  # Caminho relativo ao diretório 'static'
    return redirect(url_for('static', filename=external_file_path, _external=True))

# Rota para o link externo Gerenciado
@app.route('/external_link2', methods=['GET', 'POST'])
def external_link2():
    # Substitua 'SEU_LINK_EXTERN0' pelo link desejado
    external_file_path = 'gerenciado.pdf'  # Caminho relativo ao diretório 'static'
    return redirect(url_for('static', filename=external_file_path, _external=True))

# Rota para o link externo Gerenciado
@app.route('/external_link3', methods=['GET', 'POST'])
def external_link3():
    # Substitua 'SEU_LINK_EXTERN0' pelo link desejado
    external_file_path = 'definido.pdf'  # Caminho relativo ao diretório 'static'
    return redirect(url_for('static', filename=external_file_path, _external=True))

# Rota para o link externo Gerenciado
@app.route('/external_link4', methods=['GET', 'POST'])
def external_link4():
    # Substitua 'SEU_LINK_EXTERN0' pelo link desejado
    external_file_path = 'integrado.pdf'  # Caminho relativo ao diretório 'static'
    return redirect(url_for('static', filename=external_file_path, _external=True))

# Rota para gerar o gráfico com todas as respostas
@app.route('/generate_all_graph', methods=['GET'])
def generate_all_graph():
    # Conectar ao banco de dados
    conn = sqlite3.connect('respostas.db')
    cursor = conn.cursor()

    # Obter todas as respostas do banco de dados
    cursor.execute('SELECT * FROM respostas')
    all_responses = cursor.fetchall()

    # Fechar a conexão
    conn.close()

    # Inicializar listas para armazenar as coordenadas dos pontos
    sum_y_values = []
    sum_x_values = []

    # Processar as respostas e calcular as coordenadas
    for response in all_responses:
        sum_estrategia = sum(response[5:11])
        sum_processo = sum(response[11:17])
        sum_infra = sum(response[17:23])
        sum_tec = sum(response[23:])

        # Calcule as somas para os eixos x e y
        sum_y = sum_estrategia + sum_processo
        sum_x = sum_infra + sum_tec

        # Imprima as coordenadas do ponto de interseção
        print(sum_y, sum_x)

        sum_y_values.append(sum_y)
        sum_x_values.append(sum_x)

    # Gere o gráfico
    plt.plot([0, 120], [60, 60], 'k--', linewidth=1)  # Linha horizontal
    plt.plot([60, 60], [0, 120], 'k--', linewidth=1)  # Linha vertical
    plt.scatter(sum_x_values, sum_y_values, color='blue', marker='o')

    plt.title('Matriz de Prontidão Digital - Todas as Respostas')
    plt.xlim(0, 120)
    plt.ylim(0, 120)
    plt.xlabel('Infraestrutura + Tecnologia')
    plt.ylabel('Estratégia + Processo')
    plt.grid(True)

    # Converter o gráfico em base64
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    plt.close()

    # Codificar em base64 e retornar como string
    encoded_image = base64.b64encode(image_stream.getvalue()).decode('utf-8')

    # Renderizar a página de resultado com o gráfico
    return render_template('result_total.html', plot_image=encoded_image)


#Grafico Radar
@app.route('/radar_chart/<setor>', methods=['GET'])
def radar_chart(setor):
    # Conectar ao banco de dados
    conn = sqlite3.connect('respostas.db')
    cursor = conn.cursor()

    # Obter respostas específicas para o setor do banco de dados
    cursor.execute("SELECT * FROM respostas WHERE setor = ?", (setor,))
    sector_responses = cursor.fetchall()

    # Fechar a conexão
    conn.close()

    # Inicializar listas para armazenar as somas das pontuações para cada questão
    question_sums = [0] * 24

    # Processar as respostas e calcular as somas das pontuações para cada questão
    for response in sector_responses:
        for i in range(24):
            question_sums[i] += response[i + 5]  # As respostas começam no índice 5 da tupla

    # Garantir que o número de respostas seja maior que zero antes de calcular a média
    num_responses = len(sector_responses)
    has_responses = num_responses > 0

    # Calcular a média das pontuações para cada questão
    values = [sum_points / num_responses for sum_points in question_sums] if has_responses else [0] * 24

    # Especificar manualmente as 24 categorias
    categories = [
            'ComunicE1', 'ServNuvemE2', 'AutomSisE3', 'GerPatPropE4', 'TransfDigE5',
            'EspInfraDadE6', 'ColetDadosP7', 'ProcAutomP8', 'ProcPersExP9', 'ProcInfoP10',
            'RealVirtP11', 'ProcAprendP12', 'InfraTiSisI13', 'InfServNuvI14', 'Imp3DAtivI15',
            'PlanImpSegI16', 'InfraIotI17', 'InfraAiI18', 'AutoProcT19', 'TecI4.0T20',
            'TecSegT21', 'CapHumT22', 'AlunDadosT23', 'AccesVelT24'
        ]


    # Criar o gráfico de radar usando Plotly Express
    fig = px.line_polar(r=values + [values[0]], theta=categories + [categories[0]], line_close=True,
                        title=f'Gráfico Radar - {setor}', range_r=[0, 10],
                        color_discrete_sequence=px.colors.qualitative.Set1)

    # Ajustar o tamanho do gráfico diretamente na chamada de update_layout
    fig.update_layout(width=900, height=900)

    # Adicionar uma cor a linha que passa pelas notas (neste caso, branco)
    fig.update_polars(radialaxis=dict(gridcolor='white'))


    # Adicionar as instruções para alterar a cor da linha que marca as notas
    fig.update_traces(line=dict(color='blue', dash='solid', width=3))  # Substitua 'blue' pela cor desejada

    # Adicionar as instruções para alterar a cor de fundo do gráfico (exemplo: lightgray, cinza)
    # fig.update_layout(polar=dict(bgcolor='lightblue'))  # Substitua 'lightgray' pela cor desejada


    # Adicionar as instruções para alterar a cor da linha que marca a borda superior da polar
    fig.update_layout(
        polar=dict(
            angularaxis=dict(
                linecolor='white',  # Cor da linha da borda polar
                linewidth=4,  # Largura da linha da borda polar
            )
        )
    )

    # Salvar a imagem em BytesIO
    image_stream = BytesIO()
    fig.write_image(image_stream, format='png')

    # Codificar em base64 e retornar como string
    encoded_image = base64.b64encode(image_stream.getvalue()).decode('utf-8')

    # Renderizar a página com o gráfico de radar incorporado
    return render_template('radar_chart.html', encoded_image=encoded_image, setor=setor)



# Execute o aplicativo
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
