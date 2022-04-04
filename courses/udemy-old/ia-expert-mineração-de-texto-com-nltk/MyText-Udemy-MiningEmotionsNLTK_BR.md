# [Mineração de Emoção em Textos com Python e NLTK](https://www.udemy.com/mineracao-de-emocao-em-textos-com-python-e-nltk/)



### Dados Gerais

+ Data Inicio: 26/11/2018
+ Não é PNL
+ Outeos Links
  + https://www.researchgate.net/profile/Eduardo_Goncalves17/publication/317912973_Mineracao_de_texto_-_Conceitos_e_aplicacoes_praticas/links/5a653d454585158bca51d986/Mineracao-de-texto-Conceitos-e-aplicacoes-praticas.pdf



### Pra que pode servir Textmining

+ Para empresas:
  + Detectar nas redes sociais se estão falando bem ou mal do produto
+ Classificaçâo
  + Detectar Spam
  + Dar Rótulos quanto ao assunto do texto
  + Detectar emoções dando tags
    + Monitorar uma marca
    + Avalair o nível de raiva das epssoas entre 0 a 10
    + Entender o que as pessoas pensam
+ Detectar sinônimos errados:
  + Imagine que você coloca seu Bairro no IBGE na pressa e usa algum acronimo. O algoritmo detecta qual é o nome original. Exemplo: St. Ana == Santana
  + Para digitação errada
+ Detectar se uma noticia é de querda ou direita
+ Encontrar padrões
+ Detectar Plágio ou plágio com palavras trocadas
+ Gerar textos sinônimos
+ Separar documentos com base no que se diz deles

### Conteudo do Curso

+ Mineração de texto e classificação
+ Pré-processamento de textos:
  + Retirar StopWord: a, o, de, da
  + Stemming: 'Adiquiri um radical'
+ Avaliação do algoritmo



### 1. Módulo de Mineração de Texto e classificação

#### 1.0. Conteúdo

+ Mineração de Texto
+ Mineração de Emoções
+ Classificação (Tarefa de ML)
+ Classificação em textos

#### 1.1 Introdução

+ Hoje pode ser usado em: Redes sociais, E-mails, PDF, XML, JSON, Livros, Jornais, Revistas Páginas Web, Blogs
+ Uma dificuldade é que geralmente não se possui um esquema para descrever a estrutura
+ Existe o texto livre (sem formatação alguma como nas Redes Sociais ou em E-mail)e formatado (tem tags onde define cada campo)
+ A Área de TextMinig surgiu para conseguir interpretar textos livre

#### 1.2. Classificação

+ Detectador de Spam
  + Input: Mensagem : (Assunto, Texto)
  + Passar por um Classificador
  + Output: ["Spam", "não Spam"]
+ Classificador Multirótulo
  + Input:  Texto de Noticia
  + Passa por um Classificador Multirrótulo
  + Output: Tags dos principais assuntos

#### 1.3. Clusterização

+ Descoberta de nomes Similares
  + Como no IBGE, se a pessoa digita algo errado, o algoritmo detecta e coloca esses nomes erradosno cluster do nomecerto
+ Detecção de Plágio
  + Usado para artigos científicos. 
  + O prof falou num caso de um artgo que ele mandou mas que acusaram que era plágio, pois  ele esqueceu de áspas duplas

#### 1.4. Extração de Informação

+ Dado um texto livre com certas características é retirar informações que você está procurando

#### 1.5. Associações

+ Correlaçâo entre palarvras. Encontrar regras de Associações:
  + Exemplo: A presença da palavra pelé aumenta em 5 vezes a chacne de aparecer a palavra Copa e 1970
  + A ideia é. Dado N palavras, prever uma conclusão

#### 1.6. Correspondências semânticas

+ Corresponde a fazer mapeamento de palavras para outras que tenha a mesma semântica de acordo com o contexto.
  + Foi dado por exemplo a imigração de um banco de dados
+ Recuperação da Informação
  + Localizar e Ranquear documentos relevantes em uma coleção. Isso é semelhante a indexação feita pelo google
  + Exemplo: Dado 100 documentos fazer o indixe remersivo de em quais documentos aparece uma palavra

#### 1.7. Sumarização de Texto

+ Resumiria um texto
+ Ele orientou um TCC em que comparava 2 métodos de sumarização. Ele sumarizava de duas forma e depois entrevistava pessoas e dava o texto sumarizado, e queria saber quais dos dois dava mais informaçôes e a porcentagem de acerto. Econtrou 60% a 90%

#### 1.8 Abordagens em mneraçâo de Texto

+ Estatística
  + Frequencia dos termos, ingorando informações semticas

+ PNL
  + Interpretação sintática e semântica das frase
  + É fazer o computador **entender** textos escritos em Linguagem Humana

#### 1.9. Mineração de Emoção

+ Envolve a técnica de classificação. Dado um texto, vou submetelo ao Algoritmo de ML e resultará em um rótulo.
+ Pode ser bem usadao por empresa:
  + Avaliar um produto
  + Entender os vários níveis de satisfação ou não

