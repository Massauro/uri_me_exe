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
