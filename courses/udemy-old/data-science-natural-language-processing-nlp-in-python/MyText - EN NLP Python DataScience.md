# Data Science: Natural Language Processing (NLP) in Python

# Log

- Autor: Rafael Morais de Assis
- Data de criação: 22/01/2019
- TAGS:
- Link: https://www.udemy.com/data-science-natural-language-processing-in-python/learn/v4/content

**Fontes e Controle de Versão**

**Descrição em uma única frase**



## 0. Introduction

**Sumário do curso**

1. Rápida olhada nas tarefas de NLP
2. Construir um *spam detector*
3. Construir um *sentiment analyser*
4. Exlporar NLTK
   + Lib para processamento de texto. Pode ser usada em conjunto com outras técnicas de NLP
5. LSA: Latent Semantic Analysis
   + Servirar para separar duas palavras diferentes com mesmo
6. Construir *Article Spinner*
   + Criar uma cópia com mesma semântica

**

**O estado da arte em algumas aplicações de NLP**

**Very Good **

1. Detector de Spam
2. POS (parts-of-speech) => tags 
   + Reconhecer: Nome, pronome, verbo, adverbio, adjetivo, conjunâo e preposição
3. NER (named-entity recognition) 
   + Reconhecer que parte de uma sentença é uma pessoa ou entidade, ou data, ou local.
   + http://nlp.stanford.edu:8080/ner/process

**Pretty Good**

1. sentment analysis
2. machine translation
3. information extraction

**Needs improvement**

1. Machine COnversation
2. Paraphasing and summarization

**Interesting Progress**

**word2vec**

+ Aplicaçâo de NeuralNetwork que converte palavras em vetor

**Por que NLP é diíficl**

+ Por que a lingua é ambuigua enquanto que a computaçâo usa matemática que é presisa
+ Facilmente a NLp interpreta incorretamente e até agente comete esse erro

### 0.1 Objetivo do curso

**Objetivo do curso**: Nâo é aprender um algoritmo de Ml e sim fazer aplicações que usem ML para processamento de texto (NLP)

**Libs**: Usaremos bastante as Libs e principlamente Sci-Kut Learn  



### 0.2. Preaparano para o curso

Para aproveitar ao máximo esse cruso faça (Essa é uma revisao de uma palestra dele que esclarece como tirar o melhor proveitao do curso )

1. Uso generoso do Q&A (Perguntas e Respostas)
2. Atender aos requisitos do curso
3. Escreva e implemente o que for ensinado (IDE / Jupyter Notebook)
4. Se não entender alguns conceitos de ML tem resumos de alguns algoritmos no final do curso da udemy

**Conceitos que presisa saber**

1. O que é classificaçâo e regressâo e suas diferenças
   + E principlalemnte, ser capaz de entendelos geometricamente. Se eu te der um papela para explicar classificaçâo e regressâo como mostrar isso para uma pessoa
   + ML é um problema de GEOMETRIA.
2. Saber o basiclo de ML script com Scikit-leanr
3. Ententer que " All the date is the Same". Eles sempre seguem esse processo abaixo. O codigo não muda entre os dados
   + Se for estudar ML algoritmos, presisa entnendelos, e nâo se preocupar com o dataset

![](C:\Users\Rafael\Google Drive\Private Studies\TextMining\md_images\all_date_is_the_same.png)

## 1. Build SpamDetector

No NPL a mairo parte fica no pré-processamento dos dados como converter palavras num vetor de números

**dataset**

link do dataset: http://archive.ics.uci.edu/ml/datasets/Spambase

O dataset contem 48 colunas que possui a porcentagem de 0 à 100 da frequencia de uma palavra em relaçâo a todo o texto de email. A ultima indica a flag: 1 => sapm, 0 não é spam.

Contar a frequencia de uma palavra se chama **term-document matrix**

### Naive Bayes

> Naive Bayes has been studied extensively since the 1950s. It was introduced under a different name into the [text retrieval](https://en.wikipedia.org/wiki/Information_retrieval) community in the early 1960s,[[1\]](https://en.wikipedia.org/wiki/Naive_Bayes_classifier#cite_note-aima-1):488 and remains a popular (baseline) method for [text categorization](https://en.wikipedia.org/wiki/Text_categorization), the problem of judging documents as belonging to one category or the other (such as [spam or legitimate](https://en.wikipedia.org/wiki/Spam_filtering), sports or politics, etc.) with [word frequencies](https://en.wikipedia.org/wiki/Bag_of_words) as the features. With appropriate pre-processing, it is competitive in this domain with more advanced methods including [support vector machines](https://en.wikipedia.org/wiki/Support_vector_machine).[[2\]](https://en.wikipedia.org/wiki/Naive_Bayes_classifier#cite_note-rennie-2) It also finds application in automatic [medical diagnosis](https://en.wikipedia.org/wiki/Medical_diagnosis).[[3\]](https://en.wikipedia.org/wiki/Naive_Bayes_classifier#cite_note-rish-3)
>
> Naive Bayes classifiers are highly scalable, requiring a number of parameters linear in the number of variables (features/predictors) in a learning problem. [Maximum-likelihood](https://en.wikipedia.org/wiki/Maximum-likelihood_estimation) training can be done by evaluating a [closed-form expression](https://en.wikipedia.org/wiki/Closed-form_expression),[[1\]](https://en.wikipedia.org/wiki/Naive_Bayes_classifier#cite_note-aima-1):718 which takes [linear time](https://en.wikipedia.org/wiki/Linear_time), rather than by expensive [iterative approximation](https://en.wikipedia.org/wiki/Iterative_method) as used for many other types of classifiers.

Seja $$X$$ input features e $$Y$$ target:

Na probabilidade condicional

$$P(X|Y) = \frac{P(X,Y)}{P(Y)}$$
Agora, vamos manipular condição formula para achar $$P(Y|X)$$

$$P(Y|X) = \frac{P(X|Y)P(Y)}{P(X)}$$


Para nosso problema

P(Y|X) = A prob de Ser Y dado X é de ...

P(X|Y) = prob de X dado Y (Isso é calculado usando porcentagem )

P(Y) = probabildiade de ser Y sozinho (a porcentagem do target)

P(X) = prob de X 

**Outras features**

![](C:\Users\Rafael\Google Drive\Private Studies\TextMining\md_images\other_features.png)





P (X|Y) = P(X,Y)/ P(X)

Seja X as input features e y target



![](C:\Users\Rafael\Google Drive\Private Studies\TextMining\md_images\naivebayes.png)