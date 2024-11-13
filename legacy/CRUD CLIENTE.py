import json
import os


arquivo_clientes = os.path.join(os.path.dirname(__file__), 'clientes.json') 

def carregar_clientes():
    
    if os.path.exists(arquivo_clientes) and os.path.getsize(arquivo_clientes) > 0:
        with open(arquivo_clientes, 'r') as file:
            return json.load(file)  
    else:
        return {}

def salvar_cliente(clientes):
    
    with open(arquivo_clientes, 'w') as file:
        json.dump(clientes, file, indent=4)  

def gerar_id_cliente(clientes):
    
    if clientes:
        maxId = max(int(id_cliente) for id_cliente in clientes.keys())
        return str(maxId + 1)
    return "1" 

def adicionar_cliente():
    
    clientes = carregar_clientes()
    id_cliente = gerar_id_cliente(clientes)  
    nome = input("Nome do cliente:  ")
    telefone = input("Telefone do cliente: ")
    endereco = input("Endereço do cliente: ")
    idade = int(input("Idade do cliente:  "))
    adotado = 0

    cliente = {
        "nome": nome,
        "telefone": telefone,
        "endereco":endereco,
        "idade": idade,
        "adotado": adotado
    }

    clientes[id_cliente] = cliente
    salvar_cliente(clientes)
    print("Cliente cadastrado!")

def listar_clientes():
    
    clientes = carregar_clientes()

    if not clientes:
        print("Nenhum cliente cadastrado!")
    else:
        print("------ CLIENTES ------")
        for id_cliente, dados in clientes.items():
            print(f"ID: {id_cliente}\nNome: {dados['nome']}\nTelefone: {dados['telefone']}\nEndereco {dados['endereco']}\nIdade: {dados['idade']}\nAdotado {dados['adotado']}")
        print()

def atualizar_cliente():
    
    clientes = carregar_clientes()
    listar_clientes()
    
    if clientes:
        id_cliente = input("Digite o ID do cliente a ser atualizado: ")
        
        if id_cliente in clientes:
            print(f"\nAtualizando informações de {clientes[id_cliente]['nome']}")
            
            novo_nome_cliente = input("Novo nome do cliente: ")
            novo_telefone_cliente = input("Novo telefone do cliente: ")
            novo_endereco_cliente = input("Novo endereço: ")
            nova_idade_cliente = input("Nova idade do cliente: ")
            novo_pet_cliente = input("Novo pet do cliente: ")

            if novo_nome_cliente:
                clientes[id_cliente]['nome'] = novo_nome_cliente
            if novo_telefone_cliente:
                clientes[id_cliente]['telefone'] = novo_telefone_cliente
            if novo_endereco_cliente:
                clientes[id_cliente]['endereco'] = novo_endereco_cliente        
            if nova_idade_cliente and nova_idade_cliente.isdigit():
                clientes[id_cliente]['idade'] = int(nova_idade_cliente)
            if novo_pet_cliente:
                clientes[id_cliente]['adotado'] = novo_pet_cliente

            salvar_cliente(clientes)
            print(f"Cliente '{clientes[id_cliente]['nome']}' atualizado com sucesso!\n")
        else:
            print("Cliente não encontrado.") 

def deletar_cliente():
    
    clientes = carregar_clientes()
    listar_clientes()

    if clientes:
        id_cliente = input("Digite o ID do cliente a ser excluído: ")
        
        if id_cliente in clientes:
            del clientes[id_cliente]  
            salvar_cliente(clientes)
            print(f"Cliente '{id_cliente}' excluído com sucesso!")
        else:
            print("Cliente não encontrado.")

def menu():
   
    while True:
        print("1. Cadastrar Cliente")
        print("2. Listar Clientes")
        print("3. Atualizar Clientes")
        print("4. Excluir Clientes")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_cliente()
        elif opcao == '2':
            listar_clientes()
        elif opcao == '3':
            atualizar_cliente()
        elif opcao == '4':
            deletar_cliente()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção indisponível! Tente novamente por favor.\n")

menu()



