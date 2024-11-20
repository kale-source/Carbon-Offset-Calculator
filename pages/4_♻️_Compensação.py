import streamlit as st
from data.formas_compensacao import *
from functions.compensacao_carbono import *

# Inicializa o session state das emissoes
if 'calculos' not in st.session_state:
  st.session_state['calculos'] = []  
if 'calculos_de_consumo' not in st.session_state:
  st.session_state['calculos_de_consumo'] = []

# Inicializa o session state das compensações
if 'compensacao_veiculo' not in st.session_state:
  st.session_state['compensacao_veiculo'] = []  
if 'compensacao_energia' not in st.session_state:
  st.session_state['compensacao_energia'] = []


def compensacoes(calculos):
  st.title("Compensação de Carbono para Veículo 🚗")
  
  if calculos:
    # Separar tipos de veículos e suas emissões
    tipos_veiculos = []
    emissoes_valores = []
        
    # Preenche as listas com os dados de session_state
    for i in calculos:
      tipos_veiculos.append(f"{i['tipo_veiculo']} - {i['potencia']}: {i['emissao']} KG de CO₂")
      emissoes_valores.append(float(i['emissao']))  

    # Seleciona o veiculo e sua emissão
    veiculo = st.selectbox("Selecione a emissão para compensação.", tipos_veiculos)

    # Encontrar index da seleção e pegar na lista a emissão do mesmo
    index = tipos_veiculos.index(veiculo)
    emissao = emissoes_valores[index]

    # Extrair os títulos da lista formas_compensacao e exibe na seleção
    titulos = [item["titulo"] for item in formas_compensacao]
    compensacao = st.selectbox("Selecione a forma de compensação:", titulos, key='veiculo')

    if st.button("Calcular investimento", key="compensar_veiculo"):
      resultado = creditosCO2(compensacao, emissao)

      item = (f"{calculos[index]['tipo_veiculo']} {calculos[index]['potencia']} {calculos[index]['combustivel']}")
      distancia = calculos[index]['distancia']
      st.session_state['compensacao_veiculo'].append({
        'item': item,
        'distancia': distancia,
        'emissao': emissao,
        'compensacao': compensacao,
        'investimento': resultado
      })

      # Encontrar a forma de compensação selecionada
      forma_selecionada = next((item for item in formas_compensacao if item["titulo"] == compensacao), None)

      if forma_selecionada:
        st.title(compensacao)
        st.write(forma_selecionada["descricao"])
        st.image(forma_selecionada['img'])
        st.markdown(f"[Leia mais]({forma_selecionada['link']})")
        st.success(f"Valor para investimento: R${resultado}")

  else:
     st.write("Nenhum cálculo de veículo realizado até o momento.")

compensacoes(st.session_state['calculos'])

def compensacoesEnergia(calculos):
  st.title("Compensação de Carbono para Energia ⚡")
  if calculos:
    # Separar tipos de veículos e suas emissões
    tipos_matriz = []
    emissoes_valores = []
        
    # Preenche as listas com os dados de session_state
    for i in calculos:
      tipos_matriz.append(f"{i['matriz']} - {i['consumokWh']}: {i['emissao']} KG de CO₂")
      emissoes_valores.append(float(i['emissao']))  

    # Seleciona o veiculo e sua emissão
    matriz = st.selectbox("Selecione a emissão para compensação.", tipos_matriz)

    # Encontrar index da seleção e pegar na lista a emissão do mesmo
    index = tipos_matriz.index(matriz)
    emissao = emissoes_valores[index]

    # Extrair os títulos da lista formas_compensacao e exibe na seleção
    titulos = [item["titulo"] for item in formas_compensacao]
    compensacao = st.selectbox("Selecione a forma de compensação:", titulos, key='energia')

    if st.button("Calcular investimento", key="compensar_energia"):
      resultado = creditosCO2(compensacao, emissao)

      item = calculos[index]['matriz']
      consumo = calculos[index]['consumokWh']
      st.session_state['compensacao_energia'].append({
        'matriz': item,
        'consumo': consumo,
        'emissao': emissao,
        'compensacao': compensacao,
        'investimento': resultado
      })

      # Encontrar a forma de compensação selecionada
      forma_selecionada = next((item for item in formas_compensacao if item["titulo"] == compensacao), None)

      if forma_selecionada:
        st.title(compensacao)
        st.write(forma_selecionada["descricao"])
        st.image(forma_selecionada['img'])
        st.markdown(f"[Leia mais]({forma_selecionada['link']})")
        st.success(f"Valor para investimento: R${resultado}")

  else:
     st.write("Nenhum cálculo de consumo de energia realizado até o momento.")

compensacoesEnergia(st.session_state['calculos_de_consumo'])

