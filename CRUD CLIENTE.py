import json
import os
import uuid

clientes = os.path.join(os.path.dirname(__file__), 'clientes.json')
#carregar clientes
def carregar_clientes():
    if not os.path.exists(clientes):
        with open(clientes, 'w') as f:
            json.dump([], f, indent=4)
    with open(clientes, 'r') as f:
        return json.load(f)
#gerar ID do cliente
def gerar_id():
    return str(uuid.uuid4())

#Create
def adicionar_cliente(nome_cliente, telefone_cliente, endereco_cliente, idade_cliente, pet_adotado = 0):
    print(os.path.dirname(__file__))
    cliente = {
        "numid": gerar_id(),
        "nome": nome_cliente,
        "telefone": telefone_cliente,
        "endereço": endereco_cliente,
        "idade": idade_cliente,
        "pet_adotado": pet_adotado
        
    }
    novo_cliente = carregar_clientes()
    novo_cliente.append(cliente)
    with open(clientes, 'w') as f:
        json.dump(novo_cliente, f, indent=4)

#Read
def listar_clientes():
    clientes = carregar_clientes()
    opcao = int(input('1: Listar cliente por nome\n2: Achar cliente pelo ID\nOpção(1/2): '))
    match opcao:
        case 1:
            cliente_por_nome = sorted(clientes, key=lambda cliente: (cliente['nome']))
            for key in cliente_por_nome:
                print('-'*150)
                print(key)
            print('-'*150)
            return cliente_por_nome
        case 2:
            entrada = input('Digite o ID do cliente: ')
            for key in clientes:
                if entrada == key['numid']:
                    print(f'ID: {key['numid']}\nNome: {key['nome']}\nTelefone: {key['telefone']}\nEndereço: {key['endereço']}\nPet adotado: {key['pet_adotado']}')
        case __:
            print('Opção invalida.')
            listar_clientes() 

#Update
def atualizar_cliente():
    lista_clientes = carregar_clientes()
    entrada = input('Digite o nome ou ID do cliente: ')
    for key in lista_clientes:
        if entrada == key['nome'] or entrada == key['numid']:
            nome = input('Nome do cliente atualizado: ')           
            telefone = input('Telefone do cliente atualizado: ')            
            endereco = input('Endereço do cliente atualiziado: ')           
            while True:
                try:
                    idade = int(input('Idade do cliente atualizada: '))
                    break
                except ValueError:
                    print('Erro: Por favor, digite um número inteiro: ')   
            pet_adotado = 0
            key['nome'] = nome
            key['telefone'] = telefone
            key['endereço'] = endereco
            key['idade'] = idade
            key['pet_adotado'] = pet_adotado
            with open(clientes, 'w') as f:
                json.dump(lista_clientes, f, indent=4)
            print('CLIENTE ATUALIZADO!')
            break   

#Delete
def deletar_cliente(entrada):
    cliente = carregar_clientes()
    for key in cliente:
        if entrada == key['numid'] or entrada == key['nome']:
            cliente.remove(key)
            print('CLIENTE REMOVIDO!')
            break
    with open(clientes, 'w') as f:
        json.dump(cliente, f, indent=4)
     

#teste
while (True):
    escolha = int(input('1: Adicionar cliente\n2: Procurar cliente\n3: Atualizar cliente\n4: Deletar cliente\nOpção:(1/2/3/4): '))
    if escolha == 1:
        nome = input('Digite o nome: ')
        telefone = input('Digite o telefone: ')
        endereco = input('Digite o endereco: ')
        idade = input('Digite o idade: ')
        adicionar_cliente(nome, telefone, endereco, idade)
    elif escolha == 2:
        listar_clientes()
    elif escolha == 3:
        atualizar_cliente()
    elif escolha == 4:
        entrada = input('Digite o nome ou id do cliente: ')
        deletar_cliente(entrada)
    else:
        break    
                      

