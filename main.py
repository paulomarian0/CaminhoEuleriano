

print("Caminho Euleriano")


## array do exemplo usado na aula
array = ([[0, 2, 1, 0, 0],
          [2, 0, 1, 0, 0],
          [1, 1, 0, 1, 1],
          [0, 0, 1, 0, 2],
          [0, 0, 1, 2, 0]])


def InserirMatriz():
    for i in range(len(array)):
        for j in range(len(array)):
            array[i][j] = float(input('a[' + str(i) + '][' + str(j) + ']='))


def CaminhoEuleriano():
    soma = 0
    impares = 0

    ## declaracao da matriz
    for i in range(len(array)):
        for j in range(len(array)):
            soma += array[i][j]  ## somando a quantidade de ligações de vertice

        # verificaça~o se é impar
        if soma % 2 != 0:
            impares += 1
        soma = 0  ##reseta a veriavel da soma pra 0

    print("\nTipo de grafo:")

    if (impares == 2 or impares == 0):
        print("O grafo possui um caminho euleriano")
    else:
        print("O grafo não possui um caminho euleriano")


def ExibirMatriz():
    print("Matriz:")
    for i in range(len(array)):
        print(array[i])


if __name__ == '__main__':
    # PARA INSERIR MATRIZ BASTA DESCOMENTAR ESSA LINHA
    # InserirMatriz()

    ExibirMatriz()

    CaminhoEuleriano()
