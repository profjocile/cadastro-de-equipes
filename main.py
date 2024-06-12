import random

nomes = []

def menu():
    print("1 - Adicionar nomes")
    print("2 - Gravar nomes")
    print("3 - Sair")
    opcao = int(input("Digite a opção: "))
    return opcao

def adicionar_nomes(nomes):

    while True:
        nomes.append(input("Digite um nome: "))
        continua = input("Digite 'S' para continuar: ").lower()
        if continua!= "s":
            break
    return nomes

def gravar_nomes(nomes):
    with open("nomes.txt", "w") as arquivo:
        for nome in nomes:
            arquivo.write(nome + "\n")
    print("Nomes gravados com sucesso!")

def criar_equipes(nomes, num_equipes):
    random.shuffle(nomes)
    equipes = [[] for _ in range(num_equipes)]
    for i, nome in enumerate(nomes):
        equipes[i % num_equipes].append(nome)
    return equipes

while True:
    opcao = menu()
    if opcao == 1:
        nomes = adicionar_nomes(nomes)
    elif opcao == 2:
        gravar_nomes(nomes)
    elif opcao == 0:
        break

# Exemplo de uso
# nomes = ["João", "Maria", "Pedro", "Ana", "Carlos", "Beatriz", "Lucas", "Fernanda"]
# num_equipes = 3
# equipes = criar_equipes(nomes, num_equipes)

# for i, equipe in enumerate(equipes):
#     print(f"Equipe {i+1}: {', '.join(equipe)}")