**Classificaçâo por polaridade**

+ Pode ser chamado também de classificação por valência
+ Classifica em 3 parte: Positivo, Neutro ou Negativo
  + A maioria dos trabalhos eram só isso. Agora, aparece outras formas de detectações de emoçâo em trabalhos de doutuorado

**Classificação por Emoção**

+ As emoções do Paul Ekman (Canal Metaforando - Vitor Souza - CSI - Detectar mentira)
+ As 6 emoções: Surpresa, Alegria, Tristeza, Medo, Nojo, Raiva
+ O trabalho de doutorado dele era fazer: Polaridade mais a porcentagem de valencia para cada uma das 6 emoções

#### 1.10 Classificaçâo

+ É aquilo que vi ans aulas de Inteligência OCmputacional
+ É um aprendizagem supervisionado, eu conheço as classes
+ Dado um conjunto de Features predizer uma outra classe/target.
  + Exmeplo Do titanic: Dados os ttributos, quem morreu ou não

**Passo a Passo da Classificação (Supervisioned Learning)**

Fase 1

1. Passo um *dataset* **limpo**  com as *features* (atributos previsores) com suass respectivas classes (atributo meta). É supervisionado pois eu sei a classe
2. Aplico o Sistema de ML para aprender com esses dados
3. Obtenho o Modelo

Fase 2

1. Obtenho uma *row* a ser classificado
2. Passo ela ao Classificador/Modelo
3. Obtenho a sua classe

**Como vai funcionar a classificação para Textos**

+ Aqui,os atributos previsores são as próprias palavras.
+ Cada palavra vai representar uma coluna, e aí, será necessário fazer uma filtragem das palavras como stop words. é isso que faremos no próximo módulo
+ Se eu tiver 1 milão de texto, maior será a base de dados
+ É comun ter uma base de ter 70 mil colunas

| Frase                      | Classe  |
| -------------------------- | ------- |
| Me sinto complemente amado | Alegria |
| Eu estou bem hoje          | Alegria |
| Isso me deixa apavorada    | Medo    |
| Este lugar é apavorante    | Medo    |

### 2. Módulo Pré-processamento dos Textos

**Conteúdo**

+ Instalação da ferramenta
+ Introdução ao NLTK
+ Obter uma pequena base de frases
+ Remoção das stop Words
+ Trabalha e Obter o radical das palavras
+ Descobrir a distribuição de frequências das palavras
+ Montar uma base de dados para calssificaçâo
+ TUDO ISSO SERÁ PRÉ-´PROCESSAMENTO, PARA SÓ DEPOIS PASSAR PARA O ML

**Instalando a Ferramenta**

+ Nem sempre o ntlk vem com tudo baixado. Execute esse código para baixar todos os pacotes

````python
import nltk
nltk.download()
````

**Extra Aula do Youtube de Introdução a NTLK**

