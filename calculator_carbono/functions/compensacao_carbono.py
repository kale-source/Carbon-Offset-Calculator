def creditosCO2(projeto_compensacao, co2gasto):
    # Projetos de compensação de carbono e seus respectivos valores em reais por kg de CO2 emitido na atmosfera
    florestamento_Reflorestamento = 0.10
    conservacaoFlorestas = 0.075
    energiaRenovavel = 0.05
    ccs = 0.40
    melhoriasAgricolas_Manejos = 0.125
    biocombustiveis_biomassa = 0.075
    bvrio = 0.03
    biofilica = 0.04
    carbonext = 0.04

    projeto = projeto_compensacao

    if projeto == "Florestamento e Reflorestamento":
        compensacao = florestamento_Reflorestamento * co2gasto
    
    if projeto == "Conservação de Florestas (REDD+)":
        compensacao = conservacaoFlorestas * co2gasto
    
    if projeto == "Energia Renovável (Eólica, Solar, Hidrelétrica)":
        compensacao = energiaRenovavel * co2gasto
    
    if projeto == "Captura e Armazenamento de Carbono (CCS)":
        compensacao = ccs * co2gasto
    
    if projeto == "Melhorias na Agricultura e Manejo de Solo":
        compensacao =  melhoriasAgricolas_Manejos * co2gasto
    
    if projeto == "Biocombustíveis e Biomassa":
        compensacao = biocombustiveis_biomassa * co2gasto

    if projeto == "BVRio":
        compensacao = bvrio * co2gasto
    
    if projeto == "Biofílica":
        compensacao = biofilica * co2gasto

    if projeto == "Carbonext":
        compensacao = carbonext * co2gasto    

    # Resultado em reais
    roundCompensacao = round(compensacao, 2)
    return roundCompensacao





