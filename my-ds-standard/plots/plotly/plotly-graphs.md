# EDA com Plotly



## Cores no Plotly

Link https://plotly.com/python/builtin-colorscales/

![](G:\Personal Projects\DATA-SCIENCE-PROJECT\data-world\my-ds-standard\plots\plotly\imgs\colors-plotly.png)

Buscar paleta de cores

```
import plotly.express as px

print(px.colors.sequential.dense)
```

```
# começa do mais claro para o mais escuro
['rgb(230, 240, 240)', 'rgb(191, 221, 229)', 'rgb(156, 201, 226)', 'rgb(129, 180, 227)', 'rgb(115, 154, 228)', 'rgb(117, 127, 221)', 'rgb(120, 100, 202)', 'rgb(119, 74, 175)', 'rgb(113, 50, 141)', 'rgb(100, 31, 104)', 'rgb(80, 20, 66)', 'rgb(54, 14, 36)']
```



## Aux Functions

### Break lines of Cat Feat Long Text

**Para que serve:** Se os valores da cat-feat forem muito longos, é bom você diminuir seu tamanho apra caber nos gráficos. A função `insert_break_line` serve para por o `<br>` nisso

```python
from math import floor

def insert_break_line(astring, index_point=5):
    splited = astring.split(' ')
    for i in range(floor(len(splited)/index_point)):
        splited.insert(index_point * (i+1), '<br>')
    return " ".join(splited).replace(' <br> ','<br>')
```

Como usar

```python
# Usado na parte de valor do `value_counts`
df_aux['Valor'] = df_aux['Valor'].apply(lambda x:  x if len(x.split(' ')) > 10 else insert_break_line(x) )
```



## CATEGORIC FEAT

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

### CAT BY CAT

```python
def get_percentage_complex(df1, df_origin, col_target):
    """
    Retorna a porcentage de um valor sobre o sum no dataframe original.
    Eh necessario fazer manulamente pois se não tiver todas as combinaçoes de cat feats
    ao fazer da forma automatica da erro. Entao, eh necessario para haver
    AS COMBINAÇÇOES CAT_FEAT CUJA CONTAGEM SEJA ZERO 
    """
    array = []
    df_sum = df_origin[col_target].value_counts().reset_index()
    df_sum.columns = [col_target, 'sum']
    for index, row in df1.iterrows():
        if(row['count'] != 0):
            v = 100 * (row['count'] / df_sum[ df_sum[col_target] == row[col_target]]['sum'].iloc[0])
        else:
            v = 0
        array.append(v)
    return array

def plotly_cat_to_cat(df, catx, cat2, title='', orderby_func=None):
    """
    Amabas devem ser cat feats
    orderby_func = muitas vezes a cat_feat eh ordenavel, use essa campos para designar a funcao
    TEM QUE VERIFICAR QUANDO NAO TEM TODAS AS CATEGORIAS, AI DA ERRO
    """
    cols = [catx, cat2]
    # Faz todas as combinações dos valores unicos de cada coluna
    # por conta disos, se hovuer nao houver a ocorrencia de uma dessa combinaçoes
    # a sua contagem de porcentagem tem que ser feita  de forma analogica 
    # na funcao 'get_percentage_complex'
    df_temp = df.groupby(cols).size().to_frame('count').reindex(
        pd.MultiIndex.from_product([df[catx].unique(), df[cat2].unique()]), fill_value = 0)
    df_temp = df_temp.reset_index().dropna()
    df_temp.columns = cols + ['count']
    
    df_temp['percentage'] = get_percentage_complex(df_temp, df, catx)
    df_temp['total'] = df_temp['percentage']
    df_temp.columns = cols + ['Counts', 'Percentage', 'Total']

    fig = px.bar(df_temp, x=catx, y=['Total'], color=cat2,
       category_orders=orderby_func, hover_data=['Counts'],
       text=df_temp['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)),
       title=title)
    fig.show()
```

Exemplo de Tratamento para por ordenaçao: Nesse caso queremos ordenar por faixa salarial, mas nao da pra ordenar de forama alfabetica, entao temos que designar a ordem

