# Escreva uma função que receba as notas de um estudante e a sua frequencia e informe sua situação.

def main():
	lista = [['Maria', 2.0, 5.0, 8.0, 0.80],
                 ['João ', 2.0, 2.0, 4.0, 0.90],
                 ['José ', 6.0, 7.0, 9.0, 0.75]]

	for item in lista:
		escrever(item)

def somaNotas(item):
	return item[1] + item[2] + item[3]

def media(item):
	return somaNotas(item)/3

def situacao(item):
	frequencia = item[4]
	if frequencia >= 0.75:
		if media(item) < 3.0:
			return 'Reprovado(a)'
		elif 3.0 <= media(item) < 6.0:
			return 'em Recuperação'
		else:
			return 'Aprovado(a)'
	else:
		return 'Reprovado(a)'

def escrever(item):
	print('{} encontra-se {}.'.format(item[0], situacao(item)))


if __name__ == '__main__':
	main()
