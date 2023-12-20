def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while x < min or x > max:
        x = int(input(pergunta))
    return x


def soma_intervalo(inicio, fim):
    soma = 0
    i = inicio
    while i <= fim:
        soma += 1
        i += 1
    return soma


x = valida_int('Digite um valor inteiro positivo ', 1, 99999)
y = valida_int('Digite outro valor inteiro positivo ', 1, 99999)
print('Somatório entre {} e {} é {}'.format(x, y, soma_intervalo(x, y)))
