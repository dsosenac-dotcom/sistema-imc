import streamlit as st
import sqlite3
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

# ===== FUNÇÕES DO BANCO DE DADOS =====
def criar_banco():
    conn = sqlite3.connect("imc.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS historico (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            nome TEXT,
            idade INTEGER,
            altura REAL,
            peso REAL,
            imc REAL,
            classificacao TEXT
        )
    """)
    conn.commit()
    conn.close()

def salvar_historico(nome, idade, altura, peso, imc, classificacao):
    conn = sqlite3.connect("imc.db")
    cursor = conn.cursor()
    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    cursor.execute("""
        INSERT INTO historico (data, nome, idade, altura, peso, imc, classificacao)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (data, nome, idade, altura, peso, imc, classificacao))
    conn.commit()
    conn.close()

def carregar_historico():
    conn = sqlite3.connect("imc.db")
    cursor = conn.cursor()
    cursor.execute("SELECT data, nome, imc, classificacao FROM historico ORDER BY id DESC LIMIT 10")
    dados = cursor.fetchall()
    conn.close()
    return dados

def limpar_historico():
    conn = sqlite3.connect("imc.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM historico")
    conn.commit()
    conn.close()

# Cria o banco na primeira execução
criar_banco()

# ===== LOGIN =====
if "logado" not in st.session_state:
    st.session_state.logado = False

usuario_correto = st.secrets["credentials"]["usuario"]
senha_correta = st.secrets["credentials"]["senha"]

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
            peso_ideal = round(50 + 0.91 * (altura * 100 - 152.4), 1)
            
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
            
            # Salva no banco
            salvar_historico(nome, idade, altura, peso, round(imc, 2), classificacao)
            
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
            
            diferenca = round(peso - peso_ideal, 1)
            if diferenca > 0:
                st.write(f"Você está **{diferenca} kg** acima do peso ideal.")
            elif diferenca < 0:
                st.write(f"Você está **{abs(diferenca)} kg** abaixo do peso ideal.")
            else:
                st.write("Você está no peso ideal!")
        else:
            st.error("Altura inválida")
    
    # Histórico do banco
    st.markdown("---")
    st.subheader("📜 Histórico de Cálculos (Banco de Dados)")
    
    historico = carregar_historico()
    
    if historico:
        for i, item in enumerate(historico, 1):
            st.write(f"**{i}.** {item[0]} — {item[1]} | IMC: **{item[2]}** ({item[3]})")
        
        if st.button("🗑️ Limpar Histórico"):
            limpar_historico()
            st.rerun()
    else:
        st.write("Nenhum cálculo registrado ainda.")
    
    st.markdown("---")
    if st.button("🚪 Sair"):
        st.session_state.logado = False
        st.rerun()
