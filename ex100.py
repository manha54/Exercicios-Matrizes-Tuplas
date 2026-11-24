print("Algoritmo que solicite os valores de uma matriz de tamanho 3 x 3")
print()

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

identidade = True

for i in range(3):
    for j in range(3):
        if i == j:
            if matriz[i][j] != 1:
                identidade = False
        else:
            if matriz[i][j] != 0:
                identidade = False

if identidade:
    print("A matriz é identidade.")
else:
    print("A matriz não é identidade.")