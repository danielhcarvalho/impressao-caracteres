def imprimir_caractere():
    caractere = input('Digite um caractere para realizar a repetição:\n')
    quantidade = int(input(f'Informe quantas vezes o caractere {caractere} deve se repetir:\n'))
    print()

    for i in range(1, quantidade + 1):
        for j in range(1, quantidade + 1):
            for l in range(1, j + 1):
                print(caractere, end=' ')
            print()
        
        for j in range(quantidade, 0, -1):
            for l in range(1, j + 1):
                print(caractere, end=' ')
            print()

imprimir_caractere()