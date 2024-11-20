import streamlit as st
import matplotlib.pyplot as plt

# Inicializa 'calculos' no session_state se ainda não existir
if 'calculos' not in st.session_state:
    st.session_state['calculos'] = []
if 'calculos_de_consumo' not in st.session_state:
    st.session_state['calculos_de_consumo'] = []

# Função para atualizar e exibir o gráfico
def atualizar_grafico():
    st.title("Análise de Dados 📊")

    # Verifica se há cálculos armazenados
    if st.session_state['calculos']:
        # Limpa o gráfico anterior
        plt.clf()

        # Extrai os dados para o gráfico
        tipos_de_veiculos = [
            f"{i['tipo_veiculo']} - {i['potencia']} ({i['combustivel']})"
            for i in st.session_state['calculos']
        ]
        emissao_valores = [
            float(i['emissao']) for i in st.session_state['calculos']
        ]


        st.header("Resultados de Veículos")
        # Cria o gráfico
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(tipos_de_veiculos, emissao_valores, color='blue')
        ax.set_title('Emissões de CO₂ por Tipo de Veículo')
        ax.set_xlabel('Tipo de Veículo')
        ax.set_ylabel('Emissão de CO₂ (kg)')
        ax.tick_params(axis='x', rotation=45)
        plt.tight_layout()

        # Exibe o gráfico no Streamlit
        st.pyplot(fig)
    else:
        st.write("Nenhum cálculo de veículo realizado até o momento.")
    
    if st.session_state['calculos_de_consumo']:
        # Limpa o gráfico anterior
        plt.clf()

        # Extrai os dados para o gráfico
        tipos_de_matriz = [
            f"{i['matriz']} - {i['consumokWh']} kWh"
            for i in st.session_state['calculos_de_consumo']
        ]
        emissao_valores = [
            float(i['emissao']) for i in st.session_state['calculos_de_consumo']
        ]


        st.header("Resultados de Consumo Energético")
        # Cria o gráfico
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(tipos_de_matriz, emissao_valores, color='grey')
        ax.set_title('Emissões de CO₂ por Tipo de Matriz')
        ax.set_xlabel('Tipo de Matriz')
        ax.set_ylabel('Emissão de CO₂ (kg)')
        ax.tick_params(axis='x', rotation=45)
        plt.tight_layout()

        # Exibe o gráfico no Streamlit
        st.pyplot(fig)
    
    else:
        st.write("Nenhum cálculo de veículo realizado até o momento.")

atualizar_grafico()

# Botão para limpar os cálculos
if st.session_state['calculos'] or st.session_state['calculos_de_consumo']:
    if (st.button("Limpar cálculos")):
        st.session_state['calculos'] = []
        st.session_state['calculos_de_consumo'] = []
    
