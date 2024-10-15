# calcule o percentual de representação que cada estado teve dentro do valor total;

import json

with open('estados.json', 'r') as percent:
    listaTotal = json.load(percent)

faturamento = listaTotal['estados']

valor_total = sum(float(valor) for valor in faturamento.values())
estados = ['SP', 'RJ', 'MG', 'ES', 'Outros']

for estado in estados:
    if estado in faturamento:
        valor= float(faturamento[estado])
        percentual= (valor/valor_total) * 100
        print(f'O percentual de {estado} é: {percentual: .2f}%')

print(f'O valor total da distribuidora por estado é: R${valor_total: .2f}')