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

Todas as chaves aponta para a constante `'Minerando Dados'`

## Chcar se um valor é nulo

O que pode dar problema é que a maioria das funçoes checa se um float é Nan/None.

Com a funçâo abaixao ele vai verificar para qualquer valor, seja funçao/string/int/float e etc

````
cols_to_insert_break = ["('D6', 'anonymized_role')", "('D3', 'anonymized_degree_area')"]
for col in cols_to_insert_break:
    df[col] = df[col].apply(lambda x: insert_br_in_break_ponint(x) if not pd.isna(x) else x)
````
