# My-Notes-Redes-Neurais

## Log

+ **Data de Inicio**: 15/05/2018
+ **Data de Fim**: 26/05/2018
+ **Site Udemy**: https://www.udemy.com/redes-neurais-artificiais-em-python/learn/v4/
+ O curso é **Uma base para entrar em DeepLearning**, dando uma boa base de rede neurias simples e multicamada
+ **Avaliação:** As aula poderiam ser mais rápidas; Deixo em 1,5x pois ele fala lento; O bom que disso é que o conteudo que ele mostra é de nivel bom quanto ao de um fim de um curso de CienciaComp;  O curso é uma boa intrdoução aos conceitos bases de Redes Neurias; Calculos manuais são chatos (porém uteis para quem realmente nao sabe nada de matematica e quer aprender e não se perder em tudo). Algumas partes ele faz cálculos sobre 4 entradsa, poderia ser uma só mas mesmo assim, é bom pois voce não fica perdido quando essse números aparecerem na implementação; Bomq ue passa uapido pelas API: PyBrain e scikit-learn

## Conteúdo do curso

1. Base de Machine Learning e RNA
   1. Aplicações de RNA
   2. Tipo de Aprendizagem de Maquina (3 tipos)
2. Perceptron Passo a Passo
   1. Treinamento / Ajuste de Peso
   2. Implementação de Rede Neural com uma camada
3. Perceptron multipla camada
   + Reajuste de Peso, Delta, Dgraditene Local e BackPropagation com implementaçao raw
4. Outors conceitos
   + Conceitos iniciais de DeepLearning
   + Dúvidas, curiosidade e Códigos de PyBrain e SciKit-Learning

## IDE SPyder

+ Depurar
  + Digite `F12` para por um momento em que fara a pausa. Apartir desse ponto, voce pode exeuctar passo a passo (asism, evita fazer tudo)
  + `CTRL+F10`: Executar linha por linha, semelhante ao Jupyter
  + Comece a Depurar e depois deixa em Continuar `CRL+F12` para ir executando direto até o ponto que voc eescolheu para parar
  + Limpe o campo de varaiveis quando for depurar e executar denovo

---

## 1. Base de Machine Learning e RNA

### 1.1. Quando usar RNA ou Algoritmos de Computação

**Exemplos de utilização de algoritmos**: Nesses casos, nao presisa usar redes neurais, pois os algoritmos já existentens já resolvem isso com eficiência:

+ Sistema de Recomendaçao (Como mostrado no curos de data-science da Udemy); 
+ Buscas (google maps, rota com menor caminho)
+  Grafos (busca largura, profundidade, A*)
+  Ordenação (Bubble Sort, Quick Sort)

**Exemplos de Alta Complexidade**: Nesses casos, **não há algoritmos pré-determinados para reoslver isso**, por isso usa rede neural

+ Processamento de linguagem natural (tradução)
+ Reconhecimento Facial
+ Previsâo
+ Carros automatos (Identificação de imagens em tempo real)
+ Bolsa de Valores
+ Geraçâo de coisas abstratas: música, poema, rotulação de imagens e etcc

**Em Geral usa-se Rede Neural quando:** houver muitos dados (BigData); ou ser um problema complexo sem algortimos-pre-determinados

---


## 2. Perceptron Single Layer (Base de RNA)

### 2.1 Introdução a Redes Neurais Artificias (RNA)

Baseada no cérebro humano. A RNA é uma asbtração do cérebro, mas, nao chega nem perto da complexidade do cérebro humano. O objetivo é imitar o sistema nervoso no processo de aprendizagem. (simular a troca de informaaoes entre neuronios). É uma técnica **Bio-Inspirada pois basea em algo biológico**

+ História: RNA já existem a muito tempo, mas, hoje é tao famoso por causa do **DeepLearning**, e seus algoritmos que manipulam várias cmadas de várias formas que se iniciou em 2006. 

- Não era famoso antes pois tinha-se a SVM que superava as Redes Neurais
- Perceptron: Nome da Arquitetura de RNA (Neuronios, soma, pesos e etc..)

### 2.2 Como a rede biológica

+ **neuronio**: faz o processamento do cérebro
+ **axonio**: trasnimete sinal de um neuronio para utro (sinapse : evento de conexao entre neutrion, é lançada é feito por ligaçoes quimicas e entram no neuronio pelos dentritos que faz aumentar ou diminuir o potencial eletrico deo neurorino)
+ O neuronio dispara se a entrada for uma valor acima de um definido
+ neuronios sao os verttices e os axinnios sao as arestas

