"""
O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos
(aplicados, primeiro os impostos sobre o custo de fábrica, e depois a percentagem do distribuidor sobre oresultado). Supondo
que a percentagem do distribuidor seja de 28% e os impostos 45%. Escrever um código que leia o custo de fábrica de um
carro e informe o custo ao consumidor do mesmo.

"""

custo_fabrica_sem_impostos  =  float(input("Digite o valor do custo de fábrica: "))

# calculo do custo do carro novo considerando a aplicação de impostos de 45%
custo_fabrica_com_impostos = custo_fabrica_sem_impostos * (1 + 45/100)

# calculo do custo do carro novo considerando a aplicação percentual do distribuidor de 28% 
custo_ao_consumidor  = custo_fabrica_com_impostos * (1 + 28/100)

print("Custo do carro novo ao consumidor: {:.2f}".format(custo_ao_consumidor))



