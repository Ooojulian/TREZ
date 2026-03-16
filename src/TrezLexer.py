# Generated from Trez.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("Y\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\2\3\3\3\3\3\4")
        buf.write("\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\3\r\3\r\3\16\5\16=\n\16\3\16\6\16@\n")
        buf.write("\16\r\16\16\16A\3\16\3\16\6\16F\n\16\r\16\16\16G\5\16")
        buf.write("J\n\16\3\17\3\17\7\17N\n\17\f\17\16\17Q\13\17\3\20\6\20")
        buf.write("T\n\20\r\20\16\20U\3\20\3\20\2\2\21\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21\3\2\6\3\2\62;\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17")
        buf.write("\17\"\"\2^\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\3!\3\2\2\2\5%")
        buf.write("\3\2\2\2\7\'\3\2\2\2\t)\3\2\2\2\13+\3\2\2\2\r-\3\2\2\2")
        buf.write("\17/\3\2\2\2\21\61\3\2\2\2\23\63\3\2\2\2\25\65\3\2\2\2")
        buf.write("\27\67\3\2\2\2\319\3\2\2\2\33<\3\2\2\2\35K\3\2\2\2\37")
        buf.write("S\3\2\2\2!\"\7n\2\2\"#\7g\2\2#$\7v\2\2$\4\3\2\2\2%&\7")
        buf.write("?\2\2&\6\3\2\2\2\'(\7=\2\2(\b\3\2\2\2)*\7,\2\2*\n\3\2")
        buf.write("\2\2+,\7\61\2\2,\f\3\2\2\2-.\7-\2\2.\16\3\2\2\2/\60\7")
        buf.write("/\2\2\60\20\3\2\2\2\61\62\7*\2\2\62\22\3\2\2\2\63\64\7")
        buf.write("+\2\2\64\24\3\2\2\2\65\66\7]\2\2\66\26\3\2\2\2\678\7_")
        buf.write("\2\28\30\3\2\2\29:\7.\2\2:\32\3\2\2\2;=\7/\2\2<;\3\2\2")
        buf.write("\2<=\3\2\2\2=?\3\2\2\2>@\t\2\2\2?>\3\2\2\2@A\3\2\2\2A")
        buf.write("?\3\2\2\2AB\3\2\2\2BI\3\2\2\2CE\7\60\2\2DF\t\2\2\2ED\3")
        buf.write("\2\2\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2\2HJ\3\2\2\2IC\3\2\2")
        buf.write("\2IJ\3\2\2\2J\34\3\2\2\2KO\t\3\2\2LN\t\4\2\2ML\3\2\2\2")
        buf.write("NQ\3\2\2\2OM\3\2\2\2OP\3\2\2\2P\36\3\2\2\2QO\3\2\2\2R")
        buf.write("T\t\5\2\2SR\3\2\2\2TU\3\2\2\2US\3\2\2\2UV\3\2\2\2VW\3")
        buf.write("\2\2\2WX\b\20\2\2X \3\2\2\2\t\2<AGIOU\3\b\2\2")
        return buf.getvalue()


class TrezLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    NUMBER = 13
    ID = 14
    WS = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'let'", "'='", "';'", "'*'", "'/'", "'+'", "'-'", "'('", "')'", 
            "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "ID", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "NUMBER", "ID", 
                  "WS" ]

    grammarFileName = "Trez.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


