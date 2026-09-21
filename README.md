# 🏋️ Sistema de IMC

Aplicação web simples para **login de usuários** e **cálculo do Índice de Massa Corporal (IMC)**. Interface limpa, com persistência local em SQLite, construída com **Python + Streamlit**.

> Projeto desenvolvido como estudo de Python, autenticação básica, banco de dados SQLite e construção de interfaces web com Streamlit.

---

## 🖼️ Preview

*Em breve — print da aplicação em execução.*

---

## ✨ Funcionalidades

- 🔐 **Login de usuários** com autenticação local
- ⚖️ **Cálculo automático do IMC** a partir de peso e altura
- 💾 **Banco de dados SQLite** para persistência dos usuários e (opcionalmente) histórico de cálculos
- 🎨 **Interface estilizada** com CSS customizado in-line
- 📱 Layout centralizado, pronto para rodar em qualquer navegador

---

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

- **Python 3**
- **Streamlit** — interface web rápida para apps de dados
- **SQLite3** — banco de dados leve, baseado em arquivo
- **Datetime** — registro de data/hora
- **HTML + CSS** in-line para estilização

---

## 📂 Estrutura do projeto

```
sistema-imc/
├── .devcontainer/       # Configuração do ambiente de desenvolvimento
├── app.py               # Código principal da aplicação (Streamlit)
├── requirements.txt     # Dependências Python
└── README.md            # Este arquivo
```

---

## 🚀 Como rodar

### Pré-requisitos
- Python 3.8 ou superior
- pip instalado

### Passo a passo

1. **Clone o repositório**
   ```bash
   git clone https://github.com/dsosenac-dotcom/sistema-imc.git
   cd sistema-imc
   ```

2. **Crie um ambiente virtual (opcional, recomendado)**
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/Mac
   venv\Scripts\activate         # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação**
   ```bash
   streamlit run app.py
   ```

5. **Acesse no navegador**
   ```
   http://localhost:8501
   ```

> O banco SQLite é criado automaticamente na primeira execução.

---

## 📖 O que é o IMC?

O **Índice de Massa Corporal (IMC)** é uma fórmula que relaciona peso e altura para classificar o estado nutricional de adultos:

$$IMC = \frac{peso\ (kg)}{altura^2\ (m)}$$

| Faixa | Classificação |
|---|---|
| Abaixo de 18,5 | Magreza |
| 18,5 – 24,9 | Normal |
| 25,0 – 29,9 | Sobrepeso |
| 30,0 – 34,9 | Obesidade Grau I |
| 35,0 – 39,9 | Obesidade Grau II |
| ≥ 40,0 | Obesidade Grau III |

---

## 👤 Autor

**Dario Oliveira** — Dev Full Stack & Educador em Tecnologia

- 💼 [LinkedIn](https://www.linkedin.com/)
- 🐙 [GitHub](https://github.com/dsosenac-dotcom)

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

<sub>⭐️ Se este projeto te ajudou de alguma forma, considere dar uma estrela no repositório.</sub>
