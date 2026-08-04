import streamlit as st

st.set_page_config(page_title="Sistema de IMC", page_icon="💪", layout="centered")

st.title("Sistema de Login + Cálculo de IMC")
st.markdown("---")

# Inicializa o estado de login
if "logado" not in st.session_state:
    st.session_state.logado = False

# Dados de login
usuario_correto = "Dario"
senha_correta = "1234"

# ===== TELA DE LOGIN =====
if not st.session_state.logado:
    st.subheader("Login")
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
    st.success("Login realizado com sucesso!")
    st.markdown("---")
    
    st.subheader("Cálculo de IMC")
    
    nome = st.text_input("Seu nome")
    idade = st.number_input("Sua idade", min_value=1, max_value=120, value=25)
    altura = st.number_input("Altura (em metros)", min_value=0.50, max_value=2.50, value=1.75, step=0.01, format="%.2f")
    peso = st.number_input("Peso (em kg)", min_value=20.0, max_value=300.0, value=70.0, step=0.1)
    
    if st.button("Calcular IMC"):
        if altura > 0:
            imc = peso / (altura ** 2)
            
            st.write(f"**Nome:** {nome}")
            st.write(f"**Idade:** {idade} anos")
            st.write(f"**Altura:** {altura:.2f} m")
            st.write(f"**Peso:** {peso:.1f} kg")
            st.metric("Seu IMC", f"{imc:.2f}")
            
            if imc < 18.5:
                st.info("Classificação: Abaixo do peso")
            elif imc < 25:
                st.success("Classificação: Peso normal")
            elif imc < 30:
                st.warning("Classificação: Sobrepeso")
            else:
                st.error("Classificação: Obesidade")
        else:
            st.error("Altura inválida")
    
    st.markdown("---")
    if st.button("Sair"):
        st.session_state.logado = False
        st.rerun()
