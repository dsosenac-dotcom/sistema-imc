import streamlit as st
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="Sistema de IMC",
    page_icon="💪",
    layout="centered"
)

# CSS personalizado
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        height: 3em;
    }
    .stButton>button:hover {
        background-color: #45a049;
        color: white;
    }
    h1 {
        text-align: center;
        color: #4CAF50;
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown("<h1>💪 Sistema de IMC</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaaaaa;'>Login + Cálculo de Índice de Massa Corporal</p>", unsafe_allow_html=True)
st.markdown("---")

# Inicializa estados
if "logado" not in st.session_state:
    st.session_state.logado = False
if "historico" not in st.session_state:
    st.session_state.historico = []

# Dados de login
usuario_correto = "Dario"
senha_correta
