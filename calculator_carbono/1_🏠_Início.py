import streamlit as st

# Configuração do estilo
st.markdown('<link rel="stylesheet" href="/styles/style.css">', unsafe_allow_html=True)

# Título da Aplicação
st.title("🌱 Calculadora de Compensação de Carbono 🌱")
st.divider()
st.header("Projeto desenvolvido para cálculo e compensação de emissões de carbono com base em inputs do usuário. 🚗🪫")
st.write("Apresentamos nossa **Calculadora de Compensação de Carbono**, uma ferramenta inovadora desenvolvida para **promover a conscientização ambiental** e facilitar o acesso a informações sobre emissões de carbono e suas formas de compensação.")
st.divider()
st.header("Objetivo da calculadora ➕")
st.write("O projeto combina uma interface amigável desenvolvida com Streamlit e uma lógica de cálculos robusta, estruturada separadamente, permitindo que o usuário insira dados específicos de suas atividades para: ")
st.markdown("""
### Funcionalidades:
- Calcular emissões de gases do efeito estufa (GEE) com base em padrões confiáveis.
- Estimar os créditos de carbono necessários para compensação.
- Obter informações sobre custos financeiros e alternativas sustentáveis.
""")
st.write("Nosso objetivo é tornar a compreensão sobre impacto ambiental mais acessível, incentivando ações práticas e conscientes em prol do meio ambiente. Seja você uma pessoa física ou uma empresa, esta ferramenta é o primeiro passo para contribuir ativamente na preservação do planeta.")
st.divider()
st.subheader("Vamos juntos rumo a um futuro mais sustentável? 🌍")
