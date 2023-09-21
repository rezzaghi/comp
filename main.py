from lexer import lex
from parser import Parser
from codegen import eval

if __name__ == '__main__':
    parser = Parser(lex(
        "(3 * 3) + (3 / 2); \
         2 + 2; \
         3 / 2; \
         2 + 1"
        ))
    eval(parser.parse())
