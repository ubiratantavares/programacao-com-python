# Escrever um programa em python que leia o nome do vendedor, o seu salario fixo
# e o total de vendas efetuadas por ele no mês (em dinheiro).
# Sabendo que este vendedor ganha 15% de comissão sobre suas vendas, informar o seu nome, o salário fixo e o salário no final do mês.

def salario(salarioBase, totalDeVendas, percentualDeComissao):
	return salarioBase + percentualDeComissao * totalDeVendas

def relatorio(lista):
	print('Nome do vendedor: {}'.format(lista[0]))
	print('Salário base: {}'.format(lista[1]))
	print('Salário no final do mês: {}'.format(salario(lista[1], lista[2], lista[3])))

def main():
	lista = ['Maria', 3000.0, 4500.0, 0.15]
	relatorio(lista)

if __name__ == '__main__':
	main()


