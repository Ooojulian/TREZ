import sys
import os
sys.path.append(os.path.dirname(__file__))

from antlr4 import *
from TrezLexer import TrezLexer
from TrezParser import TrezParser
from visitor import TrezVisitor

def main():
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        print("Uso: python main.py <archivo.trez>")
        return

    lexer = TrezLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TrezParser(stream)
    tree = parser.program()

    visitor = TrezVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()
