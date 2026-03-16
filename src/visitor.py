import sys
import os
sys.path.append(os.path.dirname(__file__))

from TrezParser import TrezParser
from TrezVisitor import TrezVisitor as AntlrTrezVisitor
import math_utilsdoz

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
        if var_name in self.memory:
            return self.memory[var_name]
        raise Exception(f"Undefined variable: {var_name}")

    def visitFuncCallExpr(self, ctx: TrezParser.FuncCallExprContext):
        func_name = ctx.ID().getText()
        args = []
        if ctx.arg_list():
            # In arg_list, every child that is not a comma is an expr
            for expr_ctx in ctx.arg_list().expr():
                args.append(self.visit(expr_ctx))
        
        # dispatch to math_utils
        if func_name == 'relu':
            return math_utilsdoz.relu(args[0])
        elif func_name == 'sigmoid':
            return math_utilsdoz.sigmoid(args[0])
        elif func_name == 'dot':
            return math_utilsdoz.dot(args[0], args[1])
        elif func_name == 'transpose':
            return math_utilsdoz.transpose(args[0])
        else:
            raise Exception(f"Unknown function: {func_name}")

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
        if op == '*':
            return left * right
        else:
            return left / right

    def visitAddSubExpr(self, ctx: TrezParser.AddSubExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        if op == '+':
            return left + right
        else:
            return left - right

    def visitNumberExpr(self, ctx: TrezParser.NumberExprContext):
        return float(ctx.NUMBER().getText())

    def visitParensExpr(self, ctx: TrezParser.ParensExprContext):
        return self.visit(ctx.expr())
