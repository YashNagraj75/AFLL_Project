# Write Parser for the if construct in lua language using the ply library
import ply.lex as lex
import ply.yacc as yacc

# Define the tokens for the lexer
tokens = (
   
  'ASSIGN','NAME', 'NUMBER', 'STRING', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
  'LPAREN', 'RPAREN', 'LT', 'LE', 'GT', 'GE', 'EQ', 'NE', 'NOT',
  'IF', 'THEN', 'ELSEIF', 'ELSE', 'END','NEWLINE'
)

# Define the regular expressions for the tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_EQ = r'=='
t_NE = r'~='


t_NOT = r'not'
t_IF = r'if'
t_THEN = r'then'
t_ELSEIF = r'elseif'
t_ELSE = r'else'
t_END = r'end'

def t_UMINUS(t):
    r'-'
    t.type = 'UMINUS'
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*' 
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1] 
    return t

def t_ASSIGN(t):
    r'='
    return t

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t

def t_WHITESPACE(t):
  r'(?<=[+\-*\/])( [ \t])+(?=[+\-*\/])'
  pass


# Update statement grammar rule    
def p_statement(p):
  '''statement : IF expr THEN non_recursive_stmt'''


def p_non_recursive_stmt(p):
    '''non_recursive_stmt : NAME 
                          | ASSIGN'''
    
    '''non_recursive_stmt : statement | non_recursive_stmt statement'''



# Define the reserved keywords
reserved = {
  'and': 'AND',
  'else': 'ELSE',
  'elseif': 'ELSEIF',
  'end': 'END',
  'if': 'IF',
  'not': 'NOT',
  'or': 'OR',
  'then': 'THEN'
}

# Define the precedence and associativity of the operators
precedence = (
  ('right', 'NOT'),
  ('nonassoc', 'LT', 'LE', 'GT', 'GE', 'NE', 'EQ'),
  ('left', 'PLUS', 'MINUS'),
  ('left', 'TIMES', 'DIVIDE'),
  
)

# Define the grammar rules for the parser
def p_statement_if(p):
  '''statement : IF expr THEN statement END
         | IF expr THEN statement ELSE statement END
         | IF expr THEN statement ELSEIF expr THEN statement END
         | IF expr THEN statement ELSEIF expr THEN statement ELSE statement END'''
  pass

def p_expr(p):
  '''expr : expr LT expr
      | expr LE expr
      | expr GT expr
      | expr GE expr
      | expr NE expr
      | expr EQ expr
      | expr PLUS expr
      | expr MINUS expr
      | expr TIMES expr
      | expr DIVIDE expr
      | LPAREN expr RPAREN
      | NOT expr
      | NAME
      | NUMBER
      | STRING'''
  pass

def p_error(p):
  print("Syntax error in input!")

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

# Test the parser on a sample input
input_str = """
if x < 10 then
"""

lexer = lex.lex()
lexer.input(input_str)

for tok in lexer:
    print(tok)


print(input_str)
input_str = input_str.replace(" ", "")
parser.parse(input_str)

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
