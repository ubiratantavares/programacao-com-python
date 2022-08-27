# Um professor quer calcular a média das notas finais dos estudantes da sua turma.
# Escreva um programa que receba as notas finais de n estudantes e calcule a média final da turma

n = int(input("Digite a quantidade de estudantes da turma: "))
contador = 1
soma = 0

while contador <= n:
	nota = float(input("Digite a nota final do estudante {}: ".format(contador)))
	soma += nota
	contador += 1

media = soma / n

print("A média final da turma: {:1f}".format(media))

