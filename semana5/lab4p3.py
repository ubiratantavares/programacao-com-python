# Escreva uma função que converte horas, minutos e segundos em um número total de segundos

def horaSplit(hora):
	tempo = hora.split(':')
	h = int(tempo[0])
	m = int(tempo[1])
	s = int(tempo[2])
	print(h, m, s)
	return (h, m, s)

def converterHoraParaSegundos(hor, min, seg):
	return 3600 * hor + 60 * min + seg

def main():
	hora = '03:43:07'
	hor, min, seg = horaSplit(hora)
	print(converterHoraParaSegundos(hor, min, seg))
	hora = '00:20:03'
	hor, min, seg = horaSplit(hora)
	print(converterHoraParaSegundos(hor, min, seg))

if __name__ == '__main__':
	main()

