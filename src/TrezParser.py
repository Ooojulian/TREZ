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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("*\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\f\n\2\r\2\16")
        buf.write("\2\r\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\5\5\35\n\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5%\n\5\f\5\16")
        buf.write("\5(\13\5\3\5\2\3\b\6\2\4\6\b\2\4\3\2\4\5\3\2\6\7\2)\2")
        buf.write("\13\3\2\2\2\4\21\3\2\2\2\6\23\3\2\2\2\b\34\3\2\2\2\n\f")
        buf.write("\5\4\3\2\13\n\3\2\2\2\f\r\3\2\2\2\r\13\3\2\2\2\r\16\3")
        buf.write("\2\2\2\16\17\3\2\2\2\17\20\7\2\2\3\20\3\3\2\2\2\21\22")
        buf.write("\5\6\4\2\22\5\3\2\2\2\23\24\5\b\5\2\24\25\7\3\2\2\25\7")
        buf.write("\3\2\2\2\26\27\b\5\1\2\27\35\7\n\2\2\30\31\7\b\2\2\31")
        buf.write("\32\5\b\5\2\32\33\7\t\2\2\33\35\3\2\2\2\34\26\3\2\2\2")
        buf.write("\34\30\3\2\2\2\35&\3\2\2\2\36\37\f\6\2\2\37 \t\2\2\2 ")
        buf.write("%\5\b\5\7!\"\f\5\2\2\"#\t\3\2\2#%\5\b\5\6$\36\3\2\2\2")
        buf.write("$!\3\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'\t\3\2\2\2")
        buf.write("(&\3\2\2\2\6\r\34$&")
        return buf.getvalue()


class TrezParser ( Parser ):

    grammarFileName = "Trez.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'*'", "'/'", "'+'", "'-'", "'('", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUMBER", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_expr_stmt = 2
    RULE_expr = 3

    ruleNames =  [ "program", "statement", "expr_stmt", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    NUMBER=8
    WS=9

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
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.statement()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==TrezParser.T__5 or _la==TrezParser.NUMBER):
                    break

            self.state = 13
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
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.expr_stmt()
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
        self.enterRule(localctx, 4, self.RULE_expr_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.expr(0)
            self.state = 18
            self.match(TrezParser.T__0)
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



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TrezParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TrezParser.NUMBER]:
                localctx = TrezParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 21
                self.match(TrezParser.NUMBER)
                pass
            elif token in [TrezParser.T__5]:
                localctx = TrezParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                self.match(TrezParser.T__5)
                self.state = 23
                self.expr(0)
                self.state = 24
                self.match(TrezParser.T__6)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 34
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = TrezParser.MulDivExprContext(self, TrezParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 28
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 29
                        _la = self._input.LA(1)
                        if not(_la==TrezParser.T__1 or _la==TrezParser.T__2):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 30
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = TrezParser.AddSubExprContext(self, TrezParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 31
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 32
                        _la = self._input.LA(1)
                        if not(_la==TrezParser.T__3 or _la==TrezParser.T__4):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 33
                        self.expr(4)
                        pass

             
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




