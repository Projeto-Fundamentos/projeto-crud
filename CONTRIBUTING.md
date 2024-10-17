# Guia de Contribuição

Bem-vindo ao guia de contribuição para este projeto! Este documento detalha como nossa equipe deve contribuir, reportar problemas e seguir os padrões de desenvolvimento. Siga as instruções abaixo para garantir que o processo de colaboração seja eficiente e consistente.

## Sumário
1. [Configuração do Ambiente](#configuração-do-ambiente)
2. [Fluxo de Trabalho de Desenvolvimento](#fluxo-de-trabalho-de-desenvolvimento)
3. [Padrões de Código](#padrões-de-código)
4. [Documentação](#documentação)
5. [Como Abrir Issues](#como-abrir-issues)
6. [Criando e Revisando Pull Requests](#criando-e-revisando-pull-requests)

## Configuração do Ambiente
Certifique-se de configurar o ambiente de desenvolvimento corretamente:
1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/Projeto-Fundamentos/projeto-crud
   cd projeto-crud
   ```

## Fluxo de Trabalho de Desenvolvimento
1. **Crie uma branch:** Para cada tarefa, crie uma nova branch baseada na ```main```
    - Nomeie a branch usando o formato: ```tipo/descrição-curta-da-tarefa``` 
    - Exemplo: ```feature/adicinar-usuario``` ou ```bugfix/remover-usuario``` 
2. **Commits:** Siga o padrão de commits do projeto:
    - ```feat```: Para novas funcionalidades.
    - ```fix```: Para correção de bugs.
    - ```docs```: Alteração na documentação
    - ```style```: Formatação, espaçamento, etc.
    - ```refactor```: Mudança no código que não corrigem nem adicionam funcionalidades.
    - ```test```: Adição ou modificação de testes.
    - ```chore```: Alteração no build ou ferramentas auxiliares.

## Padrões de Código
- PEP 8 é o padrão para projetos Python.
- Nomeie Variáveis, funções e classes de maneira descritiva e coerente.
- Funções e classes devem ser curtas e focadas em uma única responsabilidade.

## Documentação
- Pendente

## Como Abrir Issues
- Antes de abrir uma nova issue, certifique-se de que o problema já não foi reportado antes.
- Inclua o máximo de detalhes possível, incluindo passos para reproduzir o problema.
- Use labels para categorizar a issue(ex.: ```bug```, ```enhancement```, ```question```).

## Criando e Revisando Pull Requests
1. **Abra um Pull Request:**
    - Descreva claramente as mudanças e por que foram feitas.
    - Relacione o PR a uma issue, se houver, usando ```Closes #número-da-issue```
2. **Revisão de Código:**
    - Peça para pelo menos um membro da equipe revisar o PR.
    - Comente sobre alterações que poderiam ser feitas e sugerir melhoras.
3. **Testes:**
    - Certifique-se de testar o código antes de pedir uma revisão.