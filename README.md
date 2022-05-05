# Curso de Python do ZERO AO DS

> Ministrado por Meigarom do canal “Seja Um Data Scientist”.

## Módulo 01 - Começando com Python

### O problema de negócio
A empresa fictícia House Rocket compra imóveis por um preço baixo e revende por um preço alto através de uma plataforma online de compra e venda de imóveis. O CEO deseja maximizar o lucro da empresa encontrando bons imóveis para comprar e revender. A principal estratégia é utilizar fontes externas para encontrar bons negócios.

#### As perguntas do CEO da House Rocket:
1. Quantas casas estão disponíveis para compra?
2. Quantos atributos as casas possuem (número de quartos, número de garagens, m2, vista para o mar)?
3. Quais são os atributos?
4. Qual a casa mais cara do portfólio (casa com maior valor)?
5. Qual a casa com o maior número de quartos?
6. Qual a soma total de quartos do conjunto de dados?
7. Quantas casas possuem 2 banheiros?
8. Qual o preço médio de todas as casas no conjunto de dados?
9. Qual o preço médio de casas com 2 banheiros?
10. Qual o preço mínimo entre as casas com 3 quartos?
11. Quantas casas possuem mais de 300 metros quadrados na sala de estar?
12. Quantas casas tem mais de 2 andares?
13. Quantas casas tem vista para o mar?
14. Das casas com vista para o mar, quantas tem 3 quartos?
15. Das casas com mais de 300 metros quadrados de sala de estar, quantas tem mais de 2 banheiros?

### Planejamento da solução

#### Planejamento do PRODUTO FINAL:
1. O que eu vou entregar (Planilha, Texto, E-mail, Modelos de ML, …)? R: Texto com as respostas.
2. Como vai ser a entrega? R: Perguntas | Respostas.

#### Planejamento do PROCESSO:
1. Onde está a informação (Excel, BD, API, manual)? R: [Nesse site](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction).
2. Como coletar essas informações (SQL, Python, Streamlit, …)? R: Download (apertar o botão).
3. Como responder as perguntas? Exemplos:
   - Quantas casas estão disponíveis para compra? R: Contar o número de linhas do conjunto de dados.
   - Quantos atributos as casas possuem (número de quartos, garagens, m2, vista para o mar)? R: Contar o número de colunas do conjunto de dados.
   - Quais são os atributos? R: Mostrar o nome das colunas (automática).
   - Qual a casa mais cara do portfólio (casa com maior valor)? R: Ordenar as linhas pela coluna de preço (atributos).
   - Qual a casa com o maior número de quartos? R: Contar o número de linhas pela coluna número de quartos (atributo).
    
#### Planejamento das FERRAMENTAS:

##### Quais ferramentas eu posso usar?

###### Excel
1. Fácil de usar;
2. Barato;
3. Muito usado pelos times não técnicos;
4. Poder de processamento limitado (1MM);
5. Não é escalável;
6. Gerenciamento complexo;
7. Limitado para grandes volumes de dados: Big data VVV (Volume, Velocidade, Variação).
        
###### Linguagem de programação
1. Originalmente criada para o desenvolvimento de software;
2. Processamento, Análise e Visualização de Dados;
3. Mais complexa;
4. Escalável (poder de processamento depende de muitos computadores);
5. Fácil gerenciamento (Git).

## Módulo 02 - Manipulação de Dados

### Novas perguntas do CEO
1. Qual a data do imóvel mais antigo no portfólio?
2. Quantos imóveis possuem o número máximo de andares?
3. Criar uma classificação para os imóveis, separando-os em baixo e alto padrão, de acordo com preço. 
   - Acima de R$ 540.000 -> alto padrão; 
   - Abaixo de R$ 540.000 -> baixo padrão.
4. Gostaria de um relatório ordenado pelo preço e contento as seguintes informações:
   - Id do imóvel;
   - Data que o imóvel ficou disponível para compra;
   - O número de quartos;
   - O tamanho total to terreno;
   - O preço;
   - A classificação do imóvel (alto e baixo padrão).
5. Gostaria de um Mapa indicando onde as casas estão localizadas geograficamente.


### Planejamento de solução

#### Produto Final
E-mail + 2 anexos:
  - E-mail:
    - Texto: Perguntas | Respostas;
  - Anexos:
    - Um relatório em .csv;
    - A foto de um mapa em html.
         

#### Ferramenta
- Python 3.8.0;
- PyCharm.


#### Processo
1. Qual a data do imóvel mais antigo no portfólio?
   - Ordenar o conjunto de dados pela menor data.
2. Quantos imóveis possuem o número máximo de andares?
   - Encontrar os números de andares e determinar o maior 
   - Contar quanto imóveis eu tenho por andar.
3. Criar uma classificação para os imóveis, separando-os em baixo e alto padrão, de acordo com preço:
   - Acima de R$ 540.000 -> alto padrão (high_standard);
   - Abaixo de R$ 540.000 -> baixo padrão (low_standard).
   - Criar uma nova coluna no conjunto de dados chamada “standard”
   - Para cada linha, eu vou comparar a coluna “price”;
   - Se “price” for maior que 540.000, eu vou escrever “high_standard” na coluna “standard”;
   - Se “price” for menor que 540.000, eu vou escrever “low_standard” na coluna “standard”.
4. Gostaria de um relatório ordenado pelo preço e contendo as seguintes informações: id do imóvel, data que o imóvel ficou disponível para compra, o número de quartos, o tamanho total do terreno, o preço, a classificação do imóvel (alto e baixo padrão).
   - Selecionar as colunas desejadas/demandas;
   - Deletar as colunas não desejadas/demandas.
