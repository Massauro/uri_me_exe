"""
URI Online Judge | 1015
Distância Entre Dois Pontos
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

Distancia =

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.
"""
l1 = input()
l2 = input()

ponto1 = l1.split(" ")
ponto2 = l2.split(" ")

formula = (((float(ponto2[0]) - float(ponto1[0])) ** 2) + ((float(ponto2[1]) - float(ponto1[1])) ** 2)) ** (1 / 2)

print(f"{formula:.4f}")
