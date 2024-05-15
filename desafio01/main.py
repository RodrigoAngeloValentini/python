agenda = []

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    agenda.append({"Nome": nome, "Telefone": telefone, "Email": email, "Favorito": False})

def listar_contatos():
    for i in range(len(agenda)):
        contato = agenda[i]
        print(f"Contato {i+1}:")
        for chave, valor in contato.items():
            print(f"{chave}: {valor}")
        print()

def editar_contato():
    indice = int(input("Digite o índice do contato que deseja editar: ")) - 1
    contato = agenda[indice]
    nome = input("Digite o novo nome do contato: ")
    telefone = input("Digite o novo telefone do contato: ")
    email = input("Digite o novo email do contato: ")
    contato["Nome"] = nome
    contato["Telefone"] = telefone
    contato["Email"] = email

def marcar_desmarcar_favorito():
    indice = int(input("Digite o índice do contato que deseja marcar/desmarcar como favorito: ")) - 1
    contato = agenda[indice]
    contato["Favorito"] = not contato["Favorito"]

def listar_favoritos():
    favoritos = [contato for contato in agenda if contato["Favorito"]]
    if favoritos:
        print("Contatos Favoritos:")
        for i in range(len(favoritos)):
            contato = favoritos[i]
            print(f"Contato {i+1}:")
            for chave, valor in contato.items():
                print(f"{chave}: {valor}")
            print()
    else:
        print("Nenhum contato favorito encontrado.")

def apagar_contato():
    indice = int(input("Digite o índice do contato que deseja apagar: ")) - 1
    del agenda[indice]

def menu():
    print("\nEscolha uma opção:")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Editar contato")
    print("4 - Marcar/Desmarcar como favorito")
    print("5 - Listar contatos favoritos")
    print("6 - Apagar contato")
    print("0 - Sair")

def main():
    while True:
        menu()
        escolha = input("Digite o número da opção desejada: ")
        if escolha == "1":
            adicionar_contato()
        elif escolha == "2":
            listar_contatos()
        elif escolha == "3":
            editar_contato()
        elif escolha == "4":
            marcar_desmarcar_favorito()
        elif escolha == "5":
            listar_favoritos()
        elif escolha == "6":
            apagar_contato()
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

main()