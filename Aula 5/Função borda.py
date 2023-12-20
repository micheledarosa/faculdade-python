def borda(titulo):
    tam = len(titulo)
    if tam:
        print('+','-' * tam,'+')
        print('|',titulo,'|')
        print('+','-' * tam,'+')

borda('Olá, Mundo!')
borda('Lógica de Programação e Algoritmos')
