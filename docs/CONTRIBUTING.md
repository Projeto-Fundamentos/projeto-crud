# Guia de Contribuição

Bem-vindo ao guia de contribuição para este projeto! Este documento detalha como nossa equipe deve contribuir, reportar problemas e seguir os padrões de desenvolvimento. Siga as instruções abaixo para garantir que o processo de colaboração seja eficiente e consistente.

## Sumário
1. [Requisitos do projeto](#requisitos-do-projeto)
2. [Configuração do Ambiente](#configuração-do-ambiente)
3. [Fluxo de Trabalho de Desenvolvimento](#fluxo-de-trabalho-de-desenvolvimento)
4. [Padrões de Código](#padrões-de-código)
5. [Documentação](#documentação)
6. [Como Abrir Issues](#como-abrir-issues)
7. [Criando e Revisando Pull Requests](#criando-e-revisando-pull-requests)

## Requisitos do projeto
Para verificar os requisitos do projeto, verifique o arquivo com os [requisitos do projeto](./specifications.md).

## Configuração do Ambiente
Certifique-se de configurar o ambiente de desenvolvimento corretamente:
1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/Projeto-Fundamentos/projeto-crud
   cd projeto-crud
   ```

## Fluxo de Trabalho de Desenvolvimento
1. **Crie uma branch:** Para cada tarefa, crie uma nova branch baseada na ```main```.
    - Nomeie a branch usando o formato: ```tipo/descrição-curta-da-tarefa``` .
    - Exemplo: ```feature/adicinar-usuario``` ou ```bugfix/remover-usuario```.
2. **Commits:** Siga o padrão de commits do projeto:
    - ```feat```: Para novas funcionalidades.
    - ```fix```: Para correção de bugs.
    - ```docs```: Alteração na documentação
    - ```style```: Formatação, espaçamento, etc.
    - ```refactor```: Mudança no código que não corrigem nem adicionam funcionalidades.
    - ```test```: Adição ou modificação de testes.
    - ```chore```: Alteração no build ou ferramentas auxiliares.
3. **Certifique-se de que as alterações estejam de conforme com os [requisitos do projeto](#requisitos-do-projeto).

### Exemplo dos comando para Desenvolvimento seguro
**Na branch 'main':**
1. **Certifique-se de estar com o projeto atualizado**:
   ```bash
   git pull
2. **Crie uma nova branch**:
   ```bash
   git checkout -b nome-nova-branch
   ```
3. **Após desenvolvimento, adicione suas alterações**:
   ```bash
   git add .
   ```
4. **Commite suas alterações**:
   <br>
   Ex: 
   ```bash
   git commit -m "feat: Adiciona criação de cliente" 
   ```
5. **Suba suas alterações para o Github**:
   ```bash
   git push origin nome-nova-branch 
   ```
6. **Crie um Pull Request**:
<br>
Para saber como criar um Pull Request, veja: [Criando e Revisando Pull Requests](#criando-e-revisando-pull-requests).

## Padrões de Código
- PEP 8 é o padrão para projetos Python.
- Nomeie Variáveis, funções e classes de maneira descritiva e coerente.
- Funções e classes devem ser curtas e focadas em uma única responsabilidade.

## Documentação
- **Pendente**

## Como Abrir Issues
Para abrir uma issue, basta acessar o item ```Issues``` no ```Readme``` do projeto, ou acessar o item ```Projects``` na barra de navegação e selecionar ```Projeto CRUD - Fundamentos```. No quadro do projeto, basta clicar no botão ```+``` e em seguida, ```Create new issue```.
- Antes de abrir uma nova issue, certifique-se de que o problema já não foi reportado antes.
- Inclua o máximo de detalhes possível, incluindo passos para reproduzir o problema.
- Use labels para categorizar a issue(ex.: ```bug```, ```enhancement```, ```question```).
- [Exemplo de issue](https://github.com/Projeto-Fundamentos/projeto-crud/issues/32)

## Criando e Revisando Pull Requests
1. **Abra um Pull Request:**
    - Ao usar o comando ```git push```, na página principal do repositório deve aparecer um aviso acima dos arquivos do repositório e um botão para ser criado o Pull Request.
    - Descreva claramente as mudanças e por que foram feitas.
    - Relacione o PR a uma issue, se houver, usando ```Closes #número-da-issue```.
    > Ao criar um PR, designe os reviewers **Victor** e **Marina**.
2. **Revisão de Código:**
    - Peça para pelo para um dos membros revisores da equipe, **Victor ou Marina**, revisar o PR.
    - Caso ache pertinente, comente sobre alterações que poderiam ser feitas e/ou sugerir melhoras.
3. **Testes:**
    - Certifique-se de testar o código antes de pedir uma revisão.
