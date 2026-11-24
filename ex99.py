print("Algoritmo que solicite para o usuário o nome e idade de 10 pessoas")
print()
pessoas = []

for i in range(10):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    pessoa = (nome, idade)
    pessoas.append(pessoa)

print("\nPessoas com menos de 18 anos:")

for pessoa in pessoas:
    if pessoa[1] < 18:
        print(pessoa[0], "-", pessoa[1], "anos")

print("\nPessoas com 18 anos ou mais:")

for pessoa in pessoas:
    if pessoa[1] >= 18:
        print(pessoa[0], "-", pessoa[1], "anos")