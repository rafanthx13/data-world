# Best Tips to Pandas





## Principais operações com python

`````
df.head()
+ lista as primeiras 5 rows. Uma amostragem dos dados

df.info()
+ lista quantidade de colunas, tamanho que consome de memória e tipo de dados

df.describe()
+ Lista estatísticas de cada coluna do DataFrame

df["column].value_counts()
+ Visualiza valores unicos e a quantidade deles

df.shape
+ Retorna tupla (rows, columns)

df.dtypes
+ Retorna os tipos dos dados. CONfira e garanta que os tipos estão certos. Não deixe como tipo object, poi isso é muito geral

df["column"].describe()
+ Faz media, desvio e etc. de uma coluna numérica

# Usando Boolean DataFrame para verificar quantos dados
print(pcnt_val.value_counts(), '\n', pcnt_val.value_counts(normalize = True))
````
True     249138
False       862
Name: passenger_count, dtype: int64 
 True     0.996552
False    0.003448
Name: passenger_count, dtype: float64
````

=============== Navegar pelo Pandas ===================================

base.loc[ base['age'] < 0]
loc : localisa as rows de acordo com o critério, retorna um dataframa

==> RETIRAR COLUNA
# 1. apagar toda a coluna (nesse caso, isso é ruim)
base.drop('age', 1, inplace=True)

==> RETIRAR ROWS
# 2. apagar somente os registros com problema
base.drop(base[base.age < 0].index, inplace=True)

=> Atualizar linha de acordo com um critério
base.loc[base.age < 0, 'age'] = media
============== 2. Lidar com NaN ========



============= 5. Datas ================================================

key.dt.strftime('%Y-%m-%d %H:%M:%S')
+ Converter a data para o formato desejado
`````



## Converter tipagem de coluna

Há várias formas de fazer mas todas elas vão dar erro se houver algum Nan.

Para passar por cima disso use o método abaixao: vai converter a tipagem e manter o Nan.

````
df[col] = df[col].astype(pd.Int32Dtype())
````

## Dict Compression

````
list_minerando = [ 'Minerando dados', 'Blog minerando dados', 'Blog Minerando Dados']
dict_minerando = {el: 'Minerando Dados' for el in list_minerando}
````

Todas as chaves vão apontar para a constante `'Minerando Dados'`

## Checar se um valor é nulo `pd.isna`

O que pode dar problema é que a maioria das funçoes checa se um float é Nan/None.

Com a funçâo abaixao ele vai verificar para qualquer valor, seja funçao/string/int/float e etc

````
cols_to_insert_break = ["('D6', 'anonymized_role')", "('D3', 'anonymized_degree_area')"]
for col in cols_to_insert_break:
    df[col] = df[col].apply(lambda x: insert_br_in_break_ponint(x) if not pd.isna(x) else x)
````

Converter coluna para float

````
df_bens['VR_BEM_CANDIDATO'] = df_bens['VR_BEM_CANDIDATO'].apply(
    lambda x: float(x.replace(',','.')) if not pd.isna(x) else x
)
````

## Converter comentario em lista

Eh nais facil que esquercer [] e umonte de '' e ','

````
list_cols_despesas_contratadas = """
DS_CARGO
SQ_CANDIDATO
NR_CANDIDATO
VR_DESPESA_CONTRATADA
"""

df_despesas_contratadas = df_despesas_contratadas[convert_long_comment_in_string(list_cols_despesas_contratadas)]
````

## Converter Float para R$

````
def format_to_br_money(the_float):
    return 'R$ {:,.2f}'.format(the_float).replace(',','x').replace('.',',').replace('x','.')

def cast_float_to_money(anumber):
    return "R$ {:,.2f}".format(anumber).replace(
        ',','x').replace('.',',').replace('x','.')

def cast_float_to_br_float(anumber):
    return "{:,.2f}".format(anumber).replace(
        ',','x').replace('.',',').replace('x','.')


````



## Panda stylus

```
## Esconde index
# Using hide_index() from the style function
planets.head(10).style.hide_index()

## Esconder colunas desnecessárias
planets.head(10).hide_columns(['method','year'])

## Destacar valores masimo ou miniomos da coluna
#Highlight the maximum number for each column
planets.head(10).style.highlight_max(color = 'yellow')
planets.head(10).style.highlight_min(color = 'lightblue')
planets.head(10).style.highlight_null(null_color = 'red')

## Ter um BarChart nas células do dataframe
# Sort the values by the year column then creating a bar chart as the background
planets.head(10).sort_values(by = 'year').style.bar(color= 'lightblue')
# A barra é de acordo com a distribuiçâo da coluna
```



## Criar `pandas_profilling`

