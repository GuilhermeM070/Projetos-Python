import numpy as np
import openai

# Valores iniciais do usuário
saldos_iniciais = {
    "Criptomoedas": 1142.40,
    "Ações": 663.13,
    "Renda Fixa e TD": 507.07,
    "FIIs": 663.13,
}

# Percentuais de alocação
percentuais = {
    "Criptomoedas": 0.10,
    "Ações": 0.20,
    "Renda Fixa e TD": 0.40,
    "FIIs": 0.30,
}

# Aporte mensal e semestral
aporte_mensal = 1500
aporte_semestral = 1800

# Período de investimento
anos_simulacao = 10  # Até 2035
meses_simulacao = anos_simulacao * 12

# Retornos médios anuais
retornos_ajustados = {
    "Renda Fixa e TD": 0.09,  # 9% ao ano
    "Criptomoedas": 0.25,  # 25% ao ano
    "Ações": 0.12,  # 12% ao ano
    "FIIs": 0.10,  # 10% ao ano
}

# Inicializando saldos com valores iniciais
saldos_2035_bonus = saldos_iniciais.copy()

# Lista para alternância dos aportes (cada mês um ativo diferente)
ativos_aporte = ["Ações", "FIIs", "Renda Fixa e TD", "Criptomoedas"]

# Simulação mensal com aportes semestrais
for mes in range(meses_simulacao):
    ativo_aporte = ativos_aporte[mes % len(ativos_aporte)]  # Alternando aportes
    
    # Aplicação de rendimentos mensais
    for ativo in saldos_2035_bonus:
        if saldos_2035_bonus[ativo] > 0:
            saldos_2035_bonus[ativo] *= (1 + retornos_ajustados[ativo] / 12)  # Rentabilidade mensal
    
    # Adicionando novo aporte ao ativo escolhido no mês
    saldos_2035_bonus[ativo_aporte] += aporte_mensal

    # Redistribuição de dividendos e aporte extra a cada 6 meses
    if (mes + 1) % 6 == 0:
        dividendos_fiis = saldos_2035_bonus["FIIs"] * 0.008  # 0,8% ao mês de dividendos acumulados
        dividendos_acoes = saldos_2035_bonus["Ações"] * 0.005  # 0,5% ao mês de dividendos acumulados

        # Reinvestindo os dividendos entre FIIs e Ações
        saldos_2035_bonus["FIIs"] += dividendos_fiis / 2
        saldos_2035_bonus["Ações"] += dividendos_acoes / 2

        # Distribuindo o aporte semestral entre os 4 ativos proporcionalmente
        for ativo in saldos_2035_bonus:
            saldos_2035_bonus[ativo] += aporte_semestral * percentuais[ativo]

# Resultados finais até 2035 com aporte extra
saldos_2035_bonus
