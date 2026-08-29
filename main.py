doacoes = []


def cadastrar_doacao():
    print("\n--- CADASTRAR DOAÇÃO ---")

    doador = input("Nome do doador: ")
    item = input("Tipo de doação: ")
    quantidade = int(input("Quantidade: "))

    doacao = {
        "doador": doador,
        "item": item,
        "quantidade": quantidade
    }

    doacoes.append(doacao)

    print("\nDoação cadastrada com sucesso!")


def listar_doacoes():
    print("\n--- DOAÇÕES CADASTRADAS ---")

    if len(doacoes) == 0:
        print("Nenhuma doação cadastrada.")
        return

    for doacao in doacoes:
        print(
            f"Doador: {doacao['doador']} | "
            f"Item: {doacao['item']} | "
            f"Quantidade: {doacao['quantidade']}"
        )


def menu():
    while True:
        print("\n==============================")
        print("      SISTEMA DE DOAÇÕES")
        print("==============================")
        print("1 - Cadastrar doação")
        print("2 - Listar doações")
        print("3 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_doacao()

        elif opcao == "2":
            listar_doacoes()

        elif opcao == "3":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


menu()