```
# Import libs
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport

# Import dataFrame
df = pd.read_csv("2004-2019.tsv", delimiter="\t")

# Generate pandas profiling
pfr = ProfileReport(df)
pfr.to_file("/home/rhavel/Documentos/example.html")
```

## pipeline pandas

=============================

Pipelin ONe-line in pandas

https://towardsdatascience.com/efficient-data-manipulation-with-pandas-2cbc4e3824f9

Se o seu codigo pandsa que começa com df.... ficar muito grande, paa ficar legivel voce pode escrever da seguinte forma 

````python
# start piping
results = (
    df
    # only keep selected columns
    [['LIMIT_BAL','EDUCATION','AGE']]
    # keep where age is atleast 25
    .query("AGE >= 25")
    # make bins for the age
    .assign(AGE= lambda x: ['youth' if i < 40 else 'mature' for i in x['AGE']])
    # apply normalization to the LIMIT_BAL
    .pipe(normalize,"LIMIT_BAL","NORMALIZED_LIMIT_BAL")
    # aggregate data by age and education
    .groupby(['AGE','EDUCATION',])
    .agg(MEAN_LIMIT_BAL=("LIMIT_BAL","mean"),MAX_NORMAL_BAL=("NORMALIZED_LIMIT_BAL","max"))
    # reset the index
    .reset_index()
)
````

====[]()=============================

Pipelin ONe-line in pandas

https://towardsdatascience.com/efficient-data-manipulation-with-pandas-2cbc4e3824f9

Se o seu codigo pandsa que começa com df.... ficar muito grande, paa ficar legivel voce pode escrever da seguinte forma 

````python
# start piping
results = (
    df
    # only keep selected columns
    [['LIMIT_BAL','EDUCATION','AGE']]
    # keep where age is atleast 25
    .query("AGE >= 25")
    # make bins for the age
    .assign(AGE= lambda x: ['youth' if i < 40 else 'mature' for i in x['AGE']])
    # apply normalization to the LIMIT_BAL
    .pipe(normalize,"LIMIT_BAL","NORMALIZED_LIMIT_BAL")
    # aggregate data by age and education
    .groupby(['AGE','EDUCATION',])
    .agg(MEAN_LIMIT_BAL=("LIMIT_BAL","mean"),MAX_NORMAL_BAL=("NORMALIZED_LIMIT_BAL","max"))
    # reset the index
    .reset_index()
)
````

## OUTROS

````
# Dicas para JNotebook: pandas, gráficos e bugs

#### Formatação da Saída em Float: Sem isso sai como e^x

`pd.options.display.float_format = '{:,.2f}'.format`

+ para voltar ao normal

`pd.reset_option("display.float_format")`

#### Evitar notaçâo cientifica (e^x)
ROW:
`pd.set_option('display.float_format', lambda x: '%.2f' % x)`

+ Essa forma tambem arredonda direto

#### python tem um len para tudo
qtd de nan = len(Series) - Series.count()

#### Verificar quantas linhas tem o dataframe (contando tudo)
len(DataFrame)

#### Retirar duplicatas
+ subset = [lista de colunas]
OneDataFrame.drop_duplicates(subset)

#### Obtendo Unique de uma Series
uniq_cliente = pd.Series(df['CHAVE_CLIENTE'].unique())

#### Convertendo para Date-Time - Isso é um procesos demorado
```
df_boxplot['SRK_DAT_ABR_ORD_SRV_TEC'] = pd.to_datetime( df_boxplot['SRK_DAT_ABR_ORD_SRV_TEC'], format = '%Y%m%d' )
df_boxplot['SRK_DAT_FCH_ORD_SRV_TEC'] = pd.to_datetime( df_boxplot['SRK_DAT_FCH_ORD_SRV_TEC'], format = '%Y%m%d' )
```

#### Lista compressiva em python
+ Em vez de fazer algo como [0,2,4,6,8,10] pode-se fazer uma lsita compressiva: um for que retorna valores numa unica linha
+ Exemplo: `[i*200 for i in range(7)] = [0,200,400,600,800,1000,1200] `

#### Numa Series, pegar o index de um valor da Series
+ Dado um valor que você sabe esta na series, quere saber qual o seu index.
+ Tem que ser index[0] pois sem ele mostra bestreia
`serie[series == valor].index[0]`

#### Bins em Hisotgrama:
+ O histograma define um intervalo, e, dado esse intevalo ele coloca em cada intervalo o elemento que estiver dentro dele.
+ Exemplo: bins = 10: Vi divir o range total da Series em 10 partes e por em 10 intervalos
+ Obvio, se o valor inicila e final não forem terminados em 0, pode ser que não fique muito legal
+ Forma mais direta: Exemplo: Quero o Hitograma (contagem de frequencia) a cada 200 (Faz intervalos de 0 a 200*i, de i = 0,1,2,3,4 ...). 
 - Nesse caso: Bins é uma lista `bins = [0,200,400,600, ...]`
