"""
Faça um programa em Python que receba um valor que foi depositado e exiba o valor com rendimento após um mês.
Considere ﬁxo o juro da poupança em 0,70% a. m.

"""
valor_depositado = float(input("Digite o valor a ser depositado: "))
juros = 0.70/100 # 0.70% a.m

# calculo do valor do rendimento
rendimento = valor_depositado * juros

valor_atual = valor_depositado + rendimento

print("O rendimento obtido após um mês: {:.2f}".format(rendimento))
print("O valor atualizado do deposito: {:.2f}".format(valor_atual))



