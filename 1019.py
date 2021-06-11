"""
URI Online Judge | 1019
Conversão de Tempo
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
"""

segundos = int(input())
segundos_saldo = segundos
tipo = "m"
minutos = 0
horas = 0

while True:
    if segundos_saldo >= 60:
        segundos_saldo -= 60
        minutos += 1
    elif minutos >= 60:
        minutos -= 60
        horas += 1
    else:
        break

print(f"{horas}:{minutos}:{segundos_saldo}")
