import streamlit as st

st.title("Histórico de Compensações 🌳")

# Inicializa o session state das compensações
if 'compensacao_veiculo' not in st.session_state:
  st.session_state['compensacao_veiculo'] = []  
if 'compensacao_energia' not in st.session_state:
  st.session_state['compensacao_energia'] = []

# Gera um historico do consumo de energia   
def gerar_relatorio_veiculo(calculos):
    if calculos:
        st.header("Veículos 🚗")

        # Criar uma tabela para exibir os cálculos
        for i, calc in enumerate(calculos, start=1):
            st.write(f"- Veículo: {calc['item']}")
            if calc['distancia'] == 1:
                st.write(f"- Distância percorrida: {calc['distancia']} quilômetro")
            else:
                st.write(f"- Distância percorrida: {calc['distancia']} quilômetros")
            st.write(f"- Emissão de CO₂: {calc['emissao']} KG")
            st.write(f"- Forma de compensação: {calc['compensacao']}")
            st.write(f"- Valor do Investimento: R${calc['investimento']}")
            st.write("---")  # Separador entre cálculos
    else:
        st.write("Nenhum cálculo de veículo realizado até o momento.") 

gerar_relatorio_veiculo(st.session_state['compensacao_veiculo'])


# Gera um historico dos veiculos e emissoes
def gerar_relatorio_energia(calculos):
    if calculos:
        st.header("Energia 🪫")

        # Criar uma tabela para exibir os cálculos
        for i, calc in enumerate(calculos, start=1):
            st.write(f"- Matriz Energética: {calc['matriz']}")
            st.write(f"- kWh consumido: {calc['consumo']}")
            st.write(f"- Forma de compensação: {calc['compensacao']}")
            st.write(f"- Valor do Investimento: R${calc['investimento']}")
            st.write("---")  # Separador entre cálculos
    else:
        st.write("Nenhum cálculo de energia realizado até o momento.")

gerar_relatorio_energia(st.session_state['compensacao_energia'])     


# Limpar as listas
if st.session_state['compensacao_veiculo'] or st.session_state['compensacao_energia']:
    if (st.button("Limpar cálculos")):
        st.session_state['compensacao_veiculo'] = []
        st.session_state['compensacao_energia'] = []