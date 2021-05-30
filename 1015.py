l1 = input()
l2 = input()

ponto1 = l1.split(" ")
ponto2 = l2.split(" ")

formula = (((float(ponto2[0]) - float(ponto1[0])) ** 2) + ((float(ponto2[1]) - float(ponto1[1])) ** 2)) ** (1 / 2)

print(f"{formula:.4f}")
