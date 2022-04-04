# Machine Learning e Data Science com Python de A a Z

Link do curso:
https://www.udemy.com/course/machine-learning-e-data-science-com-python-y/

## Classificaçâo

````
Seja muito bem-vindo(a) a primeira parte do curso que abordará sobre a tarefa de classificação da aprendizagem de máquina. Você aprenderá:

Pré-processamento e preparação de bases de dados para classificação
Aprendizagem bayesiana (algoritmo Naive Bayes)
Aprendizagem por árvores de decisão (algoritmo básico de árvores e Random Forest)
Aprendizagem por regras (algoritmo OneR)
Aprendizagem baseada em instâncias (algoritmo kNN)
Regressão logística
Máquinas de vetores de suporte (SVM)
Redes neurais artificiais
Avaliação de algoritmos de classificação
Combinação e rejeição de classificadores
````

## Recomendações de Livros Naivy Bayes

NaiveBayes Links

+ Livro Thoughtful Machine Learning de Matthew Kirk: o capítulo 4 apresenta mais sobre a teoria do 
Naive Bayes  e mostra como construir um classificador de spam

+ Livro Data Algorithms de Mahmoud Parsian: o capítulo 14 apresenta explicações sobre a teoria do Naive Bayes

## Regressão

````
Olá!

Seja muito bem-vindo(a) a segunda parte do curso que abordará sobre a tarefa de regressão da aprendizagem de máquina. Você aprenderá:

Regressão linear (simples e múltipla)

Regressão polinomial

Regressão com árvores de decisão e random forest

Regressão com vetores de suporte (SVR)

Regressão com redes neurais artificiais

Bons estudos! :)
````

Modelagem para calcular um valor numérico

Exmeplos:
+ Temperatura + Umidade + Pressão do Ar ==> Velocidade do vento
+ Idade ==> Custo do plano de saude
+ Tamnho da casa => Preço da casa

### Regressão linear

Tentar enqaontra a melhor equaçâo de primeiro grau, ou seja, uma reta. Buscamos achar o melhor parâmetro a e b para encaixar aos dados
````
y = ax + b
````

### Calculando Erro
MeanSquareError (MSE)

````
MSE = (1/N) *  sum(( valor_real_i - valor_predito_i)^2)
somatório de i à N
````

Quando tiver erros muito grnde, vai ter um erro muito alto.

Esse erro é usada como critério para treinamento

MAE - Mean Absolute Error
Usado para avaliaçâo

## Regressão linear múltipla

A regressão linaer simples busca uma reta simples, buscando somente 2 parâmetros

````
y = ax + b, onde buscao o melhor "a" e "b"

````

A Regressão Linear Múltipla busca mais parâmetros.

NO CÓDIGO
````
A difenreça entre os códigos está na quantidade de features para treinar/testar. ENquanto na Simplles é apenas 1 features, na Múltipla há mais de 1. Por isso que usam o mesmo classificador

## Regressâo Linear Polinomial

A fórmula é bem pareceida com as anteriores, agora teremos x^2, x^3 e assim por diante.

Para uma mesma feature, vocÊ faz a multiplicaçâor po x^1, x^2, x^3 e etc..

Você gera uma Curva.

No sklearn, para fazer a regresão POlinomial você deve gerar mis features que serão os dados como x^

## Avaliação de Algoritmos de Regressão

````
Durante as aulas sobre regressão você aprendeu que pode utilizar a métrica score para avaliar o desempenho de um algoritmo de regressão, juntamente com o cálculo do mean_absolute_error para comparar os resultados previstos com os resultados reais. Para uma correta avaliação de um algoritmo você pode seguir os mesmos passos apresentados nas aulas sobre classificação, ou seja:

Utilizar validação cruzada ao invés de dividir a base em porções para treinamento e teste

Executar pelo menos 30 testes com cada algoritmo, utilizando o valor retornado pelo score (opcionalmente você pode usar o mean_absolute_error)

Construir a planilha com os resultados, calculando a média dos 30 testes de cada algoritmo

Fazer os testes de Friedmann e Nemenyi para verificar se existe diferença estatística significativa entre os resultados

Por fim, por meio dos resultados escolher o melhor algoritmo

No módulo sobre classificação também foram apresentados os conceitos sobre combinação e rejeição de classificadores, que também podem ser utilizados para problemas de regressão. As diferenças são:

Na combinação de regressores, você deve obter o valor da previsão numérica de cada algoritmo e calcular a média para calcular o valor final

Na rejeição de regressores, você pode estipular um valor mínimo para o mean_absolute_error, e caso o valor previsto seja maior que esse parâmetro você pode ignorar a resposta do regressor
````

## Outros Livros para Regressão

````
Capítulo 7 (Polynomial Regression Models)  do livro Introduction to Linear Regression Analysis de G. Geoffrey Vining, Elizabeth A. Peck e Douglas C. Montgomery: mostra bastante sobre a teoria da regressão polinomial

Livro Classification and Regression Trees de Leo Breiman: livro clássico sobre árvores de decisão, tanto para classificação quanto para regressão

Livro Machine Learning with Random Forests and Decision Trees de Scott Hartshorn: material bem didático sobre árvores de decisão, que vai ajudar na compreensão de regressão com esse tipo de técnica

Livro Introduction on Support Vector Regression de Vishnu Sudheer Menon: livro específico sobre regressão e máquinas de vetores de suporte

