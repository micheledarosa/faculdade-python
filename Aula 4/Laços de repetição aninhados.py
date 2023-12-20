idade = int(input('Qual sua idade? '))
while idade > 0:
    sexo = input('Qual seu sexo? F/M ')
    if sexo == 'M' or sexo == 'm':
        print('Boa noite, Senhor. Sua idade é {}'.format(idade))
    else:
        if sexo == 'F' or sexo == 'f':
            print('Boa noite, Senhora. Sua idade é {}'.format(idade))
        else:
            print('Opção de sexo inexistente.')
    idade = int(input('Qual sua idade?\nPara sair digite 0\n'))
print('Encerrando...')