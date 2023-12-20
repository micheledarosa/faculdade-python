frase = input('Digite uma frase')
tamanho = len(frase)
while tamanho < 0 or tamanho > 30:
    frase = input('Digite uma frase: ')
    tamanho = len(frase)
print('Com espaços: {}'.format(frase))
print('Sem espaços: ', end="")
for i in range(0, tamanho):
    if frase[i] != ' ':
        print(frase[i], end="")