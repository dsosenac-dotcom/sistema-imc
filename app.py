import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Sistema de IMC",
    page_icon="💪",
    layout="centered"
)

# CSS personalizado para deixar mais bonito
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
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

# Título principal
st.markdown("<h1>💪 Sistema de IMC</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaaaaa;'>Login + Cálculo de Índice de Massa Corporal</p>", unsafe_allow_html=True)
st.markdown("---")

# Inicializa o estado de login
if "logado" not in st.session_state:
    st.session_state.logado = False

# Dados de login
usuario_correto = "Dario"
senha_correta = "1234"

# ===== TELA DE LOGIN =====
if not st.session_state.logado:
    st.subheader("🔐 Login")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        
        if st.button("Entrar"):
            if usuario == usuario_correto and senha == senha_correta:
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Usuário ou senha incorretos!")

# ===== TELA DEPOIS DO LOGIN =====
else:
    st.success("✅ Login realizado com sucesso!")
    st.markdown("---")
    
    st.subheader("📊 Cálculo de IMC")
    
    nome = st.text_input("Seu nome", value="Dario")
    
    col1, col2 = st.columns(2)
    with col1:
        idade = st.number_input("Sua idade", min_value=1, max_value=120, value=47)
        altura = st.number_input("Altura (metros)", min_value=0.50, max_value=2.50, value=1.70, step=0.01, format="%.2f")
    with col2:
        peso = st.number_input("Peso (kg)", min_value=20.0, max_value=300.0, value=82.0, step=0.1)
    
    if st.button("Calcular IMC"):
        if altura > 0:
            imc = peso / (altura ** 2)
            
            st.markdown("---")
            st.markdown(f"### Resultado de **{nome}**")
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Idade", f"{idade} anos")
            col2.metric("Altura", f"{altura:.2f} m")
            col3.metric("Peso", f"{peso:.1f} kg")
            
            st.metric("Seu IMC", f"{imc:.2f}")
            
            if imc < 18.5:
                st.info("📌 Classificação: **Abaixo do peso**")
            elif imc < 25:
                st.success("📌 Classificação: **Peso normal**")
            elif imc < 30:
                st.warning("📌 Classificação: **Sobrepeso**")
            else:
                st.error("📌 Classificação: **Obesidade**")
        else:
            st.error("Altura inválida")
    
    st.markdown("---")
    if st.button("🚪 Sair"):
        st.session_state.logado = False
        st.rerun()
