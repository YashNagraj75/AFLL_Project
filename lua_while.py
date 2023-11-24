import ply.lex as lex
import ply.yacc as yacc

# List of token names
tokens = (
    'ID',
    'ASSIGN',
    'NUMBER',
    'LPAREN',
    'RPAREN',
    'PLUS',
    'MULTIPLY',
    'INCREMENT',
    'WHILE',
    'DO',
    'END',
    'NEWLINE',
)

# Regular expression rules for simple tokens
t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PLUS = r'\+'
t_MULTIPLY = r'\*'
t_INCREMENT = r'\+\+'
t_DO = r'do'
t_END = r'end'

# Define a rule for IDs (identifiers)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'ID' if t.value not in ('while', 'do', 'end') else t.value.upper()
    return t

# Define a rule for numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters (whitespace and tabs)
t_ignore = ' \t'

# Define rule for newlines
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Define the grammar rules
def p_while_loop(p):
    '''while_loop : WHILE LPAREN condition RPAREN DO statements END'''
    # Handle the parsed while loop
    print("Parsed while loop with condition:", p[3])
    print("Body:")
    for statement in p[6]:
        print(statement)

def p_condition(p):
    '''condition : ID ASSIGN exp'''
    # Handle the condition expression
    p[0] = (p[1], p[3])

def p_exp_assign(p):
    '''exp : ID ASSIGN exp'''
    # Handle assignment expressions
    p[0] = f"{p[1]} = {p[3]}"

def p_exp_increment(p):
    '''exp : ID INCREMENT'''
    # Handle increment expressions
    p[0] = f"{p[1]} += 1"

def p_exp_number(p):
    '''exp : NUMBER'''
    # Handle number expressions
    p[0] = p[1]

def p_statements(p):
    '''statements : statements statement
                  | statement'''
    # Handle multiple statements in the while loop body
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : exp NEWLINE
                 | exp'''
    # Handle simple statements for now
    p[0] = p[1]

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
# statement = """
# while i = 10 do
#   x = x + 1
#   y += 2
#   z++
# end
# """
statement = input("Enter a while loop statement: ")
# Parsing the statement
lexer.input(statement)
for token in lexer:
    print(token)

parsed = parser.parse(statement)
