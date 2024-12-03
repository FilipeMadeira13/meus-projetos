lista_de_compras = []

def adicionar_item(item):
    item = item.strip().lower()  # Remove espaços e padroniza
    if not item:
        print('Item inválido. Digite algo.\n')
        return
    if item in lista_de_compras:
        print(f'O item "{item}" já está na lista de compras.\n')
        return
    lista_de_compras.append(item)
    print(f'"{item}" adicionado à lista de compras.\n')

def remover_item(item):
    item = item.strip().lower()
    if item not in lista_de_compras:
        print(f'"{item}" não encontrado na lista.\n')
        return
    lista_de_compras.remove(item)
    print(f'"{item}" removido da lista de compras.\n')

def mostrar_lista():
    if not lista_de_compras:
        print('A lista de compras está vazia.\n')
        return
    print('Lista de compras:')
    for indice, item in enumerate(lista_de_compras, 1):
        print(f'{indice}. {item}')
    print()

def verificar_item(item):
    item = item.strip().lower()
    if item in lista_de_compras:
        print(f'"{item}" está na lista.\n')
        return True
    print(f'"{item}" não encontrado na lista.\n')
    return False

def ordenar_lista():
    lista_de_compras.sort()
    print('Lista de compras ordenada.\n')

def menu():
    while True:
        print("\n--- LISTA DE COMPRAS ---")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Mostrar lista")
        print("4. Verificar item")
        print("5. Ordenar lista")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            item = input("Digite o item a adicionar: ")
            adicionar_item(item)
        elif opcao == '2':
            item = input("Digite o item a remover: ")
            remover_item(item)
        elif opcao == '3':
            mostrar_lista()
        elif opcao == '4':
            item = input("Digite o item a verificar: ")
            verificar_item(item)
        elif opcao == '5':
            ordenar_lista()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Descomentar para iniciar o menu interativo
# menu()