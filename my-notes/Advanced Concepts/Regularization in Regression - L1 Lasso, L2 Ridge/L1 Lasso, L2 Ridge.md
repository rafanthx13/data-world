# Ordem

0. Links e pErguntas
1. Regressão
2. REgressâo Linear
3. Regularizaçâo (Overfititng PRoblem)
4. Lasso (L1)
5. Ridge (L2)


## Perguntas da net

#####  When does regularization becomes necessary in Machine Learning?

link: https://www.analyticsvidhya.com/blog/2016/09/40-interview-questions-asked-at-startups-in-machine-learning-data-science/

Answer: **Regularization becomes necessary when the model begins to ovefit / underfit.** This technique introduces a cost term for bringing in more features with the objective function. Hence, it tries to push the coefficients for many variables to zero and hence reduce cost term. **This helps to reduce model complexity so that the model can become better at predicting (generalizing).**

##### When is Ridge regression favorable over Lasso regression?

Answer: You can quote ISLR’s authors Hastie, Tibshirani who asserted that, **in presence of few variables with medium / large sized effect, use lasso regression**. **In presence of many variables with small / medium sized effect, use ridge regression.**

Conceptually, we can say, lasso regression (L1) does both variable selection and parameter shrinkage, whereas Ridge regression only does parameter shrinkage and end up including all the coefficients in the model. In presence of correlated variables, ridge regression might be the preferred choice. Also, ridge regression works best in situations where the least square estimates have higher variance. Therefore, it depends on our model objective.

### links

**BR**
https://medium.com/turing-talks/turing-talks-20-regress%C3%A3o-de-ridge-e-lasso-a0fc467b5629

https://mineracaodedados.wordpress.com/2015/06/20/qual-a-diferenca-entre-lasso-e-ridge-regression/


**EN**
https://www.analyticsvidhya.com/blog/2016/09/40-interview-questions-asked-at-startups-in-machine-learning-data-science/
https://www.analyticsvidhya.com/blog/2016/01/ridge-lasso-regression-python-complete-tutorial/
https://www.analyticsvidhya.com/blog/2015/08/comprehensive-guide-regression/?utm_source=blog&utm_medium=RideandLassoRegressionarticle
https://www.analyticsvidhya.com/blog/2015/10/regression-python-beginners/?utm_source=blog&utm_medium=RideandLassoRegressionarticle

## Regressão e Regressão Linear

Quando falamos em predizer valores com auxílio de um dataset, estamos dizendo que queremos descrever o *target* (y) por meio das *features* (X).

Para cumprir essa tarefa vamos usar o conceito matemático de regressão linear, que, em linhas gerais, aproxima o target das features por uma reta (uma função linear). Desse modo, podemos fazer afirmações sobre valores não disponíveis no dataset.

A exemplo, temos os problemas de estimar o salário de um funcionário com base no “tempo de casa” na empresa ou o valor do IPVA de um carro com base no seu preço de venda.

Nesses casos, basicamente plotamos num gráfico pontos correspondentes a várias observações do contexto que estamos estudando, e eles seguem a forma (x, y) sendo x a observação que temos e y a que queremos tornar possível a previsão. No final, fica mais ou menos assim:

<img src="/home/rhavel/Documentos/Personal Projects/data-science-study/DS My Notes/Advanced Concepts/Regularization in Regression - L1 Lasso, L2 Ridge/imgs/0_E-V21jIRE1XWTxBZ.png" style="zoom:50%;" />

Quando dizemos prever o valor do y com base no x, que acaba sendo meio que o mote do Machine Learning, basicamente, queremos encontrar uma reta que seja a mais adequada e passa com mais “smoothness” pelos pontos, ou seja, a que melhor descreve os dados. 

O resultado do modelo vai ser uma reta, com equação f(x) = y = ax + b que vai passar por esses pontos. A visualização dela vai ser mais ou menos assim:

