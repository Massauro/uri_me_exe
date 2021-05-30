nome = str(input())
vendas = float(input())
salario = float(input())
comissao = ((salario * 15) / 100) + vendas
print(f'TOTAL = R$ {comissao:.2f}')