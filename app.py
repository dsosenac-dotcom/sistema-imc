import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Sistema de IMC",
    page_icon="💪",
    layout="centered"
)

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

st.markdown("<h1>💪 Sistema de IMC</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaaaaa;'>Login + Cálculo de Índice de Massa Corporal</p>", unsafe_allow_html=True)
st.markdown("---")

# Estados
if "logado" not in st.session_state:
    st.session_state.logado = False
if "historico" not in st.session_state:
    st.session_state.historico = []

# Login
usuario_correto = "Dario"
senha_correta = "1234"

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
            
            # Peso ideal (fórmula simples de Devine)
            peso_ideal = 50 + 0.91 * (altura * 100 - 152.4)
            peso_ideal = round(peso_ideal, 1)
            
            if imc < 18.5:
                classificacao = "Abaixo do peso"
                dica = "Tente aumentar a ingestão calórica com alimentos nutritivos e consulte um nutricionista."
                tipo = "info"
            elif imc < 25:
                classificacao = "Peso normal"
                dica = "Parabéns! Mantenha uma alimentação equilibrada e pratique exercícios regularmente."
                tipo = "success"
            elif imc < 30:
                classificacao = "Sobrepeso"
                dica = "Recomenda-se reduzir o consumo de açúcar e gorduras e aumentar a atividade física."
                tipo = "warning"
            else:
                classificacao = "Obesidade"
                dica = "É importante buscar orientação médica e nutricional para um plano seguro de emagrecimento."
                tipo = "error"
            
            st.markdown("---")
            st.markdown(f"### Resultado de **{nome}**")
            
            c1, c2, c3 = st.columns(3)
            c1.metric("Idade", f"{idade} anos")
            c2.metric("Altura", f"{altura:.2f} m")
            c3.metric("Peso", f"{peso:.1f} kg")
            
            st.metric("Seu IMC", f"{imc:.2f}")
            st.metric("Peso Ideal (aproximado)", f"{peso_ideal} kg")
            
            if tipo == "info":
                st.info(f"📌 Classificação: **{classificacao}**")
            elif tipo == "success":
                st.success(f"📌 Classificação: **{classificacao}**")
            elif tipo == "warning":
                st.warning(f"📌 Classificação: **{classificacao}**")
            else:
                st.error(f"📌 Classificação: **{classificacao}**")
            
            st.markdown("### 💡 Dica de Saúde")
            st.write(dica)
            
            # Diferença para o peso ideal
            diferenca = round(peso - peso_ideal, 1)
            if diferenca > 0:
                st.write(f"Você está **{diferenca} kg** acima do peso ideal.")
            elif diferenca < 0:
                st.write(f"Você está **{abs(diferenca)} kg** abaixo do peso ideal.")
            else:
                st.write("Você está no peso ideal!")
            
            # Histórico
            registro = {
                "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "nome": nome,
                "imc": round(imc, 2),
                "classificacao": classificacao
            }
            st.session_state.historico.append(registro)
        else:
            st.error("Altura inválida")
    
    # Histórico
    if st.session_state.historico:
        st.markdown("---")
        st.subheader("📜 Histórico de Cálculos")
        
        for i, item in enumerate(reversed(st.session_state.historico), 1):
            st.write(f"**{i}.** {item['data']} — {item['nome']} | IMC: **{item['imc']}** ({item['classificacao']})")
        
        if st.button("🗑️ Limpar Histórico"):
            st.session_state.historico = []
            st.rerun()
    
    st.markdown("---")
    if st.button("🚪 Sair"):
        st.session_state.logado = False
        st.rerun()