### 2.3 Neuronio artifical

+ McCulloch e Pitts (1943): Primeira definiçao de uma RNA
+ Frank Rosenblatt (1958): Criou o Modelo de Perceptron abaixo

![ ](C:\Users\Rafael\Google Drive\Private Studies\Computer Advanced\udemy-Python-Redes-Neurais\material-do-curso\img01.png)

**A RNA é composta de**

+ Entradas: n entradas dependens do problema (features/colunas/etc.)
+ **Pesos**: representada por w (weight = peso) Eles representam as sinapse junto com as entradas
  + Se w > 0 : sinapse exitoradora -> tem chance de ativar neuroinio
  + Se w < 0 : sinapse inibidora -
  + Pesos sao sinapse que amplicificam ou diminuiem as entradas
+ **O CONHECIMENTO DA REDE NEURAL SÂO OS PESOS, A APRENDIZAMGE É A BUSCA DO MELHOR CONJUNTO DE PESOS que reolsve o probelma**
+ **Função SOMA**: Somatória de entradas vezess seus pesos
+ **Função de Ativação:** Relacionado a ativaçâo ou nao de um neuroiinoio eplas sinapses

![](C:\Users\Rafael\Google Drive\Private Studies\Computer Advanced\udemy-Python-Redes-Neurais\material-do-curso\img02.png)



### 2.3 Codigo de um perceptron Simples

````python
import numpy as np

# usando np.array vc converte parar array do numpy, so assim ficara otimo
#   e poderar usar os recurso do numpy
entradas = np.array([1,7,5])
pesos = np.array([0.8, 0.1, 0])

# definido SOMA
def soma(entradas, pesos):
    # Dot é PRODUTO ESCALAR da Algebra
    # Parra uma lista simples, sera entao a somatoria da lista1 * lista2 
    #   como feito antes
    # So funciona sobre array
    return entradas.dot(pesos)

s = soma(entradas, pesos)
print(s)

def stepfunction(soma):
    if(soma >= 1):
        return 1
    return 0

r = stepfunction(s)
````

### 2.4 Tipos de Aprendizagem de Máquina

| Supervisionada | Nao supervisionada  | Reforço                         |
| -------------- | ------------------- | ------------------------------- |
| Classificaçâo  | Associação          | Sistema Multi Agentes           |
| Regressão      | Clusterizaçâo       | aprende com propria esperiencia |
|                | Detecçâo de Padores | Área de Robótica                |

**Supervisionada**: 1. é feito extração de FEATURES; 2. O algritmo aprende e pasamos tambems as respostas corretas (papel do supervisor) ; 3. Depois de passar parte da base de dados, o modelo está aprendido

**Nao Supervisionada**: 1. Extração de caracteristicas; 2. Aprende sem saber; 3. Modelo aprendido

### 2.5 Reajuste de Pesos

+ erro = valor obtido - valor esperado
+ new_peso = peso_atual + (taxa_de_aprendizado [0,1] * entrada * erro)
+ O reajuste de peso ocrorre até acertasr 100% (se for possivel) ou até uma taxa minima de erro aceitaval
+ **Obs: Isso é feito para cada neurônio, então, siginifca que quanto mais neuronio, mais lento. Essa é a importancia da Escolha do menor conjunto Otimo de FETAURES**

### 2.6. Codigo de AND_OR_XOR_Logic

````python
import numpy as np

# AND LOGIC - Enable this Line to Run to AND LOGIC
inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
expecteds_outputs =  np.array([0, 0, 0, 1])

# OR LOGIC - Enable this Line to Run to OR LOGIC
# inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
# expecteds_outputs =  np.array([0, 1, 1, 1])

# XOR LOGIC - Enable this Line to Run to XOR LOGIC -> Will exit ERRO
#inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
#expecteds_outputs =  np.array([0, 1, 1, 0])

weights = np.array([0.0, 0.0])
learning_rate = 0.1

def step_function(soma):
    if(soma >= 1):
        return 1
    return 0

def calcule_output(record):
    s = record.dot(weights)
    return step_function(s)

