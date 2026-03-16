# Generated from Trez.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("Y\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\6\2\22\n\2\r\2\16\2\23\3\2\3\2\3\3\3\3\5\3\32")
        buf.write("\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\62\n\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\7\6:\n\6\f\6\16\6=\13\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\7\7E\n\7\f\7\16\7H\13\7\3\7\3\7\5\7L\n")
        buf.write("\7\3\b\3\b\3\b\3\b\7\bR\n\b\f\b\16\bU\13\b\5\bW\n\b\3")
        buf.write("\b\2\3\n\t\2\4\6\b\n\f\16\2\4\3\2\6\7\3\2\b\t\2]\2\21")
        buf.write("\3\2\2\2\4\31\3\2\2\2\6\33\3\2\2\2\b!\3\2\2\2\n\61\3\2")
        buf.write("\2\2\fK\3\2\2\2\16V\3\2\2\2\20\22\5\4\3\2\21\20\3\2\2")
        buf.write("\2\22\23\3\2\2\2\23\21\3\2\2\2\23\24\3\2\2\2\24\25\3\2")
        buf.write("\2\2\25\26\7\2\2\3\26\3\3\2\2\2\27\32\5\6\4\2\30\32\5")
        buf.write("\b\5\2\31\27\3\2\2\2\31\30\3\2\2\2\32\5\3\2\2\2\33\34")
        buf.write("\7\3\2\2\34\35\7\20\2\2\35\36\7\4\2\2\36\37\5\n\6\2\37")
        buf.write(" \7\5\2\2 \7\3\2\2\2!\"\5\n\6\2\"#\7\5\2\2#\t\3\2\2\2")
        buf.write("$%\b\6\1\2%\62\7\17\2\2&\'\7\n\2\2\'(\5\n\6\2()\7\13\2")
        buf.write("\2)\62\3\2\2\2*\62\5\f\7\2+\62\7\20\2\2,-\7\20\2\2-.\7")
        buf.write("\n\2\2./\5\16\b\2/\60\7\13\2\2\60\62\3\2\2\2\61$\3\2\2")
        buf.write("\2\61&\3\2\2\2\61*\3\2\2\2\61+\3\2\2\2\61,\3\2\2\2\62")
        buf.write(";\3\2\2\2\63\64\f\t\2\2\64\65\t\2\2\2\65:\5\n\6\n\66\67")
        buf.write("\f\b\2\2\678\t\3\2\28:\5\n\6\t9\63\3\2\2\29\66\3\2\2\2")
        buf.write(":=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<\13\3\2\2\2=;\3\2\2\2>")
        buf.write("?\7\f\2\2?L\7\r\2\2@A\7\f\2\2AF\5\n\6\2BC\7\16\2\2CE\5")
        buf.write("\n\6\2DB\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2GI\3\2\2")
        buf.write("\2HF\3\2\2\2IJ\7\r\2\2JL\3\2\2\2K>\3\2\2\2K@\3\2\2\2L")
        buf.write("\r\3\2\2\2MW\3\2\2\2NS\5\n\6\2OP\7\16\2\2PR\5\n\6\2QO")
        buf.write("\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2TW\3\2\2\2US\3\2")
        buf.write("\2\2VM\3\2\2\2VN\3\2\2\2W\17\3\2\2\2\13\23\31\619;FKS")
        buf.write("V")
        return buf.getvalue()


