def diferenca(x1, x2):
	return x1 - x2

def potencia(base, expoente):
	return base**expoente

def distancia(x1, y1, x2, y2):
	dx = diferenca(x1, x2)
	dy = diferenca(y1, y2)
	ds = potencia(dx, 2) + potencia(dy, 2) 
	raiz = potencia(ds, 0.5)
	return raiz

def distancia_euclidiana(x1, y1, x2, y2):
	return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def leituraDoPonto():
	x = float(input('Digite a abcissa do ponto: '))
	y = float(input('Digite a ordenada do ponto: '))
	return x, y

def escreverResultado(distancia):
	print('A distancia entre os dois pontos é de {} m.'.format(distancia))


def main():
	x1, y1 = leituraDoPonto()
	x2, y2 = leituraDoPonto()
	escreverResultado(distancia(x1, y1, x2, y2))
	escreverResultado(distancia_euclidiana(x1, y1, x2, y2))

if __name__ == '__main__':
	main()

