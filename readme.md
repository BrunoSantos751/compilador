# Apresentação - Compilador CalcLang 2.0

## Organização das Fases do Compilador
O projeto foi estruturado para refletir com exatidão as clássicas etapas de compilação:
1. **`lexer.py` (Análise Léxica):** Responsável por consumir o texto do programa, agrupar caracteres e transformá-los em uma fita de `Tokens` válidos, ou emitir erro se um caractere inválido for inserido.
2. **`parser.py` (Análise Sintática):** Analisa a ordem dos `Tokens` para validar as estruturas. Se um `PRINT` for seguido de um número em vez de um identificador (variável), é nesta fase que a falha é mapeada e notificada, além dessa etapa ser responsável por fornecer uma Árvore de Sintaxe Abstrata (AST) simplificada pelas classes de Nós.
3. **`semantic.py` (Análise Semântica):** Verifica o significado. Lê nó por nó gerado construindo as validações de linguagem (garantindo, por exemplo, que não tentaremos somar variáveis inexistentes).
4. **`translator.py` (Geração de Código Python):** Estando o código completamente livre de erros (léxicos, sintáticos ou semânticos), esta fase se encarregará de emitir o arquivo `saida.py` convertendo cada nó para sua contraparte real na linguagem Python.
5. **`main.py`:** Orquestra a leitura linha por linha, invocando adequadamente as fases supracitadas.

## Estrutura da Tabela de Símbolos
Para implementar a **Tabela de Símbolos**, o sistema adotou a estrutura de dados **`set()` (Conjunto)** disponível no Python.
O `set` foi escolhido pois, como na atual versão do compilador (CalcLang 2.0) só precisamos garantir a prévia declaração de uma variável, basta-nos uma chave de checagem. Isso fornece tempo de busca `O(1)`, tornando as validações semânticas extremamente performáticas, bastando armazenar a *string* do nome da variável toda vez que esta for declarada no código via instrução `SET`.

## Estratégia de Verificação Semântica
A estratégia de verificação atua processando operações sequenciais. Para isso, o analisador age da seguinte forma:
- Trata **Declarações (`SET`)**: Atualiza imediatamente a **Tabela de Símbolos** com a variável registrada.
- Trata **Expressões Matemáticas e `PRINT`**: Sempre que o utilizador fornecer uma variável como operando ao invés de um valor numérico bruto, obrigatoriamente é efetuada a verificação na *Tabela de Símbolos*. Caso a estrutura verifique que aquele identificador é novo e inóspito, o Analisador Semântico cancela imediatamente a compilação, relatando `Erro semântico na linha X: variável 'Y' não declarada`. Essa limitação barra comportamentos inesperados do código-objetivo em Python, mantendo o controle total pelo nosso compilador.
