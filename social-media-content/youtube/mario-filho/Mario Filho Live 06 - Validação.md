# Mario Filho Live 06 - Validação

Link: https://www.youtube.com/watch?v=zpafprzVQT8

## O que é

Validação é simular o modelo a um conjunto de dados novos que já sabemos o Y e então ver se ele acerta ou não.

Para fazer isso, separamos o dados em test e train (em geral 80% train e 20% test).

**Lembre-se: divida os seus dados na forma mais próxima que vai receber em produção**

## Validação Cruzada : `cross-validation`

Ex: Imagine um dataset de 1000 linhas. Vamos separar esse dataset em 4 (250 rows cada) e cada parte tem linhas aleatória das mil linhas. Você tem 4 conjuntos diferentes.

Como agente tem 4 blocos, pegamos 3 blocos para treinar o que sobrou agente usa para avaliar. 

em suma: você usa n-1 blocos pra treinar e 1 bloco pra validar, faz isso com todas as combinações de blocos

Assim você tem uma estimativa mais robusta (você faz a media das previsões) e você muda train/test várias vezes num mesmo dataset.

## Validação cruzada - por grupo

As vezes agente não pode separar linha por linha por causa de um **DESBALANCEAMENTO** ou por qualquer outro motivo. Um outro caso seria ter linhas que se referenciam a um mesmo grupo.

**Se existe dependência entre as linhas, você não deve colocá-las em blocos diferentes entre test/train, ou essa linhas dependentes ficam no train ou no test, mas não em ambas**

## Time Series

Em uma time series, há a dimensão de tempo. A forma mais comum é: 

Ordenar o dataSet por tempo e dividir na metade do tempo: Usar a primeira metade para treino e a segunda metade para teste.

### Expanding

Se quiser cross validation com time series você deve calcular o intervalo de tempo e dividí-lo em K subconjuntos. Em ordem, usar os primeiros blocos para treino e um único bloco sucessor para teste

### Sliding

Janela deslizante.

As vezes esse é melhor que o expanding, pois eu treino meu modelo com dados mais recentes do que no 'expanding' que pega dados muito antigos.

### Block

É uma validação incomum. Nela você consegue simular um outro comportamento da time series

### Validar Churn

**É bastante confuso mas essencial para você não errar seu modelo de churn quando vai pra produção**

**CUIDADO**: Muitas vezes, em modelos de predizer Churn, agente faz um treinamento com os dados no futuro, após o cliente dar churn. Isso causa vazamento de dados e deixa inválido o nosso modelo.

Você não pode pegar linhas aleatórias ou dividir em 4 blocos.

Você pegar, por exemplo, um bloco de 3 meses e treina. Depois você usa os 3 meses seguintes não para validar, mas para ser o Y do seu churn. No churn o Y é: **A mudança da feature de IN para OUT: você treina por 3 meses e validar por outros 3 meses se o modelo, só tento os dados dos 3 primeiros messe, consegue ou não prever essa mudança de features (IN/OUT) nos próximos 3 messes**

A mesma coisa também aconteceria na validação.

## Divisão de dados entre train/teste

Ter mais dados de treino:
+ Menos estável a estimativa do *score* de validação
+ modelo mais generalizável

Mais dados na validação
+ mais estável a estimativa do score na validação
+ Maior possibilidade de overfitting no treinamento

## Como avaliar a validação cruzada

Em geral usamos a média de cada etapa da validação cruzada.

Agora, se você quiser fazer o tuning ou alguma coisa para melhorar a cross validation. **Você deve olhar o resultado de cada divisão, se em todos os casos aumentou apos o tuning**.

## Final - Comentários

+ Mario não costuma fazer k-fold cross-validation 