```python
mapping_faixa_salario_re = {
    'Menos de RS 1.000/mês': 1,
    'de RS 1.001/mês a RS 2.000/mês': 2,
    'de RS 2.001/mês a RS 3000/mês': 3,
    'de RS 3.001/mês a RS 4.000/mês': 4, 
    'de RS 4.001/mês a RS 6.000/mês': 5,
    'de RS 6.001/mês a RS 8.000/mês': 6,
    'de RS 8.001/mês a RS 12.000/mês': 7, 
    'de RS 12.001/mês a RS 16.000/mês': 8,
    'de RS 16.001/mês a RS 20.000/mês': 9,
    'de RS 20.001/mês a RS 25.000/mês': 10, 
    'de RS 25.001/mês a RS 30.000/mês': 11,
    'de RS 30.001/mês a RS 40.000/mês': 12,
    'Acima de RS 40.001/mês': 13,  
}

sort_by_faixa_salarial = {"('P2_h ', 'Faixa salarial')": list(mapping_faixa_salario_re.keys()) }

# Chamando a funçâo. Esse foi um caso especial do dataslack kaggle kernel
# em que tem que tratar os dados antes
cat_salary, cat_y = "('P2_h ', 'Faixa salarial')", "('P2_g ', 'Nivel')"
cols = [cat_salary, cat_y]

df_temp = df[cols].dropna()
df_temp[cat_salary] = df_temp[cat_salary].apply(
    lambda x: x.replace('R$', 'RS') )

plotly_cat_to_cat(
    df_temp,
    cat_salary, cat_y,
    'Faixa Salarial por Nivel',
    sort_by_faixa_salarial
)
```

![](G:\Personal Projects\DATA-SCIENCE-PROJECT\data-world\my-ds-standard\plots\plotly\imgs\plotly_cat_to_cat.png)





### CAT BY CAT KDE

```python
def plotly_kde_cat_to_cat(df, catx, caty, width=800, title='',
                          height=500, x_title='',
                          order_func=None):
    # source: https://www.kaggle.com/code/ceruttivini/cientista-ou-analista-de-dados-qual-a-diferen-a
    
    cols = [catx, caty]
    df_temp = df.groupby(cols).size().to_frame('count').reindex(
        pd.MultiIndex.from_product([df[catx].unique(), df[caty].unique()]), fill_value = 0)
    df_temp = df_temp.reset_index().dropna()
    df_temp.columns = cols + ['count']
    
    df_temp['percentage'] = get_percentage_complex(df_temp, df, catx)
    df_temp['total'] = df_temp['percentage']
    df_temp.columns = cols + ['Counts', 'Percentage', 'Total']
    
    if(order_func):
        df_temp['ordem'] = df_temp[catx].apply(lambda x: order_func(x))
        df_temp = df_temp.sort_values(['ordem', catx])
    
    fig = go.Figure()
    caty_values = list(df[caty].unique())

    for caty_val in caty_values:

        fig.add_trace(go.Scatter(
            y = df_temp[df_temp[caty] == caty_val]['Percentage'],
            x = df_temp[df_temp[caty] == caty_val][catx],
            text = df_temp[df_temp[caty] == caty_val]['Percentage'],
#             marker_color = df_temp[df_temp[caty] == caty_val]['Color'].iloc[0],
            name = caty_val,
            marker_size = 4.5, # tamanho do indicador que fica na linha
            textfont_size = 9, # tamanho da fonte dos textos
            line_shape='spline', # habilitar linhas suavizadas
            line_smoothing=0.8, # % de suavidade aplicada nas linhas
            orientation= 'v',
            customdata = round(df_temp[df_temp[caty] == caty_val]['Percentage'],2),
            hovertemplate= "%{customdata}% - %{x}<extra></extra>"
        ))

    fig.update_layout(
        title = '<b>' + title + '</b>',
        showlegend=True, # habilitar legenda
        plot_bgcolor = "#fff", # cor de fundo
        yaxis_showgrid = False, # remoção das linhas dos fundos do eixo y
        legend_yanchor="top", # posição da legenda
        legend_xanchor="left", # início do espaçamento da legenda
        legend_y=1.15, # espaçamento vertical da legenda
        legend_x= -0.1, # espaçamento horizontal da legenda
        legend_orientation="h", # orientação da legenda
        width = width,
        height = height,
        xaxis_title_text = x_title if x_title else catx, # titulo que fica ao lado do eixo x
        xaxis_title_font_color='grey',# cor do título que fica ao lado do eixo x
        xaxis_color='grey', # cor do eixo x
        yaxis_title_text = 'Percentage', # titulo que fica ao lado do eixo y
        yaxis_title_font_color='grey',# cor do título que fica ao lado do eixo y
        yaxis_color='grey', # cor do eixo y
        yaxis_showticksuffix = 'all', # habilitação de sufixo para eixo y
        yaxis_ticksuffix  ='%', # adição de "%" na label do eixo y se for porcentagem

    )

    fig.show()
    
```

