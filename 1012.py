val = input().split(" ")
A,B,C = val # atribuindo valores de variaveis usando lista
A = float(A)
B = float(B)
C = float(C)

tri = (A * C) / 2
cir = 3.14159 * (C**2)
tra = ((A + B) / 2) * C
qua = B**2
ret = A * B

print(f'TRIANGULO: {tri:.3f}')
print(f'CIRCULO: {cir:.3f}')
print(f'TRAPEZIO: {tra:.3f}')
print(f'QUADRADO: {qua:.3f}')
print(f'RETANGULO: {ret:.3f}')
