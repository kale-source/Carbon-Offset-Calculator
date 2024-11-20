def emissoesVeiculos(km_distancia, potencia_motor, tipo_combustivel):
    # CO2 = (DISTANCIA * CONSUMO) / FATOR EMISSAO
    
    # Quanto gasta de combustível em litros de cada motor em média por KM rodado
    motor1_0_1_2 = 0.071
    motor1_4_1_6 = 0.1
    motor1_8_2_0 = 0.125
    motor2_0acima = 0.142

    moto125cc_150cc = 0.025
    moto250cc_300cc = 0.03
    moto300cc_acima = 0.05

    caminhaoLeve = 0.2
    caminhaoMedio = 0.25
    caminhaoPesado = 0.33

    # Liberação de kg CO2 de cada tipo de combustivel por litro gasto
    gasolina =  2.264
    diesel =  2.93
    etanol = 0.389
    eletricidadeBrasil = 0.084
    eletriciaMediaGlobal = 0.475

    # Distancia percorrida
    distancia = int(km_distancia)
    motor = potencia_motor


    # Motor de carro
    if motor == "1.0 a 1.2":
        consumo = motor1_0_1_2 * distancia
    if motor == "1.4 a 1.6":
        consumo = motor1_4_1_6 * distancia
    if motor == "1.8 a 2.0":
        consumo = motor1_8_2_0 * distancia  
    if motor == "Acima de 2.0":
        consumo = motor2_0acima * distancia
    
    # Motor de moto
    if motor == "125 a 150 cilindradas":
        consumo = moto125cc_150cc * distancia
    if motor == "250 a 300 cilindradas":
        consumo = moto250cc_300cc * distancia
    if motor == "Acima de 300 cilindradas":
        consumo = moto300cc_acima * distancia
    
    # Motor de caminhão
    if motor == "Caminhão Leve":
        consumo = caminhaoLeve * distancia
    if motor == "Caminhão Médio":
        consumo = caminhaoMedio * distancia
    if motor == "Caminhão Pesado":
        consumo = caminhaoPesado * distancia


    # Emissão por combustivel
    combustivel = tipo_combustivel
    
    if combustivel == "Gasolina":
        fatorEmissao = gasolina
    if combustivel == "Diesel":
        fatorEmissao = diesel
    if combustivel == "Etanol":    
        fatorEmissao = etanol
    if combustivel == "Elétrico":
        fatorEmissao = eletricidadeBrasil
    
    formula = consumo * fatorEmissao
    roundFormula = round(formula, 2)
    return roundFormula

def emissoesEnergia(matriz_energetica, consumo_energia):
    # Consumo de Energia (kWh) × Fator de Emissão (kg CO₂e/kWh)

    # Fatores de emissão (kg CO₂e/kWh) de cada matriz energética
    carvaoMineral = 0.90
    petroleo_derivados = 0.30
    gasNatural = 0.25
    biomassa = 0.10
    hidreletrica = 0.03 #Emissões indiretas
    solar = 0.07 #Emissões indiretas
    eolica = 0.01 #Emissões indiretas 
    nuclear = 0.012 #Emissões indiretas

    matriz = matriz_energetica
    consumo = consumo_energia

    if matriz == 'Carvão Mineral':
        emissao = consumo * carvaoMineral
    if matriz == "Petróleo e Derivados":
        emissao = consumo * petroleo_derivados
    if matriz == "Gás Natural":
        emissao = consumo * gasNatural
    if matriz == "Biomassa":
        emissao = consumo * biomassa
    if matriz == "Hidrelétrica":
        emissao = consumo * hidreletrica
    if matriz == "Solar":
        emissao = consumo * solar
    if matriz == "Eólica":
        emissao = consumo * eolica
    if matriz == "Nuclear":
        emissao = consumo * nuclear
    
    emissaoRound = round(emissao, 2)
    return emissaoRound







    
    

    

