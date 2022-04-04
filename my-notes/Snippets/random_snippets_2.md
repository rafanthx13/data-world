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
	




-----------------------------------------------------------------------
