def pot(b, p):
	return b**p

def quadrado(x):
	return pot(x, 2)

def main():
	n = 5
	resultado = quadrado(n)
	print(resultado)

if __name__ == '__main__':
	main()


