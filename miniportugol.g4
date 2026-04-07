grammar miniportugol;

program
    :
    declaracao_variavel*
    lista_comandos*
    ;

/* Definição da estrutura dos comandos */
cond_op: (expr_aritmeticas ID)? expr_condicionais ID;
condicao: AP ID cond_op? FP;

/* Comandos */
declaracao_variavel: tipos_variaveis ID ID* PV;
comando_escreva: ESCREVA AP STRING FP PV;
comando_ler: LEIA AP ID FP PV;
comando_se: SE AP ID cond_op? FP AC lista_comandos lista_comandos* FC comando_senao?;
comando_senao: SENAO condicao? AC lista_comandos lista_comandos* FC comando_senao?;
comando_enquanto: ENQUANTO AP ID cond_op? FP AC lista_comandos lista_comandos* FC;

/* Definição de expressões*/
expr_condicionais: '=='
                 | '&&'
                 | '||'
                 | '=!'
                 ;

expr_aritmeticas: '+'
                | '-'
                | '/'
                ;

/* Definição das variáveis*/
tipos_variaveis: 'INT'
               | 'String'
               ;

/* Declarações*/
lista_comandos: comando_escreva
              | comando_ler
              | comando_se
              | comando_enquanto
              ;

/* Regra de skip*/
WS: [ \t\r\n] -> skip ;

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
ID: 'a'..'z'|'0'..'9' ('a'..'z'|'0'..'9')*;
