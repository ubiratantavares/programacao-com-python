"""
Escrever um algoritmo para determinar o consumo médio de um automovel sendo fornecida a distância total
percorrida pelo automóvel e o total de combustível gasto.

"""

distancia_total = float(input("Digite a distância total percorrida pelo automóvel em km: "))
consumo_total = float(input("Digite o total de combustivel consumido pelo automóvel em l: "))

consumo_medio = distancia_total / consumo_total 

print("O consumo médio do automóvel em km/l = {:.2f}".format(consumo_medio))




