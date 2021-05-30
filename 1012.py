"""
URI Online Judge | 1012
Área
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.
Entrada
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Saída
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.
"""
val = input().split(" ")
A, B, C = val  # atribuindo valores de variaveis usando lista
A = float(A)
B = float(B)
C = float(C)

tri = (A * C) / 2
cir = 3.14159 * (C ** 2)
tra = ((A + B) / 2) * C
qua = B ** 2
ret = A * B

print(f"TRIANGULO: {tri:.3f}")
print(f"CIRCULO: {cir:.3f}")
print(f"TRAPEZIO: {tra:.3f}")
print(f"QUADRADO: {qua:.3f}")
print(f"RETANGULO: {ret:.3f}")
