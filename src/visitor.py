import sys
import os
sys.path.append(os.path.dirname(__file__))

from TrezParser import TrezParser
from TrezVisitor import TrezVisitor as AntlrTrezVisitor

class TrezVisitor(AntlrTrezVisitor):
    
    def visitProgram(self, ctx: TrezParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)
        return None

    def visitExpr_stmt(self, ctx: TrezParser.Expr_stmtContext):
        result = self.visit(ctx.expr())
        print(result) # Print the result of the expression
        return result

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