+ Assim fica certinha a linha do eixo x

#### Listar de colunas do dataframe quando tem muitas colunas
`list(my_dataframe.keys())`
ou
`" , ".join(list(df_alldata_only_top10.keys()))`

#### Substituir valores invalidaos por Null (em pytohn, é o None)
`df_temp_1.replace({'-3': None, '-5': None, '-1': None})`

+ Só usando dict desse jeito você faz corretamente. Olhe a Doc dessa funçâo, dependeno de como você faz, nâo vai dá certo, ele vai substituir um que você quer pelo anteiror válido: e não é isso que queremos

#### Escolhendo range ao fazer um gráfico no matplot

`plt.xticks(df['bits'])`

+ Quando você gera um gráfico de pontos (x,y) os eixos x e y são configurados de acordo com o range de x e y. Colocando esse código, vai especificar onde colocar as labelas
+ Sem ele é decidido autimaticamente, e, dependendo da situaçâo, é melhor para visualizar colocar ele

#### Obrigar a sair ponto de outlyer no boxplot
ROW:

```python
ax = ax.boxplot(df['df'][attr].dropna(), showfliers=True)
    for flier in ax['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)
```

#### Renomear Colunas de um DataFrame
link: http://cmdlinetips.com/2018/03/how-to-change-column-names-and-row-indexes-in-pandas/

+ Você recupera as colunas por:  dataFrame.columns
+ Isso é um atributo, e como talv, você pode substituilo por outro desde que tenha o mesmo tamanho.
+ em `generate_all_equipamentas` eu consegui colocar um prefixo em todos de uma só vez e substituir as colunas


#### Format of datetime in python
Consulte esse link:
https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior

#### Remover Coluna do DataFrame
`result = result.drop(['Tipo'], axis=1)`

#### Iterar Dictionary iterar

```
for value in dict.values():
	print(value)

for key in dict.keys():
	print(key)

for key, value in dict.items():
	print(key, value)
```

#### Colocar com o separador de milhar em um número (BR)

OBS: Se vocêr for usar muito, eu aconselho a criar uma funçâo no início pra chamar ela. pode ate´ter uma padrao default para caso quiser fazer  um round e coloca nos arg a quantidade de casas decimais.
 `("{:,}".format(len( NUMERO_HERE))).replace(',','.')`


##### Iterar row por row de um dataFrame

```
for index, row in df.iterrows():
     print(index, row['inner_vlan'], row['outer_vlan'])
```

