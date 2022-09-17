# Escreva uma função qie receba um número inteiro n e devolve o fatorial de n, ou seja, n!.

def fatorial(n):
	fat = 1
	for i in range(2, n+1):
		fat *= i
	return fat

# use a funcao anterior para calcular o número de combinações possíveis de m elementos em grupos
# de n elementos (n <= m), dada pela fórmula de combinações: m! / ((m - n)! n!.
def  combinacao(m, n):
	if n <= m:
		return int(fatorial(m) / (fatorial(m - n) * fatorial(n)))
	else:
		return 'valor de m é menor do que o n.'

def escrever(resultado):
	print(resultado)

def main():
	n = int(input('Digite o valor para o cálculo do fatorial: '))
	escrever(fatorial(n))	
	m = int(input('Digite o valor dos m elementos: '))
	n = int(input('Digite o valor dos n elementos: '))
	escrever(combinacao(m, n))

if __name__ == '__main__':
	main()


