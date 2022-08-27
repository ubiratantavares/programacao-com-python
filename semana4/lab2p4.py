# dado um número inteiro n > 1, escreva um programa que verifique se ele possui dois digitos adjacentes iguais.

numero = int(input("Digite o número: "))

adjacente = False

resto1 = numero % 10

numero = numero // 10

while  numero != 0  and not adjacente:
	resto2 = numero % 10
	if resto1 == resto2:
		adjacente = True
	numero = numero // 10
	resto1 = resto2


if adjacente:
	print("O número possui dígitos adjacentes iguais.")
else :
	print("O número não  possui dígitos adjacentes iguais.")

