def potencia(base, expoente):
	pot = 1
	for i in range(expoente):
		pot *= base
	return pot

def main():
	base = float(input('Digite o valor da base: '))
	expoente =  int(input('Digite o valor do expoente: '))
	p = potencia(base, expoente)
	print('A potenciação da {} elevado a {} é igual a {}.'.format(base, expoente, p))

if __name__ == '__main__':
	main()

