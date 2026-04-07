lexer grammar miniportugolLexer;

NUMBER : [0-9]+;
ID     : [a-z]+;
WS     : [ \t\r\n]+ -> skip; // Ignore whitespace