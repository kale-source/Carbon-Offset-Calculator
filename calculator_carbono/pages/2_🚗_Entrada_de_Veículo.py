import streamlit as st
from functions.emissao_carbono import *

# Inicializa o session state se não existir
if 'calculos' not in st.session_state:
    st.session_state['calculos'] = []  # Inicializar com lista vazia se ainda não existir

# Função para mostrar inputs e realizar cálculos
def mostrar_input():
    st.title("Entrada de Veículo 🚗")

    # Seleção do tipo de veículo
    tipo_veiculo = st.selectbox("Selecione o tipo de veículo:", ["Carro", "Moto", "Caminhão"], key="tipo_veiculo")
    
    # Placeholder para entradas adicionais com base no tipo de veículo
    if tipo_veiculo == "Carro":
        potencia = st.selectbox("Potência do Motor:", ["1.0 a 1.2", "1.4 a 1.6", "1.8 a 2.0", "Acima de 2.0"], key="potencia")
        tipo_combustivel = st.selectbox("Tipo de combustível:", [
            "Gasolina", 
            "Diesel", 
            "Etanol"
        ], key="tipo_combustivel")

        km_percorrido = st.number_input("Distância percorrida em km:", min_value=1, key="km_percorrido")

        if km_percorrido > 0:
            if st.button("Calcular", key="calcular_button"):
                # Cálculo da emissão
                resultado = emissoesVeiculos(km_percorrido, potencia, tipo_combustivel)
                
                # Armazenar o resultado com informações detalhadas no session state
                st.session_state['calculos'].append({
                    'tipo_veiculo': tipo_veiculo,
                    'potencia': potencia,
                    'combustivel': tipo_combustivel,
                    'emissao': resultado,
                    'distancia': km_percorrido
                })

                st.write(f"Emissão: {resultado} KG de CO₂")
                st.success("Cálculo realizado! Visualize o histórico de cálculos e a análise de dados nos menus ao lado.")

        else:
            st.warning("Distância precisa ser maior que zero!")
    
    elif tipo_veiculo == "Moto":
        potencia = st.selectbox("Potência do Motor:", ["125 a 150 cilindradas", "250 a 300 cilindradas", "Acima de 300 cilindradas"], key="potencia")
        tipo_combustivel = st.selectbox("Tipo de combustível:", [
            "Gasolina", 
            "Diesel", 
            "Etanol"
        ], key="tipo_combustivel")

        km_percorrido = st.number_input("Distância percorrida em km:", min_value=1, key="km_percorrido")

        if km_percorrido > 0:
            if st.button("Calcular", key="calcular_button"):
                # Cálculo da emissão
                resultado = emissoesVeiculos(km_percorrido, potencia, tipo_combustivel)
                
                # Armazenar o resultado com informações detalhadas no session state
                st.session_state['calculos'].append({
                    'tipo_veiculo': tipo_veiculo,
                    'potencia': potencia,
                    'combustivel': tipo_combustivel,
                    'emissao': resultado,
                    'distancia': km_percorrido
                })

                st.write(f"Emissão: {resultado} KG de CO₂")
                st.success("Cálculo realizado! Visualize o histórico de cálculos e a análise de dados nos menus ao lado.")

        else:
            st.warning("Distância precisa ser maior que zero!")
    
    elif tipo_veiculo == "Caminhão":
        potencia = st.selectbox("Potência do Motor:", ["Caminhão Leve", "Caminhão Médio", "Caminhão Pesado"], key="potencia")
        tipo_combustivel = st.selectbox("Tipo de combustível:", [
            "Gasolina", 
            "Diesel", 
            "Etanol"
        ], key="tipo_combustivel")
        
        km_percorrido = st.number_input("Distância percorrida em km:", min_value=1, key="km_percorrido")

        if km_percorrido > 0:
            if st.button("Calcular", key="calcular_button"):
                # Cálculo da emissão
                resultado = emissoesVeiculos(km_percorrido, potencia, tipo_combustivel)
                
                # Armazenar o resultado com informações detalhadas no session state
                st.session_state['calculos'].append({
                    'tipo_veiculo': tipo_veiculo,
                    'potencia': potencia,
                    'combustivel': tipo_combustivel,
                    'emissao': resultado,
                    'distancia': km_percorrido
                })

                st.write(f"Emissão: {resultado} KG de CO₂")
                st.success("Cálculo realizado! Visualize o histórico de cálculos e a análise de dados nos menus ao lado.")

        else:
            st.warning("Distância precisa ser maior que zero!")


mostrar_input()




