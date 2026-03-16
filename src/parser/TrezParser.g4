parser grammar TrezParser;

options { tokenVocab = TrezLexer; }

// Parser Rules
program: statement+ EOF;

statement: let_stmt
         | expr_stmt
         ;

let_stmt: LET ID EQ expr SEMI;

expr_stmt: expr SEMI;

expr: expr (MUL | DIV) expr              # MulDivExpr
    | expr (PLUS | MINUS) expr           # AddSubExpr
    | NUMBER                              # NumExpr
    | STRING                              # StringExpr
    | ID                                  # VarExpr
    | LPAREN expr RPAREN                  # ParenExpr
    | array                               # ArrayExpr
    | ID LPAREN (expr (COMMA expr)*)? RPAREN  # FuncCallExpr
    ;

array: LBRACK RBRACK
     | LBRACK expr (COMMA expr)* RBRACK
     ;
