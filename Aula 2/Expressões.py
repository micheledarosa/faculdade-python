x = 10
y = 1
res = not x > y
print(res)

x = 10
y = 1
z = 5.5
res = x > y and z == y
print(res)

m1 = float(input('Digite a nota da 1ª matéria:'))
m2 = float(input('Digite a nota da 2ª matéria:'))
m3 = float(input('Digite a nota da 3ª matéria:'))
if m1 >= 7 and m2 >= 7 and m3 >= 7:
    print('Aluno aprovado')
else:
    print('reprovado')
