"""
This is an example of using the PLY (Python Lex-Yacc) library to create a parser for a simple calculator language.
The grammar rules for the calculator are defined using functions, which are then used to build the parser.
The parser reads input from the user and evaluates the input as a mathematical expression.
"""

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
tokens = (
   
  'ASSIGN','NAME', 'NUMBER', 'STRING', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
  'LPAREN', 'RPAREN', 'LT', 'LE', 'GT', 'GE', 'EQ', 'NE', 'NOT',
  'IF', 'THEN', 'ELSEIF', 'ELSE', 'END','NEWLINE'
)



# To specify the grammar rules we have to define functions in our yacc file. 
# The syntax for the same is as follows: 



def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    '''
    factor : LPAREN expression RPAREN
    This function takes in a parsing object p and sets the value of p[0] to the value of p[2].
    '''
    p[0] = p[2]
def p_factor_expr(p):
    '''
    Parse the factor expression within parentheses.

    Args:
        p: The parsing object.

    Returns:
        None.

    Sets the value of p[0] to the expression within parentheses.
    The expression is obtained from p[2].
    '''
    p[0] = p[2]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)