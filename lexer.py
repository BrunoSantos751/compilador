class Token:
    def __init__(self, type_, value, line):
        self.type = type_
        self.value = value
        self.line = line

    def __repr__(self):
        return f"[{self.type}:{self.value}]"

class Lexer:
    def __init__(self, text, line_num):
        """
        Responsável por ler o código fonte caractere por caractere e transformá-lo em tokens,
        agora adaptado para uma única linha já que a leitura será linha por linha.
        """
        self.text = text
        self.pos = 0
        self.line_num = line_num
        self.current_char = self.text[self.pos] if len(self.text) > 0 else None
        
        self.keywords = {'SET', 'ADD', 'SUB', 'MUL', 'DIV', 'PRINT'}

    def advance(self):
        """Avança para o próximo caractere."""
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        """Ignora espaços em branco."""
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def number(self):
        """Lê números inteiros da entrada."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token('NUMBER', int(result), self.line_num)

    def identifier_or_keyword(self):
        """Lê identificadores ou palavras reservadas."""
        result = ''
        while self.current_char is not None and self.current_char.isalpha():
            result += self.current_char
            self.advance()
            
        if result in self.keywords:
            return Token(result, result, self.line_num) # type = keyword, value = keyword
        return Token('IDENTIFIER', result, self.line_num)

    def get_next_token(self):
        """Analisa o próximo elemento léxico e retorna um token."""
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
                
            if self.current_char.isdigit():
                return self.number()
                
            if self.current_char.isalpha():
                return self.identifier_or_keyword()
                
            # Qualquer outro caractere
            char = self.current_char
            self.advance()
            return Token('ERROR', char, self.line_num)
            
        return Token('EOF', None, self.line_num)

    def tokenize(self):
        """Converte toda a linha de entrada em uma lista de tokens."""
        tokens = []
        token = self.get_next_token()
        while token.type != 'EOF':
            if token.type == 'ERROR':
                raise Exception(f"Erro léxico na linha {self.line_num}: caractere '{token.value}' inesperado")
            tokens.append(token)
            token = self.get_next_token()
        return tokens
