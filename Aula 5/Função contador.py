def contador(v_final, v_inicial= 0, passos= 1):
    for i in range(v_inicial, v_final, passos):
        print(f'{i}', end=' ')
    print()

contador(20, 10, 2)
contador(11)
