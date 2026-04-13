import os
import pandas as pd
import time

dados_pets = []  # lista para armazenar os dados dos pets cadastrados


def menu():
    os.system("cls")

    print("Bem Vindo ao Pet Shop, escolha uma dos nossos serviços abaixo: ")
    print("1 - Cadastrar Pet")
    print("2 - Listar Pets")
    print("3 - Alterar Pets")
    print("4 - Excluir pets")
    print("5 - EXCLUIR TODOS OS REGISTROS")
    print("6 - SAIR")


def retornarMenu():
    input("\nPressione Enter para retornar ao menu principal...")
    main()


def escolha():
    while True:
        try:
            escolha = int(input("Digite a opção desejada: "))
            if escolha in range(1, 7):
                return escolha
            else:
                print("Opção inválida. Por favor, escolha uma opção entre 1 e 6.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um valor númerico inteiro.")


def cadastrarPet():  # função para cadastrar pet e armazenar os dados em uma lista ou banco de dados
    while True:
        os.system("cls")
        print("CADASTRAR PET:")
        while True:
            nome = str(input("Digite o nome do pet: "))
            if nome.isalpha():
                break
            else:
                print("Nome inválido. Por favor, utilize apenas letras.")
                time.sleep(1.5)
                os.system("cls")
                print("CADASTRAR PET:")

        while True:
            tipo = str(
                input("Digite o tipo do pet (ex: cachorro, gato, etc.): "))
            if tipo.isalpha():
                break
            else:
                print("Tipo inválido. Por favor, utilize apenas letras.")
                time.sleep(1.5)
                os.system("cls")
                print("CADASTRAR PET:")

        while True:
            try:
                idade = int(input("Digite a idade do pet: "))
                break
            except ValueError:
                print("Idade inválida. Por favor, digite um valor numérico inteiro.")
                time.sleep(1.5)
                os.system("cls")
                print("CADASTRAR PET:")
        # Armazena os dados do pet na lista
        dados_pets.append({"nome": nome, "tipo": tipo, "idade": idade})
        print(
            f"\nPet cadastrado com sucesso!\nNome: {nome.ljust(10)} | Tipo: {tipo.ljust(10)} | Idade: {idade}\n")
        break
    retornarMenu()


def alterarPets():
    os.system("cls")
    print("ALTERAR PETS:")
    nome_pet = input("Digite o nome do pet que deseja alterar: ")
    for dado in dados_pets:
        if dado["nome"] == nome_pet:
            while True:
                novo_nome = input("Digite o novo nome do pet: ")
                if novo_nome.isalpha():
                    break
                else:
                    print("Nome inválido. Por favor, utilize apenas letras.")
                    time.sleep(1.5)
                    os.system("cls")
                    print("ALTERAR PETS:")

            while True:
                novo_tipo = input("Digite o novo tipo do pet: ")
                if novo_tipo.isalpha():
                    break
                else:
                    print("Tipo inválido. Por favor, utilize apenas letras.")
                    time.sleep(1.5)
                    os.system("cls")
                    print("ALTERAR PETS:")
            while True:
                try:
                    nova_idade = int(input("Digite a nova idade do pet: "))
                    break
                except ValueError:
                    print(
                        "Idade inválida. Por favor, digite um valor numérico inteiro.")
                    time.sleep(1.5)
                    os.system("cls")
                    print("ALTERAR PETS:")

            # Atualiza os dados do pet na lista
            dado["nome"] = novo_nome
            dado["tipo"] = novo_tipo
            dado["idade"] = nova_idade
            # muda o nome do pet para o novo nome, tipo e idade para o novo tipo e idade
            dadosAtualizados = {"nome": novo_nome,
                                "tipo": novo_tipo, "idade": nova_idade}
            dados_pets[dados_pets.index(dado)] = dadosAtualizados

            print(
                f"Pet alterado com sucesso!\nNovo Nome: {novo_nome.ljust(10)} | Novo Tipo: {novo_tipo.ljust(10)} | Nova Idade: {nova_idade}")
            break
    else:
        print("Pet não encontrado.")
    retornarMenu()


def listarPets():
    os.system("cls")
    print("LISTAR PETS:")
    for dado in dados_pets:
        nome = dado["nome"]
        tipo = dado["tipo"]
        idade = dado["idade"]
        print(f"Nome: {nome.ljust(10)} Tipo: {tipo.ljust(10)} Idade: {idade}")
    retornarMenu()


def excluirPet():
    os.system("cls")
    print("EXCLUIR PET:")
    nome_pet = input("Digite o nome do pet que deseja excluir: ")
    for dado in dados_pets:
        if dado["nome"] == nome_pet:
            dados_pets.remove(dado)
            print(f"Pet '{nome_pet}' excluído com sucesso!")
            break
    else:
        print("Pet não encontrado.")
    retornarMenu()

def excluirTodosPets():
    os.system("cls")
    print("EXCLUIR TODOS OS PETS:")
    confirmacao = input("Tem certeza que deseja excluir todos os pets? (s/n): ")
    if confirmacao.lower() == 's':
        dados_pets.clear()
        print("Todos os pets foram excluídos com sucesso!")
    else:
        print("Operação cancelada.")
    retornarMenu()
    
def acessarEscolha(escolha):
    if escolha == 1:
        cadastrarPet()
    elif escolha == 2:
        listarPets()
    elif escolha == 3:
        alterarPets()
    elif escolha == 4:
        excluirPet()
    elif escolha == 5:
        excluirTodosPets()
    elif escolha == 6:
        print("Saindo do programa...")
        time.sleep(1)
        os.system("cls")
        exit()
    


def main():
    os.system("cls")
    menu()
    escolha_usuario = escolha()
    acessarEscolha(escolha_usuario)


if __name__ == "__main__":
    main()
