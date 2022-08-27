# Escreva um programa que receba uma sequência de numeros inteiros positivos e
# verifique se os numeros estão ou não em ordem crescente

num = int(input("Digite o primeiro numero da sequencia: "))

freqMaior = 0

if num != 0:
	contador = 1

while num != 0 :
	prox  = int(input("Digite o proximo numero da sequencia: "))
	if prox != 0:
		contador += 1
		if num > prox:
			freqMaior += 1
	num = prox

if contador > 1:
	if freqMaior == 0:
		print("Estão em ordem crescente")
	else:
		print("Não estão em ordem crescente")



