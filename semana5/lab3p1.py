# Escreva um programa que determine o máximo da função f(x) = y + xy + x**2, com x, y números inteiros
# nos intervalos -1 <= x <= 2 e 0 <= y <= 4.

x = -1
y = 0
f = y + x * y + x**2
x_max = x
y_max = y

f_max = f
dx = 0.1
dy = dx
num_iteracoes = 0

while (-1 <= x <= 2) and (0 <= y <= 4):
	x += dx
	y += dy
	f = y + x * y + x**2
	if f > f_max:
		f_max = f
		x_max = x
		y_max = y
	num_iteracoes += 1

print("O máximo da função f({:.1f}, {:.1f}) = {:.1f}".format(x_max, y_max, f_max))
print("Total de iteracoes: {}".format(num_iteracoes))
