lexer grammar TrezLexer;

// Keywords
LET: 'let';

// Symbols
LPAREN: '(';
RPAREN: ')';
LBRACK: '[';
RBRACK: ']';
COMMA: ',';
SEMI: ';';
EQ: '=';
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';

// Literals
NUMBER: '-'? [0-9]+ ('.' [0-9]+)?;
STRING: '"' (~["\r\n\\] | '\\' .)* '"';

// Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Skip
WS: [ \t\r\n]+ -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
