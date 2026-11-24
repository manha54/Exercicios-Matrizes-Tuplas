print("Algoritmo que solicite os valores de uma matriz de tamanho 3 x 3.")
print()

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

determinante = (
    matriz[0][0] * matriz[1][1] * matriz[2][2]
    + matriz[0][1] * matriz[1][2] * matriz[2][0]
    + matriz[0][2] * matriz[1][0] * matriz[2][1]
    - matriz[0][2] * matriz[1][1] * matriz[2][0]
    - matriz[0][1] * matriz[1][0] * matriz[2][2]
    - matriz[0][0] * matriz[1][2] * matriz[2][1]
)

print("Matriz:")

for linha in matriz:
    print(linha)

print("Determinante:", determinante)