```python
import plotly.graph_objects as go

def order_by_salary(x):
    return mapping_faixa_salario_re[x]
    
cat_salary, cat_y = "('P2_h ', 'Faixa salarial')", "('P2_g ', 'Nivel')"
cols = [cat_salary, cat_y]

df_temp = df[cols].dropna()
df_temp[cat_salary] = df_temp[cat_salary].apply(
    lambda x: x.replace('R$', 'RS') )

plotly_kde_cat_to_cat(df_temp, cat_salary, cat_y,
                      title='Faixa Salarial por Senioridade',
                      x_title='Faixa Salarial',
                      order_func=order_by_salary)
```

![](G:\Personal Projects\DATA-SCIENCE-PROJECT\data-world\my-ds-standard\plots\plotly\imgs\plotly_kde_cat_to_cat.png)

### SCATTER POLAR -> CAT BY CAT FILTERING

```python
def plotly_scatter_polar(df, catx, x_vals, caty, y_vals, title, range_=100):
    """
    Faz ScatterPolar de cat com cat, escolhendo cat values de X com y
    range eh tamanho do angulo, deve ser regulado para cada grafico em particular apos ver como fica em 100
    """
    # source: https://www.kaggle.com/code/ceruttivini/cientista-ou-analista-de-dados-qual-a-diferen-a
    
    adict_dfs = {}
    for xval in x_vals:
        df_start = df[ df[catx] == xval]
        df_aux = df_start[caty].value_counts().reset_index().rename(
            columns={'index': caty, caty: 'count'})
        df_aux['percent'] = 100 * (df_aux['count'] / df_start[caty].count())
        df_aux = df_aux[ df_aux[caty].isin(y_vals) ]
        # para fazer um contorno no formato de círculo é necessário
        # fazer a inclusão do primeiro valor como último
        df_aux = df_aux.append(df_aux.iloc[0,:])
        adict_dfs[xval] = df_aux
        
    fig = go.Figure()
    
    for key, value in adict_dfs.items():
        fig.add_trace(go.Scatterpolar(
            r=value['percent'],
            theta=value[caty],
            name=key,
            marker_size = 9.5, # tamanho dos indicadores das linhas (bolinhas)
            line_width=2.6, # grossura da linha da resposta,
            showlegend = True, # showlegend and len(self.polar_layout)+1 < 2, # opção de adicionar legenda para cada linha
            hoverinfo='r+theta+name', # padrão quando passar o mouse em cima
            customdata = value['count'],
            hovertemplate='%{r:0.0f}%<br>%{theta}<br>%{customdata}'
        ))
        
    fig_polar_layout = {
        "bgcolor":"white", # cor de fundo
        "radialaxis_visible":True, # apresentação da grid
        "radialaxis_showticklabels":True, # apresentação de texto da grid
        "radialaxis_tickfont_color":"darkgrey", # cor do texto da grid
        "radialaxis_layer":"below traces", # se a linha passa os pontos ou nao
        "radialaxis_gridcolor":"#d9d7d7", # cor da grid
        "radialaxis_tickangle": -350, # angular da label da grid
        "radialaxis_range":(0,range_),# intervalo da grid
        "radialaxis_tickvals":list(range(10,range_,10)),# intervalo do texto grid
        "radialaxis_ticktext":[ f"{t}%" if t % 20 == 0 else "" for t in range(10,range_,10)], # texto da grid 
        "radialaxis_tickfont_size" : 10, # fonte da grid
        "angularaxis_tickfont_size" : 14} # fonte das opções de resposta
    fig.update_layout(
        title=title,
        polar=fig_polar_layout
    )
    
    fig.show()
```

Usando

```python
x_col = "('P2_f ', 'Cargo Atual')"
x_vals = ['Cientista de Dados/Data Scientist',                      
'Analista de BI/BI Analyst/Analytics Engineer',               
'Analista de Dados/Data Analyst',                             
'Engenheiro de Dados/Data Engineer']   

y_col = "('P4_e ', 'Entre as linguagens listadas abaixo, qual é a que você mais utiliza no trabalho?')"
y_vals = ['Python', 'SQL', 'R', 'Java', 'Scala']


plotly_scatter_polar(df, x_col, x_vals, y_col, y_vals, 'Linguagens por Cargos', 85)
```

