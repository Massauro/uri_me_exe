"""
URI Online Judge | 1018
Cédulas
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1

"""
saque = int(input())
saldo = saque
nota = 100
totalCedulas = 0
print(saque)
while True:
    if saldo >= nota:
        saldo -= nota
        totalCedulas += 1
    else:
        if saldo < nota:
            print(f"{totalCedulas} nota(s) de R$ {nota},00")
        if nota == 100:
            nota = 50
            totalCedulas = 0
        elif nota == 50:
            nota = 20
            totalCedulas = 0
        elif nota == 20:
            nota = 10
            totalCedulas = 0
        elif nota == 10:
            nota = 5
            totalCedulas = 0
        elif nota == 5:
            nota = 2
            totalCedulas = 0
        elif nota == 2:
            nota = 1
            totalCedulas = 0
        else:
            break
