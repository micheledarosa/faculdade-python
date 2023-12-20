ano_nasc = int(input('Qual o seu ano de nascimento?'))
ano_atual = int(input('Informe o ano atual: '))
idade = ano_atual - ano_nasc

if idade >= 18:
    print('Você já pode tirar sua carteira de motorista')