# 1. INtro a ML

## Terminalogias da Área de IA

+ INteligência Artificial (IA)
	- Termo mais geral que engloba toda a área do desenvolvimento da capacidade humana de resolver problemas
+ Inteligência Computacional
	- Redes Neurais, COMputaçâo evolutiva e lógica fuzzy. Somente esssa tres técniacas são consideradas como inteligência computacialna
+ Machine Learning (ML)
	- Algoritmos que aprendem com a leitura de dados: Métodos matemáticos para treinar algoritmos
+ MIneraçâo de Dados / Data Minig
	- Extrair conhecimento de bases de dados usando ML

+ Sistemas Especialistas
	- Sistemas que aprende a partir da inserção de conhecnimento humano como regra para a máquina
+ Visão Computacional
	- Área responsável com a reprodução da visão humana para a máquina. ENvolve a área de reconhecimento de imagens
+ BigData
	- UMimenso volume de Dados
+ DataScience
	- Exploraçâo de Análise de dados. COmbina: Ciência da COmputação + Estatística + ML

+ Processamento de linguagem Natural (NLP)
	- Entender a linguagem humana
+ Algoritmos Genéticos
+ Mineração de Dados
+ Sistemas MUltiAgente
+ Resoluçâo de problemas de Busca
+ Lógica Fuzzy
+ Raciocínio baseado em Casos
+ Redes Neurais
	- Um algoritmo de ML
+ Deep Learning
	- Redes Neurais com muitas camadas que consomem muito mais dadaos e CPUs. POr cosnumir muito recurso, só pode se desenvolver agora.

## Métodos de ML

+ Métodos Preditivas (Aprendizagem SUpervisionada)
	- Classificaçâo: Dividir os dados em classes/rótulos e saber diferencialas
		+ Exemplos: RIsoc de crédito, Filtro de SPAM, sepraçâo de notícias, Reocnhecimento de voz/face. Previsão de doenças
	- Regreção: Prever um valor numérico. Exmplo:prever o luvro
		+ Exemplos: Baseados em fatores externos, prever o dolar; Risco de investimento


+ Métodos Descritivos: (Aprendizagem nâo-supervisionada)
==> Analisa automaticamente os dados sem necessiatar, assim, nâo há quem diga se está certo ou não
	+ REgras de Associaçâo: Prateleiras de Mercado, serve para organizar as prateleiras. Tem um exemplo de Fraudas e Cerveja, a muito tempo perceberam que se compram os dois juntos; Promoçâo com itens que sâo vendidos em conjunto; Planejar catálogos das lojas e folhetos de promoção


+ agrupamento: Separar os dadso em grupos de forma que haja sentido.
	- Exmeplo: Segmentaçâo de Mercado: Exemplo, mandar propaganada de vídeo game para quem provalviemnte é do grupo de que joga videogame; Agrupamento de documentos/notícias; Perfis de clientes

 
+ detecçao de desvios/outliers
	- Dectar frasde em cartão de crédito; Uso de energia de água/telefone fora do normal; Desempenho de atleas (doping)


+ padrões sequenciais
	- Detectar sequência de acontecimentos. Exemplo, se vem a doença A, depois deve vir a B, C, e assim em diante

+ SUmarização
	- Criar um resumo de um agrupamento, porxemplo, entender o que tem em comun todos os cliente homesns com idade entre 25 e 35 anos


Aprendizagem por reforço
+ APrender por causa e efeito, com a própria expericience. Muito utilizada em robótica

Difenreça entre supervisionada e n-supervisionada
==> Na aprendizagem supervisionada, o programa é treinado a partir do conhecimento de um supervisor e um conjunto de dados pré-definidos. Por outro lado, na aprendizagem não-supervisionada o programa encontra automaticamente padrões e relações em um conjunto de dados.

## 2. PreProcessamento de Dados (numpy, panads e sciki-learning)

## Conteudo
+ Carregar Bases
+ O que fazer quando encontrara valores inconsistentes ou faltattnte
+ Escalonamento de atributos
+ tanrofrmar variáveis categóricas
+ INtro a Avaliar algoritmos
+ Separar vases de testes e de treino
