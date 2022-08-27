"""
Escrever um código em Python que leia dois valores inteiros distintos e informe qual é o maior

"""

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if num1 != num2:
	if num1 > num2:
		maior = num1
	else:
		maior = num2
	print("maior numero lido é o numero {}.".format(maior))



