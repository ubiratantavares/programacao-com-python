"""
Escrever um programa em Python que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por
ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o seu
nome, o salário fixo e salário no final do mês.

"""

nome = input("Digite o nome do vendedor: ")
salario_base = float(input("Digite o salário fixo do vendedor: "))
total_vendas = float(input("Digite o total de vendas do vendedor (em dinheiro): "))

salario_total = salario_base + 15/100 * total_vendas

print("Nome do vendedor: {}".format(nome))
print("Salário fixo: {:.2f}".format(salario_base))
print("Salário no final do mês: {:.2f}".format(salario_total))
 


