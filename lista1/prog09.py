"""
A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros. Escreva um codigo em Python
que receba um valor de uma compra e mostre o valor das prestações.

"""
numero_de_prestacoes = 5

valor_de_compra = float(input("Digite o valor total da compra: "))

valor_da_prestacao =  valor_de_compra / numero_de_prestacoes

print("O valor da prestação: {:.2f}".format(valor_da_prestacao))




