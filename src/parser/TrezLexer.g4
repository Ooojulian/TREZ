lexer grammar TrezLexer;

// Keywords
LET: 'let';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
TRUE: 'true';
FALSE: 'false';

// Symbols
// Symbols (longer tokens first)
POW: '**';
AND: '&&';
OR: '||';
EQEQ: '==';
NEQ: '!=';
LE: '<=';
GE: '>=';
LT: '<';
GT: '>';
MOD: '%';

LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
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
