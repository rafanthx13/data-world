# Geat Unkwon Libs

![rise](https://pypi.org/project/rise/)
+ Lib que permite tranformar o JupyterNotebook em Slide
+ Idela para apressntaçâo, e você pode configurar que celulas msotra ou não
+ pip install rise
+ jupyter nbextension enable rise --py --sys-prefix
** Como funciona**
+ Na aba `View>Cell Toolbar` coluq em `Slideshow`
  - Agora cada celula terá um campo `Slide Type` no topo direito
+ Escolha entre os tipos
  - Slide
  - Sub-Slide
  - Fragment
  - Skip
+ Para ativar e desativar o modo slide: ``Altr + R``

pip install nbdime
+ compara base com remoto das celulas do jupyter nnotebok. um gri aprimorado para ver a diff


$ pipreqsnb . 
+ salar libs python de acordo com os imports do jupyter notebook

=======================

https://nbqa.readthedocs.io/en/latest/readme.html
nbqua : 
+ Lib no CLI sobre o arquivo jupyter: aplica diversas coisa (liter, sort-imports e etcc, muiota cosia cmo PEP8)

Nesse link mostra todas as opçoes

https://nbqa.readthedocs.io/en/latest/examples.html

black — formats Python code
flake8 — checks the style and quality of your Python code
isort — automatically sorts imported libraries alphabetically and separates them into sections and types.
mypy — checks static type
nbstripout — strips output from Jupyter notebooks

pycatet: etapas de ds e ml automaticas


=================

dtale
+ lib abruda que permite analisar df em uma nova janela com umpnte de coisa, sem precisar usar mais celulas do jupyer notebok
+ É ALGO INCRIVEL
+ EXMEPLO} https://alphatechadmin.pythonanywhere.com/dtale/main/1
https://github.com/man-group/dtale

=============

klib : data anlisys in one line

repo ofiical: https://github.com/akanz1/klib

import klib
import pandas as pd

df = pd.DataFrame(data)

# klib.describe - functions for visualizing datasets
- klib.cat_plot(df) # returns a visualization of the number and frequency of categorical features
- klib.corr_mat(df) # returns a color-encoded correlation matrix
- klib.corr_plot(df) # returns a color-encoded heatmap, ideal for correlations
- klib.dist_plot(df) # returns a distribution plot for every numeric feature
- klib.missingval_plot(df) # returns a figure containing information about missing values

# klib.clean - functions for cleaning datasets
- klib.data_cleaning(df) # performs datacleaning (drop duplicates & empty rows/cols, adjust dtypes,...)
- klib.clean_column_names(df) # cleans and standardizes column names, also called inside data_cleaning()
- klib.convert_datatypes(df) # converts existing to more efficient dtypes, also called inside data_cleaning()
- klib.drop_missing(df) # drops missing values, also called in data_cleaning()
- klib.mv_col_handling(df) # drops features with high ratio of missing vals based on informational content
- klib.pool_duplicate_subsets(df) # pools subset of cols based on duplicates with min. loss of information
=
=================

Degubar Jupyter

!pip install pixiedust
import pixiedust

%%pixie_debugger
import random
def find_max (values):
    max = 0
    for val in values:
        if val > max:
            max = val
    return max
find_max(random.sample(range(100), 10))


================

chema: lib que valida se os dados estâo num certo tipo

https://towardsdatascience.com/introduction-to-schema-a-python-libary-to-validate-your-data-c6d99e06d56a

Exemmplo

pip install schema


from schema import Schema
schema = Schema([{'name': int,
                 'city': str, 
                 'closeness (1-5)': int,
                 'extrovert': bool,
                 'favorite_temperature': float}])

schema.validate(data)

Se eu não me interreso pelo tipo do dao coloco como obj

schema = Schema([{'name': str,
                 'city': str, 
                 'favorite_temperature': float,
                  str: object
                 }])
                
schema.is_valid(data)

Validaão de valores com lambda

schema = Schema([{'name': str,
                 'city': str, 
                 'favorite_temperature': float,
                  'closeness (1-5)': lambda n : 1 <= n <= 5,
                  str: object
                 }])

schema.is_valid(data)


Adicionar mais de uma validaçao: AND e OR

'city': Or(lambda n: len(n.split())==2, lambda n: len(n.split()) ==1), 
'city': And(str, Or(lambda n: len(n.split())==2, lambda n: len(n.split()) ==1)),
'closeness (1-5)': And(lambda n : 1 <= n <= 5, float),


=================================

Faz semelhante ao Schema 

lib pandera

https://towardsdatascience.com/validate-your-pandas-dataframe-with-pandera-2995910e564#02ed-516b1986ac24


==============


Visualize Feature Importances with Yellowbrick

####################


EDA IN ONE ONLINE LINE

https://towardsdatascience.com/4-libraries-that-can-perform-eda-in-one-line-of-python-code-b13938a06ae

PADSN-PROFILIN
D-TALE: pip install dtale
pip install autoviz
Sweetviz 

Meu seumo: As 2 que nao conheço sao parecidas com pandas-profiling mas com UX difernete, valea a pena testar