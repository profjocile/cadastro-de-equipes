import random

nomes = []

def menu():
    print("1 - Adicionar nomes")
    print("2 - Gravar nomes")
    print("3 - Ler nomes")
    print("4 - Sortear nomes para equipe")
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

def criar_equipes(nomes):
    num_integrantes = int(input("Digite o número de integrantes (máximo 4): "))
    random.shuffle(nomes)
    equipe = [[] for _ in range(num_integrantes)]
    for i in range(num_integrantes):
        equipe[i % num_integrantes].append(nomes.pop())
    print(equipe)
    confirma = input("Confirma a criação das equipes? (S/N): ").lower()
    if confirma == "s":
        salvar_equipes(equipe)
    else:
        for i in range(num_integrantes):
            nomes.append(equipe.pop()) 
    return nomes

def salvar_equipes(equipe):
    with open("equipes.txt", "a") as arquivo:
        for nome in equipe:
            arquivo.write(", ".join(nome) + "\n")
    print("Equipe gravadas com sucesso!")

while True:
    opcao = menu()
    if opcao == 1:
        nomes = adicionar_nomes(nomes)
    elif opcao == 2:
        gravar_nomes(nomes)
    elif opcao == 3:
        ler_nomes(nomes)
    elif opcao == 4:
        nomes = criar_equipes(nomes)
    elif opcao == 0:
        break

# Exemplo de uso
# nomes = ["João", "Maria", "Pedro", "Ana", "Carlos", "Beatriz", "Lucas", "Fernanda"]
# num_equipes = 3
# equipes = criar_equipes(nomes, num_equipes)

# for i, equipe in enumerate(equipes):
#     print(f"Equipe {i+1}: {', '.join(equipe)}")
