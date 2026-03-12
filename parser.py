class ASTNode:
    pass

class SetNode(ASTNode):
    def __init__(self, identifier, number):
        self.identifier = identifier
        self.number = number

class OpNode(ASTNode):
    def __init__(self, op, operand1, operand2):
        self.op = op
        self.operand1 = operand1
        self.operand2 = operand2

class PrintNode(ASTNode):
    def __init__(self, identifier):
        self.identifier = identifier


class Parser:
    """
    Análise Sintática (Parser)
    Verifica se a sequência de tokens segue a gramática da linguagem e gera uma AST simplificada.
    """
    def __init__(self):
        pass

    def parse_line(self, tokens, line_num):
        if not tokens:
            return None
            
        command = tokens[0]
        
        if command.type == 'SET':
            if len(tokens) != 3:
                raise Exception(f"Erro sintático na linha {line_num}: estrutura inválida. Esperado: SET IDENTIFIER NUMBER")
            if tokens[1].type != 'IDENTIFIER' or tokens[2].type != 'NUMBER':
                raise Exception(f"Erro sintático na linha {line_num}: estrutura inválida. Esperado: SET IDENTIFIER NUMBER")
            return SetNode(tokens[1].value, tokens[2].value)
            
        elif command.type in ('ADD', 'SUB', 'MUL', 'DIV'):
            if len(tokens) != 3:
                raise Exception(f"Erro sintático na linha {line_num}: estrutura inválida. Esperado: {command.type} OPERANDO OPERANDO")
            if tokens[1].type not in ('IDENTIFIER', 'NUMBER') or tokens[2].type not in ('IDENTIFIER', 'NUMBER'):
                raise Exception(f"Erro sintático na linha {line_num}: estrutura inválida. Esperado: {command.type} OPERANDO OPERANDO")
            return OpNode(command.type, tokens[1], tokens[2])
            
        elif command.type == 'PRINT':
            if len(tokens) != 2:
                raise Exception(f"Erro sintático na linha {line_num}: estrutura inválida. Esperado: PRINT IDENTIFIER")
            if tokens[1].type != 'IDENTIFIER':
                raise Exception(f"Erro sintático na linha {line_num}: estrutura inválida. Esperado: PRINT IDENTIFIER")
            return PrintNode(tokens[1].value)
            
        else:
            raise Exception(f"Erro sintático na linha {line_num}: Comando '{command.value}' desconhecido")
