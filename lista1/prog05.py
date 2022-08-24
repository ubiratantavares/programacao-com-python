"""
Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a variável A passe a possuir o valor
da variável B e a variável B passe a possuir o valor da variável A. Apresentar os valores trocados.

"""
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

# efetua a troca dos valores entre as variáveis
aux = a
a = b
b = aux

print("O valor de A: {}".format(a))
print("O valor de B: {}".format(b))

 



