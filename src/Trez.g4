grammar Trez;

// Parser Rules
program: statement+ EOF;

statement: expr_stmt;

expr_stmt: expr ';' ;

expr: expr ('*' | '/') expr      # MulDivExpr
    | expr ('+' | '-') expr      # AddSubExpr
    | NUMBER                     # NumberExpr
    | '(' expr ')'               # ParensExpr
    ;

// Lexer Rules
NUMBER: [0-9]+ ('.' [0-9]+)?;
WS: [ \t\r\n]+ -> skip;
