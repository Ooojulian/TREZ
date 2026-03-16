grammar Trez;

// Parser Rules
program: statement+ EOF;

statement: let_stmt
         | expr_stmt
         ;

let_stmt: 'let' ID '=' expr ';' ;

expr_stmt: expr ';' ;

expr: expr ('*' | '/') expr      # MulDivExpr
    | expr ('+' | '-') expr      # AddSubExpr
    | NUMBER                     # NumberExpr
    | '(' expr ')'               # ParensExpr
    | array                      # ArrayExpr
    | ID                         # VarExpr
    | ID '(' arg_list ')'        # FuncCallExpr
    ;

array: '[' ']'
     | '[' expr (',' expr)* ']'
     ;

arg_list: /* empty */
        | expr (',' expr)*
        ;

// Lexer Rules
NUMBER: '-'? [0-9]+ ('.' [0-9]+)?;
ID: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;
