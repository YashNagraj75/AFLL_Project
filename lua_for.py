import ply.lex as lex
import ply.yacc as yacc

# List of token names
tokens = (
    'ID',
    'ASSIGN',
    'NUMBER',
    'FOR',
    'EQUALS',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'DO',
    'END',
)

# Regular expression rules for simple tokens
t_ASSIGN = r'='
t_EQUALS = r'=='
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DO = r'do'
t_END = r'end'

# Define a rule for IDs (identifiers)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'ID' if t.value not in ('for', 'do', 'end') else t.value.upper()
    return t

# Define a rule for numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters (whitespace and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Define the grammar rules
def p_for_loop(p):
    '''for_loop : FOR ID ASSIGN NUMBER COMMA NUMBER DO END'''
    # Handle the parsed for loop
    print("Parsed for loop:", p[2], "starting from", p[4], "to", p[6])

# Error handling in parsing
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

# Test statement to parse
statement = "for i = 1, i++ do end"
# Parsing the statement
lexer.input(statement)
for token in lexer:
    print(token)

parsed = parser.parse(statement)
