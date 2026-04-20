import sys
import os
sys.path.append(os.path.dirname(__file__))

from parser.TrezParser import TrezParser
from parser.TrezParserVisitor import TrezParserVisitor as AntlrTrezVisitor
import math_utils
from errors import TrezRuntimeError
from lib.io import read_file, write_file

class TrezVisitor(AntlrTrezVisitor):
    def __init__(self):
        super().__init__()
        self.memory = {} # Simulating functional bindings/memory

    def visitProgram(self, ctx: TrezParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)
        return None

    def visitLet_stmt(self, ctx: TrezParser.Let_stmtContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[var_name] = value # Immutable in theory, but storing state
        return value

    def visitExpr_stmt(self, ctx: TrezParser.Expr_stmtContext):
        result = self.visit(ctx.expr())
        print(result) # Print the result of the expression
        return result

    def visitVarExpr(self, ctx: TrezParser.VarExprContext):
        var_name = ctx.ID().getText()
        # Verificar constantes matemáticas reservadas (ej. PI, E)
        if hasattr(math_utils, 'constants') and var_name in math_utils.constants:
            return math_utils.constants[var_name]

        if var_name in self.memory:
            return self.memory[var_name]
        raise TrezRuntimeError(f"Undefined variable: '{var_name}'")

    def visitFuncCallExpr(self, ctx: TrezParser.FuncCallExprContext):
        func_name = ctx.ID().getText()
        # With the updated grammar, ctx.expr() returns all argument expressions directly
        args = [self.visit(expr_ctx) for expr_ctx in ctx.expr()]

        # dispatch to math_utils
        if func_name == 'relu':
            return math_utils.relu(args[0])
        elif func_name == 'sigmoid':
            return math_utils.sigmoid(args[0])
        elif func_name == 'dot':
            return math_utils.dot(args[0], args[1])
        elif func_name == 'transpose':
            return math_utils.transpose(args[0])
        elif func_name == 'mse':
            return math_utils.mse(args[0], args[1])
        elif func_name == 'mse_grad':
            return math_utils.mse_grad(args[0], args[1])
        # Native Core Math API
        elif func_name == 'abs':
            return math_utils.abs(args[0])
        elif func_name == 'sqrt':
            return math_utils.sqrt(args[0])
        elif func_name == 'pow':
            return math_utils.pow(args[0], args[1])
        elif func_name == 'exp':
            return math_utils.exp(args[0])
        elif func_name == 'log':
            return math_utils.log(args[0])
        elif func_name == 'sin':
            return math_utils.sin(args[0])
        elif func_name == 'cos':
            return math_utils.cos(args[0])
        elif func_name == 'tan':
            return math_utils.tan(args[0])
        elif func_name == 'factorial':
            return math_utils.factorial(args[0])
        # Native File I/O API
        elif func_name == 'leer':
            return read_file(args[0])
        elif func_name == 'escribir':
            return write_file(args[0], args[1])
        elif func_name == 'mostrar' or func_name == 'print':
            # mostrar(x) - print to stdout
            print(args[0])
            return None
        else:
            raise TrezRuntimeError(f"Unknown system function: '{func_name}'")

    def visitBlock(self, ctx: TrezParser.BlockContext):
        result = None
        for stmt in ctx.statement():
            result = self.visit(stmt)
        return result

    def visitIf_stmt(self, ctx: TrezParser.If_stmtContext):
        cond = self.visit(ctx.expr())
        if cond:
            return self.visit(ctx.block(0))
        elif ctx.block(1) is not None:
            return self.visit(ctx.block(1))
        return None

    def visitWhile_stmt(self, ctx: TrezParser.While_stmtContext):
        # Simple while loop; beware infinite loops
        while self.visit(ctx.expr()):
            self.visit(ctx.block())
        return None

    def visitArrayExpr(self, ctx: TrezParser.ArrayExprContext):
        # Visit the array rule context
        return self.visit(ctx.array())

    def visitArray(self, ctx: TrezParser.ArrayContext):
        items = []
        for expr_ctx in ctx.expr():
            items.append(self.visit(expr_ctx))
        return items

    def visitMulDivExpr(self, ctx: TrezParser.MulDivExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        
        # Scalar multiplication over arrays (for Learning Rate `lr * array`)
        if op == '*':
            if isinstance(left, (int, float)) and isinstance(right, list):
                return [left * r for r in right]
            elif isinstance(left, list) and isinstance(right, (int, float)):
                return [l * right for l in left]
            return left * right
        elif op == '/':
            return left / right
        else: # modulo
            return left % right

    def visitPowExpr(self, ctx: TrezParser.PowExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        # prefer math_utils if available
        if hasattr(math_utils, 'pow'):
            return math_utils.pow(left, right)
        return left ** right

    def visitUnaryMinusExpr(self, ctx: TrezParser.UnaryMinusExprContext):
        val = self.visit(ctx.expr())
        if isinstance(val, list):
            return [-v for v in val]
        return -val

    def visitBoolExpr(self, ctx: TrezParser.BoolExprContext):
        txt = ctx.getText()
        return True if txt == 'true' else False

    def visitEqExpr(self, ctx: TrezParser.EqExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        if op == '==':
            return left == right
        else:
            return left != right

    def visitCompareExpr(self, ctx: TrezParser.CompareExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        if op == '<':
            return left < right
        elif op == '<=':
            return left <= right
        elif op == '>':
            return left > right
        else:
            return left >= right

    def visitAndExpr(self, ctx: TrezParser.AndExprContext):
        left = self.visit(ctx.expr(0))
        # short-circuit
        if not bool(left):
            return False
        right = self.visit(ctx.expr(1))
        return bool(right)

    def visitOrExpr(self, ctx: TrezParser.OrExprContext):
        left = self.visit(ctx.expr(0))
        if bool(left):
            return True
        right = self.visit(ctx.expr(1))
        return bool(right)

    def visitAddSubExpr(self, ctx: TrezParser.AddSubExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        
        # Support array component-wise addition/subtraction
        if isinstance(left, list) and isinstance(right, list):
            if len(left) != len(right):
                raise TrezRuntimeError("Cannot add/subtract arrays of different lengths")
            if op == '+':
                return [l + r for l, r in zip(left, right)]
            else:
                return [l - r for l, r in zip(left, right)]

        if op == '+':
            return left + right
        else:
            return left - right

    def visitNumExpr(self, ctx: TrezParser.NumExprContext):
        val = ctx.getText()
        return float(val) if '.' in val else int(val)

    def visitStringExpr(self, ctx: TrezParser.StringExprContext):
        # Remove surrounding quotes and process escape sequences
        raw = ctx.getText()[1:-1]
        raw = raw.replace('\\n', '\n')
        raw = raw.replace('\\t', '\t')
        raw = raw.replace('\\"', '"')
        raw = raw.replace('\\\\', '\\')
        return raw
        
    def visitParenExpr(self, ctx: TrezParser.ParenExprContext):
        return self.visit(ctx.expr())
