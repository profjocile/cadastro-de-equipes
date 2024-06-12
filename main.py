import random

nomes = []
nomes_equipes = []

def menu():
    print("1 - Adicionar nomes")
    print("2 - Gravar nomes")
    print("3 - Ler nomes")
    print("4 - Sortear nomes para equipe")
    print("5 - Ler nomes da equipe")
    print("0 - Sair")
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

def ler_nomes(nomes):
    with open("nomes.txt", "r") as arquivo:
        for nome in arquivo:
            nomes.append(nome.strip())
    for nome in nomes:
        print(nome)
    quantos_nomes = len(nomes)
    print(f"{quantos_nomes} Nomes lidos com sucesso!")

def criar_equipes(nomes, nomes_equipes):
    num_integrantes = 5
    while num_integrantes > 4:
        num_integrantes = int(input(f"Digite o número de integrantes (máximo 4 de {len(nomes)}): "))
    if num_integrantes > len(nomes):
        num_integrantes = len(nomes)
    random.shuffle(nomes)
    equipe = [[] for _ in range(num_integrantes)]
    for i in range(num_integrantes):
        equipe[i % num_integrantes].append(nomes.pop())
    print(equipe)
    confirma = input("Confirma a criação das equipes? (S/N): ").lower()
    if confirma == "s":
        nome_equipe = input("Digite o nome da equipe: ")
        with open(f"{nome_equipe}.txt", "w") as arquivo:
            for nome in equipe:
                arquivo.write(", ".join(nome) + "\n")
        nomes_equipes.append(nome_equipe)
        print("Equipe gravadas com sucesso!")
    else:
        for i in range(num_integrantes):
            nomes.append(equipe.pop()) 
    return nomes, nomes_equipes

def mostrar_equipes(nomes_equipes):
    for nome_equipe in nomes_equipes:
        with open(f"{nome_equipe}.txt", "r") as arquivo:
            print('=' * 10)
            print(f"Equipe {nome_equipe}:")
            for nome in arquivo:
                print(nome.strip())
    print(f"{len(nomes_equipes)} equipes criadas com sucesso!")

# Programa principal

while True:
    opcao = menu()
    if opcao == 1:
        nomes = adicionar_nomes(nomes)
    elif opcao == 2:
        gravar_nomes(nomes)
    elif opcao == 3:
        ler_nomes(nomes)
    elif opcao == 4:
        nomes, nomes_equipes = criar_equipes(nomes, nomes_equipes)
    elif opcao == 5:
        mostrar_equipes(nomes_equipes)
    elif opcao == 0:
        break
