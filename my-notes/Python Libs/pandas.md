1. Geral dos dados
2. Lidar com NaN
3. Lidar com arquivos grande

============== 0. Random Valiosas =====================================

pd.set_option('display.float_format', lambda x: '%.3f' % x)
+ Número em notações científicas seraõ mostradas em float normal até com a casa



============== 1. Geral dos Dados =====================================

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


FILTRAGEM DE DADOS
pcnt_val = (pcnt >= 1) & (pcnt <= 6) # DataFrame de Boolean 
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
# JUNTANDOS VARIOS FILTROS
val_entries = fare_val & plon_val & plat_val & dlon_val & dlat_val & pcnt_val
# VENDO O QUANTO VAI TIRAR DA NOSSA BASE
print(val_entries.value_counts(), '\n', val_entries.value_counts(normalize = True))
# DROP AS ROW NA NOSSA BASE
train = train.drop(val_entries[val_entries == False].index)

# Contar quantidade
## O Counter é uma classe do Python especial com vários métodos
from collections import Counter
common_fares_zoom = Counter(fare_zoom)

=============== Navegar pelo Pandas ===================================

base.loc[ base['age'] < 0]
loc : localisa as rows de acordo com o critério, retorna um dataframa

==> RETIRAR COLUNA
# 1. apagar toda a coluna (nesse caso, isso é ruim)
base.drop('age', 1, inplace=True)

==> RETIRAR ROWS
# 2. apagar somente os registros com problema
base.drop(base[base.age < 0].index, inplace=True)

=> Atualizar linha de acordo com WRHTRR
base.loc[base.age < 0, 'age'] = media
============== 2. Lidar com NaN =======================================

df.isna()
+ Retorna DF de boolean para Nan

df.replace('', np.nan)
+ Substitui por Nan

df[col].fillna(col_mean)
+ Prencher Nans de uma coluna por um valor

============= 3. Lidar com arquivos grande ============================

+ TIP: Se por exemplo, a base for 5GB, pegue uma parte (250k rows) para trabalhar com o modelo e só no final avaliar 5GB. Pois é muito dado e a parte de treinar o modelo é muito demorada

+ TIP: para qualquer seleçâo arbitrária procure fazer de forma random

number_rows_in_file = sum(1 for line in open('train.csv'))
+ Contar número de linhas


============= 4. Load and Save CSV ====================================

Exemplo
````python
## parse_dates : converter os atributos que são datas
## dtype: passar os tipos dos atributos para converter já no read_csv
train = pd.read_csv('train_sample_' + str(sample_size) + '.csv',
    parse_dates = ['key', 'pickup_datetime'],
    dtype = {'fare_amount': np.float32,
             'pickup_latitude': np.float32,
             'pickup_longitude': np.float32,
             'dropoff_latitude': np.float32,
             'dropoff_longitude': np.float32,
             'passenger_count': np.int32             
    })
````

============= 5. Datas ================================================

key.dt.strftime('%Y-%m-%d %H:%M:%S')
+ Converter a data para o formato desejado

============= 6. Escalonamento

````python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)
````

============== Lidar com variáveis categóricas ===========

ONEHOTENCONDER: conveter cada categoria em coluna
````
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

onehotencorder = ColumnTransformer(transformers=[("OneHot", OneHotEncoder(), [1,3,5,6,7,8,9,13])],remainder='passthrough')
previsores_census = onehotencorder.fit_transform(previsores_census).toarray()
````

LABEL_ENCODER: Cada classe vira um número
````
from sklearn.preprocessing import LabelEncoder

labelencorder_classe = LabelEncoder()
classe_census = labelencorder_classe.fit_transform(classe_census)


============= DIVISÂO DA BASE EM TESTE/TREINO ========================

````
from sklearn.model_selection import train_test_split 

features_train, features_tests, class_train, class_test = train_test_split(
    features, classs, test_size = 0.25, random_state = 0)
````
````




==============================

......................


# DOC PANDAS CheatSheet

Documentação de acesso rápido e para o caso de nâo ter internet.
Além disso serve para especificar melhor os args, o que fazem e dicas de como usálos.

### df.drop_duplicates()
+ Retira Duplicatas
+ Link: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html
+ `DataFrame.drop_duplicates(subset=None, keep='first', inplace=False) `
+ Onde:
 - subset: list de colunas um uma coluna. por default considera todas quando não expecificar
 - keep: 'first' / 'last'
 - inplace: Boolean
  
