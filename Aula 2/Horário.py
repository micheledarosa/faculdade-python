d = int(input('Quantos dias? '))
h = int(input('Quantas horas? '))
m = int(input('Quantos minutos? '))
s = int(input('Quantos segundos? '))

total = s + (m * 60) + (h * 60 * 60) + (d * 24 * 60 * 60)
res = print('O total de segundos calculado é de {}'.format(total))

