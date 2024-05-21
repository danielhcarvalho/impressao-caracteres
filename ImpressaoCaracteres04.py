def imprimir_caractere():
    caractere = input('Digite um caractere para realizar a repetição:\n')

    for i in range(1, 3):
        for j in range(1, 9):
            for l in range(1, pow(2, j - 1)):
                print(caractere, end='')
            print()

        for j in range(7, 0, -1):
            for l in range(1, pow(2, j - 1)):
                print(caractere, end='')
            print()

imprimir_caractere()
