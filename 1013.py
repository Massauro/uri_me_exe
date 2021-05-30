'''
URI Online Judge | 1013
O Maior
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:



Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
'''
entrada = input().split(" ")
valores = []
contagem = 0
for val in entrada:
    valores.append(int(entrada[contagem]))
    contagem += 1
maior = 0
for x in valores:
    if x >= maior:
        maior = x
print(f"{maior} eh o maior")
