import sys
import os
from lexer import Lexer
from parser import Parser
from semantic import SemanticAnalyzer
from translator import Translator



def compile_file(input_file, output_file):
    parser = Parser()
    semantic = SemanticAnalyzer()
    translator = Translator()
    
    has_errors = False

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            for line_num, line_text in enumerate(f, 1):
                raw_line = line_text.strip()
                if not raw_line:
                    continue
                    
                try:
                    # 1. Análise Léxica
                    lexer = Lexer(raw_line, line_num)
                    tokens = lexer.tokenize()
                    
                    if not tokens: # Linha vazia ou apenas espaços
                        continue
                        
                    # 2. Análise Sintática
                    ast_node = parser.parse_line(tokens, line_num)
                    
                    # 3. Análise Semântica
                    semantic.check(ast_node, line_num)
                    
                    # 4. Geração de código (adiciona na memória)
                    translator.translate(ast_node)
                    
                except Exception as e:
                    # Captura qualquer exceção lançada pelas fases e imprime
                    print(e)
                    has_errors = True
                    
        if not has_errors:
            with open(output_file, 'w', encoding='utf-8') as out_f:
                out_f.write(translator.get_code())
            print(f"Compilação concluída com sucesso. Código gerado em '{output_file}'.")
        else:
            print("Erros encontrados durante a compilação. Nenhum arquivo de saída foi gerado.")
            
    except FileNotFoundError:
        print(f"Erro: O arquivo '{input_file}' não foi encontrado.")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    in_file = sys.argv[1] if len(sys.argv) > 1 else os.path.join(base_dir, 'entrada.calc')
    out_file = sys.argv[2] if len(sys.argv) > 2 else os.path.join(base_dir, 'saida.py')
    
    print(f"Iniciando compilação: {in_file} -> {out_file}")
    compile_file(in_file, out_file)
