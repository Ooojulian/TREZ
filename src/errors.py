class TrezError(Exception):
    """Base class for all TREZ language errors."""
    pass

class TrezSyntaxError(TrezError):
    """Raised when there is a syntax error during parsing."""
    def __init__(self, line, column, msg):
        self.line = line
        self.column = column
        self.msg = msg
        super().__init__(f"Syntax Error at Line {line}, Column {column}: {msg}")

class TrezRuntimeError(TrezError):
    """Raised when a semantic/evaluation error occurs."""
    def __init__(self, msg):
        self.msg = msg
        super().__init__(f"Runtime Error: {msg}")