E caso você queira saber mais sobre regressão com redes neurais, você pode consultar as referências complementares do módulo sobre redes neurais (em geral são apresentados conceitos tanto para classificação quanto para regressão no mesmo material)

# Regras de Associação

````
Olá!

Seja bem-vindo(a) a terceira parte do curso, que vai abordar sobre a descoberta de regras de associação! Você aprenderá sobre:

Uma introdução teórica sobre as regras de associação e suas principais aplicações

O passo a passo completo do funcionamento do Apriori, que é o algoritmo clássico para regras de associação

Dois exemplo práticos para análise de cestas de compras em mercados utilizando a biblioteca apyori

E como bônus você terá também duas aulas sobre o algoritmo ECLAT para geração de itens frequentes

Esse conteúdo é o mesmo do meu outro curso Mineração de Regras de Associação com Python, Apriori e SQL (com exceção do material sobre o ECLAT). Caso você queira aprender mais sobre esse assunto eu recomendo você fazer esse curso, que aborda também como fazer a transformação de bases de dados comerciais em um formato para aplicação do algoritmo Apriori! São mostrados mais dois exemplos com bases de dados reais, ou seja, o cenário de uma pizzaria e de uma universidade! Nos recursos dessa aula você pode acessar o link para o curso!

Bons estudos!

Jones
````

É dados do curso:

**mineracao-de-regras-de-associacao-com-python-apriori-e-sql/**

https://www.udemy.com/course/mineracao-de-regras-de-associacao-com-python-apriori-e-sql/


Descriçâo do curso
````
A descoberta de regras de associação é uma das subáreas da Mineração de Dados mais populares e que apresenta uma diversidade muito grande de aplicações práticas e comerciais! Se você estuda Inteligência Artificial, talvez já tenha ouvido falar daquele clássico exemplo das fraudas e cervejas! Caso não, há vários anos um mercado muito famoso descobriu um padrão bem interessante em seus dados: em certos dias da semana existiam muitas vendas em conjunto tanto de fraudas quanto de cervejas. De posse desse conhecimento, eles decidiram alterar a disposição das prateleiras do mercado e conseguiram otimizar as vendas desses dois produtos em conjunto (o que aumentou significativamente as receitas). O segredo disso é que eles usaram a técnica de regras de associação, que tem como objetivo a descoberta de padrões nos dados que não podem ser facilmente encontrados somente "batendo o olho" nos registros. Essa técnica utiliza um algoritmo (o mais famoso é o Apriori) que é capaz de descobrir esse tipo de associação, podendo ser aplicado nos mais variados cenários!

E neste curso você verá passo a passo o funcionamento do algoritmo Apriori, ou seja, dada uma base de dados você vai aprender como ele consegue gerar as regras de associação, bem como compreender como são feitos os cálculos de suporte, confiança e lift; que são as métricas mais utilizadas neste tipo de cenário. Utilizaremos a linguagem Python e o banco de dados MySql para o desenvolvimento dos exemplos. Inicialmente trabalharemos com duas bases de dados prontas de mercado e o objetivo será analisar as associações que podem ser encontradas entre os produtos que são vendidos em conjunto, processo conhecido como Market Basket Analysis (análise de cestas de mercado). Logo depois, utilizaremos duas bases de dados reais: a primeira de uma pizzaria (inclusive a pizzaria era minha!) e a segunda de uma pesquisa sócio-econômica de alunos que fizerem o vestibular em uma universidade! A ideia é realizar o processo KDD completo (Knowledge Discovery in Databases - Descoberta de Conhecimento em Bases de Dados) nessas duas bases de dados, passando pelos processos de seleção de atributos, pré-processamento e transformação dos dados antes de realizar as análises com o algoritmo Apriori. O objetivo dessas seções é que você tenha uma visão prática e comercial de como funciona esse processo em bases de dados comerciais, visto que a maioria dos materiais sobre o assunto abordam somente a aplicação do algoritmo e deixa de lado todo o processo de preparação das bases de dados!

Por fim, ainda teremos mais um módulo adicional que mostrará como importar uma base de dados fictícia de mercado para um padrão na qual as análises possam ser realizadas. Nessas aulas, é mostrado passo a passo como realizar a conexão do Python com o MySql e realizar as consultas para obter os dados no padrão requerido para aplicação do Apriori. Esse módulo é útil caso você tenha uma base de dados no modelo Entidade Relacionamento e deseja aprender os processos básicos para conversão dos dados. Ao final do curso, você será capaz de implementar suas próprias análises e em suas próprias bases de dados, o que pode abrir diversas oportunidades de negócio e de renda extra para você! É importante enfatizar que este curso é para todos os níveis, seja para você que está iniciando nessa área ou para você que já possui conhecimentos sobre regras de associação e deseja conhecer mais sobre o assunto.
````

## Agrupamento - CLustering

> Seja bem-vindo(a) a quarta parte do curso, que vai abordar sobre a técnica não supervisionada de agrupamento! Você aprenderá sobre a teoria e a prática sobre três dos principais algoritmos de agrupamento:

K-means

Agrupamento hierárquico

DBSCAN

Implementaremos os três algoritmos usando a biblioteca scikit-learn e vamos usar uma base de dados real com 30.000 registros sobre cartões de crédito. O objetivo será encontrar grupos de clientes baseado no limite do cartão e nos gastos do cliente!
