# 🧭 Autodiagnóstico de Prontidão Digital

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-lightgrey?logo=flask&logoColor=black)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1234567.svg)](https://doi.org/10.5281/zenodo.1234567)
[![Build Status](https://img.shields.io/badge/Build-Passing-success.svg)]()
[![Made with ❤️ in Brazil](https://img.shields.io/badge/Made%20with%20❤️-Brazil-green)]()

![Python Logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

**Autor:** Guilherme Lopes dos Santos  
**Orientador:** Prof. Dr. Murilo Alvarenga Oliveira  
**Instituição:** Universidade Federal Fluminense (UFF)  
**E-mail:** guilhermels@id.uff.br  

---

## 🎯 Descrição do Projeto

Este repositório apresenta o sistema **“Autodiagnóstico de Prontidão Digital”**, desenvolvido como produto tecnológico da dissertação de mestrado no **Programa de Pós-Graduação em Administração (PPGA/UFF)** em colaboração com a **Universidade Federal de Mato Grosso (UFMT)**.

Inspirado nos conceitos da **Indústria 4.0**, o sistema tem como propósito avaliar o **nível de prontidão digital** de universidades públicas, promovendo decisões estratégicas orientadas por dados e apoiando a transformação digital institucional.

---

## 🧩 Objetivos

- **Propor e validar** um modelo de prontidão digital voltado à gestão universitária.  
- **Desenvolver** uma aplicação web para autodiagnóstico de maturidade digital.  
- **Mensurar e visualizar** os níveis de prontidão digital com base em dimensões de estratégia, processos, tecnologia e infraestrutura.  
- **Oferecer** uma ferramenta escalável e replicável para diferentes instituições públicas.

---

## ⚙️ Arquitetura do Sistema

O sistema foi construído em **arquitetura de três camadas (Frontend, Backend e Banco de Dados)**, baseada no modelo **Client-Server**.

![Arquitetura do Protótipo](https://www.publicdomainpictures.net/pictures/330000/velka/technology-2020-15851520000wf.jpg)
*Fonte: Autoria própria.*

| Camada | Tecnologias | Função Principal |
|:--|:--|:--|
| **Frontend** | HTML5, CSS3, JavaScript, MDB Bootstrap | Interface interativa, responsiva e moderna baseada em Material Design. |
| **Backend** | Python 3.12 + Flask | Processamento lógico, integração com banco e controle de rotas. |
| **Banco de Dados** | SQLite | Armazena respostas dos usuários e resultados do autodiagnóstico. |
| **Hospedagem / IDE** | PythonAnywhere | Plataforma de execução e testes de aplicações Python na nuvem. |

---

## 🧠 Tecnologias Fundamentais

Segundo **Jeon et al. (2019)**, o **SQLite** é um mecanismo leve e eficiente amplamente usado em software embarcado e aplicações locais.  
O **Python**, conforme **Kumar e Panda (2019)**, destaca-se por sua natureza multiparadigma e por fornecer bibliotecas para análise e ciência de dados, enquanto o **Flask**, de acordo com **Mufid et al. (2019)**, oferece um microframework simples e extensível para aplicações web.  
Para a prova de conceito (**PoC**), o Flask viabilizou a prototipagem ágil do sistema, validando a aplicabilidade do modelo de prontidão digital.  
O frontend, desenvolvido com **MDB Bootstrap**, combina a simplicidade do Bootstrap com a sofisticação do Material Design, resultando em uma experiência de usuário rica e responsiva.

---

## 🧪 Prova de Conceito (PoC)

A abordagem **Proof of Concept (PoC)** permitiu verificar a viabilidade técnica do protótipo antes da sua expansão.  
Segundo **Yu et al. (2021)**, o PoC em software tem como foco validar desempenho, usabilidade e confiabilidade em um ambiente controlado, servindo como base para a implementação completa.

---

## 💻 Interfaces do Sistema

### Página Principal (Mobile)
![Figura 4 - Página principal em um celular](https://github.com/user/repo/assets/figura4.png)  
*Fonte: Autoria própria.*

### Página Principal (Notebook)
![Figura 5 - Página principal em um notebook](https://github.com/user/repo/assets/figura5.png)  
*Fonte: Autoria própria.*

### Dashboard Administrativo
![Figura 9 - Tela Administrativa](https://github.com/user/repo/assets/figura9.png)  
*Fonte: Autoria própria.*

---

## 📊 Visualizações e Análises

Os resultados do autodiagnóstico são apresentados através de:

- **Matriz 2x2 de Prontidão Digital (Figura 10):**  
  Adaptação do modelo de **Westerman et al. (2012)**, categorizando as instituições nos níveis *Inicial, Gerenciado, Definido* e *Integrado*.  

- **Gráficos Radar (Figura 11):**  
  Representam as médias por dimensão, destacando forças e fraquezas setoriais.  

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
│   └── questionarios/        # Dados de respostas e testes
│
└── README.md                 # Este arquivo
