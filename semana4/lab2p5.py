# cálculo de potência (n elevado a k)

base = int(input("Digite a base da potenciação: "))
expoente = int(input("Digite o expoente da potenciação: "))

produto = 1
contador = 0

while contador < expoente:
	produto *= base
	contador += 1

print("A potência de {} elevado a {} é igual a {}.".format(base, expoente, produto))

