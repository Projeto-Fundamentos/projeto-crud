import json
import os
import uuid


arquivo_funcionarios = "funcionarios.json"

def carregar_funcionarios():
#os.path.getsize(arquivo_funcionarios) > 0: Verifica se o arquivo não está vazio 
# antes de tentar carregá-lo. Caso o arquivo esteja vazio, a função carregar_funcionarios retornará uma lista vazia,
#  evitando o erro.
    if os.path.exists(arquivo_funcionarios) and os.path.getsize(arquivo_funcionarios) > 0:
        with open(arquivo_funcionarios, 'r') as file:
            return json.load(file)
    else:
        return []

def salvar_funcionario(funcionarios):
#Salva o funcionário inserido dicionário no arquivo json
    with open(arquivo_funcionarios, 'w') as file:
        json.dump(funcionarios, file, indent=4)

def add_funcionario():
    #função para adicionar funcionário no sistema
    id = str(uuid.uuid4())  # Gera um ID único como string
    nome = input("Insira o nome do funcionário:  ")
    idade = int(input("Insira a idade do funcionário:  "))
    cargo = input("Insira o cargo do funcionário:  ")

    funcionario = {
        "id_funcionario": id,
        "nome": nome,
        "idade": idade,
        "cargo": cargo
    } # dicionário que carregará as informações de cada funcionário, aparecendo dessa forma no JSON

    funcionarios = carregar_funcionarios()
    funcionarios.append(funcionario)
    salvar_funcionario(funcionarios)
    print("Funcionário cadastrado com sucesso!!")

def listar_funcionarios():
    #Função para que mostre todos os funcionários cadastrados até o momento
    funcionarios = carregar_funcionarios()

    if not funcionarios:
        #verifica se o arquivo JSON está vazio
        print("Nenhum funcionário cadastrado!")
    else:
        print("--- FUNCIONÁRIOS ---")
        for i, funcionario in enumerate(funcionarios, start=1):
            print(f"{i}. ID: {funcionario['id_funcionario']}\nNome: {funcionario['nome']}\nIdade: {funcionario['idade']}\nCargo: {funcionario['cargo']}")
            #Listará os funcionários cadastrados com suas informações
        print()

def excluir_funcionario():
    listar_funcionarios()
    funcionarios = carregar_funcionarios()

    if funcionarios:
        try:
            indice = int(input("Digite o número do funcionário a ser excluído: ")) - 1
            if 0 <= indice < len(funcionarios):
                funcionario_removido = funcionarios.pop(indice)
                salvar_funcionario(funcionarios)
                print(f"Funcionário '{funcionario_removido['nome']}' excluído com sucesso!!")
            else:
                print("Número inválido.")
        except ValueError:
            print("Por favor, insira um número válido!")


def atualizar_funcionario():
    # Carregar a lista atual de funcionários
    funcionarios = carregar_funcionarios()
    
    # Listar os funcionários para o usuário escolher qual atualizar
    listar_funcionarios()
    
    if funcionarios:
        # Solicitar o número do funcionário a ser atualizado
        indice = input("Digite o número do funcionário a ser atualizado: ")

        # Verificar se o número é um dígito e corresponde a um índice válido
        if indice.isdigit():
            indice = int(indice) - 1
            if 0 <= indice < len(funcionarios):
                funcionario = funcionarios[indice]

                # Exibir as informações atuais do funcionário
                print(f"\nAtualizando informações de {funcionario['nome']}")

                # Solicitar novos dados do usuário
                novo_nome = input("Novo nome (ou pressione Enter para manter o atual): ")
                nova_idade = input("Nova idade (ou pressione Enter para manter a atual): ")
                novo_cargo = input("Novo cargo (ou pressione Enter para manter o atual): ")

                # Atualizar os campos somente se o usuário inserir um novo valor
                if novo_nome:
                    funcionario['nome'] = novo_nome
                if nova_idade and nova_idade.isdigit():
                    funcionario['idade'] = int(nova_idade)
                if novo_cargo:
                    funcionario['cargo'] = novo_cargo

                # Salvar a lista de funcionários atualizada
                salvar_funcionario(funcionarios)
                print(f"Funcionário '{funcionario['nome']}' atualizado com sucesso!\n")
            else:
                print("Número inválido. Tente novamente.")
        else:
            print("Entrada inválida. Por favor, insira um número válido.")


def menu():
    while True:
        print("1. Cadastrar Funcionário")
        print("2. Listar Funcionários")
        print("3. Excluir Funcionário")
        print("4. Atualizar Funcionário")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            add_funcionario()
        elif opcao == '2':
            listar_funcionarios()
        elif opcao == '3':
            excluir_funcionario()
        elif opcao == '4':
            atualizar_funcionario()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

menu()
