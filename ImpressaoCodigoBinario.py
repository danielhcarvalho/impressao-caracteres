def imprimir_binario():
    for i in range(1, 6):
        for j in range(1, 6):
            if i % 2 == 0 and j % 2 == 0 or i % 2 != 0 and j % 2 != 0:
                print('0 ', end='')
            else:
                print('1 ', end='')
        print()

imprimir_binario()