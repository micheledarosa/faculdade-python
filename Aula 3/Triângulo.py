A = int(input('Digite o 1º lado do triângulo\n'))
B = int(input('Digite o 2º lado do triângulo\n'))
C = int(input('Digite o 3º lado do triângulo\n'))

if A > 0 and B > 0 and C > 0:
    if A + B > C and A + C > B and B + C > A:
        if A != B and A != C and B != C:
            print('Triângulo escaleno')
        elif A == B and B == C:
            print('Triângulo equilátero')
        else:
            print('Triângulo Isósceles')
    else:
        print('Ao menos um dos valores indicados não servem para formar um triângulo')
else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo')