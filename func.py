import json
import os

# Define o caminho para o arquivo JSON onde os dados dos funcionários serão salvos
arquivo_funcionarios = os.path.join(os.path.dirname(__file__), 'funcionarios.json')
def carregar_funcionarios():
    
   # Carrega os funcionários do arquivo JSON.
    #Retorna um dicionário onde as chaves são os IDs dos funcionários e os valores são os dados dos funcionários.
    
    if os.path.exists(arquivo_funcionarios) and os.path.getsize(arquivo_funcionarios) > 0:
        with open(arquivo_funcionarios, 'r') as file:
            return json.load(file)  # Carrega os dados no formato de dicionário
    else:
        return {}  # Retorna um dicionário vazio se o arquivo não existe ou está vazio

def salvar_funcionario(funcionarios):
    
    #Salva o dicionário de funcionários no arquivo JSON.
    
    with open(arquivo_funcionarios, 'w') as file:
        json.dump(funcionarios, file, indent=4)  # Salva os dados no formato JSON com indentação

def gerar_id_funcionario(funcionarios):
    
    #Gera um novo ID único para um funcionário.
    #Baseia-se no maior ID atual, incrementando-o em 1.
    
    if funcionarios:
        maxId = max(int(id_funcionario) for id_funcionario in funcionarios.keys())
        return str(maxId + 1)
    return "1"  # Retorna "1" se não houver funcionários

def add_funcionario():
    
    #Adiciona um novo funcionário ao dicionário de funcionários.
    #Solicita os dados do funcionário ao usuário e salva no arquivo JSON.
    
    funcionarios = carregar_funcionarios()
    id_funcionario = gerar_id_funcionario(funcionarios)  # Gera um ID único
    nome = input("Insira o nome do funcionário:  ")
    idade = int(input("Insira a idade do funcionário:  "))
    cargo = input("Insira o cargo do funcionário:  ")

    # Cria um dicionário com as informações do funcionário
    funcionario = {
        "nome": nome,
        "idade": idade,
        "cargo": cargo,
        "obs": ""
    }

    # Adiciona o novo funcionário ao dicionário com o ID como chave
    funcionarios[id_funcionario] = funcionario
    salvar_funcionario(funcionarios)
    print("Funcionário cadastrado com sucesso!!")

def listar_funcionarios():
    
    #Lista todos os funcionários cadastrados.
    #Exibe as informações do funcionário, incluindo ID, nome, idade e cargo.
    
    funcionarios = carregar_funcionarios()

    if not funcionarios:
        print("Nenhum funcionário cadastrado!")
    else:
        print("--- FUNCIONÁRIOS ---")
        for id_funcionario, dados in funcionarios.items():
            print(f"ID: {id_funcionario}\nNome: {dados['nome']}\nIdade: {dados['idade']}\nCargo: {dados['cargo']}\nObs: {dados['obs']}")
        print()

def excluir_funcionario():
    
    #Exclui um funcionário com base no ID fornecido pelo usuário.
    #Remove o funcionário do dicionário e atualiza o arquivo JSON.
    
    funcionarios = carregar_funcionarios()
    listar_funcionarios()

    if funcionarios:
        id_funcionario = input("Digite o ID do funcionário a ser excluído: ")
        
        # Verifica se o ID existe no dicionário
        if id_funcionario in funcionarios:
            del funcionarios[id_funcionario]  # Remove o funcionário pelo ID
            salvar_funcionario(funcionarios)
            print(f"Funcionário '{id_funcionario}' excluído com sucesso!!")
        else:
            print("Funcionário não encontrado.")

def atualizar_funcionario():
    
    #Atualiza as informações de um funcionário com base no ID.
    #Permite modificar nome, idade e cargo, conforme as entradas do usuário.
    
    funcionarios = carregar_funcionarios()
    listar_funcionarios()
    
    if funcionarios:
        id_funcionario = input("Digite o ID do funcionário a ser atualizado: ")
        
        # Verifica se o ID existe no dicionário
        if id_funcionario in funcionarios:
            print(f"\nAtualizando informações de {funcionarios[id_funcionario]['nome']}")
            
            # Solicita novos dados, permitindo manter o valor atual caso o usuário pressione Enter
            novo_nome = input("Novo nome (ou pressione Enter para manter o atual): ")
            nova_idade = input("Nova idade (ou pressione Enter para manter a atual): ")
            novo_cargo = input("Novo cargo (ou pressione Enter para manter o atual): ")
            obs = input("Nova observação (ou pressione Enter para manter o atual):  ")

            # Atualiza os campos somente se o usuário inserir um novo valor
            if novo_nome:
                funcionarios[id_funcionario]['nome'] = novo_nome
            if nova_idade and nova_idade.isdigit():
                funcionarios[id_funcionario]['idade'] = int(nova_idade)
            if novo_cargo:
                funcionarios[id_funcionario]['cargo'] = novo_cargo
            if obs:
                funcionarios[id_funcionario]['obs'] = obs

            salvar_funcionario(funcionarios)
            print(f"Funcionário '{funcionarios[id_funcionario]['nome']}' atualizado com sucesso!\n")
        else:
            print("Funcionário não encontrado.")

def menu():
    