class TrezParser ( Parser ):

    grammarFileName = "Trez.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'let'", "'='", "';'", "'*'", "'/'", "'+'", 
                     "'-'", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUMBER", "ID", "WS", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_let_stmt = 2
    RULE_expr_stmt = 3
    RULE_expr = 4
    RULE_array = 5
    RULE_arg_list = 6

    ruleNames =  [ "program", "statement", "let_stmt", "expr_stmt", "expr", 
                   "array", "arg_list" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    NUMBER=13
    ID=14
    WS=15
    LINE_COMMENT=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TrezParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TrezParser.StatementContext)
            else:
                return self.getTypedRuleContext(TrezParser.StatementContext,i)


        def getRuleIndex(self):
            return TrezParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = TrezParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.statement()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TrezParser.T__0) | (1 << TrezParser.T__7) | (1 << TrezParser.T__9) | (1 << TrezParser.NUMBER) | (1 << TrezParser.ID))) != 0)):
                    break

            self.state = 19
            self.match(TrezParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def let_stmt(self):
            return self.getTypedRuleContext(TrezParser.Let_stmtContext,0)


        def expr_stmt(self):
            return self.getTypedRuleContext(TrezParser.Expr_stmtContext,0)


        def getRuleIndex(self):
            return TrezParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = TrezParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TrezParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.let_stmt()
                pass
            elif token in [TrezParser.T__7, TrezParser.T__9, TrezParser.NUMBER, TrezParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.expr_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Let_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TrezParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(TrezParser.ExprContext,0)


        def getRuleIndex(self):
            return TrezParser.RULE_let_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLet_stmt" ):
                return visitor.visitLet_stmt(self)
            else:
                return visitor.visitChildren(self)




    def let_stmt(self):

        localctx = TrezParser.Let_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_let_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(TrezParser.T__0)
            self.state = 26
            self.match(TrezParser.ID)
            self.state = 27
            self.match(TrezParser.T__1)
            self.state = 28
            self.expr(0)
            self.state = 29
            self.match(TrezParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(TrezParser.ExprContext,0)


        def getRuleIndex(self):
            return TrezParser.RULE_expr_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_stmt" ):
                return visitor.visitExpr_stmt(self)
            else:
                return visitor.visitChildren(self)




    def expr_stmt(self):

        localctx = TrezParser.Expr_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.expr(0)
            self.state = 32
            self.match(TrezParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TrezParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ArrayExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def array(self):
            return self.getTypedRuleContext(TrezParser.ArrayContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayExpr" ):
                return visitor.visitArrayExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TrezParser.ExprContext)
            else:
                return self.getTypedRuleContext(TrezParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumberExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(TrezParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParensExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TrezParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensExpr" ):
                return visitor.visitParensExpr(self)
            else:
                return visitor.visitChildren(self)


    class VarExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(TrezParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarExpr" ):
                return visitor.visitVarExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TrezParser.ExprContext)
            else:
                return self.getTypedRuleContext(TrezParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)


    class FuncCallExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TrezParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(TrezParser.ID, 0)
        def arg_list(self):
            return self.getTypedRuleContext(TrezParser.Arg_listContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCallExpr" ):
                return visitor.visitFuncCallExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TrezParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = TrezParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 35
                self.match(TrezParser.NUMBER)
                pass

            elif la_ == 2:
                localctx = TrezParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 36
                self.match(TrezParser.T__7)
                self.state = 37
                self.expr(0)
                self.state = 38
                self.match(TrezParser.T__8)
                pass

            elif la_ == 3:
                localctx = TrezParser.ArrayExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 40
                self.array()
                pass

            elif la_ == 4:
                localctx = TrezParser.VarExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 41
                self.match(TrezParser.ID)
                pass

            elif la_ == 5:
                localctx = TrezParser.FuncCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 42
                self.match(TrezParser.ID)
                self.state = 43
                self.match(TrezParser.T__7)
                self.state = 44
                self.arg_list()
                self.state = 45
                self.match(TrezParser.T__8)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 57
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 55
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = TrezParser.MulDivExprContext(self, TrezParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 49
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 50
                        _la = self._input.LA(1)
                        if not(_la==TrezParser.T__3 or _la==TrezParser.T__4):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 51
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = TrezParser.AddSubExprContext(self, TrezParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 52
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 53
                        _la = self._input.LA(1)
                        if not(_la==TrezParser.T__5 or _la==TrezParser.T__6):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 54
                        self.expr(7)
                        pass

             
                self.state = 59
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TrezParser.ExprContext)
            else:
                return self.getTypedRuleContext(TrezParser.ExprContext,i)


        def getRuleIndex(self):
            return TrezParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = TrezParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.match(TrezParser.T__9)
                self.state = 61
                self.match(TrezParser.T__10)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(TrezParser.T__9)
                self.state = 63
                self.expr(0)
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==TrezParser.T__11:
                    self.state = 64
                    self.match(TrezParser.T__11)
                    self.state = 65
                    self.expr(0)
                    self.state = 70
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 71
                self.match(TrezParser.T__10)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Arg_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TrezParser.ExprContext)
            else:
                return self.getTypedRuleContext(TrezParser.ExprContext,i)


        def getRuleIndex(self):
            return TrezParser.RULE_arg_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_list" ):
                return visitor.visitArg_list(self)
            else:
                return visitor.visitChildren(self)




    def arg_list(self):

        localctx = TrezParser.Arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arg_list)
        self._la = 0 # Token type
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TrezParser.T__8]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [TrezParser.T__7, TrezParser.T__9, TrezParser.NUMBER, TrezParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.expr(0)
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==TrezParser.T__11:
                    self.state = 77
                    self.match(TrezParser.T__11)
                    self.state = 78
                    self.expr(0)
                    self.state = 83
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         




