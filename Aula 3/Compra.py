print('Escolha o que deseja comprar: ')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual fruta deseja comprar? '))
qtd = int(input('Quantas unidades deseja? '))

if produto == 1:
    preco = qtd * 2.3
    print('Você comprou {} maçã(s). Total à pagar: {}'.format(qtd, preco))
elif produto == 2:
    preco = qtd * 3.6
    print('Você comprou {} laranja(s). Total à pagar: {}'.format(qtd, preco))
elif produto == 3:
    preco = qtd * 1.85
    print('Você comprou {} banana(s). Total à pagar: {}'.format(qtd, preco))
else:
    print('Produto inexistente')