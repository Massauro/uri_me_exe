"""
URI Online Judge | 1020
Idade em Dias
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
"""

dias = int(input())
anos = int(dias / 365)
meses = int(dias % 365 / 30)
dias = int(dias % 365 % 30)

print(f"{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)")
