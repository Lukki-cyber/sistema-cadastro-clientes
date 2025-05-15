clientes = []

def cadastrar_cliente():
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    cliente = {
        "id": len(clientes) + 1,
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "endereco": endereco
    }
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!\n")

def listar_clientes():
    for cliente in clientes:
        print(f"ID: {cliente['id']} | Nome: {cliente['nome']} | Email: {cliente['email']}")

def excluir_cliente():
    id_excluir = int(input("Digite o ID do cliente para excluir: "))
    for cliente in clientes:
        if cliente["id"] == id_excluir:
            clientes.remove(cliente)
            print("Cliente excluído com sucesso!\n")
            return
    print("Cliente não encontrado.\n")

def menu():
    while True:
        print("1. Cadastrar Cliente")
        print("2. Listar Clientes")
        print("3. Excluir Cliente")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            excluir_cliente()
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")

menu()
