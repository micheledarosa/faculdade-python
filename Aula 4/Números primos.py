print('Primos de 2 até 99:')
for numero in range(2, 100):
    # variável que altera seu valor caso o num não seja primo
    flag = 0
    for i in range(2, numero):
        if numero % 1 == 0:
            flag = 1
            # caso encontre um valor fazer um break, para n testar até o fim sem necessidade
            break
    if not flag:
        print(numero)