print('Bem vindo a Lanchonete da Misha :)')
print('***************Cardápio***************')
print('| Código |       Descrição       | Valor |')
print('|   100  |    Cachorro Quente    |  9,00 |')
print('|   101  | Cachorro Quente Duplo | 11,00 |')
print('|   102  |        X-Egg          | 12,00 |')
print('|   103  |       X-Salada        | 12,00 |')
print('|   104  |        X-Bacon        | 14,00 |')
print('|   105  |        X-Tudo         | 17,00 |')
print('|   200  |   Refrigerante Lata   |  5,00 |')
print('|   201  |       Chá Gelado      |  4,00 |')

valor = 0

while True:
    codigo = int(input('Entre com o código do produto desejado: '))

    if codigo == 100:
        print('Você pediu um Cachorro Quente no valor de 9,00')
        valor += 9
    elif codigo == 101:
        print('Você pediu um Cachorro Quente Duplo no valor de 11,00')
        valor += 11
    elif codigo == 102:
        print('Você pediu um X-Egg no valor de 12,00')
        valor += 12
    elif codigo == 103:
        print('Você pediu um X-Salada no valor de 12,00')
        valor += 12
    elif codigo == 104:
        print('Você pediu um X-Bacon no valor de 14,00')
        valor += 14
    elif codigo == 105:
        print('Você pediu um X-Tudo no valor de 17,00')
        valor += 17
    elif codigo == 200:
        print('Você pediu um Refrigerante no valor de 5,00')
        valor += 5
    elif codigo == 201:
        print('Você pediu um Chá Gelado no valor de 4,00')
        valor += 4
    else:
        print('Opção Inválida')
        continue

    resposta = input('Deseja pedir mais alguma coisa?\n1 - Sim\n0 - Não\n')

    if resposta == '1':
        continue
    else:
        print(f'O total a ser pago é: {valor}')
        break
    