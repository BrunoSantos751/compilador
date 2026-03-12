from parser import SetNode, OpNode, PrintNode

class SymbolTable:
    """
    Tabela de Símbolos auxiliar para análise semântica.
    Registra variáveis declaradas.
    """
    def __init__(self):
        self.symbols = set()

    def declare(self, name):
        self.symbols.add(name)

    def is_declared(self, name):
        return name in self.symbols

class SemanticAnalyzer:
    """
    Análise Semântica
    Após validação sintática, verifica regras de significado (ex: uso de variáveis declaradas).
    """
    def __init__(self):
        self.symbol_table = SymbolTable()

    def check(self, node, line_num):
        if node is None:
            return
            
        if isinstance(node, SetNode):
            # Adiciona a variável na tabela de símbolos na sua declaração
            self.symbol_table.declare(node.identifier)
            
        elif isinstance(node, OpNode):
            # Verifica se operandos, quando forem identificadores, já foram declarados
            for operand in (node.operand1, node.operand2):
                if operand.type == 'IDENTIFIER':
                    if not self.symbol_table.is_declared(operand.value):
                        raise Exception(f"Erro semântico na linha {line_num}: variável '{operand.value}' não declarada")
                        
        elif isinstance(node, PrintNode):
            # Verifica se a variável a ser impressa foi declarada
            if not self.symbol_table.is_declared(node.identifier):
                raise Exception(f"Erro semântico na linha {line_num}: variável '{node.identifier}' não declarada")
