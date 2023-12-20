tabuada = int(input('Digite o valor que deseja calcular a tabuada: '))
n = int(input('Digite até qual número deseja mostrar a tabuada: '))
for i in range(1, n + 1):
    print('{} * {} = {}'.format(tabuada, i, tabuada * i))