"""
Escreva um código que receba o preço de custo de um produto e mostre o valor de venda. Sabe-se que o preço de custo
receberá um acréscimo de acordo com um percentual informado pelo usuário.

"""

preco_de_custo = float(input("Digite o preço de custo do produto: "))
percentual_de_lucro = float(input("Digite o percentual de lucro do produto: "))

# calculo do preco de venda do produto
preco_de_venda = preco_de_custo * (1 + percentual_de_lucro/100.0)

print("Preco de venda do produto: {:.2f}".format(preco_de_venda))



