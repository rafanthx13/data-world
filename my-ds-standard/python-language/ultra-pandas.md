# Best Tips to Pandas

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

## Chcar se um valor é nulo

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
