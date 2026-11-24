print("Algoritmo que solicite o valor de 2 matrizes de tamanho  4 x 3")
print()

matriz1 = []
matriz2 = []
matriz3 = []

print("Digite os valores da primeira matriz:")

for i in range(4):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite [{i}][{j}]: "))
        linha.append(valor)
    matriz1.append(linha)

print("Digite os valores da segunda matriz:")

for i in range(4):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite [{i}][{j}]: "))
        linha.append(valor)
    matriz2.append(linha)

for i in range(4):
    linha = []
    for j in range(3):
        soma = matriz1[i][j] + matriz2[i][j]
        linha.append(soma)
    matriz3.append(linha)

print("Resultado da soma:")

for linha in matriz3:
    print(linha)