<img src="/home/rhavel/Documentos/Personal Projects/data-science-study/DS My Notes/Advanced Concepts/Regularization in Regression - L1 Lasso, L2 Ridge/imgs/0_OzaA9v1EJkK0Smav.png" style="zoom:50%;" />

O nosso trabalho vai ser encontrar os coeficientes angular (a) e linear (b) que tornam essa reta ideal — e isso vamos ver com bastante detalhe no tópico 2.

Importante dizer que o y pode ser previsto também com base em vários x’s, o que ocorre quando temos mais de uma feature. Nesse caso, que fica mais difícil de visualizar, a aproximação não se dá por uma reta, mas por planos ou hiperplanos dependendo da quantidade de features.

Para esses casos, o target da predição é calculado de forma que cada feature (x1, x2, x3…, xn) tenha um “peso” associado a si. Veremos isso com mais detalhes a seguir.

Partindo para explicação matemática do modelo de regressão linear, nosso objetivo será encontrar uma função cujas variáveis independentes sejam as features e a dependente, o target.

NAO USAMOS MSE, VAMOS USAR O CONCEITO DE RSS QUE É UMA OUTRA FUNÇÂO DE CUSTO

Como já sabemos uma regressão linear tenta ajustar uma função linear aos dados:

<img src="/home/rhavel/Documentos/Personal Projects/data-science-study/DS My Notes/Advanced Concepts/Regularization in Regression - L1 Lasso, L2 Ridge/imgs/1_Ta_6UL6CaGZU7pvL7BMsLQ.png" />

O procedimento de ajuste envolve a função de custo como soma residual dos quadrados ou RSS. Os coeficientes w são escolhidos para minimizar essa função de custo com base nos dados de treinamento:

<img src="/home/rhavel/Documentos/Personal Projects/data-science-study/DS My Notes/Advanced Concepts/Regularization in Regression - L1 Lasso, L2 Ridge/imgs/1_UFsN2JHfP5t_E1a9icTbwQ.png" />

No entanto, pode ocorrer overfitting, ou seja, o modelo pode “memorizar” o ruído dos dados de treinamento. Nesse caso, dizemos que o modelo tem um erro de generalização (erro na base de teste) elevado. Esse fenômeno está associado à variância do modelo, como vimos acima. Portanto, uma forma de diminuir o erro é aumentar o bias.

Para isso, regularizamos os coeficientes w, ou seja, restringimos o seu tamanho. Isso é feito adicionando um termo na função de custo, de forma que minimizar a função de custo automaticamente minimize também os coeficientes.

## Bias e Variancia

Para entender melhor os erros de predição é necessário entender que fatores influenciam tais erros, bem como a relação entre eles.

O primeiro fator, chamado de *bias* (viés), é a diferença entre a predição média do nosso modelo e o valor correto esperado. Sendo assim, um modelo com bias aprende relações erradas e gera previsões longe do esperado. O modelo não aprende corretamente com o dataset, assumindo muitas informações sobre os dados que não são necessariamente corretas. Dessa forma, modelos com alto bias possuem um problema de underfitting.

O segundo fator, *variance*, é a variabilidade do modelo para um determinado dado, ou seja, a capacidade do modelo de se adaptar à base de treino e ao ruído. Dessa forma, modelos com alta variance focam excessivamente se ajustar aos dados e, inclusive, ao ruído. Assim, esses modelos têm um problema de overfitting, ou seja, se adaptam tão bem ao dataset que não conseguem generalizar para além dele.

<img src="/home/rhavel/Documentos/Personal Projects/data-science-study/DS My Notes/Advanced Concepts/Regularization in Regression - L1 Lasso, L2 Ridge/imgs/1_HvTRuVbZpyzMnUCvept_Fw.png" />

De uma maneira bem simplificada, bias e variance são métricas de erro do modelo e um bom balanceamento de seus valores corroboram para se obter alta acurácia preditiva.

Para facilitar a compreensão desses conceitos vamos pensar na regressão linear. Sabemos que se trata de ajustar os dados a uma reta. E que obtemos essa reta minimizando o erro quadrático médio (MSE).

