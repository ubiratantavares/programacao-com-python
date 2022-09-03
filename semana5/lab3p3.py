# Dados n > 0 e uma sequencia de n números reais, escreva um programa que imprima os números na ordem inversa

n = int(input("Digite a quantidade de elementos da lista: "))

lista = []

for i in range(0, n):
	lista.append(int(input("Digite o elemento {} da lista: ".format(i+1))))

for i in range(n - 1, -1, -1):
	if i != 0:
		print(lista[i], end=", ")
	else:
		print(lista[i], end=".")
print("\n")