![](G:\Personal Projects\DATA-SCIENCE-PROJECT\data-world\my-ds-standard\plots\plotly\imgs\plotly_scatter_polar.png)

### Describe cat Feat filtering by others cat-feats in df

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

CUIDADO COM A ORDENAÇÃO: você pode criar uma coluna com a ordem, fazer um `sort` usando elas no df e assim vai sair ordenado

![](G:\Personal Projects\DATA-SCIENCE-PROJECT\data-world\my-ds-standard\plots\plotly\imgs\bar_plotly_describe_cat_feat_filter_cat_feats_values.png)

## NUMBER FEAT

### DESCRIBE NUMBER FEAT

```python
def plotly_number_feat_describe(df, number_col, rename_col='', title=''):
    """
    Pra uma coluna numerica cria: pandas.describe, histograma e violin plot
    """
    # DEFINE CONSTANTS
    rename_col = number_col if not rename_col else rename_col
    the_title = number_col if not title else title
    # Create Table
    adf = df[number_col].describe().reset_index().rename(
        columns={'index': 'Statistics', number_col: rename_col})
    interval = df[number_col].max() - df[number_col].min()
    adf.at[1,rename_col] = round(adf.at[1,rename_col], 2) # mean
    adf.at[2,rename_col] = round(adf.at[2,rename_col], 2) # std
    adf = adf.append({'Statistics': 'interval', rename_col: interval },
                     ignore_index = True)
    # CREATE SUBPLOT
    fig = make_subplots(
        rows=1, cols=3,
        vertical_spacing=0.01,
        specs=[[{"type": "table"},
                {"type": "bar"},
               {'type': 'violin'}]]
    )
    # FIG 1: PLOTLY TABLE
    fig.add_trace(
        go.Table(
            header=dict(
                values=list(adf.columns),
                fill_color='rgb(100, 31, 104)',
                align='left',
                font=dict(color='white', size=14),
            ),
            cells=dict(
                values=[adf['Statistics'], adf[rename_col] ],
                fill_color='rgb(230, 240, 240)',
                align='left'),
        ),
        row=1, col=1
    )
    # FIG 2 : HISTOGRAM PURE
    fig.add_trace(
        go.Histogram(
            x=df[number_col],
            marker=dict(color='rgb(120, 100, 202)'),
            name='Histogram',
        ),
        row=1, col=2
    )
    # FIG 3: VIOLIN PLOT
    fig.add_trace(
        go.Violin(
            y=df[number_col], 
            box_visible=True, 
            line_color='black',           
            meanline_visible=True, 
            fillcolor='rgb(129, 180, 227)', 
            opacity=0.6,
            x0=rename_col,
            name='Violin',
        ), row=1, col=3
    )
    # FIGURE CONFIGS
    fig.update_layout(
        width=900, height=500,
        title_text=the_title
    )
    fig.show()
    # use print(px.colors.sequential.dense) para gerar paleta de cores
```

```python
plotly_number_feat_describe(df, "('P1_a ', 'Idade')", 'Idade', 'Estatisticas Descritivas para a Idade')
```

![](G:\Personal Projects\DATA-SCIENCE-PROJECT\data-world\my-ds-standard\plots\plotly\imgs\plotly_number_feat_describe.png)

### NUMBER -> CAT FEAT

```python
def plotly_describe_numberf_by_catf(df, number_feat, cat_feat, title=''):
    title = number_feat + ' by ' + cat_feat if not title else title
    # dropnan pois se houver nao conegue por as cores corretamente
    # e tambem nao muda em nada, pois so faz o box de quem NAO TEM NAN
    cols = [number_feat, cat_feat]
    adf = df[cols].dropna(axis='index', subset=cols)
    # Box Plot
    fig = px.box(adf, 
         x=cat_feat, 
         y=number_feat,
         color=cat_feat,
        )
    # Configs
    fig.update_layout(
        title_text=title, title_x=0.5,
    )
    fig.show()
    
```

```python
plotly_describe_numberf_by_catf(df, "('P1_a ', 'Idade')", "('P2_g ', 'Nivel')", 'Idade por Nivel')
```

![](G:\Personal Projects\DATA-SCIENCE-PROJECT\data-world\my-ds-standard\plots\plotly\imgs\plotly_describe_numberf_by_catf.png)