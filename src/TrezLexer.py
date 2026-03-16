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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t")
        buf.write("\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\5\16?\n\16\3\16")
        buf.write("\6\16B\n\16\r\16\16\16C\3\16\3\16\6\16H\n\16\r\16\16\16")
        buf.write("I\5\16L\n\16\3\17\3\17\7\17P\n\17\f\17\16\17S\13\17\3")
        buf.write("\20\6\20V\n\20\r\20\16\20W\3\20\3\20\3\21\3\21\3\21\3")
        buf.write("\21\7\21`\n\21\f\21\16\21c\13\21\3\21\3\21\2\2\22\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22\3\2\7\3\2\62;\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\5\2\13\f\17\17\"\"\4\2\f\f\17\17\2l\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\3#\3\2\2\2\5\'\3\2\2\2")
        buf.write("\7)\3\2\2\2\t+\3\2\2\2\13-\3\2\2\2\r/\3\2\2\2\17\61\3")
        buf.write("\2\2\2\21\63\3\2\2\2\23\65\3\2\2\2\25\67\3\2\2\2\279\3")
        buf.write("\2\2\2\31;\3\2\2\2\33>\3\2\2\2\35M\3\2\2\2\37U\3\2\2\2")
        buf.write("![\3\2\2\2#$\7n\2\2$%\7g\2\2%&\7v\2\2&\4\3\2\2\2\'(\7")
        buf.write("?\2\2(\6\3\2\2\2)*\7=\2\2*\b\3\2\2\2+,\7,\2\2,\n\3\2\2")
        buf.write("\2-.\7\61\2\2.\f\3\2\2\2/\60\7-\2\2\60\16\3\2\2\2\61\62")
        buf.write("\7/\2\2\62\20\3\2\2\2\63\64\7*\2\2\64\22\3\2\2\2\65\66")
        buf.write("\7+\2\2\66\24\3\2\2\2\678\7]\2\28\26\3\2\2\29:\7_\2\2")
        buf.write(":\30\3\2\2\2;<\7.\2\2<\32\3\2\2\2=?\7/\2\2>=\3\2\2\2>")
        buf.write("?\3\2\2\2?A\3\2\2\2@B\t\2\2\2A@\3\2\2\2BC\3\2\2\2CA\3")
        buf.write("\2\2\2CD\3\2\2\2DK\3\2\2\2EG\7\60\2\2FH\t\2\2\2GF\3\2")
        buf.write("\2\2HI\3\2\2\2IG\3\2\2\2IJ\3\2\2\2JL\3\2\2\2KE\3\2\2\2")
        buf.write("KL\3\2\2\2L\34\3\2\2\2MQ\t\3\2\2NP\t\4\2\2ON\3\2\2\2P")
        buf.write("S\3\2\2\2QO\3\2\2\2QR\3\2\2\2R\36\3\2\2\2SQ\3\2\2\2TV")
        buf.write("\t\5\2\2UT\3\2\2\2VW\3\2\2\2WU\3\2\2\2WX\3\2\2\2XY\3\2")
        buf.write("\2\2YZ\b\20\2\2Z \3\2\2\2[\\\7\61\2\2\\]\7\61\2\2]a\3")
        buf.write("\2\2\2^`\n\6\2\2_^\3\2\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2")
        buf.write("\2bd\3\2\2\2ca\3\2\2\2de\b\21\2\2e\"\3\2\2\2\n\2>CIKQ")
        buf.write("Wa\3\b\2\2")
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
    LINE_COMMENT = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'let'", "'='", "';'", "'*'", "'/'", "'+'", "'-'", "'('", "')'", 
            "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "ID", "WS", "LINE_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "NUMBER", "ID", 
                  "WS", "LINE_COMMENT" ]

    grammarFileName = "Trez.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


