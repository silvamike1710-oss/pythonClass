# dicionario estoque
estoque = {}

# funções

def adicionar():
    nome = input("nome do produto: ").strip()

    if nome in estoque:
        print("produto já adicionado")
        return
    
    try:
        quantidade = int(input("quantidade: "))
        preco = float(input("preço: "))
    except ValueError:
        print("valor invalido")
        return
    
    estoque[nome] = {
        "quantidade": quantidade,
        "preço": preco
    }

    print("produto adicionado")


def lista():
    if not estoque:
        print("estoque vazio")
        return
    
    print("\n--- produtos ---")

    # ordenação com lambda
    for nome, dados in sorted(estoque.items(), key=lambda item: item[0]):
        print(f"{nome}: {dados['quantidade']} unidades - R$ {dados['preço']:.2f}")


def remover():
    nome = input("remover produto: ").strip()

    if nome in estoque:
        del estoque[nome]
        print("produto removido")
    else:
        print("produto não encontrado")


def atualizarQuantidade():
    nome = input("nome do produto: ").strip()

    if nome not in estoque:
        print("produto não encontrado")
        return

    try:
        quantidadeAtualizada = int(input("atualizar quantidade: "))
    except ValueError:
        print("valor invalido")
        return
        
    estoque[nome]["quantidade"] = quantidadeAtualizada
    print("quantidade atualizada")


def menu():
    while True:
        print("\n---MENU---")
        print("1 - adicionar produto")
        print("2 - listar produto")
        print("3 - remover produto")
        print("4 - atualizar produto")
        print("5 - sair")
        
        opcao = input("escolha uma opcao: ")

        if opcao == "1":
            adicionar()
        elif opcao == "2":
            lista()
        elif opcao == "3":
            remover()
        elif opcao == "4":
            atualizarQuantidade()
        elif opcao == "5":
            print("encerrando")
            break
        else:
            print("opção invalida")


menu()