[Introdução ao NLTK na Prática](https://www.youtube.com/watch?v=siVUal-TeMc)

O RESTO SE ENCONTRA NO JUPYTER NOTEBOOK

**Resumo do Processo**

1. Retirar Stop Words: Palavras que não ajudam a classificar nada
2. Steming: Retirar radicais das palavras
3. Crio uma lista de palavras únicas com todo o banco de frases
4. Para uma frase: retornar lista de {word => True/False} para cada palavra do banco anterior

## 3. ML: Detectando Emoções com Naives Bayes

+ O algoritmo vaia prender com base em nossa base

**Conteúdo**

+ Naive Bayes: Algoritmo de ML baseado em probabilidade
+ Naive Bayes: Usando em textos
+ Classificação  usando o modelo de Naive Bayes para determinar a emoção em frases

**Introdução em Naive Bayes**

+ É uma abordagem probabilística utilizando Teorema de Bayes
+ Exemplo de Aplicação
  + Filtro de SPAM
  + Mineração de Emoções (Computação Afetiva)
  + Separação de Documentos
+ **O Naive Bayes constroi uma tabela de Probabilidade**
  + O treinamento é pegar a base de dados original e gerar a tabela de probabilidade. E com base nela, classificar um registro.
  + Naive Bayes trabalha bem com features que tem om conjunto bem limitado de valores
  + Ele trabalha com probabilidade com base no dataset original.
    + **Para cada Freatures, qual a trob para uma classificação**

Exemplo de data set 

+ Vamos prever o Risco com base no Histórico de Crédito, usando uma única feature

| Histórico de Crédito | Risco    |
| -------------------- | -------- |
| Ruim                 | Alto     |
| Desconhecido         | Alto     |
| Desconhecido         | Moderado |
| Desconhecido         | Alto     |
| Desconhecido         | Baixo    |
| Desconhecido         | Baixo    |
| Ruim                 | Moderado |
| Ruim                 | Baixo    |
| Boa                  | Baixo    |
| Boa                  | Baixo    |

Tabela do Naive Bayes (Distribuição de Probabilidade)

| Risco de Crédito     |           | Histórico do Crédito |           |
| -------------------- | --------- | -------------------- | --------- |
|                      | Boa       | Desconhecido         | Ruim      |
| Alto    = 3/10 = 30% | 0/2 = 0%  | 2/3 = 66%            | 1/3 = 33% |
| Mode = 2/20 = 20%    | 0/2 = 0%  | 1/2 = 50%            | 1/2 = 50% |
| Baixo = 5/10 = 50%   | 2/5 = 40% | 2/5 = 40%            | 1/5= 20%  |

**Como aplicar Naive Bayes num Registro**

+ Classifico um registro fazendo a probabilidade para cada classe
+ Exemplo: ***Registro: (Histórico de Crédito : Desconhecido)***
  + P(Alto) = 30% *  66% = 19,8%
  + P(Moderado) = 20% * 50% = 10%
  + P(Baixo) = 50% * 40% =  20% !!!!!
+ O calculo é o produtório para cada classe, sendo a multiplicação dos possíveis valores para cada features
+ //OBS: Esse caso é bem simples, é uma única *feature* se tiver mais, são mais multiplicações que irá fazer mas da mesma forma.
+ O resultado final será:
+ Calculo a doma dos resultados das classes:
  + 0,198 + 0,10 + 0,2 = 0,498
+ Esse será o 100%, agora eu divido cada resultado por esse valor
  + P(Alto) = 0,198/0,498 = 39,7 %
  + P(Moderado) = 0,10/0,498 = 20%
  + P(Baixo) = 0,2/0,498 = 40%
+ **RESPOSTA: Será P(Baixo) com 40% de Chance**

**Obs: E caso não tiver uma palavra para uma classe, ela entraria como 0 no produtório?**

+ A resposta é nâo. Por exemplo, o radical `apav` de apavorado, que pertencem a classe de emoçâo medo dificilmente entraria numa frase com a `tag` de alegria. Entâo, em seu produtorio, isso resultaria em 0%. 
+ Mas o Naive Bayes nâo faz isso. Quando ele observa esse caso ele adiciona um registro a mais com este caso para que não ocorra isso, para que fique `1/(qtd_origin + 1)`



### 4. Avaliação do Algoritmo

+ É muito importante para quando você for distribuir sua aplicação. Verifica o quanto acerta ou não
+ Usaremos uma maior base: (alegria, desgosto,medo, raiva, surpresam tristeza)
+ Vamos dividir a base em treinamento e em teste
+ Há também formas de se avaliar pelo próprio NLTK

**Matriz de Confusão**

+ Tem esse nome devido a confuso que o modelo pode apresentar
+ Consiste em uma matriz de tamanho |Classes| x |Classes| onde a diagonal representa os registros que realmente forma bem classificados
  + **ELA É FEITA BASEADA NA BASE DE TESTO**
+ O QUE AVALIAR NELA?
  + Porcentagem de acerto (diagonal) e porcentagem de erro (complemento)
  + Verificar qual classe acerta mais e qual classe erra menos
+ A porcentagem de acurácia depende do contexto
+ Se trabalhar para artigos científicos, você terá que ter um número igual ou maior de acerto que a literatura
+ **Avaliaçâo de acordo com o número de calsse**
  + Exemplo: Te apresento 3 cartas distintas, qual a prob de se tirar uma carta especifica. É de 33%.
  + Assim, se você criar um modelo que classifica registros em 3 classe, porcentagme de acerto deverá que ser concerteza maior que 33%
  + E em geral, deve ser maior que 50%
+ **Zero Rules**
  + É Fazer 
    + `ZeroRules = sum(reg_da_class_com_mais_registro)/total`
  + Exemplo: para 3 classes, digamos que a classe que teve mais registors era a que tinha 35% dos registors
  + Se o seu modelo nâo for maior que 35% entâo será um desastre, você poderia simplesimentes colocar na ordem das classes qcom mais registros de ordem decrescente

**Base de Treinamento e Base de Teste**

+ Dado uma base, eu devo divir:
  + 70% para treinamento
  + 30% para teste
+ É necessário também observar a quantidade de linhas do seu dataset
+ Obviamento, as rows quue estâo na base de treinamento não devem está na de teste
+ O scikilearng já tem funçôes que fazem essa divisâo da base dae dados
+ É identificado que:
  + **Nem sempre as stopwords do NLTK Default pegam tudo que presisamos**
  + Nas aula, observou-se que as palavras `vou` e `tão` indicara emoçâo mas ela não fazem isso. 
    + Outras: `vai`
    + Para analisar essas palavras, execute
      + `classificador.show_most_informative_features()` 
    + Que retorna as palavras mais imporatens e edentifique stopwords ou palavras que não atribui ao que queremos

**Medindo Acurácia**

+ Acurácia: 32%
+ Cenário: Não é bom, **É DIFÍCIL FAZER** um de 60% mas ascima desse valor é mais válido
+ Número de classes - 16%
+ Zero Rules: 32%