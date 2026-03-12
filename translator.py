from parser import SetNode, OpNode, PrintNode

class Translator:
    """
    Tradutor / Gerador de Código
    Mapeia os nós da Árvore Sintática (AST) validados nas etapas
    anteriores para código funcional correspondente em Python.
    """
    def __init__(self):
        self.python_code = []

    def translate(self, node):
        if node is None:
            return
            
        if isinstance(node, SetNode):
            self.python_code.append(f"{node.identifier} = {node.number}")
            
        elif isinstance(node, OpNode):
            op_map = {
                'ADD': '+',
                'SUB': '-',
                'MUL': '*',
                'DIV': '/'
            }
            op = op_map[node.op]
            op1_val = str(node.operand1.value)
            op2_val = str(node.operand2.value)
            
            # Operações isoladas não modificam dados, para ter efeito imprimimos seu valor
            self.python_code.append(f"print({op1_val} {op} {op2_val})")
            
        elif isinstance(node, PrintNode):
            self.python_code.append(f"print({node.identifier})")

    def get_code(self):
        """Retorna o código Python como texto, juntando as linhas geradas."""
        return "\n".join(self.python_code) + "\n"
