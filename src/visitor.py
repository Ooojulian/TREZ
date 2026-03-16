import sys
import os
sys.path.append(os.path.dirname(__file__))

from parser.TrezParser import TrezParser
from parser.TrezParserVisitor import TrezParserVisitor as AntlrTrezVisitor
import math_utilsdoz
from errors import TrezRuntimeError
from lib.iodoz.iodoz import read_file_doz, write_file_doz

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
        if hasattr(math_utilsdoz, 'constants') and var_name in math_utilsdoz.constants:
            return math_utilsdoz.constants[var_name]
            
        if var_name in self.memory:
            return self.memory[var_name]
        raise TrezRuntimeError(f"Undefined variable: '{var_name}'")

    def visitFuncCallExpr(self, ctx: TrezParser.FuncCallExprContext):
        func_name = ctx.ID().getText()
        # With the updated grammar, ctx.expr() returns all argument expressions directly
        args = [self.visit(expr_ctx) for expr_ctx in ctx.expr()]
        
        # dispatch to math_utils
        if func_name == 'relu':
            return math_utilsdoz.relu(args[0])
        elif func_name == 'sigmoid':
            return math_utilsdoz.sigmoid(args[0])
        elif func_name == 'dot':
            return math_utilsdoz.dot(args[0], args[1])
        elif func_name == 'transpose':
            return math_utilsdoz.transpose(args[0])
        elif func_name == 'mse':
            return math_utilsdoz.mse(args[0], args[1])
        elif func_name == 'mse_grad':
            return math_utilsdoz.mse_grad(args[0], args[1])
        # Native Core Math API
        elif func_name == 'abs':
            return math_utilsdoz.abs_doz(args[0])
        elif func_name == 'sqrt':
            return math_utilsdoz.sqrt_doz(args[0])
        elif func_name == 'pow':
            return math_utilsdoz.pow_doz(args[0], args[1])
        elif func_name == 'exp':
            return math_utilsdoz.exp_doz(args[0])
        elif func_name == 'log':
            return math_utilsdoz.log_doz(args[0])
        elif func_name == 'sin':
            return math_utilsdoz.sin_doz(args[0])
        elif func_name == 'cos':
            return math_utilsdoz.cos_doz(args[0])
        elif func_name == 'tan':
            return math_utilsdoz.tan_doz(args[0])
        elif func_name == 'factorial':
            return math_utilsdoz.factorial_doz(args[0])
        # Native File I/O API
        elif func_name == 'leer':
            return read_file_doz(args[0])
        elif func_name == 'escribir':
            return write_file_doz(args[0], args[1])
        else:
            raise TrezRuntimeError(f"Unknown system function: '{func_name}'")

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
        else:
            return left / right

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
