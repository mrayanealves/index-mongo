# Rayndex MongoDB
Atividade da disciplina de Banco de Dados NOSQL

### Pre requisitos
1. Python
2. MongoDB

### Informações gerais
A proposta dessa atividade é aplicar o conhecimento adquirido em sala de aula sobre Index no MongoDB, desenvolvendo um pequeno programa que crie e salve documentos em uma coleção tal que:

1. O documento tem que possuir dois campos (**var1 e var2**) numéricos com valores aleatórios de 0 a 100; 

2. Sejam implementados os seguintes itens:

    - **Item 1**: Gere e insira 1.000.000 de documentos na coleção e calcule o tempo gasto nessa operação;
    
    - **Item 2**: Busque por valores de var1 que estejam entre 0 e 10 e calcule o tempo gasto nessa operação;
    
    - **Item 3**: Crie um index para var1, repita a consulta anterior e calcule o tempo gasto nessa operação;
    
    - **Item 4**: Repita a consulta anterior retornando somente o valor de var1, removendo os demais usando projeção, e calcule o tempo gasto nessa operação;
    
    - **Item 5**: Gere e insira mais 1.000.000 de documentos na coleção e calcule o tempo gasto nessa operação.
    
A ideia é comparar os tempos gastos nessas operações considerando dois cenários: antes e depois da criação do indíce.
