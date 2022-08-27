"""
Elaborar um programa em Python que efetue a apresentação do valor da conversão em real (R$) de um valor lido em dólar
(US$). O algoritmo deverá solicitar o valor da cotação do dólar e também a quantidade de dólares disponíveis com o usuário.

"""

cotacao = float(input("Digite o valor da cotação do dólar: "))
quantidade_dolar = float(input("Digite a quantidade de dólares a ser convertido para reais: "))

# cálculo de  conversão de US$ para R$
quantidade_reais = cotacao * quantidade_dolar

print("A quantidade em reais: {:.2f}".format(quantidade_reais))


