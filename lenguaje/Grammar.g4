grammar Grammar;
program:[statement NEWLINE]*EOF;

statement: assign|print|if_statement|for_statement;

assing:ID'='expr;

print:'print''('expr')'

if_statement:'if''('expr')'block;

for_statement:'for''('assing';'expr';'assing')'block;

block:'{'(statement NEW LINE)*'}';

expr:expr op=('*'|'/')expr
    |expr op=('+'|'-')expr
    |expr op=('>'|'<'|'<='|'>=')expr
    |expr op=('=='|'!=')expr
    |ID
    |'('expr')'
    ;

ID:[a-zA-Z][a-zA-Z_0-9]*;
NEWLINE:[\r\n];
WS:[\t]->skip;
SEMI:';';