Bias, quando em alta, indica que o modelo se ajusta pouco aos dados de treino, causando o que é chamado de underfitting. O que significa que o MSE é alto, para a base de teste.

Variance, em alta, diz que o modelo se ajusta demais aos dados, causando por sua vez, overfitting. Nesse caso o MSE é zero para os dados de teste, mas podemos dizer que não generaliza bem os dados.

<img src="/home/rhavel/Documentos/Personal Projects/data-science-study/DS My Notes/Advanced Concepts/Regularization in Regression - L1 Lasso, L2 Ridge/imgs/1_ePMqfevdkn4GBgvsZKrCcw.png" />

Mas você pode estar se perguntando, como avalio esses indicadores na prática? Ambos tipos de erros podem ser avaliados, analisando-se os erros em dados de treino e dados de teste. Veja:

- Baixo erro em dados de treino e alto erro em dados de teste indica que temos alta variância.
- Alto erro em dados de treino e erro parecido em dados de teste indicam presença de um valor alto de bias.
- Alto erro em dados de treino e erro maior em dados de teste mostra que o modelo tem alto bias e alta variância.
- Baixo erro em dados de treino e baixo erro em dados de teste indica baixa variância e baixo bias.

Lembrando que sempre comparamos os erros dos modelos a um erro base. Por exemplo, se desejamos classificar imagens de cachorros em um dataset, o erro base é que o ser humano teria ao analisar essas imagens. Isso é definido porque não desejamos obter um erro muito maior do que o que um ser humano teria ao realizar essa classificação.

# Regularização

 A regularização é o processo de adicionar informações para resolver um problema incorreto ou impedir o excesso de ajustes.



De uma maneira bem direta, podemos entender regularização como a inserção de bias em um modelo. Ou em outras palavras, essa técnica desencoraja o ajuste excessivo dos dados, afim de diminuir a sua variância.

Dentro da regressão linear, Ridge e Lasso são formas de regularizarmos a nossa função através de penalidades. De forma simples, dentro de uma equação estatística dos dados, nós alteramos os fatores de forma a priorizar ou não certas parcelas da equação e, assim, evitamos ‘overfitting’ e melhoramos a qualidade de predição.

---

---

https://towardsdatascience.com/over-fitting-and-regularization-64d16100f45c

Em ML, os modelos são treinados sobre um dataset, que costuma ser dividido entre dasdos de teste e de treinamento (20% para teste e 80% para treinamento (em geral)).

EM uma regressâo por exemplo é dados as features encontrar o valor alvo (target).

Overfitting (ou ajuste excessivo (traduzido)) é quando o modelo aprende a identificar extamante aqueles dados. Seria o caso de, depois de treinar conseguir etr uma grande porcetagem de acerto sobre os dados de treinamento, mas quando for para outro dataSet (o de testse) terá um péssimo desempenho  porque os dados são umpouqinho diferentes.

NO exemplo absixo temos isos

<img src="/home/rhavel/Documentos/Personal Projects/interview-questions/imgs/overrifting.gif" style="zoom: 50%;" />



Agora, existem poucas maneiras de evitar o ajuste excessivo do seu modelo nos dados de treinamento, como amostragem de validação cruzada, redução do número de recursos, remoção, regularização etc.

A regularização basicamente adiciona a penalidade à medida que a complexidade do modelo aumenta. O parâmetro de regularização (lambda) penaliza todos os parâmetros, exceto a interceptação, para que o modelo generalize os dados e não se ajuste demais.

No gif acima, à medida que a complexidade aumenta, a regularização adicionará uma penalidade para termos mais altos. Isso diminuirá a importância atribuída a termos mais altos e levará o modelo a uma equação menos complexa.

Fique atento ao próximo post, que abordará os diferentes tipos de técnicas de regularização.

## Diferneça entre ambas L1/L2 LASSO/RIDGE

