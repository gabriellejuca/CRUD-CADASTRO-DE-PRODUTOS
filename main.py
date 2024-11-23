banco_de_dados = [
  {
    "codigo": 1,
    "nome" : "mouse",
    "preco" :150.50,
    "disponivel": True
  }
]

codigo_atual = 1
def cadastrar_produto(nome:str, preco: float) -> None:
  global codigo_atual
  codigo_atual += 1

  produto = {
    "codigo" : codigo_atual,
    "nome": nome,
    "preco": preco,
    "disponivel": True 
  }
  banco_de_dados.append(produto)
  print("Produto adicionado com sucesso!")

def listar_produtos():
  print('----PRODUTOS CADASTRADOS ----')
  for produto in banco_de_dados:
    print(f"Código :{produto ['codigo']}")
    print(f"Nome: {produto ['nome']}")
    print(f"Preco: {produto ['preco']}")
    print(f"disponivel: {produto ['disponivel']}")
    print('-'*50)

def buscar_produtos(codigo:int):
  for produto in banco_de_dados:
    if produto['codigo'] == codigo:
      return produto
  return None

def deletar_produto(codigo: int):
  produto = buscar_produtos(codigo)
  if produto:
    banco_de_dados.remove(produto)
    print('produto removido com sucesso!')
    return
  print('produto não encontrado!')

cadastrar_produto("fone de ouvido", 59.99)
listar_produtos()
deletar_produto(1)
print(banco_de_dados)
deletar_produto(-1)

def menu():
  print('--- BEM VINDO AO MENU ---')
  while True:
    print('1 - adicionar produto')
    print('2 - editar produto')
    print('3 - listar produtos')
    print('4 - buscar produto')
    print('5 - deletar produto')
    print('0 - sair ')
    opcao = input('selecione uma opção: ')
    if opcao == '1':
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            cadastrar_produto(nome, preco)
    
    elif opcao == '2':
            codigo = int(input("Código do produto a editar: "))
            produto = buscar_produtos(codigo)
            if produto:
                novo_nome = input("Novo nome do produto (ou deixar vazio para não alterar): ")
                novo_preco = input("Novo preço do produto (ou deixar vazio para não alterar): ")
                if novo_nome:
                    produto['nome'] = novo_nome
                if novo_preco:
                    produto['preco'] = float(novo_preco)
                print("Produto editado com sucesso!")
            else:
                print("Produto não encontrado!")
        
    elif opcao == '3':
            listar_produtos()
        
    elif opcao == '4':
            codigo = int(input("Código do produto a buscar: "))
            produto = buscar_produtos(codigo)
            if produto:
                print(produto)
            else:
                print("Produto não encontrado!")
        
    elif opcao == '5':
            codigo = int(input("Código do produto a deletar: "))
            deletar_produto(codigo)
        
    elif opcao == '0':
            print("Saindo do sistema...")
            break
    else:
            print("Opção inválida! Tente novamente.")