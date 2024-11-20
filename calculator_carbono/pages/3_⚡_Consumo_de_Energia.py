import streamlit as st
from functions.emissao_carbono import *

# Inicializa o session state se não existir
if 'calculos_de_consumo' not in st.session_state:
    st.session_state['calculos_de_consumo'] = []  # Inicializar com lista vazia se ainda não existir

# Função para mostrar inputs e realizar cálculos
def mostrar_input():
    st.title("Entrada de Consumo de Energia ⚡")

    # Seleção do tipo de matriz
    tipo_matriz = st.selectbox("Selecione o tipo de Matriz Energética:", ["Carvão Mineral", "Petróleo e Derivados", "Gás Natural", "Hidrelétrica", "Biomassa", "Solar", "Eólica", "Nuclear"], key="tipo_matriz")
    
    # Placeholder para entradas adicionais com base no tipo de matriz
    if tipo_matriz == "Carvão Mineral":
        kwh_consumido = st.number_input("Energia utilizada em kWh:", min_value=1, key="kwh_consumido")

        if kwh_consumido > 0:
            if st.button("Calcular", key="calcular_button"):
                # Cálculo da emissão
                resultado = emissoesEnergia(tipo_matriz, kwh_consumido)
                
                # Armazenar o resultado com informações detalhadas no session state
                st.session_state['calculos_de_consumo'].append({
                    'matriz': tipo_matriz,
                    'consumokWh': kwh_consumido,
                    'emissao': resultado
                })

                st.write(f"Emissão: {resultado} KG de CO₂")
                st.success("Cálculo realizado! Visualize o histórico de cálculos e a análise de dados nos menus ao lado.")

        else:
            st.warning("Distância precisa ser maior que zero!")

    if tipo_matriz == "Petróleo e Derivados":
        kwh_consumido = st.number_input("Energia utilizada em kWh:", min_value=1, key="kwh_consumido")

        if kwh_consumido > 0:
            if st.button("Calcular", key="calcular_button"):
                # Cálculo da emissão
                resultado = emissoesEnergia(tipo_matriz, kwh_consumido)
                
                # Armazenar o resultado com informações detalhadas no session state
                st.session_state['calculos_de_consumo'].append({
                    'matriz': tipo_matriz,
                    'consumokWh': kwh_consumido,
                    'emissao': resultado
                })

                st.write(f"Emissão: {resultado} KG de CO₂")
                st.success("Cálculo realizado! Visualize o histórico de cálculos e a análise de dados nos menus ao lado.")

        else:
            st.warning("Distância precisa ser maior que zero!")
    
    if tipo_matriz == "Gás Natural":
        kwh_consumido = st.number_input("Energia utilizada em kWh:", min_value=1, key="kwh_consumido")

        if kwh_consumido > 0:
            if st.button("Calcular", key="calcular_button"):
                # Cálculo da emissão
                resultado = emissoesEnergia(tipo_matriz, kwh_consumido)
                
                # Armazenar o resultado com informações detalhadas no session state
                st.session_state['calculos_de_consumo'].append({
                    'matriz': tipo_matriz,
                    'consumokWh': kwh_consumido,
                    'emissao': resultado
                })

                st.write(f"Emissão: {resultado} KG de CO₂")
                st.success("Cálculo realizado! Visualize o histórico de cálculos e a análise de dados nos menus ao lado.")

        else:
            st.warning("Distância precisa ser maior que zero!")
    
    if tipo_matriz == "Hidrelétrica":
        kwh_consumido = st.number_input("Energia utilizada em kWh:", min_value=1, key="kwh_consumido")

        if kwh_consumido > 0:
            if st.button("Calcular", key="calcular_button"):
                # Cálculo da emissão
                resultado = emissoesEnergia(tipo_matriz, kwh_consumido)
                
                # Armazenar o resultado com informações detalhadas no session state
                st.session_state['calculos_de_consumo'].append({
                    'matriz': tipo_matriz,
                    'consumokWh': kwh_consumido,
                    'emissao': resultado
                })

                st.write(f"Emissão: {resultado} KG de CO₂")
                st.success("Cálculo realizado! Visualize o histórico de cálculos e a análise de dados nos menus ao lado.")

        else:
            st.warning("Distância precisa ser maior que zero!")
    
    if tipo_matriz == "Biomassa":
        kwh_consumido = st.number_input("Energia utilizada em kWh:", min_value=1, key="kwh_consumido")

        if kwh_consumido > 0:
            if st.button("Calcular", key="calcular_button"):
                # Cálculo da emissão
                resultado = emissoesEnergia(tipo_matriz, kwh_consumido)
                
                # Armazenar o resultado com informações detalhadas no session state
                st.session_state['calculos_de_consumo'].append({
                    'matriz': tipo_matriz,
                    'consumokWh': kwh_consumido,
                    'emissao': resultado
                })

                st.write(f"Emissão: {resultado} KG de CO₂")
                st.success("Cálculo realizado! Visualize o histórico de cálculos e a análise de dados nos menus ao lado.")

        else:
            st.warning("Distância precisa ser maior que zero!")
    
    if tipo_matriz == "Solar":
        kwh_consumido = st.number_input("Energia utilizada em kWh:", min_value=1, key="kwh_consumido")

        if kwh_consumido > 0:
            if st.button("Calcular", key="calcular_button"):
                # Cálculo da emissão
                resultado = emissoesEnergia(tipo_matriz, kwh_consumido)
                
                # Armazenar o resultado com informações detalhadas no session state
                st.session_state['calculos_de_consumo'].append({
                    'matriz': tipo_matriz,
                    'consumokWh': kwh_consumido,
                    'emissao': resultado
                })

                st.write(f"Emissão: {resultado} KG de CO₂")
                st.success("Cálculo realizado! Visualize o histórico de cálculos e a análise de dados nos menus ao lado.")

        else:
            st.warning("Distância precisa ser maior que zero!")
    
    if tipo_matriz == "Eólica":
        kwh_consumido = st.number_input("Energia utilizada em kWh:", min_value=1, key="kwh_consumido")

        if kwh_consumido > 0:
            if st.button("Calcular", key="calcular_button"):
                # Cálculo da emissão
                resultado = emissoesEnergia(tipo_matriz, kwh_consumido)
                
                # Armazenar o resultado com informações detalhadas no session state
                st.session_state['calculos_de_consumo'].append({
                    'matriz': tipo_matriz,
                    'consumokWh': kwh_consumido,
                    'emissao': resultado
                })

                st.write(f"Emissão: {resultado} KG de CO₂")
                st.success("Cálculo realizado! Visualize o histórico de cálculos e a análise de dados nos menus ao lado.")

        else:
            st.warning("Distância precisa ser maior que zero!")
    
    if tipo_matriz == "Nuclear":
        kwh_consumido = st.number_input("Energia utilizada em kWh:", min_value=1, key="kwh_consumido")

        if kwh_consumido > 0:
            if st.button("Calcular", key="calcular_button"):
                # Cálculo da emissão
                resultado = emissoesEnergia(tipo_matriz, kwh_consumido)
                
                # Armazenar o resultado com informações detalhadas no session state
                st.session_state['calculos_de_consumo'].append({
                    'matriz': tipo_matriz,
                    'consumokWh': kwh_consumido,
                    'emissao': resultado
                })

                st.write(f"Emissão: {resultado} KG de CO₂")
                st.success("Cálculo realizado! Visualize o histórico de cálculos e a análise de dados nos menus ao lado.")

        else:
            st.warning("Distância precisa ser maior que zero!")
            

mostrar_input()