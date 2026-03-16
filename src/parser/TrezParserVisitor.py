# Generated from TrezParser.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TrezParser import TrezParser
else:
    from TrezParser import TrezParser

# This class defines a complete generic visitor for a parse tree produced by TrezParser.

class TrezParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TrezParser#program.
    def visitProgram(self, ctx:TrezParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TrezParser#statement.
    def visitStatement(self, ctx:TrezParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TrezParser#let_stmt.
    def visitLet_stmt(self, ctx:TrezParser.Let_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TrezParser#expr_stmt.
    def visitExpr_stmt(self, ctx:TrezParser.Expr_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TrezParser#StringExpr.
    def visitStringExpr(self, ctx:TrezParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TrezParser#ArrayExpr.
    def visitArrayExpr(self, ctx:TrezParser.ArrayExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TrezParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:TrezParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TrezParser#NumExpr.
    def visitNumExpr(self, ctx:TrezParser.NumExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TrezParser#VarExpr.
    def visitVarExpr(self, ctx:TrezParser.VarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TrezParser#ParenExpr.
    def visitParenExpr(self, ctx:TrezParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TrezParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:TrezParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TrezParser#FuncCallExpr.
    def visitFuncCallExpr(self, ctx:TrezParser.FuncCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TrezParser#array.
    def visitArray(self, ctx:TrezParser.ArrayContext):
        return self.visitChildren(ctx)



del TrezParser