parser grammar TrezParser;

options { tokenVocab = TrezLexer; }

// Parser Rules
program: statement+ EOF;

statement: let_stmt
         | expr_stmt
         | if_stmt
         | while_stmt
         | block
         ;

let_stmt: LET ID EQ expr SEMI;

expr_stmt: expr SEMI;

if_stmt: IF LPAREN expr RPAREN block (ELSE block)?;

while_stmt: WHILE LPAREN expr RPAREN block;

block: LBRACE statement* RBRACE;

expr: expr OR expr                      # OrExpr
    | expr AND expr                     # AndExpr
    | expr (EQEQ | NEQ) expr            # EqExpr
    | expr (LT | LE | GT | GE) expr     # CompareExpr
    | expr (PLUS | MINUS) expr          # AddSubExpr
    | expr (MUL | DIV | MOD) expr       # MulDivExpr
    | expr POW expr                     # PowExpr
    | MINUS expr                        # UnaryMinusExpr
    | NUMBER                            # NumExpr
    | STRING                            # StringExpr
    | TRUE                              # BoolExpr
    | FALSE                             # BoolExpr
    | ID LPAREN (expr (COMMA expr)*)? RPAREN  # FuncCallExpr
    | ID                                # VarExpr
    | LPAREN expr RPAREN                # ParenExpr
    | array                             # ArrayExpr
    ;

array: LBRACK RBRACK
     | LBRACK expr (COMMA expr)* RBRACK
     ;
