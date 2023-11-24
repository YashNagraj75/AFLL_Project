import ply.lex as lex
import ply.yacc as yacc

# Tokens
tokens = (
    'LOCAL',
    'NAME',
    'ASSIGN',
    'REQUIRE',
    'STRING',
    'LPAREN',
    'RPAREN',
)

# Define token regex patterns
t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_LOCAL(t):
    r'local'
    return t

def t_REQUIRE(t):
    r'require'
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_STRING(t):
    r'"(?:[^"\\]|\\.)*"'
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Grammar rules
def p_import_statement(p):
    '''
    import_statement : LOCAL NAME ASSIGN REQUIRE LPAREN STRING RPAREN
    '''
    p[0] = ('import', p[2], p[5])

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

if __name__ == "__main__":
    input_text = """
    local module = require("module_name")
    """

    lexer.input(input_text)
    for token in lexer:
        print(token)

    parsed = parser.parse(input_text)
    print(parsed)
