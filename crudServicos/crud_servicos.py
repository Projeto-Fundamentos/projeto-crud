import json
import os
import uuid

services = os.path.join(os.path.dirname(__file__), 'services.json')

def carregar_servicos():
    if not os.path.exists(services):
        with open(services, 'w') as f:
            json.dump([], f, indent=4)
    with open(services, 'r') as f:
        return json.load(f)


#CREATE    
def adicionar_servicos(id, nome, descricao, duracao):
    servico = {
        "id": id,
        "nome": nome,
        "descricao": descricao,
        "duracao": duracao
    }
    novo_servico = carregar_servicos()
    novo_servico.append(servico)
    with open(services, 'w') as f:
        json.dump(novo_servico, f, indent=4)


#READ
def listar_servicos():
    servicos = carregar_servicos()

    print('SERVICOS OFERECIDOS:')
    for servico in servicos:
        print('--------------------------------------------------------------')
        print(f'ID: {servico['id']}\tNome: {servico['nome']}\tdescricao: {servico['descricao']}\tduracao: {servico['duracao']}')
    print('--------------------------------------------------------------')


#UPDATE
def atualizar_servico(id, nome, descricao, duracao):
    servico_atualizado = carregar_servicos()
    for servico in servico_atualizado:
        if id == servico['id']:
            servico['nome'] = nome  
            servico['descricao'] = descricao            
            servico['duracao'] = duracao            
            break
    with open(services, 'w') as f:
        json.dump(servico_atualizado, f, indent=4)
    print('Atualizado')

#DELETE
def excluir_servico(id):
    servico_excluido = carregar_servicos()
    for servico in servico_excluido:
        if id == servico['id']:
            print(id, servico['id'], servico['nome'])
            servico_excluido.remove(servico)
            break
    with open(services, 'w') as f:
        json.dump(servico_excluido, f, indent=4)
    print('servico excluido!')






# #TESTE
# adicionar_servicos('1','banho', 'blabla','10')
# adicionar_servicos('2','banho e tosa', 'kakaka','30')
# adicionar_servicos('3','cortar unha', 'bugbug','3')

# listar_servicos()


# atualizar_servico('1', 'banho premium plus', '500 dolares', '300')
# print('-------------Atualizados---------------')
# listar_servicos()

# excluir_servico('1')

# print('-------------Atualizado---------------')
# listar_servicos()

