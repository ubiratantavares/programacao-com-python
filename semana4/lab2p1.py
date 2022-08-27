# Dados dois números inteiros, escreva um programa que os mostre em ordem crescente

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if num1 <= num2:
	print("{},{}".format(num1, num2))
else:
	print("{},{}".format(num2, num1))

