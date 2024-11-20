### **Arquivos e Explicações**

# Calculadora de Carbono 🌱

Projeto desenvolvido para cálculo e compensação de emissões de carbono com base em inputs do usuário. O sistema inclui a interface desenvolvida em **Streamlit** e a lógica de cálculos estruturada separadamente. A aplicação busca promover conscientização ambiental e facilitar o acesso a informações sobre emissões de carbono e formas de compensação.

---

## Estrutura do Projeto 📂

### SUPER IMPORTANTE! ⚠️:
É necessário instalar duas bibliotecas para a calculadora funcionar corretamente!

1. **`Streamlit`**
   Vá até seu terminal e digite o seguinte comando:
      ``pip install streamlit``

2. **`Matplotlib`**
   Vá até seu terminal e digite o seguinte comando:
      ``pip install matplotlib``

Com as duas bibliotecas instaladas, a calculadora irá funcionar sem erros.

### Principais Arquivos e Funcionalidades:

1. **`Inicio.py`**  
   Arquivo principal da aplicação, que gerencia a estruturação das abas e a navegação entre elas.  

2. **`Entrada de Veiculo.py`**  
   Aba para cálculos relacionados a emissões de carbono de veículos. Solicita informações como tipo de veículo, combustível utilizado e distância percorrida, e calcula as emissões associadas.  

3. **`Consumo de Energia.py`**  
   Aba dedicada aos cálculos de emissões relacionadas ao consumo de energia elétrica. Solicita dados como o consumo em kWh e a matriz energética utilizada.  

4. **`Compensacao.py`**  
   Aba para sugerir e calcular formas de compensação para as emissões geradas. Inclui investimentos estimados em projetos de compensação, como reflorestamento.  

5. **`Resultados.py`**  
   Aba que exibe os cálculos realizadas pelo usuário, atráves de gráficos, separadas por categorias: veículos e energia.

6. **`Historico de Emissoes.py`**  
   Aba que exibe o **histórico de cálculos de emissões** realizadas pelo usuário, separadas por categorias: veículos e energia. Permite a visualização detalhada de cada cálculo e a opção de limpar o histórico armazenado no estado da aplicação.  

7. **`Historico de Compensacoes.py`**  
   Aba que apresenta o **histórico de compensações realizadas**. Mostra os itens compensados, formas de compensação utilizadas e os valores de investimento. Também oferece a opção de limpar o histórico das compensações.  

---

## Como Utilizar 🚀

1. Certifique-se de ter o **Python** e **Streamlit** instalado em sua máquina.  
2. Na pasta principal execute o comando `streamlit run 1_🏠_Início.py.py` para iniciar a aplicação.  

---

**Desenvolvido com 💚 pela equipe do projeto Calculadora de Carbono**  