def trainning():
    erro_total = 1
    while(erro_total != 0):
        erro_total = 0
        for i in range(len(expecteds_outputs)):
            output_calculated = calcule_output(np.asarray(inputs[i]))
            erro = abs(expecteds_outputs[i] - output_calculated)
            erro_total += erro
            # UPDATE Weights
            for j in range(len(weights)):
                weights[j] = weights[j] + (learning_rate * inputs[i][j] * erro)
                print("Updated Weight: " + str(weights[j]))
            print('Total Erros: ' + str(erro_total))
            
trainning()
print("Neural Net Trained: Testing it")
print("1 input (0,0) ==>", calcule_output(inputs[0]))
print("2 input (0,1) ==>", calcule_output(inputs[1]))
print("3 input (1,0) ==>", calcule_output(inputs[2]))
print("4 input (1,1) ==>", calcule_output(inputs[3]))
print('Weights Useds: ' + str(weights[0]) + ', ' + str(weights[1]))
````

+ Não Funciona com XOR pois:

  + **PERCEPTRO SIMPLES SÓ TRATA PROBLEMAS LINEARMENTE SEPARÁRVEIS**
  + Para Resolver isso, utiliza-se **Multiplas Cmadas ==> Camadas Ocultas**

  

![](C:\Users\Rafael\Google Drive\Private Studies\Computer Advanced\udemy-Python-Redes-Neurais\material-do-curso\img04.png)

---

## 3. MultiLayer Perceptron

### 3.1. MultiLayer Perceptron

+ Possui **uma camada oculta (hidden Layer)**

+ Iremos construir uma rede neural multicamada feedforward

  + Em resumo, uma camada tem todos os esus neuronios ligado com a camada da frente
  + fedd = alimentaçâo, forward = pra frente

  ![](C:\Users\Rafael\Google Drive\Private Studies\Computer Advanced\udemy-Python-Redes-Neurais\material-do-curso\img05.png)

### 3.2 Estudo de funções de Ativação 

+ StepFunction (Degrau)
  + Retorna 0 ou 1 => serve para classificação binária
  + Pode ser usada somente em percetron Simples, pois, nao tem derivada

![](C:\Users\Rafael\Google Drive\Private Studies\Computer Advanced\udemy-Python-Redes-Neurais\material-do-curso\img06.png)

+ Sigmoide

  + Tem esse nome por fazer um **S**

  + Melhor que a degrau, retorna valores entre [0,1] 

  + A grande vantagem é que a degrau é muito absoluta, uma pequena mudança muda tudo. Enquanto que a sgmoide é mais suave. Ex: se na degrau ta saindo 1, se mudar uma netrada vai sair 0, mas, como é so uma , poderia ainda assim sair 1, mas nao sai, por que nao aceita nehuma diferença

  + Em resumo, a fçâo retorna 1 se for muito alto sua entrda ou -1 se for muito baixo su anetrada
  + **OBS IMPORTANTE!!!**: Se voce usar ela para uma classifcaçâo binária [0 XOR 1], dificilemnte vai chegar a exatamente 0 ou 1. Chega em valores super aproximados mas que não serão 0 e 1 exatamente quando fizer o ==, então, se for usála para esse caso, faça um tratamento. (Ex: se > 0.9999 => 1, se < 0.001 ==> 0)

    ````python
    import numpy as np
    
    def sigmoid(soma):
        return 1 / (1 + np.exp(-soma))
    ````

![](C:\Users\Rafael\Google Drive\Private Studies\Computer Advanced\udemy-Python-Redes-Neurais\material-do-curso\img07.png)

+ **Tangente Hieprbolica**

  + Possibilita valores negativos entre [-1,1]

    ![](C:\Users\Rafael\Google Drive\Private Studies\Computer Advanced\udemy-Python-Redes-Neurais\material-do-curso\img08.png)

+ Link com mais funções:

  + https://en.wikipedia.org/wiki/Activation_function

### 3.3 Criar Rede feedforward (feed = alimentaçâo, forward => pra fente) no XOR

+ Vamos montar uma rede multicamada para XOR. A Soma e a função de ativação, agora, nao ficará somente em um único neurônio, ficara agora tambem nos neuronios de hidden layer

![](C:\Users\Rafael\Google Drive\Private Studies\Computer Advanced\udemy-Python-Redes-Neurais\material-do-curso\img09.png)

+ Perceba que apenas nessa rede é feito varios calculos de soma/ativacao e futuramente para reajusde de peso. Nao é atoa que rede_neural gasta muito tempo e muitos pesquisadores jogam-an para servidores dedicados para processalas