5. Gostaria de um Mapa indicando onde as casas estão localizadas geograficamente.
   - Procurar uma biblioteca em Python que armazena uma função que desenhe mapa;
   - Aprender a usar a função que desenha mapas.


##### Mais perguntas do CEO:
1. Crie uma nova coluna chamada: “house_age”:
   - Se o valor da coluna “date” for maior que 2014-01-01 => ‘new_house’;
   - Se o valor da coluna “date” for menor que 2014-01-01 => ‘old_house’.
2. Crie uma nova coluna chamada “dormitory_type”:
   - Se o valor da coluna “bedrooms” for igual à 1 => ‘studio’;
   - Se o valor da coluna “bedrooms” for igual a 2 => ‘apartament’;
   - Se o valor da coluna “bedrooms” for maior que 2 => ‘house’.
3. Crie uma nova coluna chamada “condition_type”:
   - Se o valor da coluna “condition” for menor ou igual à 2 => ‘bad’;
   - Se o valor da coluna “condition” for igual à 3 ou 4 => ‘regular’;
   - Se o valor da coluna “condition” for igual à 5 => ‘good’.
4. Modifique o TIPO da Coluna “condition” para STRING.
5. Delete as colunas “sqft_living15” e “sqft_lot15”.
6. Modifique o TIPO da Coluna “yr_build” para DATE.
7. Modifique o TIPO da Coluna “yr_renovated” para DATE.
8. Qual a data mais antiga de construção de um imóvel?
9. Qual a data mais antiga de renovação de um imóvel?
10. Quantos imóveis tem 2 andares?
11. Quantos imóveis estão com a condição igual a “regular”?
12. Quantos imóveis estão com a condição igual a “bad”e possuem “vista para água”?
13. Quantos imóveis estão com a condição igual a “good” e são “new_house”?
14. Qual o valor do imóvel mais caro do tipo “studio”?
15. Quantos imóveis do tipo “apartment” foram reformados em 2015?
16. Qual o maior número de quartos que um imóveis do tipo “house” possui?
17. Quantos imóveis “new_house” foram reformados no ano de 2014?
18. Selecione as colunas “id”, “date”, “price”, “floors”, “zipcode” pelos métodos:
    - Direto pelo nome das colunas;
    - Pelos Índices;
    - Pelos Índices das linhas e o nome das colunas;
    - Índices Booleanos.
19. Salve um arquivo .csv com somente as colunas do item 10 ao 17.
20. Modifique a cor dos pontos no mapa de “pink” para “verde-escuro”.


## Módulo 03 - Estruturas de dados
### Novas perguntas do CEO:
1. Qual o número de imóveis por ano de construção?
2. Qual o menor número de quartos por ano de construção dos imóveis?
3. Qual o preço de compra mais alto por cada número de quartos?
4. Qual a soma de todos os preços de compra por cada número de quartos?
5. Qual a soma de todos os preços de compra pelo número de quartos e banheiros?
6. Qual o tamanho médio das salas dos imóveis por ano de construção?
7. Qual o tamanho mediano das salas dos imóveis por ano de construção?
8. Qual o desvio-padrão do tamanho das salas dos imóveis por ano de construção?
9. Como é o crescimento médio preços de compra dos imóveis, por dia e semana do ano?
10. Eu gostaria de olhar no mapa e conseguir identificar as casas com o maior preço.


### Planejamento da solução:

#### Produto Final (O que eu vou entregar?)
- Email + 2 anexos:
  - Email: As respostas das perguntas no formato Pergunta |Resposta;
  - Anexo 01: Um dashboard com 3 gráfico;
  - Anexo 02: A foto de um mapa 2.0 em .html


#### Ferramentas:
- Python 3.8.0;
- Jupyter Notebook.


#### Processo:
1. Qual o número de imóveis por ano de construção?
   - Contar o número de ids por ano de construção.
2. Qual o menor número de quartos por ano de construção dos imóveis?
   - Filtrar todos os imóveis por ano de construção e selecionar o menor número de quartos.
3. Qual o preço de compra mais alto por cada número de quartos?
   - Filtrar todos os imóveis por número de quarto e selecionar o maior preço.
4. Qual a soma de todos os preços de compra por cada número de quartos?
   - Filtrar todos os imóveis por número de quarto e somar todos os preços.
5. Qual a soma de todos os preços de compra pelo número de quartos e banheiros?
   - Filtrar todos os imóveis por número de quarto e banheiro e somar todos os preços.
6. Qual o tamanho médio das salas dos imóveis por ano de construção?
   - Filtrar todos os imóveis por ano de construção e fazer a média do tamanho das salas.
7. Qual o tamanho mediano das salas dos imóveis por ano de construção?
   - Filtrar todos os imóveis por ano de construção e calcular a mediana do tamanho das salas.
8. Qual o desvio-padrão do tamanho das salas dos imóveis por ano de construção?
   - Filtrar todos os imóveis por ano de construção e calcular o desvio-padrão do tamanho das salas.
9. Como é o crescimento médio preços de compra dos imóveis, por dia e semana do ano?
   - Filtrar todos os imóveis por data e calcular o preço médio.
   - Procurar uma Biblioteca em Python que tenha uma Função que desenhe um gráfico de linha;
   - Aprender a usar a função e desenhar um a variação do preço médio por dia e semana do ano.
10. Eu gostaria de olhar no mapa e conseguir identificar as casas com o maior preço.
    - Modificar o mapa da entrega anterior fazendo com que os pontos tenham o tamanho dependente do preço.

