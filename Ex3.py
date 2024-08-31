# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

import json

with open("data_ex3.json", encoding='utf-8') as dados:
    faturamento = json.load(dados)


faturamento_filtrado = [chave['valor'] for chave in faturamento if chave['valor'] > 0]

menor_valor = min(faturamento_filtrado)
maior_valor = max(faturamento_filtrado)

media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)

dias_acima_da_media = len([valor for valor in faturamento_filtrado if valor > media_mensal])

print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Número de dias com faturamento superior à média: {dias_acima_da_media}")