### 3.4 Algoritmo da MultiLayer para Reajuste de Pesos

![](C:\Users\Rafael\Google Drive\Private Studies\Computer Advanced\udemy-Python-Redes-Neurais\material-do-curso\img10.png)

## 3.5 Gradiente Descent (descida do gradite) e Derivada da Funçâo de Ativação

![](C:\Users\Rafael\Google Drive\Private Studies\Computer Advanced\udemy-Python-Redes-Neurais\material-do-curso\img11.png)

A ideia do gradiente é que: Temos um ponto que reprezenta um vetor de peso e a altura representa o erro. O objetivo é minimizar o erro (min C(CostFunction==erro)(vector[w1,w2,w3,w4,w5,..,wn])). Para isso pasta calcular a derivada parcial no ponto para mover na direçâo do gradiente.

O objetivo é chegar no fundo do poço, e para isso, usaremos Cálculo para ir em direçâo ao mínimo global

Obj: Encontrar a combinaçâo de pesos com menor peso possivel

+ Alem da forma do cálculo de gradiente há outras formas de fazer isso
  + Força Bruta  : fazer todas as combinaçôes possiveis de pesos (inviavel)
  + Algoritmos genéticos: Servem muito bem para problemas de otimizaçao (encontrar vetor (cromossomos) que maxima ou minimiza

#### Derivada Parcial

+ Valor que Direciona para onde está o mínimo

  ![](C:\Users\Rafael\Google Drive\Private Studies\Computer Advanced\udemy-Python-Redes-Neurais\material-do-curso\img12.png)

### Calculo do Delta da Camada de Saida (Ultima Camda)

Tendo o valor do delta, podemose seguir o gradiente (minimo global) sem cair no minmo local

![](C:\Users\Rafael\Google Drive\Private Studies\Computer Advanced\udemy-Python-Redes-Neurais\material-do-curso\img13.png)

Erro = Valor esperado - valor obtido

Derivada_sigmoide => aplciar a derivada da sigmoide sobre o resultado da ativaçâo (depois de aplicar a sigmoide ao souma)

### Calculo do delta das Camadas Ocultas (A partir da penultima camada)

![](C:\Users\Rafael\Google Drive\Private Studies\Computer Advanced\udemy-Python-Redes-Neurais\material-do-curso\img14.png)



## 3.6 Backpropagation (Ald de atualização dos pesos)

Ele tem esse nome pois, as redes em geral são feedforward (esquerda pra direita) mas, o algortim atualiza os pesos da direita para resquerda

![](C:\Users\Rafael\Google Drive\Private Studies\Computer Advanced\udemy-Python-Redes-Neurais\material-do-curso\img15.png)

### 3.7 Bias (Vieis em PT-BR)

+ Adiciona um atributo constaten a mais em cada uma das camadas, e, ele é tratado como uma nova entrada

---

# 4. Outros Conceitos

## 4.1 DeepLearning

Até 2006, o que mais usada era SVM (Máquinas de Vetores de Suporte). Mas, apartir de 2006, foi-se criados algoritmos eficiente de Rede Neurais.

DEEP_LEARNING: Não tem definição exaa, mas, seria **UMA REDE COM MAIS DE DUAS CAMDAS OCULTAS**

Em muitos casos, ocorre o vanish gradient problem. O gradiente fica pequeno e complicadode trabalhar

Pode ser que acabe tendo que usar outras funçôes de ativaçãp

Para continua seus estudos nessa área, veja:

+ Conv Net
+ Redes neurais recorrentes
+ Ferramentas: Weka, Keras, theano, tensorFlow (mais utilizadas)
+ Programaçâo em GPU : Proporciona mais recursos de hardware para melhorar o treinamento
		 A NVIDIA está queredo pessoas que saibam programação em GPU para assim melhorar o desempenho do treinmaento das redes neurais

## 4.2 Dúvidas das aulas

**Quantos Neuronios uma camada oculta vai ter?**

qtd_neuronios_na_camada_oculta = teto(Entradas + Saidas / 2). Nâo é uma formula perfeita, pois não há um critério. Mas, comece por essa formula e depois tente melhorar se conseguir

Problemas linearmente seraparaveis nao presisam de camdas ocultas

**O que fazer para uma classifcaçâo nâo binária?**

Quando voce trabalha com valores categorios como saida, se vc tem 3 ou mais saidas possiveis, entao, esse será o número de neuronios da camada de saida.

O que ocorre muito em DeepLearning, é ter funções de ativação diferente, uma para camada de saida e outras para os neurionios para camadas ocultas

+ Em DeepLearning, usa-se muito a função RELU nas camdas ocultas e a sigmoide no final

Observe: A sigmoide vai de [0,1] mas é dificil ela chegar a 0 ou 1, entâo, faça um tratamento, pois, para chegar a exatamente a 0,1 memso no XOR feito, é nescessario milhoes de epocsa

**Dados categoricos de saida**: Se há mais de duas clase, faz-se **encoding**, ou seja, a classe A = 1 0 0 0 0 0 0, Clase B = 0 1 0 0 0 0 , enfim, cada neuronio representa uma classe, devera ser ativdado somente esse neuronio.



## 4.3 Tipos de Descida do Graditen Bath e Stocastica e outras

**A BATH** 

+ Foi a que ele usou na programaçâo. nesse curso

+ É necessario carregar e ler o erro de todos os dados e so depois fazer o reajuste de pesos. é diferente do que a Rita passou
+ Carrega todos os registros por vês

**Estocastico**

+ É o que a Rita passou em sala de aula (eu acho)
+ Evita atingir minimos locais, eé mais rapida e carrega menos coisa na meoria pois é feito por registro
+ Boa parte das APIS o usa

**Mini Batch gradiente decent**

+ é mio que a combinaçâo dos dois, é o Bath, so que , vc esoclher u numero  de registro para rodar e atualizar os pesos

![](C:\Users\Rafael\Google Drive\Private Studies\Computer Advanced\udemy-Python-Redes-Neurais\material-do-curso\img16.png)



## 4.4 Codigo no pybrain (Estutura de uma rede em Pybrain)

![](C:\Users\Rafael\Google Drive\Private Studies\Computer Advanced\udemy-Python-Redes-Neurais\material-do-curso\img17.png)

**Agora, vamos converter essa rede acima para o Pybrain (ela contém bias)**

```python
# Isso é somente a esturturação, não tem dado de entrada

# Importa um FeedForward
from pybrain.structure import FeedForwardNetwork

# LinearLaye => Camada de Entrada		# Bias => Vies
# SigmoidLaye = Camada  em que o dado passa pela Sigmoide (Oculta e Intermedia)
from pybrain.structure import LinearLayer, SigmoidLayer, BiasUnit
from pybrain.structure import FullConnection

# Estrutura da Rede
rede = FeedForwardNetwork()

# Camdas Sepradas
camadaEntrada = LinearLayer(2) # 2 entradas
camadaOculta = SigmoidLayer(3) # 3 neuronios na camda oculta
camadaSaida = SigmoidLayer(1)

# UNidades de Bias
bias1 = BiasUnit()
bias2 = BiasUnit()

# Inserindo essas camdas na estutura da rede
rede.addModule(camadaEntrada)
rede.addModule(camadaOculta)
rede.addModule(camadaSaida)
rede.addModule(bias1)
rede.addModule(bias2)

# Ligaçâo entre as camdas (vai ligar os neurosios do @1 para todos do @2)
entradaOculta = FullConnection(camadaEntrada, camadaOculta)
ocultaSaida = FullConnection(camadaOculta, camadaSaida)
# bias tambem é ligado, nao tem como juntar a camdaEntraa
biasOculta = FullConnection(bias1, camadaOculta)
biasSaida = FullConnection(bias2, camadaSaida)

# Efitivamente vai construir e vai fazer
# ele já poe os pesos
rede.sortModules()

print(rede)
# esse .prams mostra os pesos das camdas
print(entradaOculta.params)
print(ocultaSaida.params)
print(biasOculta.params)
print(biasSaida.params)
```

## 4.5 Scikit-learning Iris Problem

```python
from sklearn.neural_network import MLPClassifier
from sklearn import datasets

# manipulando dataset do irirs já encontrado na lib
iris = datasets.load_iris()
entradas = iris.data
saidas = iris.target

# criar a rede
redeNeural = MLPClassifier(verbose = True, max_iter = 1000, tol = 0.0001,
	activation = 'logistic', learning_rate = 0.01)

# treinar
redeNeural.fit(entradas, saidas)

# predizer para um valor
redeNeural.predict([[5, 7.2, 5.1, 2.2]])
```

