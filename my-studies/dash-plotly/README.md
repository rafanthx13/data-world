# Dash + Plotly: Construindo DashBoards com Python

## Links

**Links Officiais**

+ Documentação: https://dash.plotly.com/

**Cursos**

+ Udemy - Python Interactive Dashboards with Plotly Dash (4h25min) [down]
  - url: https://www.udemy.com/course/python-interactive-dashboards-with-plotly-dash/

## Instalar Dash + Plotly

```bash
pip install dash # criar dashboards com plotly a partir de codigo python
pip install dash-bootstrap-components # bootstrap css para dash
pip install jupyter-dash # é possível ter os graficos interativos no jupyter
```

## Dicas para uso do Dash + Plotly

+ `help(dash.Dash)`: caso houver alguma duvida

+ Comandos antigos. Substitua:

  + ```
    `import dash_html_components as html` por `from dash import html`
    `import dash_core_components as dcc` por `from dash import dcc`
    ```

    

## Detalhes importatnes

+ **Gráficos Interativos**: Semelhante ao PowerBI, permite acrecentar a opçâo de mudar o parametro e assim gerar graficos dinamicos. Econozmia por excmplo, se tenhpo 50 cidade, e quereo fazer umaa analise de preço de casa, ao invez de fazer um grafico com 50 colunas, ou, fazer 50 graficos, eu uso o dash e coloca essa cidade como um `input` do graficos. **ECONOMIZA TEMPO E ESPAÇO**
+ **`jupyter-dash`**: É possível gerar esse gráfico interativo direto no Jupyter notebook
  + [Artigo Medium - jupyter-dash](https://medium.com/plotly/introducing-jupyterdash-811f1f57c02e)
+ **Deploy no Heroku**: Como o server é feito em falsk, dá pra fazer o deploy no heroku. Além disso é possível adicionar autenticaçâo simples (HTML Auth: user e senha HTML) especificando user/pass validos no codigo (infelsimtne teria que passar o codigo de user/pass validos )
+ **Extensão VSCode**: Existe extensão do plotly + Dash com snippets para gerar os princiapsi compoentnes
  + A lista dos snippets estão no link a seguir:  [MarketPlace VSCode](https://marketplace.visualstudio.com/items?itemName=PlotlyDashSnippets.plotly-dash-snippets)
+ **Dash-BootStrap-Components**:
  + Permite fazer um SideBar com menu, ou seja, links de navegação. [link](https://dash-bootstrap-components.opensource.faculty.ai/examples/simple-sidebar/)
+ Hot Reload: Dash uses “***Hot-reloading\***” which enables developers to see their code changes automatically in browser. Note that you must include the following line of code in your application ‘*app.run_server(debug=True)*’ 





## Curso 1 - Udemy - Python Interactive Dashboards with Plotly Dash (4h25min) [down]

url: https://www.udemy.com/course/python-interactive-dashboards-with-plotly-dash/

### Exemplo 01 - Primeio Dash + Plotly

````python
import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div('My Dashboard')

if __name__ == '__main__':
    app.run_server(debug=True)
````

Cria um dashboard com 2 coisas

+ 1 - Uma `div` simples com `my dashboard`
+ 2 - um botao embaixo de debugar

Ao executar esse codigo python tem a seguinte saida:

````
Dash is running on http://127.0.0.1:8050/

 * Serving Flask app '010 creating_your_first_dashboard' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
````

![](G:\Personal Projects\DATA-SCIENCE-PROJECT\data-world\my-studies\dash-plotly\udemy-python-interactive-dashboards-with-plotly-dash\example-01.png)

Vai subir um, e acessadno você tem o dashboard como uma webpage interativa.

**Está no modo auto-reload, basta mudar o arquivo que vai recarrega na hora as mudanças**

### Exemplo 02 - Escrevendo mais html

```python
import dash
from dash import html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='World Happiness Dashboard'),
    html.P(['This dashboard shows the happiness score.',
            html.Br(),
            html.A('World Happiness Report Data Source',
                   href='https://worldhappiness.report/',
                   target="_blank")])])

if __name__ == '__main__':
    app.run_server(debug=True)

```

![](G:\Personal Projects\DATA-SCIENCE-PROJECT\data-world\my-studies\dash-plotly\udemy-python-interactive-dashboards-with-plotly-dash\example-02.png)

### Exemplo 03 - Elementos interativos mais estáticos

Nesse terceiro exemplo é porto alunss itens de interaçao que ainda nao interragem:

RadionButton; Checklist; dropdowne até mesmo um gráfico.

Élido um scsv com padnas e feito uma manipulação

```python
import dash
from dash import html
from dash import dcc
import pandas as pd
import plotly.express as px

happiness = pd.read_csv('world_happiness.csv')

region_options = [{'label': i, 'value': i} for i in happiness[
    'region'].unique()]
# Formato dos dados
# [{'label': 'Australia', 'value': 'Australia'},
#  {'label': 'New Zealand', 'value': 'New Zealand'},
#  {'label': 'Albania', 'value': 'Albania'},
#  {'label': 'Armenia', 'value': 'Armenia'},

country_options = [{'label': i, 'value': i} for i in happiness[
    'country'].unique()]
# Formato dos dados
# [{'label': 'Australia and New Zealand', 
#   'value': 'Australia and New Zealand'},
#  {'label': 'Central and Eastern Europe',
#   'value': 'Central and Eastern Europe'},

line_fig = px.line(happiness[happiness['country'] == 'United States'],
                   x="year", y="happiness_score",
                   title='Happiness Score in the USA')

app = dash.Dash()

app.layout = html.Div([
    html.H1('World Happiness Dashboard'),
    html.P(['This dashboard shows the happiness score.',
            html.Br(),
            html.A('World Happiness Report Data Source',
                   href='https://worldhappiness.report/',
                   target="_blank")]),
    dcc.RadioItems(options=region_options, value='North America'),
    dcc.Checklist(options=region_options, value=['North America']),
    dcc.Dropdown(options=country_options, value='United States'),
    dcc.Graph(figure=line_fig)])

if __name__ == '__main__':
    app.run_server(debug=True)
    
```

![](G:\Personal Projects\DATA-SCIENCE-PROJECT\data-world\my-studies\dash-plotly\udemy-python-interactive-dashboards-with-plotly-dash\example-03.png)

O que é `happiness[happiness['country'] == 'United States']` que gera açinha

```
 .  country	region	happiness_rank	happiness_score	year
450	United States	North America	15	7.119	2015
451	United States	North America	13	7.104	2016
452	United States	North America	14	6.993	2017
453	United States	North America	18	6.886	2018
454	United States	North America	19	6.892	2019
455	United States	North America	17	6.939	2020
```

Perceba, está constante para `United States`

### Example 04 - Input e Output

```python
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='input-text', value='Change this text', type='text'),
    html.Div(children='', id='output-text')
                       ])

# Faz o bind entre 'ids' e 'propriedades'
# @app.callback é um decorator que atua na função 'update_output_div'
# Ele especifica a entrada e a saida (entra value-de-input, sai no children-da-div)
# A entrada é o parametro da funçâo, e o que sai é o retorno da função
@app.callback(
    Output(component_id='output-text', component_property='children'),
    Input(component_id='input-text', component_property='value')
)
def update_output_div(input_text):
    return f'Text: {input_text}'


if __name__ == '__main__':
    app.run_server(debug=True)
    

```

![](G:\Personal Projects\DATA-SCIENCE-PROJECT\data-world\my-studies\dash-plotly\udemy-python-interactive-dashboards-with-plotly-dash\example-04.png)

### Exemplo 05 - Grafico interativo com dropwdonw

Com fazer: atribui id no gtafico (saida) e no dropdown) entrada 

```python
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

happiness = pd.read_csv('world_happiness.csv')

country_options = [{'label': i, 'value': i} for i in happiness[
    'country'].unique()]

app = dash.Dash()

app.layout = html.Div([
    html.H1('World Happiness Dashboard'),
    html.P(['This dashboard shows the happiness score.',
            html.Br(),
            html.A('World Happiness Report Data Source',
                   href='https://worldhappiness.report/',
                   target="_blank")]),
    # Diff de antes: aqui é adicionado ID no dropdown e Graph
    dcc.Dropdown(id='country-dropdown',
                 options=country_options,
                 value='United States'),
    # diff de antes: figure começa vazio pois esse figure é criada dinamicamente por update_graph
    dcc.Graph(id='happiness-graph', figure={})])


## esse app.callback faz :
# 1. linca entrada e saida aos elementos hmtl
# 2. gera o grafico randomicamente a depender de 'selected_country' que é outro nome para a propriedade de entrada 'o value de country-dropdown'
# 3. a saida sera a pro figure do graph
# é feito o grafico dinamentico denro da funçao. Assim, quando mudar a entrda, cria um novo graficao, cqd
@app.callback(
    Output(component_id='happiness-graph', component_property='figure'),
    Input(component_id='country-dropdown', component_property='value'))
def update_graph(selected_country):
    filtered_happiness = happiness[happiness['country'] == selected_country]
    line_fig = px.line(filtered_happiness,
                       x='year', y='happiness_score',
                       title=f'Happiness Score in {selected_country}')
    return line_fig


if __name__ == '__main__':
    app.run_server(debug=True)

```

![](G:\Personal Projects\DATA-SCIENCE-PROJECT\data-world\my-studies\dash-plotly\udemy-python-interactive-dashboards-with-plotly-dash\example-05.png)

### Exemplo 06 - Grafico interativo com multiplas entrdas e saidas

**É necessário a entrda e saida da função está na ordem definida na chamada do `@app.callback`**



```python
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

happiness = pd.read_csv('world_happiness.csv')

country_options = [{'label': i, 'value': i} for i in happiness[
    'country'].unique()]
data_options = [{'label': 'Happiness Score', 'value': 'happiness_score'},
                {'label': 'Happiness Rank', 'value': 'happiness_rank'}]


app = dash.Dash()

app.layout = html.Div([
    html.H1('World Happiness Dashboard'),
    html.P(['This dashboard shows the happiness score.',
            html.Br(),
            html.A('World Happiness Report Data Source',
                   href='https://worldhappiness.report/',
                   target="_blank")]),
    dcc.Dropdown(id='country-dropdown',
                 options=country_options,
                 value='United States'),
    dcc.RadioItems(id='data-radio',
                   options=data_options,
                   value='happiness_score'),
    dcc.Graph(id='happiness-graph'),
    html.Div(id='average-div')])


@app.callback(
    Output('happiness-graph', 'figure'), # 1ª output : return line_fig
    Output('average-div', 'children'), # 2ª output: f'The average ...'
    Input('country-dropdown', 'value'), # 1ª input : selected_country
    Input('data-radio', 'value')) # 2ª input: selected_data
def update_graph(selected_country, selected_data):
    filtered_happiness = happiness[happiness['country'] == selected_country]
    line_fig = px.line(filtered_happiness,
                       x="year", y=selected_data,
                       title=f'{selected_data} in {selected_country}')
    selected_avg = filtered_happiness[selected_data].mean()
    return line_fig, f'The average {selected_data} for {selected_country} is {selected_avg}'


if __name__ == '__main__':
    app.run_server(debug=True)

```

![](G:\Personal Projects\DATA-SCIENCE-PROJECT\data-world\my-studies\dash-plotly\udemy-python-interactive-dashboards-with-plotly-dash\example-06.png)

### Exemplo 07 - Encademaneto de callbacks

O que muda de antes: agora tem um radio button que muda o dropwodwn que por sua vez muda a figure de acordo com a figura

Isos acaontece por **ENCADEMANETO DE CALLBACKS**: A saida de uma callback vai afetar a entraadad de outra callback

obs: só de mudar o radio button vai mudar a entrada de pais automaticamente

**O que diferen de antes: é adicionado um radiobutton que ler o continete, e a escolha de continete vai afetar o pais mostrado**

[]

```python
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

happiness = pd.read_csv('world_happiness.csv')

region_options = [{'label': i, 'value': i} for i in happiness[
    'region'].unique()]
data_options = [{'label': 'Happiness Score', 'value': 'happiness_score'},
                {'label': 'Happiness Rank', 'value': 'happiness_rank'}]


app = dash.Dash()

app.layout = html.Div([
    html.H1('World Happiness Dashboard'),
    html.P(['This dashboard shows the happiness score.',
            html.Br(),
            html.A('World Happiness Report Data Source',
                   href='https://worldhappiness.report/',
                   target="_blank")]),
    dcc.RadioItems(id='region-radio',
                   options=region_options,
                   value='North America'),
    dcc.Dropdown(id='country-dropdown',
                 options=[],
                 value=''),
    dcc.RadioItems(id='data-radio',
                   options=data_options,
                   value='happiness_score'),
    dcc.Graph(id='happiness-graph'),
    html.Div(id='average-div')])


# relacao radio-button com a escolha de pais
# FILTRA PAIS DE ACORDO COM O CONTINETE
@app.callback(
    Output('country-dropdown', 'options'),
    Output('country-dropdown', 'value'),
    Input('region-radio', 'value'))
def update_dropdown(selected_region):
    filtered_happiness = happiness[happiness['region'] == selected_region]
    country_options = [{'label': i, 'value': i} for i in
                       filtered_happiness['country'].unique()]
    return country_options, country_options[0]['value']


@app.callback(
    Output('happiness-graph', 'figure'),
    Output('average-div', 'children'),
    Input('country-dropdown', 'value'),
    Input('data-radio', 'value'))
def update_graph(selected_country, selected_data):
    filtered_happiness = happiness[happiness['country'] == selected_country]
    line_fig = px.line(filtered_happiness,
                       x="year", y=selected_data,
                       title=f'{selected_data} in {selected_country}')
    selected_avg = filtered_happiness[selected_data].mean()
    return line_fig, f'The average {selected_data} for {selected_country} is {selected_avg}'


if __name__ == '__main__':
    app.run_server(debug=True)

```

![](G:\Personal Projects\DATA-SCIENCE-PROJECT\data-world\my-studies\dash-plotly\udemy-python-interactive-dashboards-with-plotly-dash\example-07.png)

### Exemplo 08 - Avocado Example - Porque graficos interativos são bons

Com o csv `avocado.csv` e comparando o dashboar com o `.ipynb` pomdeo perceber que: **Com graficos interativos sâo bons para um mesmo dao para parametros difenrete**.

Por exemplo; o  objetivo é ver a varaioçao de preço do avocado orgaizo e convenciaol. Acontece que há 50 cidae; ao **invez de fazer 50 graficos, um grafico interativo já bastatria**

```python
# Step 1: Exploring the dataset
# The columns that will be used are: date, average_price, type, and geography


# Step 2: Preparing to build the Dash app
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

avocado = pd.read_csv('avocado.csv')

app = dash.Dash()


# Step 3: Building the layout
app.layout = html.Div(children=[
    html.H1(children='Avocado Prices Dashboard'),
    dcc.Dropdown(id='geo-dropdown',
                 options=[{'label': i, 'value': i}
                          for i in avocado['geography'].unique()],
                 value='New York'),
    dcc.Graph(id='price-graph')
])


# Step 4: Adding the callback function
@app.callback(
    Output(component_id='price-graph', component_property='figure'),
    Input(component_id='geo-dropdown', component_property='value')
)
def update_graph(selected_geography):
    filtered_avocado = avocado[avocado['geography'] == selected_geography]
    line_fig = px.line(filtered_avocado,
                       x='date', y='average_price',
                       color='type',
                       title=f'Avocado Prices in {selected_geography}')
    return line_fig


# Step 5: Running the dashboard
if __name__ == '__main__':
    app.run_server(debug=True)

```

![](G:\Personal Projects\DATA-SCIENCE-PROJECT\data-world\my-studies\dash-plotly\udemy-python-interactive-dashboards-with-plotly-dash\example-08.png)

### Examplo09 - CSS inline nos componentes HTML

```
import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd

soccer = pd.read_csv('fifa_soccer_players.csv')

player_name_options = [{'label': i, 'value': i} for i in soccer[
    'long_name'].unique()]

app = dash.Dash()

app.layout = html.Div([
    html.H1('Soccer Players Dashboard',
            style={'textAlign': 'center',
                   'fontFamily': 'fantasy',
                   'fontSize': 50,
                   'color': 'blue'}),
    html.P(['Source: ',
            html.A('Sofifa',
                   href='https://sofifa.com/',
                   target="_blank")],
           style={'border': 'solid'}),
    html.Label('Player name: '),
    dcc.Dropdown(
        options=player_name_options, value=player_name_options[0][
            'value'],
        style={'backgroundColor': 'lightblue'})],
    style={'padding': 100, 'border': 'solid'})

if __name__ == '__main__':
    app.run_server(debug=True)

```

![](G:\Personal Projects\DATA-SCIENCE-PROJECT\data-world\my-studies\dash-plotly\udemy-python-interactive-dashboards-with-plotly-dash\example-09.png)

### Exemplo 10 - CSS do bootstrap

prinpais comandos

```
import dash_bootstrap_components as dbc
..
app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])
```

**obs**: You should note that the keys in the style dictionary are **camelCased** — i.e. the *text-align* CSS property will be *textAlign* within Dash.

![](G:\Personal Projects\DATA-SCIENCE-PROJECT\data-world\my-studies\dash-plotly\youtube-articles-projects\youtube-hashtag\img-01.png)

```python
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import pandas as pd

soccer = pd.read_csv('fifa_soccer_players.csv')

player_name_options = [{'label': i, 'value': i} for i in soccer[
    'long_name'].unique()]

app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])

app.layout = html.Div([
    html.H1('Soccer Players Dashboard'),
    html.P(['Source: ',
            html.A('Sofifa',
                   href='https://sofifa.com/',
                   target="_blank")]),
    html.Label('Player name: '),
    dcc.Dropdown(
        options=player_name_options,
        value=player_name_options[0]['value'])
])

if __name__ == '__main__':
    app.run_server(debug=True)

```

![](G:\Personal Projects\DATA-SCIENCE-PROJECT\data-world\my-studies\dash-plotly\udemy-python-interactive-dashboards-with-plotly-dash\example-10.png)

### Exemplo 11 - Usando GridLaout do BootStrap

prinapcias comandos

```
# usar componente do dash_bootstrap_components as dbc
# e asism criar o layout
dbc.Row([
dbc.Col(
```



```python
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import pandas as pd

soccer = pd.read_csv('fifa_soccer_players.csv')

player_name_options = [{'label': i, 'value': i} for i in soccer[
    'long_name'].unique()]

app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])

app.layout = html.Div([
    html.H1('Soccer Players Dashboard'),
    dbc.Row([
        dbc.Col(
            html.P(['Source: ',
                    html.A('Sofifa',
                           href='https://sofifa.com/',
                           target="_blank")
                    ])
        ),
        dbc.Col([
            html.Label('Player name: '),
            dcc.Dropdown(
                options=player_name_options,
                value=player_name_options[0]['value'])
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)

```

![](G:\Personal Projects\DATA-SCIENCE-PROJECT\data-world\my-studies\dash-plotly\udemy-python-interactive-dashboards-with-plotly-dash\example-11.png)

### Exemplo 12 - RangeSlider, Choropleth e DataTable

Usano um csv de eletricidade temos 3 componentes

+ RangeSlider de anos, do min ao max do dataset
+ Choropleth : mapa do EUA, e o mapa é clicável
+ DataTable = ao clicar num estado americanos, voce pode ver os seus dados filtrados pelo ano do slicer

```python
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_table
import plotly.express as px
import pandas as pd

electricity = pd.read_csv('electricity.csv')

year_min = electricity['Year'].min()
year_max = electricity['Year'].max()


app = dash.Dash(external_stylesheets=[dbc.themes.SOLAR])

app.layout = html.Div([
    html.H1('Electricity Prices by US State'),
    dcc.RangeSlider(id='year-slider',
                    min=year_min,
                    max=year_max,
                    value=[year_min, year_max],
                    marks={i: str(i) for i in range(
                        year_min, year_max+1)}
                    ),
    # o grafico choropleth tem o atributo 'clickData' que permite capturar o clique no estado
    dcc.Graph(id='map-graph'),
    dash_table.DataTable(
        id='price-info',
        columns=[{'name': col, 'id': col} for col in electricity.columns]
        )
])


# callback do slicer para o mapa
@app.callback(
    Output('map-graph', 'figure'),
    Input('year-slider', 'value'))
def update_map_graph(selected_years):
    filtered_electricity = electricity[(
        electricity['Year'] >= selected_years[0]) & (electricity['Year'] <= selected_years[1])]
    avg_price_electricity = filtered_electricity.groupby('US_State')['Residential Price'].mean().reset_index()
    map_fig = px.choropleth(avg_price_electricity,
                            locations='US_State', locationmode='USA-states',
                            color='Residential Price', scope='usa',
                            color_continuous_scale='reds')
    return map_fig

# callback do mapa, slicer para datatable
@app.callback(
    Output('price-info', 'data'),
    Input('map-graph', 'clickData'),
    Input('year-slider', 'value'))
def update_datatable(clicked_data, selected_years):
    if clicked_data is None:
        return []
    us_state = clicked_data['points'][0]['location']
    filtered_electricity = electricity[
        (electricity['Year'] >= selected_years[0]) &
        (electricity['Year'] <= selected_years[1]) &
        (electricity['US_State'] == us_state)]
    return filtered_electricity.to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)

```

![](G:\Personal Projects\DATA-SCIENCE-PROJECT\data-world\my-studies\dash-plotly\udemy-python-interactive-dashboards-with-plotly-dash\example-12.png)



## Curso 2 - Udemy - Interactive Python Dashboards with Plotly and Dash

Jose Portilla - 9h43min - EN - Down



link do git com repo dos códigos: https://github.com/Pierian-Data/Plotly-Dashboards-with-Dash

O zip é o repo sem a parte de plots basicos de plotly

### Eventos e interação do usuário

#### Hover

Só de passa o mouse, alem de aparecer o hover no scatterplot, aparece tambem a imagem por hover

```python
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import base64

app = dash.Dash()

df = pd.read_csv('../data/wheels.csv')

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

app.layout = html.Div([
    html.Div([
    dcc.Graph(
        id='wheels-plot',
        figure={
            'data': [
                go.Scatter(
                    x = df['color'],
                    y = df['wheels'],
                    dy = 1,
                    mode = 'markers',
                    marker = {
                        'size': 12,
                        'color': 'rgb(51,204,153)',
                        'line': {'width': 2}
                        }
                )
            ],
            'layout': go.Layout(
                title = 'Wheels & Colors Scatterplot',
                xaxis = {'title': 'Color'},
                yaxis = {'title': '# of Wheels','nticks':3},
                hovermode='closest'
            )
        }
    )], style={'width':'30%', 'float':'left'}),

    html.Div([
    html.Img(id='hover-image', src='children', height=300)
    ], style={'paddingTop':35})
])

@app.callback(
    Output('hover-image', 'src'),
    [Input('wheels-plot', 'hoverData')])
def callback_image(hoverData):
    wheel=hoverData['points'][0]['y']
    color=hoverData['points'][0]['x']
    path = '../data/images/'
    return encode_image(path+df[(df['wheels']==wheel) & \
    (df['color']==color)]['image'].values[0])

if __name__ == '__main__':
    app.run_server()

```

![](G:\Personal Projects\DATA-SCIENCE-PROJECT\data-world\my-studies\dash-plotly\udemy-interactive-python-dashboards-with-plotly-and-dash\imgs\example-01.png)

#### Click

A imagem só aparece apos clica

```python
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import base64

app = dash.Dash()

df = pd.read_csv('../data/wheels.csv')

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

app.layout = html.Div([
    html.Div([
    dcc.Graph(
        id='wheels-plot',
        figure={
            'data': [
                go.Scatter(
                    x = df['color'],
                    y = df['wheels'],
                    dy = 1,
                    mode = 'markers',
                    marker = {
                        'size': 12,
                        'color': 'rgb(51,204,153)',
                        'line': {'width': 2}
                        }
                )
            ],
            'layout': go.Layout(
                title = 'Wheels & Colors Scatterplot',
                xaxis = {'title': 'Color'},
                yaxis = {'title': '# of Wheels','nticks':3},
                hovermode='closest'
            )
        }
    )], style={'width':'30%', 'float':'left'}),

    html.Div([
    html.Img(id='click-image', src='children', height=300)
    ], style={'paddingTop':35})
])

@app.callback(
    Output('click-image', 'src'),
    [Input('wheels-plot', 'clickData')])
def callback_image(clickData):
    wheel=clickData['points'][0]['y']
    color=clickData['points'][0]['x']
    path = '../data/images/'
    return encode_image(path+df[(df['wheels']==wheel) & \
    (df['color']==color)]['image'].values[0])

if __name__ == '__main__':
    app.run_server()

```

Faz a mesma coisa que o caso do *hover* mas com click

#### Selected data

permite usar o recuro de box select / lasso select do plotly para selecionar alguns pontos e mostrar seus dados como json ao lado

```python
#######
# This shows the mpg.csv dataset as a spread out scatter plot
# that sends hoverData to another graph via callback, and to
# a Markdown component through a second callback.
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from numpy import random

app = dash.Dash()

df = pd.read_csv('../data/mpg.csv')

# Add a random "jitter" to model_year to spread out the plot
df['year'] = df['model_year'] + random.randint(-4,5,len(df))*0.10

app.layout = html.Div([
    html.Div([   # this Div contains our scatter plot
    dcc.Graph(
        id='mpg_scatter',
        figure={
            'data': [go.Scatter(
                x = df['year']+1900,  # our "jittered" data
                y = df['mpg'],
                text = df['name'],
                hoverinfo = 'text',
                mode = 'markers'
            )],
            'layout': go.Layout(
                title = 'mpg.csv dataset',
                xaxis = {'title': 'model year'},
                yaxis = {'title': 'miles per gallon'},
                hovermode='closest'
            )
        }
    )], style={'width':'50%','display':'inline-block'}),
    html.Div([  # this Div contains our output graph and vehicle stats
    dcc.Graph(
        id='mpg_line',
        figure={
            'data': [go.Scatter(
                x = [0,1],
                y = [0,1],
                mode = 'lines'
            )],
            'layout': go.Layout(
                title = 'acceleration',
                margin = {'l':0}
            )
        }
    ),
    dcc.Markdown(
        id='mpg_stats'
    )
    ], style={'width':'20%', 'height':'50%','display':'inline-block'})
])

@app.callback(
    Output('mpg_line', 'figure'),
    [Input('mpg_scatter', 'hoverData')])
def callback_graph(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    fig = {
        'data': [go.Scatter(
            x = [0,1],
            y = [0,60/df.iloc[v_index]['acceleration']],
            mode='lines',
            line={'width':2*df.iloc[v_index]['cylinders']}
        )],
        'layout': go.Layout(
            title = df.iloc[v_index]['name'],
            xaxis = {'visible':False},
            yaxis = {'visible':False, 'range':[0,60/df['acceleration'].min()]},
            margin = {'l':0},
            height = 300
        )
    }
    return fig

@app.callback(
    Output('mpg_stats', 'children'),
    [Input('mpg_scatter', 'hoverData')])
def callback_stats(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    stats = """
        {} cylinders
        {}cc displacement
        0 to 60mph in {} seconds
        """.format(df.iloc[v_index]['cylinders'],
            df.iloc[v_index]['displacement'],
            df.iloc[v_index]['acceleration'])
    return stats

if __name__ == '__main__':
    app.run_server()

```

![](G:\Personal Projects\DATA-SCIENCE-PROJECT\data-world\my-studies\dash-plotly\udemy-interactive-python-dashboards-with-plotly-and-dash\imgs\example-03.png)

#### Hover revela outro gráfico



### automaticamente recarregar `dcc.Interval`

Apartir de `dcc.Interval` consigo recarregar informaçoes, asism pego informaçoes mais atualizadas

no exemplo a seguir, epga dados de avioes ao redor do mundo. Isos é atualizada a todo momento. Colocamos o `dcc.Interval` para ser de 6 segundos.

```python
#######
# This script will make regular API calls to http://data-live.flightradar24.com
# to obtain updated total worldwide flights data.
# ** This version continuously updates the number of flights worldwide,
#    AND GRAPHS THOSE RESULTS OVER TIME! **
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import requests

app = dash.Dash()

app.layout = html.Div([
    html.Div([
        html.Iframe(src = 'https://www.flightradar24.com', height = 500, width = 1200)
    ]),

    html.Div([
    html.Pre(
        id='counter_text',
        children='Active flights worldwide:'
    ),
    dcc.Graph(id='live-update-graph',style={'width':1200}),
    dcc.Interval(
        id='interval-component',
        interval=6000, # 6000 milliseconds = 6 seconds
        n_intervals=0
    )])
])
counter_list = []

@app.callback(Output('counter_text', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_layout(n):
    url = "https://data-live.flightradar24.com/zones/fcgi/feed.js?faa=1\
           &mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&stats=1"
    # A fake header is necessary to access the site:
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = res.json()
    counter = 0
    for element in data["stats"]["total"]:
        counter += data["stats"]["total"][element]
    counter_list.append(counter)
    return 'Active flights worldwide: {}'.format(counter)

@app.callback(Output('live-update-graph','figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph(n):
    fig = go.Figure(
        data = [go.Scatter(
        x = list(range(len(counter_list))),
        y = counter_list,
        mode='lines+markers'
        )])
    return fig

if __name__ == '__main__':
    app.run_server()

```

### Autorização para acessar dashboard

`dash_auth` e define hardcode user/pass

```python
import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

USERNAME_PASSWORD_PAIRS = [
    ['JamesBond', '007'],['LouisArmstrong', 'satchmo']
]

app = dash.Dash()
auth = dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)

app.layout = html.Div([
    dcc.RangeSlider(
        id='range-slider',
        min=-5,
        max=6,
        marks={i:str(i) for i in range(-5, 7)},
        value=[-3, 4]
    ),
    html.H1(id='product')  # this is the output
], style={'width':'50%'})

@app.callback(
    Output('product', 'children'),
    [Input('range-slider', 'value')])
def update_value(value_list):
    return value_list[0]*value_list[1]

if __name__ == '__main__':
    app.run_server()

```



### Deploy heroku

Semelhante a qualquer projeto flask. Leia pdf



