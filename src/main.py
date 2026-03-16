import sys
import os
sys.path.append(os.path.dirname(__file__))

from antlr4 import *
from TrezLexer import TrezLexer
from TrezParser import TrezParser
from visitor import TrezVisitor
from error_listener import TrezErrorListener
from errors import TrezRuntimeError

def main():
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1], encoding='utf-8')
    else:
        print("Uso: python main.py <archivo.trez>")
        return

    lexer = TrezLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TrezParser(stream)

    # Attach custom error listeners
    error_listener = TrezErrorListener()
    lexer.removeErrorListeners()
    parser.removeErrorListeners()
    lexer.addErrorListener(error_listener)
    parser.addErrorListener(error_listener)

    tree = parser.program()

    # Stop execution if parsing failed
    if error_listener.has_errors:
        error_listener.print_errors()
        sys.exit(1)

    # Execute AST and catch runtime semantic errors
    visitor = TrezVisitor()
    try:
        visitor.visit(tree)
    except TrezRuntimeError as e:
        print(f"\n❌ {e.msg}\n")
        sys.exit(1)

if __name__ == '__main__':
    main()
