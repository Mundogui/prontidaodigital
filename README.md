# 🧭 Autodiagnóstico de Prontidão Digital

![Python Logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

**Autor:** Guilherme Lopes dos Santos  
**Orientador:** Prof. Dr. Murilo Alvarenga Oliveira  
**Instituição:** Universidade Federal Fluminense (UFF)  
**E-mail:** guilhermels@id.uff.br  

---

## 🎯 Descrição do Projeto

Este repositório reúne o **protótipo funcional** e a documentação do sistema **“Autodiagnóstico de Prontidão Digital”**, desenvolvido como parte da dissertação de mestrado no Programa de Pós-Graduação em Administração (PPGA/UFF), em colaboração com a Universidade Federal de Mato Grosso (UFMT).

O projeto foi inspirado nas tecnologias da **Indústria 4.0** e visa avaliar o **nível de prontidão digital** de universidades públicas, apoiando decisões estratégicas para **transformação digital** e integração tecnológica institucional.

---

## 🧩 Objetivos

1. **Propor e validar** um modelo de prontidão digital adaptado à gestão universitária.
2. **Desenvolver** um sistema web interativo de autodiagnóstico.
3. **Mensurar** os níveis de maturidade digital de docentes e técnicos.
4. **Fornecer** uma ferramenta escalável, replicável e acessível a outras instituições.

---

## ⚙️ Arquitetura do Sistema

O sistema foi desenvolvido com uma **arquitetura de três camadas (Frontend, Backend e Banco de Dados)**, conforme o modelo **Client-Server**.

![Arquitetura do Protótipo](https://www.publicdomainpictures.net/pictures/330000/velka/technology-2020-15851520000wf.jpg)
*Fonte: Autoria própria.*

- **Frontend:** Interface web responsiva construída com **HTML**, **CSS**, **JavaScript** e **MDB Bootstrap**, combinando o **Material Design da Google** com os componentes do **Bootstrap**.
- **Backend:** Desenvolvido em **Python** com o **microframework Flask**, responsável pelo roteamento, lógica de negócios e integração com o banco de dados.
- **Banco de Dados:** Utiliza o **SQLite**, projetado para armazenar eficientemente as respostas dos questionários submetidos pelos usuários (Jeon et al., 2019).

---

## 🧠 Tecnologias Utilizadas

| Camada | Tecnologia | Descrição |
|:--------|:-------------|:------------|
| **Banco de Dados** | SQLite | Leve, eficiente e amplamente usado em dispositivos embarcados e aplicações locais (Jeon et al., 2019). |
| **Backend** | Python + Flask | Plataforma multiparadigma ideal para aplicações científicas e web (Kumar & Panda, 2019; Mufid et al., 2019). |
| **Frontend** | MDB Bootstrap | Combina o poder do Bootstrap com a estética do Material Design, garantindo responsividade e usabilidade. |
| **IDE / Hospedagem** | PythonAnywhere | Ambiente para execução e testes de aplicações Python na nuvem. |

---

## 🧪 Prova de Conceito (PoC)

O **Flask** foi adotado pela sua simplicidade e flexibilidade para o desenvolvimento rápido de um **Proof of Concept (PoC)**.  
Segundo Yu et al. (2021), uma PoC demonstra a viabilidade técnica de um protótipo, permitindo validar funcionalidades e interações antes da implantação final.

---

## 💻 Interfaces do Sistema

- **Página Principal (Mobile):**  
  ![Figura 4 - Página principal em um celular](https://github.com/user/repo/assets/figura4.png)  
  *Fonte: Autoria própria.*

- **Página Principal (Notebook):**  
  ![Figura 5 - Página principal em um notebook](https://github.com/user/repo/assets/figura5.png)  
  *Fonte: Autoria própria.*

- **Dashboard Administrativo:**  
  ![Figura 9 - Tela Administrativa](https://github.com/user/repo/assets/figura9.png)  
  *Fonte: Autoria própria.*

---

## 📊 Visualizações e Gráficos

Os resultados do autodiagnóstico são apresentados em múltiplas formas visuais, permitindo interpretação detalhada da **maturidade digital institucional**.

- **Matriz 2x2 de Prontidão Digital (Figura 10)**  
  Representa a classificação dos respondentes em quatro níveis: *Inicial, Gerenciado, Definido e Integrado* (Westerman et al., 2012).

- **Gráfico Radar (Figura 11)**  
  Exibe a média das respostas por dimensão, evidenciando forças e fraquezas setoriais.

![Dashboards e Visualizações](https://upload.wikimedia.org/wikipedia/commons/a/ae/Digital_transformation.webp)

---

## 📂 Estrutura do Repositório

```bash
autodiagnostico-prontidao-digital/
│
├── src/
│   ├── app.py                # Backend Flask
│   ├── static/               # CSS, JS e imagens
│   ├── templates/            # Páginas HTML (Jinja2)
│   └── database/             # Base SQLite
│
├── data/
│   └── questionarios/        # Arquivos de coleta (CSV / JSON)
│
└── README.md                 # Este arquivo



![Modelo de Prontidão Digital](https://www.publicdomainpictures.net/pictures/560000/velka/digitale-transformation-1703238796NiE.jpg)
