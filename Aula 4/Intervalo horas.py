h_inicial = int(input('Deseja iniciar em qual hora? '))
h_final = int(input('Deseja terminar em qual hora? '))
while h_inicial > h_final or h_inicial < 0 or h_inicial > 23 or h_final < 0 or h_final > 23:
    h_inicial = int(input('Deseja iniciar em qual hora? '))
    h_final = int(input('Deseja terminar em qual hora? '))
for h in range(h_inicial, h_final + 1):
    for m in range(0, 60):
        for s in range(0, 60):
            print(h, ':', m, ':', s, 'h')