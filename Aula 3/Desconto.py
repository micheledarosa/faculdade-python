print('Cálculo de descontos')

valor_original = float(input('Informe o valor do produto: R$'))
quantidade = int(input('Informe a quantidade do produto: '))

if 0 <= quantidade <= 9:
    desconto = 0
    sem_desconto = valor_original * quantidade
elif 10 <= quantidade < 100:
    desconto = 0.05
elif 100 <= quantidade < 1000:
    desconto = 0.10
else:
    desconto = 0.15

com_desconto = sem_desconto - sem_desconto * desconto

print(f'O valor Sem desconto foi R${sem_desconto:.2f}')
print(f'O valor Com desconto foi R${com_desconto:.2f}')
