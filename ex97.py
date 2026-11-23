print("Algoritmo para calcular o determinante de uma matriz")
print()

matriz = []

for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input(f"Digite o valor [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

determinante = (matriz[0][0] * matriz[1][1]) - (matriz[0][1] * matriz[1][0])

print("Matriz:")
for linha in matriz:
    print(linha)

print("Determinante:", determinante)