https://towardsdatascience.com/l1-and-l2-regularization-methods-ce25e7fc831c

A regression model that uses L1 regularization technique is called ***Lasso Regression\*** and model which uses L2 is called ***Ridge Regression\***.

*The key difference between these two is the penalty term.*

....

The **key difference** between these techniques is that Lasso shrinks the less important feature’s coefficient to zero thus, removing some feature altogether. So, this works well for **feature selection** in case we have a huge number of features.

Traditional methods like cross-validation, stepwise regression to handle overfitting and perform feature selection work well with a small set of features but these techniques are a great alternative when we are dealing with a large set of features.

----

----

https://www.analyticsvidhya.com/blog/2016/01/ridge-lasso-regression-python-complete-tutorial/#three

Ridge and Lasso [regression ](https://courses.analyticsvidhya.com/courses/introduction-to-data-science-2?utm_source=blog&utm_medium=RideandLassoRegressionarticle)are powerful techniques generally used for creating parsimonious models in presence of a ‘large’ number of features. Here ‘large’ can typically mean either of two things:

1. Large enough to enhance the *tendency of a model to overfit* (as low as 10 variables might cause overfitting)
2. Large enough to *cause computational challenges*. With modern systems, this situation might arise in case of millions or billions of features

Though Ridge and Lasso might appear to work towards a common goal, the inherent properties and practical use cases differ substantially. If you’ve heard of them before, you must know that they work by penalizing the magnitude of coefficients of features along with minimizing the error between predicted and actual observations. These are called ‘regularization’ techniques. The key difference is in how they assign penalty to the coefficients:

1. Ridge Regression:
   - Performs L2 regularization, i.e. adds penalty equivalent to **square of the magnitude** of coefficients
   - Minimization objective = LS Obj + α * (sum of square of coefficients)
2. Lasso Regression:
   - Performs L1 regularization, i.e. adds penalty equivalent to **absolute value of the magnitude** of coefficients
   - Minimization objective = LS Obj + α * (sum of absolute value of coefficients)

Note that here ‘LS Obj’ refers to ‘least squares objective’, i.e. the linear regression objective without regularization.

If terms like ‘penalty’ and ‘regularization’ seem very unfamiliar to you, don’t worry we’ll talk about these in more detail through the course of this article. Before digging further into how they work, lets try to get some intuition into why penalizing the magnitude of coefficients should work in the first place.

....

....

....

## 6. Conclusion

Now that we have a fair idea of how ridge and lasso regression work, lets try to consolidate our understanding by comparing them and try to appreciate their specific use cases. I will also compare them with some alternate approaches. Lets analyze these under three buckets:

### 1. Key Difference

- **Ridge:** It includes all (or none) of the features in the model. Thus, the major advantage of ridge regression is coefficient shrinkage and reducing model complexity.
- **Lasso:** Along with shrinking coefficients, lasso performs feature selection as well. (Remember the ‘*selection*‘ in the lasso full-form?) As we observed earlier, some of the coefficients become exactly zero, which is equivalent to the particular feature being excluded from the model.

Traditionally, techniques like **stepwise regression** were used to perform feature selection and make parsimonious models. But with advancements in Machine Learning, ridge and lasso regression provide very good alternatives as they give much **better output**, require **fewer tuning parameters** and can be **automated** to a large extend.

 

### 2. Typical Use Cases

- **Ridge:** It is majorly used to *prevent overfitting*. Since it includes all the features, it is not very useful in case of exorbitantly high #features, say in millions, as it will pose computational challenges.
- **Lasso:** Since it provides *sparse solutions*, it is generally the model of choice (or some variant of this concept) for modelling cases where the #features are in millions or more. In such a case, getting a sparse solution is of great computational advantage as the features with zero coefficients can simply be ignored.

Its not hard to see why the stepwise selection techniques become practically very cumbersome to implement in high dimensionality cases. Thus, lasso provides a significant advantage.

 

### 3. Presence of Highly Correlated Features

- **Ridge:** It generally works well even in presence of highly correlated features as it will include all of them in the model but the coefficients will be distributed among them depending on the correlation.
- **Lasso:** It arbitrarily selects any one feature among the highly correlated ones and reduced the coefficients of the rest to zero. Also, the chosen variable changes randomly with change in model parameters. This generally doesn’t work that well as compared to ridge regression.

This disadvantage of lasso can be observed in the example we discussed above. Since we used a polynomial regression, the variables were highly correlated. ( Not sure why? Check the output of data.corr() ). Thus, we saw that even small values of alpha were giving significant sparsity (i.e. high #coefficients as zero).

Along with Ridge and Lasso, Elastic Net is another useful techniques which combines both L1 and L2 regularization. It can be used to balance out the pros and cons of ridge and lasso regression. I encourage you to explore it further.

## Lasso Regression - L1 Regulazriação

https://towardsdatascience.com/l1-and-l2-regularization-methods-ce25e7fc831c

**Lasso Regression** (Least Absolute Shrinkage and Selection Operator) adds “*absolute value of magnitude*” of coefficient as penalty term to the loss function.



![img](https://miro.medium.com/max/240/1*4MlW1d3xszVAGuXiJ1U6Fg.png)

Cost function acima

Again, if *lambda* is zero then we will get back OLS whereas very large value will make coefficients zero hence it will under-fit.

https://en.wikipedia.org/wiki/Lasso_(statistics)

In [statistics](https://en.wikipedia.org/wiki/Statistics) and [machine learning](https://en.wikipedia.org/wiki/Machine_learning), **lasso** (**least absolute shrinkage and selection operator**; also **Lasso** or **LASSO**) is a [regression analysis](https://en.wikipedia.org/wiki/Regression_analysis) method that performs both [variable selection](https://en.wikipedia.org/wiki/Variable_selection) and [regularization](https://en.wikipedia.org/wiki/Regularization_(mathematics)) in order to enhance the prediction accuracy and interpretability of the [statistical model](https://en.wikipedia.org/wiki/Statistical_model) it produces. It was originally introduced in geophysics literature in 1986,[[1\]](https://en.wikipedia.org/wiki/Lasso_(statistics)#cite_note-1) and later independently rediscovered and popularized in 1996 by [Robert Tibshirani](https://en.wikipedia.org/wiki/Robert_Tibshirani),[[2\]](https://en.wikipedia.org/wiki/Lasso_(statistics)#cite_note-Tibshirani_1996-2) who coined the term and provided further insights into the observed performance.

https://www.analyticsvidhya.com/blog/2015/08/comprehensive-guide-regression/?utm_source=blog&utm_medium=RideandLassoRegressionarticle

<img src="/home/rhavel/Documentos/Personal Projects/interview-questions/imgs/Lasso-300x107.png" />

Similar to Ridge Regression, Lasso (Least Absolute Shrinkage and Selection Operator) also penalizes the absolute size of the regression coefficients. In addition, it is capable of reducing the variability and improving the accuracy of linear regression models.  Look at the equation below: Lasso regression differs from ridge regression in a way that it uses absolute values in the penalty function, instead of squares. This leads to penalizing (or equivalently constraining the sum of the absolute values of the estimates) values which causes some of the parameter estimates to turn out exactly zero. Larger the penalty applied, further the estimates get shrunk towards absolute zero. This results to variable selection out of given n variables.

#### Important Points:

- The assumptions of lasso regression is same as least squared regression except normality is not to be assumed
- Lasso Regression shrinks coefficients to zero (exactly zero), which certainly helps in feature selection
- Lasso is a regularization method and uses [l1 regularization](https://en.wikipedia.org/wiki/Regularization_(mathematics))
- If group of predictors are highly correlated, lasso picks only one of them and shrinks the others to zero

## Ridgge Regression - L2 Regularização

https://towardsdatascience.com/l1-and-l2-regularization-methods-ce25e7fc831c

**Ridge regression** adds “*squared magnitude*” of coefficient as penalty term to the loss function. Here the *highlighted* part represents L2 regularization element.

![img](https://miro.medium.com/max/243/1*jgWOhDiGjVp-NCSPa5abmg.png)

Cost function acima

Here, if *lambda* is zero then you can imagine we get back OLS. However, if *lambda* is very large then it will add too much weight and it will lead to under-fitting. Having said that it’s important how *lambda* is chosen. This technique works very well to avoid over-fitting issue.

https://en.wikipedia.org/wiki/Tikhonov_regularization

**Tikhonov regularization**, named for [Andrey Tikhonov](https://en.wikipedia.org/wiki/Andrey_Nikolayevich_Tikhonov), is a method of [regularization](https://en.wikipedia.org/wiki/Regularization_(mathematics)) of [ill-posed problems](https://en.wikipedia.org/wiki/Ill-posed_problem). Also known as **ridge regression**,[[a\]](https://en.wikipedia.org/wiki/Tikhonov_regularization#cite_note-1) it is particularly useful to mitigate the problem of [multicollinearity](https://en.wikipedia.org/wiki/Multicollinearity) in [linear regression](https://en.wikipedia.org/wiki/Linear_regression), which commonly occurs in models with large numbers of parameters.[[1\]](https://en.wikipedia.org/wiki/Tikhonov_regularization#cite_note-2) In general, the method provides improved [efficiency](https://en.wikipedia.org/wiki/Efficient_estimator) in parameter estimation problems in exchange for a tolerable amount of [bias](https://en.wikipedia.org/wiki/Bias_of_an_estimator) (see [bias–variance tradeoff](https://en.wikipedia.org/wiki/Bias–variance_tradeoff)).



https://www.analyticsvidhya.com/blog/2015/08/comprehensive-guide-regression/?utm_source=blog&utm_medium=RideandLassoRegressionarticle

Ridge Regression is a technique used when the data suffers from multicollinearity (independent variables are highly correlated). In multicollinearity, even though the least squares estimates (OLS) are unbiased, their variances are large which deviates the observed value far from the true value. By adding a degree of bias to the regression estimates, ridge regression reduces the standard errors.

Above, we saw the equation for linear regression. Remember? It can be represented as:

y=a+ b*x

This equation also has an error term. The complete equation becomes:

```
y=a+b*x+e (error term),  [error term is the value needed to correct for a prediction error between the observed and predicted value]
=> y=a+y= a+ b1x1+ b2x2+....+e, for multiple independent variables.
```

In a linear equation, prediction errors can be decomposed into two sub components. First is due to the **biased** and second is due to the **variance**. Prediction error can occur due to any one of these two or both components. Here, we’ll discuss about the error caused due to variance.

Ridge regression solves the multicollinearity problem through [shrinkage parameter](https://en.wikipedia.org/wiki/Shrinkage_estimator) λ (lambda). Look at the equation below.

<img src="/home/rhavel/Documentos/Personal Projects/interview-questions/imgs/Ridge2.png" />

In this equation, we have two components. First one is least square term and other one is lambda of the summation of β2 (beta- square) where β is the coefficient. This is added to least square term in order to shrink the parameter to have a very low variance.

#### Important Points:

- The assumptions of this regression is same as least squared regression except normality is not to be assumed
- Ridge regression shrinks the value of coefficients but doesn’t reaches zero, which suggests no feature selection feature
- This is a regularization method and uses [l2 regularization](https://en.wikipedia.org/wiki/Regularization_(mathematics)).

 

























----

# MSE (Extra)

Dessa forma temos:

<img src="/home/rhavel/Documentos/Personal Projects/data-science-study/DS My Notes/Advanced Concepts/Regularization in Regression - L1 Lasso, L2 Ridge/imgs/1_ECmDqiiLw7y9taVDRvMKVw.png" />



onde *ŷ* é a predição do modelo, e Erro o quão longe está da previsão correta. Para cada combinação dos coeficientes (*a*1, *a*2, …, *an*, *b*), com os dados de treino, temos um Erro, isso é, uma função que determina o quão erradas as previsões do nosso modelo estão. A modelagem da regressão linear consiste em encontrar os valores dos coeficientes da função que minimizam o erro.

**MSE para Regressão**

MSE = Bias² + Variance + Erro Irredutível,

onde MSE é o erro quadrático médio

Por outro lado, para avaliar um problema de regressão, uma métrica muito comum é a do erro quadrático médio. Sendo assim, um modelo bom é aquele que possui menor erro quadrático médio, calculado por:

<img src="/home/rhavel/Documentos/Personal Projects/data-science-study/DS My Notes/Advanced Concepts/Regularization in Regression - L1 Lasso, L2 Ridge/imgs/1_x_JnqP8VKTf3kjChoNvwIg.png" />

em que *n* é o número de observações, yi é o valor real e ŷi é a predição do modelo. Algumas consequências da diferença (ŷ-y) ser elevada ao quadrado são:

1. Se simplesmente somássemos as diferenças, elas poderiam se anular. Por exemplo, se um modelo desse algumas predições com diferença positiva (ŷ > y) e outras com diferença negativa (ŷ < y), essas diferenças poderiam se cancelar, dando um erro médio de 0. Com a diferença ao quadrado, isso não ocorre.
2. Como a diferença é elevada ao quadrado, erros maiores impactam o erro quadrático médio desproporcionalmente mais do que erros pequenos.

**Usasmo MSE**

No entanto, a função Erro tem um valor diferente para cada observação do dataset. Precisamos então converter essa função em um número que possamos minimizar. Em problemas de regressão, uma boa prática é usar a função do erro quadrático médio (como vimos no [último post](https://medium.com/turing-talks/turing-talks-10-introdução-à-predição-a75cd61c268d)):

onde *m* é o número de observações do dataset. Usamos essa equação não somente por apresentar bons resultados, mas porque, se apenas usássemos o erro médio, erros positivos poderiam cancelar os erros negativos. Ao considerar o erro ao quadrado, todos os termos se tornam positivos e não temos mais esse problema. Além disso, temos como efeitos colaterais que:



<img src="/home/rhavel/Documentos/Personal Projects/data-science-study/DS My Notes/Advanced Concepts/Regularization in Regression - L1 Lasso, L2 Ridge/imgs/1_NHIxQt1M6pviPknGPh69Lg.png" />

1. erros maiores importam muito mais, já que, se maiores que 1, quando elevados ao quadrado aumentam bastante;
2. nossa função de custo *L* ganha a forma de parábola (ou paraboloide) com concavidade para cima, de forma que no gráfico de *L*, todo mínimo local é também mínimo global. Isso está exemplificado na imagem abaixo. O erro quadrático médio na regressão linear se comporta como o gráfico da esquerda, ou seja, é impossível achar um mínimo local que não seja ótimo (isso pode ser falso em outros modelos diferentes da regressão linear).

----





Artigo da UFPR

http://cursos.leg.ufpr.br/ML4all/apoio/Regularizacao.html

Em problemas  de regularização onde  “*small* *n* *and* *large* *p*” (muitas features e poucas rows), a maioria dos métodos modernos de análise de dados falha, por diferentes razões:

> **O que é small n and large p**
>
> Here p refers to the number of features and n refers to the number of samples.
>
> Let's say you have 10 x 10, 2-Dimesional feature space. Total number of possibilities for data points is 100. Now assume you have 10 data points spread across this space.
>
> If you move these 10 data points to a 3- Dimensional feature space (10 x 10 x 10), the sparsity will increase and you will need more data points to explain this new 3 -Dimesional feature space.
>
> Therefore, a larger p needs a larger n.



Diante dessas situações, os métodos de regularização são aconselhados, pois permitem cenários contínuos do domínio da função custo e lidam bem com casos em que *p*>*n*p>n. 