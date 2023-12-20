def ordenar_valores():
    lista_valores = list()
    while True:
        lista_valores.append(int(input(f'Adicione um valor: ')))
        continua = ' '
        while continua not in 'SN':
            continua = str(input('Gostaria de adicionar outro valor na lista? [S/N] ')).strip().upper()[0]
        if continua == 'N':
            break
    lista_valores.sort()
    return lista_valores


print(f'Valores ordenados: {ordenar_valores()}')
