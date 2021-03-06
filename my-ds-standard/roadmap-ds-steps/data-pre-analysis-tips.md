

1. Verificar Tipos de dados

2. Verificar se para um tipo de dados (int/string) todas as rows nessa coluna é mesmo do tipo int/string. (dtypes do pandas)
	+ int,flot, string/object, datetime

3. Remover dados inválidos:
+ Idenficá-los e substituir por Nan (np.nan) que indica que é um dado faltante. O Scik-Learnig e outros frameworkss tratam melhor Nan do que qualquer outra coisa
  - Verifica positivo/negatio onde deve ser s[o positivo
  - Em string, string vazias e nulo
==> Para dados numéricos, faça um histograma para detectar outliers inválidos e faça a filtragem. A filtragem é do EXEMPLO 2 (Preço de Taxi de NY) Você cria uma DataF e Boolean que atende a uma condiçâo, junta tudo e com isso faz a filtragem das rows

4. Converter o tipo da coluna para o tipo correto "float", "category"

5. Observar se uma coluna tem mitos dados faltantes
+ Se tiver, entâo retire essa coluna
  - Se deixar uma coluna com muito Nan é ruim para qualquer modelo

6. Decidir critério para retirar coluna
  - QUantidade mínima de valores válidos

7. Preencher os valores faltante com algum dado?
  - Se númerico, daria para preencher pela média? 
  - Se categóricos, poderia substituir por uma nova categoria chamda "missign"
  - TUdo isso são estratégias, nâo é algo engessado

8. Verificar se as variáveis categoricas tem muitas categorias?
+ `features[cat_vars].apply(lambda x: len(set(x)))`
+ Talvez muitas categorias para uma string nâo representa muita informaçâi. 
+ Um exemplo disso é o nome por exemplo 

9. Fazer seleção de variáveis baseadas na árvore de decisão
+ ExtraTreeClassifier

10. Otimizar classificador
+ Uma boa prática e alterar parâmetros separadamente, de forma a obter um valor que otimiza o classificador só com aquele parâmetro. E, no final, juntar tudo.

================= Testar Alg de ML  ===================================

+ Em geral, define-se um valor 'cv' que é a quantidade de divisão da base para testá-la. Em artigos cientificos costuma-se usar 10, mas, quanto maior o número, mais demora. Para casos simples, use 3.
+ `cv = 3`

+ Função de erro:  
  - Servem para qualificar uma ML, quanto menor, melhor
  - RMSE : root-mean-square error
    * `scoring = 'neg_mean_squared_error'`
  - RMSD : root-mean-square deviation

+ Quantidade de núcleos:
````python
import multiprocessing
n_jobs = multiprocessing.cpu_count() - 1
````

+ Pode usar por exemplo a métrica RMSE para saber qual é melhor sem treinar muito.

================= FEATURES ENGENEERING ==============================

Com base nos dados que nós temos, vamos criar outras colunas.

Exemplo
````
Prevendo Preço de Taxi em NY

Algo que influencia a duração da viagem é a condição do tráfego. Podemos deduzir usando `pickup_datetime`.

* *hora do dia*: tráfego será menor durante a noite
* *dia da semana*: tráfego será menor nos finais de semana
* *dia do ano*: referiados e férias, por exemplo
* *ano*: pode ser influenciado por mudanças nas regras de transporte ou inflação
````

==> Ao fazer a engenharia de features, se você, por exmeplo, pegar uma data completa "%h %m %s / %d %M %y" e deixar separado, entâo, a coluna com o dado original "%h %m %s / %d %M %y" deve ser excluida **para evitar repetição de features e duplicaçâo, oq ue atrapalha na ML**

=================== NORMALIZAÇÃO =============================

Quando as colunas Numéricos tem escala valores muito diferentes entre si, é recomendável normzliar. Colocar tudo entre [0,1]. Assim o treinamento de ML será mais rápido.

Exemplo
````python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
````

================== REFRESSÃO LINEAR - SciKIt-Learning =============

## LinearRegression
````python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
scores = cross_val_score(model, X_train_scaled, y_train, cv = cv,
                         scoring = scoring, n_jobs = n_jobs)
np.sqrt(-scores.mean())


from sklearn.linear_model import Ridge
model = Ridge()
scores = cross_val_score(model, X_train_scaled, y_train, cv = cv,
                         scoring = scoring, n_jobs = n_jobs)
np.sqrt(-scores.mean())

from sklearn.linear_model import Lasso
model = Lasso()
scores = cross_val_score(model, X_train_scaled, y_train, cv = cv,
                         scoring = scoring, n_jobs = n_jobs)
np.sqrt(-scores.mean())

from sklearn.neighbors import KNeighborsRegressor
model = KNeighborsRegressor()
scores = cross_val_score(model, X_train_scaled, y_train, cv = cv,
                         scoring = scoring, n_jobs = n_jobs)
np.sqrt(-scores.mean())

from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor()
scores = cross_val_score(model, X_train_scaled, y_train, cv = cv,
                         scoring = scoring, n_jobs = n_jobs)
np.sqrt(-scores.mean())

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
scores = cross_val_score(model, X_train_scaled, y_train, cv = cv,
                         scoring = scoring, n_jobs = n_jobs)
np.sqrt(-scores.mean())

from sklearn.ensemble import GradientBoostingRegressor
model = GradientBoostingRegressor()
scores = cross_val_score(model, X_train_scaled, y_train, cv = cv,
                         scoring = scoring, n_jobs = n_jobs)
np.sqrt(-scores.mean())

from sklearn.neural_network import MLPRegressor
model = MLPRegressor()
scores = cross_val_score(model, X_train_scaled, y_train, cv = cv,
                         scoring = scoring, n_jobs = n_jobs)
np.sqrt(-scores.mean())
````


================== O que é o 'y' num problema de regressão? =============


According to [Hair et al. (2013)](https://amzn.to/2uC3j9p), four assumptions should be tested:

* <b>Normality</b> - When we talk about normality what we mean is that the data should look like a normal distribution. This is important because several statistic tests rely  on this (e.g. t-statistics). In this exercise we'll just check univariate normality for 'SalePrice' (which is a limited approach). Remember that univariate normality doesn't ensure multivariate normality (which is what we would like to have), but it helps. Another detail to take into account is that in big samples (>200 observations) normality is not such an issue. However, if we solve normality, we avoid a lot of other problems (e.g. heteroscedacity) so that's the main reason why we are doing this analysis.

* <b>Homoscedasticity</b> - I just hope I wrote it right. Homoscedasticity refers to the 'assumption that dependent variable(s) exhibit equal levels of variance across the range of predictor variable(s)' [(Hair et al., 2013)](https://amzn.to/2uC3j9p). Homoscedasticity is desirable because we want the error term to be the same across all values of the independent variables.

* <b>Linearity</b>- The most common way to assess linearity is to examine scatter plots and search for linear patterns. If patterns are not linear, it would be worthwhile to explore data transformations. However, we'll not get into this because most of the scatter plots we've seen appear to have linear relationships.

* <b>Absence of correlated errors</b> - Correlated errors, like the definition suggests, happen when one error is correlated to another. For instance, if one positive error makes a negative error systematically, it means that there's a relationship between these variables. This occurs often in time series, where some patterns are time related. We'll also not get into this. However, if you detect something, try to add a variable that can explain the effect you're getting. That's the most common solution for correlated errors.


=================== Analisando Kernel Pedro Marcelino - COMPREHENSIVE DATA EXPLORATION WITH PYTHON ========

Um NOtebook Cehio de conhecimento, feito por um estastístico de verdade.

DataExploration
1. Entender as colunas do problema
    - Fazer um Excel com as colunas e colocar os seguintes dados:
    - 0. Descrição
    - 1. Tipo: Numérico/Categórica
    - 2. Identificar o Segmento que pertence essa variável no contexto do problema. No exemplo de regressão do preço de casa, havia 3 segmentos "a construçâo", "o espaço" e a "localidade
    - 3. Expectativa: O quanto de inicio você espera que aquela variável tenha relevância para o problema
    - 4. Conclusâo: Se após a análise a variável está de acordo com suas espectativas

Funções mais usadas:
````python
#descriptive statistics summary
df_train['SalePrice'].describe()

#histogram
sns.distplot(df_train['SalePrice']);
````

2. Buscar correlações entre as variáveis numéricas que vocẽ cahar mais importantes

````python
#scatter plot totalbsmtsf/saleprice
var = 'TotalBsmtSF'
data = pd.concat([df_train['SalePrice'], df_train[var]], axis=1)
data.plot.scatter(x=var, y='SalePrice', ylim=(0,800000));
````

3. Correlaçâo com as categóricas

````python
df_train["OverallQual"].value_counts()

print("min = ", df_train["OverallQual"].min())
print("max = ", df_train["OverallQual"].max())


var = 'OverallQual'
data = pd.concat([df_train['SalePrice'], df_train[var]], axis=1)
f, ax = plt.subplots(figsize=(8, 6))
fig = sns.boxplot(x=var, y="SalePrice", data=data)
fig.axis(ymin=0, ymax=800000);
````

3. Fazer a correlaçâo de tudo de uma vez com HeartMap

````python
#correlation matrix
corrmat = df_train.corr()
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat, vmax=.8, square=True);
````

Depois dar um zoom

````python
#saleprice correlation matrix
k = 10 #number of variables for heatmap
# get the 'k' largest correlations values columns with 'SalePrice'
cols = corrmat.nlargest(k, 'SalePrice')['SalePrice'].index
cm = np.corrcoef(df_train[cols].values.T)
sns.set(font_scale=1.25)
hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)
plt.show()

4. Observar a correlaçÂo entre as mais imporatnte com pairplot

````python
#scatterplot
sns.set()
cols = ['SalePrice', 'OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt']
sns.pairplot(df_train[cols], size = 2.5)
plt.show();
````

5. Tratar com dados faltantes

Identificar

````python
#missing data
total = df_train.isnull().sum().sort_values(ascending=False) # Qtd of missing Values
percent = (df_train.isnull().sum()/df_train.isnull().count()).sort_values(ascending=False) # Make Percentage of missing_values
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent']) # concat in DataFrame
missing_data.head(20) # View the top '20' coluns with most missing_values
````

Deletar

````python
#dealing with missing data
df_train = df_train.drop((missing_data[missing_data['Total'] > 1]).index,1) # drop coluns with more of 1 missing_values
df_train = df_train.drop(df_train.loc[df_train['Electrical'].isnull()].index) # drop only rows
df_train.isnull().sum().max() #just checking that there's no missing data missing...
````


6. Tratar as variáveis Categóricas

````python
df_train = pd.get_dummies(df_train)
````







# Converter value_counts => Percentage dataFrame
re = df['year'].value_counts()
re2 = re / re.values.sum()
re2.name = "percentage"
re.name = "quantity"
re4 = pd.concat([re, re2], axis = 1)
re4.reset_index(level=0, inplace=True)
re4 = re4.rename(columns = {'index': 'year'})
re4

re4.plot.pie(y='percentage', figsize=(5, 5), autopct="%.2f", labels = re4['year'].tolist(), legend=None)
