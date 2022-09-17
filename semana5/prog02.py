def pertence(item, lista):
	p = False
	for i in lista:
		if i == item:
			p = True
	return p

def main():
	lista = [2, 3, 5, 7, 9]
	numero = 4
	print(pertence(numero, lista))


if __name__ == '__main__':
	main()
