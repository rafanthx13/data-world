# Teste ANOVA em DataScience

https://machinelearningmastery.com/feature-selection-with-numerical-input-data/

## O que é anova

Análise de vainaia, ou seja, calcula correlçaâo entre numero e categoria. 

Se foses etnre 2 numeros usarmeos pearson

## Conceito de Feature Selection

Imagine um dataset com 100 features, e você tem que fazer modelo para predizer uma classificação categórica. Por exmeplo: ter 100 features de vinhos e predizer qualtipo de vinho é entre 10 possibilidades.

100 features é muito, entâo tem que reduzir: PCA, t-sns e etcc...

Acontece que, mesmo assim isso nao pode ajudar. o problema **éVocê nâo sabe quais variáveis podem ou não ser boas para predizer**

Se fosse uma regressão, ou seja, de uma sérei de numero prever outro, isso ficaria fácil. Basta fazer Pearson.

**Quando você tem um dado numérico e quer predizer um categórico há 2 formas: ANOVA e mutual information statistic.**

### Machine Learning Mastery - ANOVA f-test Feature Selection

https://machinelearningmastery.com/feature-selection-with-numerical-input-data/

**ANOVA is an acronym for “[analysis of variance](https://en.wikipedia.org/wiki/One-way_analysis_of_variance)” and is a [parametric statistical hypothesis](https://machinelearningmastery.com/parametric-statistical-significance-tests-in-python/) test for determining whether the means from two or more samples of data (often three or more) come from the same distribution or not.**

An [F-statistic](https://en.wikipedia.org/wiki/F-test), or F-test, is a class of statistical tests that calculate the ratio between variances values, such as the variance from two different samples or the explained and unexplained variance by a statistical test, like ANOVA. The ANOVA method is a type of F-statistic referred to here as an ANOVA f-test.

Importantly, **ANOVA is used when one variable is numeric and one is categorical, such as numerical input variables and a classification target variable in a classification task.**

The results of this test can be used for feature selection where those features that are independent of the target variable can be removed from the dataset.

### Codigo

A classe `SelectKBest` serve para selecionar features de acordo com um critério, no caso será anova com a funçâo já pronta que calcula ANOVA : `f_classif`

```python
# configure to select all features
fs = SelectKBest(score_func=f_classif, k='all')
# learn relationship from training data
fs.fit(X_train, y_train)

# what are scores for the features
for i in range(len(fs.scores_)):
	print('Feature %d: %f' % (i, fs.scores_[i]))
# plot the scores
pyplot.bar([i for i in range(len(fs.scores_))], fs.scores_)
pyplot.show()
```

Como serve para fazer feature-seelction, podemos colcoar de forma que além de calular, já atue nos dados de entrada `X` para filtrar as mehlores feature de acordo com o `k`. No codigo acima, k=all apra msotrar o f-test de todos, agora, poderiamos por por exemplo k=3 para reduzri fetaures e pegar as 3 melhores. Aplicando esse `SelectKBest` no vetor X  faz com que já filtre as 3 melhore

```python
# configure to select all features
fs = SelectKBest(score_func=f_classif, k=3)
# learn relationship from training data
fs.fit(X_train, y_train)
# transform train input data
X_train_fs = fs.transform(X_train)
# transform test input data
X_test_fs = fs.transform(X_test)
```

### Mutual Information Feature selectiion

Relacionado ao grau de entropia

a mesma coisa que o anova,, com `mutual_info_classif` ao ivnvez do `f_classif`