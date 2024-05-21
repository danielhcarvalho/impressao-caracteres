def imprimir_carcacter():
    caractere = input('Digite um caractere para realizar a repetição:\n')
    quantidade = int(input('Informe quantas linhas e colunas deve ter a repetição:\n'))
    print()
    #repete a impressão do caractere com x linhas, de acordo com o número informado pelo usuário
    for i in range(1, quantidade + 1):
        #repete a impressão do caractere com y colunas, de acordo com o número informado pelo usuário
        for j in range(1, quantidade + 1):
            print(caractere, end=' ')
        print()
    
imprimir_carcacter()