print('Escolha a forma de pagamento:')
print('1- Pagamento à vista')
print('2- Pagamento em 3x')
print('3- Pagamento em 5x')
print('4- Pagamento em 10x')
op = int(input('Qual a forma de pagamento deseja fazer? '))
valor = float(input('Qual o valor do produto? '))

if op == 1:
    valor_total = valor * 0.95
    print('Produto comprado à vista. Total a pagar: {}'.format(valor_total))
elif op == 2:
    valor_total = valor
    parcela = valor_total / 3
    print('Produto comprado em 3x. Total a pagar: {}. Valor da parcela: {:.2f}'.format(valor_total, parcela))
elif op == 3:
    valor_total = valor * 1.02
    parcela = valor_total / 5
    print('Produto comprado em 5x. Total a pagar: {}. Valor da parcela: {:.2f}'.format(valor_total, parcela))
elif op == 4:
    valor_total = valor * 1.08
    parcela = valor_total / 10
    print('Produto comprado em 10x. Total a pagar: {}. Valor da parcela: {:.2f}'.format(valor_total, parcela))
else:
    print('Operação inválida')
