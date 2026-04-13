import sys
import os
from antlr4 import *
from miniportugolLexer import miniportugolLexer

def get_token_name(lexer, token_type):
    if hasattr(lexer, 'vocabulary'):
        token_name = lexer.vocabulary.getSymbolicName(token_type)
        if token_name:
            return token_name
        literal_name = lexer.vocabulary.getLiteralName(token_type)
        if literal_name:
            return literal_name.strip("'")

    if token_type < len(lexer.symbolicNames):
        token_name = lexer.symbolicNames[token_type]
        if token_name and token_name != '<INVALID>':
            return token_name

    if token_type < len(lexer.literalNames):
        literal_name = lexer.literalNames[token_type]
        if literal_name and literal_name != '<INVALID>':
            return literal_name.strip("'")

    return f"TOKEN_{token_type}"

def processar_lexico(arquivo_fonte):
    if not os.path.exists(arquivo_fonte):
        print(f"Erro: Arquivo {arquivo_fonte} não encontrado.")
        return

    input_stream = FileStream(arquivo_fonte, encoding='utf-8')
    lexer = miniportugolLexer(input_stream)
    
    log_filename = "logs/scanner_log.txt"
    
    # Abrimos o arquivo de log para escrita (limpa o anterior)
    with open(log_filename, "w", encoding="utf-8") as f_log:
        print(f"--- INICIANDO SCANNER PARA: {arquivo_fonte} ---\n")
        f_log.write(f"--- LOG DO SCANNER: {arquivo_fonte} ---\n\n")
        
        token = lexer.nextToken()
        while token.type != Token.EOF:
            nome_token = get_token_name(lexer, token.type)
            lexema = token.text
            linha = token.line
            coluna = token.column

            # Requisito 3: Reportar Erro Léxico se cair na regra de erro
            if nome_token == "ERRO_CARACTERE":
                msg_erro = f"ERRO LÉXICO [Linha {linha}, Coluna {coluna}]: Símbolo '{lexema}' inválido."
                print(msg_erro)
                f_log.write(msg_erro + "\n")
            else:
                # Requisito 1: Formato <Tipo, Lexema, Linha, Coluna>
                saida = f"<{nome_token}, '{lexema}', {linha}, {coluna}>"
                print(saida)
                f_log.write(saida + "\n")
            
            token = lexer.nextToken()

    print(f"\n--- SCANNER FINALIZADO. Log gerado em: {log_filename} ---")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        processar_lexico(sys.argv[1])
    else:
        print("Uso: python main.py exemplos/exemplo1.txt")