import ply.lex as lex
import ply.yacc as yacc

# Tokens
tokens = (
    'FUNCTION',
    'NAME',
    'LPAREN',
    'RPAREN',
    'END',
    'COMMA',
    'PLUS',
    'NEWLINE',
)

# Define token regex patterns
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_PLUS = r'\+'

def t_FUNCTION(t):
    r'function'
    return t

def t_END(t):
    r'end'
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Grammar rules
def p_function_declaration(p):
    '''
    function_declaration : FUNCTION NAME LPAREN opt_parameters RPAREN block END
    '''
    p[0] = ('function', p[2], p[4], p[6])

def p_opt_parameters(p):
    '''
    opt_parameters : parameters
                   | empty
    '''
    p[0] = p[1]

def p_parameters(p):
    '''
    parameters : NAME
               | parameters COMMA NAME
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]

def p_block(p):
    '''
    block : statement
          | block statement
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + '\n' + p[2]

def p_statement(p):
    '''
    statement : NAME
              | expression
    '''
    p[0] = p[1]

def p_expression(p):
    '''
    expression : NAME PLUS NAME
    '''
    p[0] = p[1] + ' ' + p[2] + ' ' + p[3]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

if __name__ == "__main__":
    input_text = input("Enter a function declaration: ")

    lexer.input(input_text)
    for token in lexer:
        print(token)

    parsed = parser.parse(input_text)
    print(parsed)
