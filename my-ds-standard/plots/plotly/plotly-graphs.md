# EDA com Plotly



## Cores no Plotly

Link https://plotly.com/python/builtin-colorscales/

![](G:\Personal Projects\DATA-SCIENCE-PROJECT\data-world\my-ds-standard\plots\plotly\imgs\colors-plotly.png)



## Aux Functions

### Break lines of Cat Feat Long Text

**Para que serve:** Se os valores da cat-feat forem muito longos, é bom você diminuir seu tamanho apra caber nos gráficos. A função `insert_break_line` serve para por o `<br>` nisso

```
from math import floor

def insert_break_line(astring, index_point=5):
    splited = astring.split(' ')
    for i in range(floor(len(splited)/index_point)):
        splited.insert(index_point * (i+1), '<br>')
    return " ".join(splited).replace(' <br> ','<br>')
```

Como usar

```
# Usado na parte de valor do `value_counts`
df_aux['Valor'] = df_aux['Valor'].apply(lambda x:  x if len(x.split(' ')) > 10 else insert_break_line(x) )
```



## Describe Cat Feat

### `pie_plotly_cat_feat`

BarPlot com Porcentagem

```python
def pie_plotly_cat_feat(adf, col, title):
    """
    Cria PiePlot usando dados de uma Series. Faz por `value_counts`
    """
    # Pre-Processing Series
    df_col = adf[col]
    df_aux = df_col.value_counts().reset_index().rename(
        columns={'index': 'Valor', col: 'Quantidade'})
    second_col = df_aux.columns.tolist()[1]
	# Plotly Figure
    fig = px.pie(df_aux, values='Quantidade', names='Valor', title=title,
                 color_discrete_sequence=px.colors.sequential.Rainbow 
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.show()   
```

![](G:\Personal Projects\DATA-SCIENCE-PROJECT\data-world\my-ds-standard\plots\plotly\imgs\pie_plot_one_cat_feat.png)

### `bar_plotly_cat_feat`

```python
def bar_plotly_cat_feat(adf, col, title='', x_col_rename=''):
    """
    Cria BarPlotly usando Value counts de uma Series  cat-feat
    """
    # Define Constants
    qtd_col = 'Quantidade' # pode ser mudado para 'count'
    percentage_col = 'Porcentagem' # pode ser mudado para 'percent'
    x_col = x_col_rename if x_col_rename else col
    # Pre-Processing
    df_temp = adf[col].value_counts().reset_index().rename(
        columns={'index': x_col, col: qtd_col}
    )
    # Col Percentage in String
    df_temp[percentage_col] = round(
        (df_temp[qtd_col] / df_temp[qtd_col].sum()) * 100.0, 2).apply(
        lambda x: str(format(x,'.2f')) + '%' )
    # BarPlotly Figure
    fig = px.bar(
        df_temp, y=qtd_col, x=x_col,
        color=qtd_col, hover_data=[percentage_col],
        text=percentage_col, title=title,
        color_continuous_scale='dense'
    )
    fig.show()
```

Exemplo

```python
bar_plotly_cat_feat(df, "('P2_h ', 'Faixa salarial')", 'Novo Titulo', 'Faixa Salarial')
```

![](G:\Personal Projects\DATA-SCIENCE-PROJECT\data-world\my-ds-standard\plots\plotly\imgs\bar_plotly_cat_feat.png)

## Describe Cross many cat Feat

Tenha como base uma cat-feat, depois é feito uma filtragem do DataFrame de outras cat-feats usando valores fornecidos em um dicionário. Por fim é aplicado o bar_plot_one feat sobre esse dataframe filstrado. O titulo é feito pela composiçâo das colunas usadas para filtrar.

```python
def bar_plotly_describe_cat_feat_filter_cat_feats_values(adf, x_feat, adict, start_title='', x_col_rename=''):
    """
    Filtra dataframe por hard-code de cat-feats. Em seguida aplica barPlotlyOneCatFeat.
    O titulo é feito por uma base inicial e em sequencia concatenações dos valores usados
    """
    # Filter DataFrame by values of cat feats
    df_temp, title = adf, start_title
    for col in adict.keys():
        df_temp = df_temp[ df_temp[col] == adict[col] ]
        title = title + ' - ' + adict[col]
    # Bar PLotly One Cat Feat
    bar_plotly_cat_feat(df_temp, x_feat, title, x_col_rename)
```

Exemplo: Observe que usa uma outra função já definida aqui

```python
adict = {
    "('P2_f ', 'Cargo Atual')": 'Engenheiro de Dados/Data Engineer',
    "('P2_g ', 'Nivel')": 'Pleno',
    "('P2_a ', 'Qual sua situação atual de trabalho?')": 'Empregado (CLT)',
}

bar_plotly_describe_cat_feat_filter_cat_feats_values(
    df,
    "('P2_h ', 'Faixa salarial')",
    adict=adict,
    start_title='Faixa Salarial de',
    x_col_rename='Faixa Salarial',
)
```

![](G:\Personal Projects\DATA-SCIENCE-PROJECT\data-world\my-ds-standard\plots\plotly\imgs\bar_plotly_describe_cat_feat_filter_cat_feats_values.png)