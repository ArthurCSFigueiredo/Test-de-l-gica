# O menor valor de faturamento ocorrido em um dia do mês; FEITO
# O maior valor de faturamento ocorrido em um dia do mês; FEITO
# Número de dias no mês em que o valor de faturamento diário foi superior à média mensal; FEITO
# média mensal; FEITO
# Criar faturamento no com cada dia json; FEITO
# dias sem faturamento, finais de semana e feriados. ignorar no cálculo da média; FEITO

import json

with open('../faturamento.json', 'r') as fatuTemp:
    lista = json.load(fatuTemp)

faturamento_filtrado=[]

for faturamento_diario in lista['faturamento'].values():
    if faturamento_diario > 0:
        faturamento_filtrado.append(faturamento_diario)

maior_faturamento = max(faturamento_filtrado)
menor_faturamento = min(faturamento_filtrado)
media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)
valor_maior = {}
for maior, faturamento_diario in lista['faturamento'].items():
    if int(faturamento_diario) > media_mensal:
        valor_maior[maior] = faturamento_diario


print(f'O maior valor de faturamento ocorrido em um dia do mês:', maior_faturamento)
print(f'O menor valor de faturamento ocorrido em um dia do mês:', menor_faturamento)
print(f'Dias com faturamento superior a média mensal: {valor_maior}')
print(f'A média mensal é:{media_mensal: .2f}')



