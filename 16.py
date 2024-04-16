lanches = {
    '1': {'produto': 'Cachorro quente', 'preco': 8.10},
    '2': {'produto': 'Bauru simples', 'preco': 11.30},
    '3': {'produto': 'Bauru c/ ovo', 'preco': 15.50},
    '4': {'produto': 'Hamburguer', 'preco': 13.10},
    '5': {'produto': 'Cheeseburguer', 'preco': 14.30},
    '6': {'produto': 'Refrigerante', 'preco': 5}
}

for lanche, descricao in lanches.items():
    # print(lanche)
    print()

    for info in descricao.values():
        print(lanche, info)
        # print()
total = 0 

while True:
    pedido = input("Digite o numero do pedido: ")
    amount = int(input('Digite a quantidade: '))
    

    if pedido in lanches:
        # print(lanches[pedido])
        total += lanches[pedido]['preco']*amount
        # print(f'{total}')
    else:
        print('Não tem este produto')
        
    continuar = input('Deseja algo mais? (Y/N) ').lower()

    if continuar == 'y':
        continue
    elif continuar == 'n':
        print(f'O valor da conta é de:R${total:.2f}')
        break
    else:
        print('Saindo...')
        break

        

    
    

    
   