+ OBS: É necessário por o index da forma como está, pois o 1 para é o index.
+ OBS: o conteudo da linha fica no 2 arg, você acessa usando ['column_name"]

##### FORMAT DATE

EXISTE DIFERENÇA: NO ANO
OS
`format = '%d/%m/%Y %H:%M:%S'`
SNAP.CREATION_DATE
`format = '%d/%m/%y %H:%M:%S'`

#### Normalized a Column

```python
import pandas as pd
from sklearn import preprocessing

%matplotlib inline

# Create x, where x the 'scores' column's values as floats

x = df[['score']].values.astype(float)

# Create a minimum and maximum processor object

min_max_scaler = preprocessing.MinMaxScaler( feature_range = (min_value, max_value))

# Create an object to transform the data to fit minmax processor

x_scaled = min_max_scaler.fit_transform(x)

# Run the normalizer on the dataframe

df_normalized = pd.DataFrame(x_scaled)

df_normalized # Estará com valores entre 0 e 1
```

#### TRY CATH em Python
```
try:
	
    raise Exception('Nao existe a coluna alvo no df_target')

except Exception as e:
```

#### `reset_index(drop=True)`

Se vocÊ mexer nas linhas ou ordem das linhas, faça isso caso for atribui ou fazer merge/join/concat ou atribuição

TODA ATRIBUIÇÂO, CONCATENAÇAO, JOIN OU MERGE. ISSO VAI INFLUCNECIAR
Exemplo: se vco atribuo uma series de mesmo tamanho para substituir uma outra, nao vai
por causa do indeice, buga tudo. Entao, de ese reset_index principlamente se vc titoru coisa

#### `to_csv`

df_customer_name.to_csv(
'final_predict_all.csv', sep = ';', index = False)

#### Ver o tipo de dado da coluna DataFrame

basta dar um print nesse atributo que mostra corretamente

For a single column:

`dataframe.column.dtype`
For all columns:

`dataframe.dtypes`

Retorna da seguinte forma:

#A     int64
#B      bool
#C    object
#dtype: object

#### Converter tipo da coluna no pandas

df['colun'] = df['colun'].astype(str)
o tupo pode ser:
str, int, float

#### profile profiling pandas report relatorio

Quando gerar um Arquivo csv, gere usando a seguinte linha:
+ OBS: Se o arquivo for muito grande, mais de 800MB o profiling vai demorar demais
```
import pandas_profiling
path_file ='path_to_file'
df.to_csv(path_file + '.csv', sep = ';',index = False)
pandas_profiling.ProfileReport(df).to_file( path_file + ".html")
```

### raise Exception exeçâo exception

raise Exception('Nao existe a coluna alvo no df_target')

### parametro default em python

Pasta colocar um igual e o valor. Se nada for passado vai ele
def func (new_column = 'new_column'):

## contar quantidade de valores unicos 
No final de um value_counts mostra essa quantidade em lenght: o tamanho da seire produzia do valeu_counts
Mas tambem vou fazer uma funçâo no util
	

````

## rANDOM RANDOM

`````
# Random Snippets of Kaggle

## Template

````python

````

## Não mostrar nada desnecessário

````python
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline
````

## 

## Zoom HeartMap most important correlation

````python
k = 10 #number of variables for heatmap
# get the 'k' largest correlations values columns with 'SalePrice'
cols = corrmat.nlargest(k, 'SalePrice')['SalePrice'].index
cm = np.corrcoef(df_train[cols].values.T)
sns.set(font_scale=1.25)
hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)
plt.show()
# The heartmap is order_by correlation value with 'Sale Price' in row of 'Sale Price'
````

##  pairplot: scaterplot and histogram in diagonal


````python
#scatterplot
sns.set()
cols = ['SalePrice', 'OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt']
sns.pairplot(df_train[cols], size = 2.5)
plt.show();
````


### Missing Data

````python
#missing data
total = df_train.isnull().sum().sort_values(ascending=False) # Qtd of missing Values
percent = (df_train.isnull().sum()/df_train.isnull().count()).sort_values(ascending=False) # Make Percentage of missing_values
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent']) # concat in DataFrame
missing_data.head(20) # View the top '20' coluns with most missing_values


#dealing with missing data
df_train = df_train.drop((missing_data[missing_data['Total'] > 1]).index,1) # drop coluns with more of 1 missing_values
df_train = df_train.drop(df_train.loc[df_train['Electrical'].isnull()].index) # drop rows
df_train.isnull().sum().max() #just checking that there's no missing data missing...
````

#### Seaborn e printar dados faltantes em gráfico

````python
# set up aesthetic design
plt.style.use('seaborn')
sns.set_style('whitegrid')

# create NA plot for train data
plt.subplots(0,0,figsize = (15,3)) # positioning for 1st plot
train.isnull().mean().sort_values(ascending = False).plot.bar(color = 'blue')
plt.axhline(y=0.1, color='r', linestyle='-')
plt.title('Missing values average per columns in TRAIN data', fontsize = 20)
plt.show()
````

## Acessar diretorio e listar arquivos

````python
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
````

/input/house-prices-advanced-regression-techniques/data_description.txt
````
## Categorical Data

````python
# get categorical columns
categorical_cols = [col for col in train.columns if train[col].dtypes == "object"]
print("number of categorical columns is: ")
print(len(categorical_cols))
print("categorical columns:\n", categorical_cols)
````

## Fill Mising data

### Fill Categorical MIssing Data

````python
# fill NA value by missing
for col in categorical_cols:
    df[col] = df[col].fillna("missing")
````

## Cálculo de RMLSE

````python
def rmsle(y_true, y_pred):
    return 'RMSLE', np.sqrt(np.mean(np.power(np.log1p(y_pred) - np.log1p(y_true), 2))), False
````

## Como usar parâmetros de GridSearchCV

````python
svr_model = SVR(**clf.best_params_)
````

## View Importance Features of XGBoost

````python
xgb_feature_importances = xgb_model.feature_importances_
xgb_feature_importances = pd.Series(
    xgb_feature_importances, index=X_train.columns.values
    ).sort_values(ascending=False).head(15)

fig, ax = plt.subplots(figsize=(7, 5))
sns.barplot(x=xgb_feature_importances, 
            y=xgb_feature_importances.index, 
            color="#003f5c");
plt.xlabel('Feature Importance');
plt.ylabel('Feature');
````

````python
rf_feature_importances = pd.Series(
    rf_feature_importances, index=X_train.columns.values
    ).sort_values(ascending=False).head(15)

fig, ax = plt.subplots(figsize=(7,5))
sns.barplot(x=rf_feature_importances, 
            y=rf_feature_importances.index, 
            color="#ffa600");
plt.xlabel('Feature Importance');
plt.ylabel('Feature');
````

`````

