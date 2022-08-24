"""
Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit.

"""

C = float(input("Digite a temperatura em graus Celsius: "))

# converter a temperatura em graus Celsius para graus Fahrenheit
F = (9 * C + 160) / 5.0

print("Temperatura em graus Fahrenheit: {:.2f}".format(F))



