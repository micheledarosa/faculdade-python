salario = float(input('Qual é o seu salário? '))
ano_ad = int(input('Informe seu ano de admissão: '))
ano_atual = int(input('Informe o ano atual: '))
tempo = ano_atual - ano_ad

if tempo > 5:
    print('Você recebeu um bônus de {}'.format(salario * 0.2))
else:
    print('Você recebeu um bônus de {}'.format(salario * 0.1))