# Dados dois números naturais m e n e duas sequencias ordenadas com m e n números inteiros,
# obtenha uma única sequencia ordenada contendo todos os elementos das sequencias originais sem repetição.

num1 = int(input("Digite a quantidade de elementos da primeira lista: "))
num2 = int(input("Digite a quantidade de elementos da segunda lista: "))

lista1 = []
lista2 = []

for i in range(0, num1):
	lista1.append(int(input("Digite o elemento {} da primeira lista: ".format(i+1))))

for i in range(0, num2):
	lista2.append(int(input("Digite o elemento {} da segunda lista: ".format(i+1))))

lista = []

for elemento in lista1:
	lista.append(elemento)

for elemento in lista2:
	if elemento not in lista:
		lista.append(elemento)

lista.sort()

print(lista)

