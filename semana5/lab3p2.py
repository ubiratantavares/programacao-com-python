# Escreva um programa que receba um número inteiro e devolva o fatorial de n.
# exemplo: entrada, n = 5. saída: 120

numero = int(input("Digite o numero inteiro para o fatorial: "))

fatorial = 1
for i in range(1, numero+1):
	fatorial *= i
print("O fatorial de {} = {}".format(numero, fatorial))


