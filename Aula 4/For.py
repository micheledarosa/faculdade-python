soma = 0
qtd = 0
for i in range(1, 101):
    if i % 2 == 0:
        soma += 1
        qtd += 1
media = soma / qtd
print('A média dos pares de até 100 é: {}'.format(media))
