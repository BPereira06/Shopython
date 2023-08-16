from time import sleep
print('-=' *16)
print(' BEM VINDO A loja do Breno ')
print('-=' *16)

lista = []
while True:

    print("""
    [1] Adicionar produto
    [2] Remover produto
    [3] Mostrar Catálogo
    [0] Sair
    """)
    opcao= int(input("Digite uma opção [0-3]: "))

    if opcao== 0:
        break

    elif opcao == 1:
        nome=input("Nome do produto: ")
        preço=input("Preço do produto: ")
        produto={"nome": nome, "preço": preço}
        lista.append(produto)
        print(f"{nome} foi adicionado")

    elif opcao== 2:
        nome =input("Ditige o nome do produto que deseja remover: ")

        produto_encontrado = False
        for produto in lista:
            if produto["nome"] == nome:
                lista.remove(produto)
                print(f"{produto} foi removido.")
                produto_encontrado = True
                break
        if produto_encontrado == False:
            print(f"{produto} não foi encontrado.")


    elif opcao == 3:
        print("\n CATÁLOGO:")
        for produto in lista:
            print(f"Nome: {produto['nome']}")
            print(f"Preço: {produto['preço']}")
    else:
        print("Opção Inválida")