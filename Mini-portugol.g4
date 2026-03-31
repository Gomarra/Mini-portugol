grammar lingua;

program
    :  
    INICIO
    declaracao_variavel*
    lista_comando*
    FIM
    ;

/* Definição de palavras e simbolos*/
INICIO:'inicio';
FIM:'fim';
LEIA:'leia';
ESCREVA:'escreva';
SE:'se';
SENAO:'senao';
ENQUANTO:'enquanto';
PARA:'para';
AP:'(';
FP:')';
PV:';';
AC:'{';
FC:'}';

/* Definição de tipos de variáveis */
STRING: '"' .*? '"' ;
ID: 'a'..'z'('a'..'z'|'0'..'9')*; /* Mudar para poder colocar letras e números no inicio*/

WS: [ \t\r\n] -> skip ;

expr_condicionais:
    '=='
    | '&&'
    | '||'
    | '=!'
    ;

expr_aritmeticas:
    '+'
    | '-'
    | '/'
    ;

tipos_variaveis:
    'INT'
    | 'String'
    ;

/* Definição da estrutura dos comandos */
cond_op: expr_condicionais ID;
condicao: AP ID cond_op? FP;

/* Comandos */
declaracao_variavel: tipos_variaveis ID ID* PV;
comando_escreva: ESCREVA AP STRING FP PV;
comando_ler: LEIA AP ID FP PV;
comando_se: SE AP ID cond_op? FP AC lista_comando lista_comando* FC;
comando_senao: comando_se SENAO comando_enquanto? AC lista_comando lista_comando* FC;
comando_enquanto: ENQUANTO AP ID cond_op? FP AC lista_comando lista_comando* FC;

lista_comando:
    comando_escreva
    | comando_ler
    | comando_se
    | comando_senao
    | comando_enquanto
    ;
