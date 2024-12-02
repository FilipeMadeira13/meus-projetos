estoque = []

def adicionar_produto(nome, quantidade, preco):
    for produto in estoque:
        if produto['nome'] == nome:
            print('O produto já está no estoque\n')
            return
    estoque.append({'nome': nome, 'quantidade': quantidade, 'preco' : preco})
    print(f'{nome} adicionado ao estoque\n')

def atualizar_quantidade(nome, quantidade):
    if quantidade < 0:
        print(f'Não é permitido inserir quantidades negativas.\n')
        return
    for produto in estoque:
        if produto['nome'] == nome:
            produto['quantidade'] += quantidade
            print(f'Foram adicionados {quantidade} unidades de {nome}')
            return
    print(f'Produto não encontrado no estoque\n')

def remover_produto(nome, quantidade):
    for produto in estoque:
        if produto['nome'] == nome:
            if quantidade > produto['quantidade']:
                print(f'Estoque insuficiente de {nome}\n')
            else:
                produto['quantidade'] -= quantidade
                print(f'Removido {quantidade} unidades de {nome}\n')

            if produto['quantidade'] == 0:
                estoque.remove(produto)
                print(f'Nenhuma unidade de {nome} no estoque\n')
            return            
    print('Produto não encontrado\n')

def mostrar_produtos():
    if not estoque:
        print('O estoque está vazio\n')
        return
    print('Produtos:\n')
    for produto in estoque:
        print(f"- {produto['nome']}: {produto['quantidade']} unidades. Preço: R$ {produto['preco']:.2f}")
    print()

def calcular_valor_total():
    total = 0
    for produto in estoque:
        total += produto['preco'] * produto['quantidade']
    print(f'Valor total do estoque: R$ {total:.2f}\n')

adicionar_produto('Feijão', 2, 6.5)
adicionar_produto('Arroz', 5, 8.5)

mostrar_produtos()
calcular_valor_total()