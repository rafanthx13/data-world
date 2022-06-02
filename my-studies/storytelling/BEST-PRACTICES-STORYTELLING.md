# Dicas para bom Storytelling - DataViz



## Main Tips de Vídeos do Youtube



### Youtube Data Hacker #38 - Main Tips

+ DICA: O Storytelling não é um `pandas_profilling` você nao quer analise de todas as variáveis. **VOCE QUER CONTAR UM HISTÓRIA BEM CONTADA, FECHADA, INTERRESSANTE**
  - Mostre o que for interressante, se cruzar os dados e nao revelar nada de amis, entao nao coloca


+ DICA: Sempre que você descobriu algo incrivel, é bem capaz de você está olhando para um dado errado. CUIDADO COM OUTILIES

+ O que vocês acham uma história ser boa
  - Tem que se rengajadora. Voce tem que começar e quere ir até o fim
  - Históiria é igal piada, se tem que explicar demais emntâo é porque é ruim
  - Tem que gerar vontande do outroq quere contar a hist´ria para outra pessoa


DICAS VALIOSAS
+ TER UM PADRÂ ÚNICO DE COR. **PADRONIZAR CORES É IMPORTANTE**
+ Não mude o estilo dos gráficos nem ter gráficos muito diferentes
+ **ANDRE SINOK VENCEU USANDO SOMENTE UM TIPO DE GRÁFICO**
  + Pois basta ver o primeiro gráfico para entender todos os outros. 
  + **DICA ULTRA: POR ISSO, PARA PADROINZAR CORES, SERA NECESSÁRIO REMODELAR OS DADOS PARA ELIMINAR MUITAS FEAUTERS QUE FICARIA INÚTIL. EXEMPLO: LINGUAGES DE PROGRAMAÇAO PARA DATASCIENCE: DEIXE AS 5 PRINCIAPSI, SE HOUVER MAIS, JUNTE ELAS NUMA COISA SÓ**


Tentar falar de tudo numa só história
+ Menos é mais. Você não precisa falar de todos os insghts que os dados  dão. Agrupe e fala de um único conjunto só
+ Se tem muitas features, vá aos poucos
+ Uma história tem que ser escolhida e a ela dar destaque
+ É muito fácil se perder. O Sionek pegou uma história e a conta bem contada de um enorme volumes de *features*.


+ Ao fazer uma análise exploratória você pode ppor qualquer tipo de gráfico. Agora para apresentar precisa de algo mais trabalhado


+ **Há muita gente que não é capaz de fazer autocrítica. De pegar o seu comprar com os outros e ver os pros e contras. Já pensa que é superior porque é seu e pronto. Não é capaz de se por noa visão do outro que vai ler aquilo, LIRETALEMNTE**



### Youtube Live

+ Alan Senne - O foco é story telling

  + Contar historia por meio dos dados. 
  + Nâo quer textao e nem artigo cientifico
  + Fuja de formato de papaer e artigo cientifico.
  + Quermeos algo mais acessível de forma que: **UM LEIGO CONSEGUE LER E ENTENDER**

+ 43min00s: DICA DO QUE NAO FAZER Quem poe muito gráfico e nao escreve nada

  + ```
    A galera que faz 500 gráficos sem escplicar nada. Tipo, por todas as features. Isso nao vai ganhar.
    Menos é mais
    É capaz de que qquem ganahr, ganahr com um único gráfico com uma boa história por trás
    Se preocupe mais com a história que você está contando do que com o gráfico que está fazneod
    ```
    
  
+ 475min00s: Dicas do que fazer
  +  Ser sucinto com poucas visualizações. Lingueagem clara e objetiva
  + Plotly_Dash: Interavividade pode ser interressante
  + Ex: Um cara construiu uma calculadora de quanto seria o salario de um cientiista de dados com base nos dados. Contruiu e ganheou um premio em uma competiçao
  + Usar a pesquisa de 2019 antse da pandemia. 
  + Usar tambem a kaggle survey da propria kaggle. Pode ser que tenha algo ai de bom.
  + Olhar o relatório que a kaggle lança. Usar relatoriso do stackOverflow e Git: Lianugens, salarios e asism tirar alguma ideia do que fazer

**Dicas e ideias que eu tiro da live**

+ Henriquece os dados com mais informçaoes (outros dataset) (nao sei qual)
  + FGV, maro-enconomia, ibge, dados abertos. OPEN-DATA-BRASIL
  + Eles já fizeram uma versoa 2020, olhe a competiçâo apssada do data hackers
  + Comprara com ano anterior
+ **O QUE SERÁ AVALIADO É ORIGINIALIDADE E CRIATIVIDADE, POR ISSO USAR OUTROS DATA-SETS CONTA MUITO**
+ **Vai ganahr que propor boa historia e solucionar elas**
+ Pesquisa competiçoes de data-viz e storiy telling



## Dicas

+ Se você coloca informaçao que nâo dá pra ver, nao coloque
+ PiePlot deve tere poucuqissimas categorias
+ Variável Categóricas ordiniais podem ser convertidas para número para melhor visualização
  - Exmeplo: Faixa Salarial poderia ser simplificado para inteiro
+ **Padronize cor, principalemnte apquando o foco fa análise for em certaos valores/categorias**

+ Em StoryTelling contar uma boa história é a meta. Por isso você não precisa manter os dados puros, é claro, eles devem ser verdadeiros, por conta disso: **PODE-SE FAZER MODIFICAÇÔES (REPLACES E SHRINK)**
  - No DataSlak, na parte de faixa salarial, são 13 faixas

```
dicio_faixa_salarial = {
    "Menos de R$ 1.000/mês" : 1,
    "de R$ 1.001/mês a R$ 2.000/mês" : 2,
    "de R$ 2.001/mês a R$ 3000/mês" : 3,
    "de R$ 3.001/mês a R$ 4.000/mês" : 4,
    "de R$ 4.001/mês a R$ 6.000/mês" : 5,
    "de R$ 6.001/mês a R$ 8.000/mês" : 6,
    "de R$ 8.001/mês a R$ 12.000/mês" : 7,
    "de R$ 12.001/mês a R$ 16.000/mês" : 8,
    "de R$ 16.001/mês a R$ 20.000/mês" : 9,
    "de R$ 20.001/mês a R$ 25.000/mês" : 10,
    "de R$ 25.001/mês a R$ 30.000/mês" : 11,
    "de R$ 30.001/mês a R$ 40.000/mês" : 12,
    "Acima de R$ 40.001/mês" : 13
}
```

* Perceba alguns detalhes que poderia melhorar esse dado

* (LEGIBILDIADE) É ruim olhar essas faixas, são `strings` grandes, por isso 

* (QUANTIDADE DE FAIXAS): 13 categorias é muito para visualizar, seria melhor reduzir se possivel.

* (REPETIÇÂ) repete muito 'de' 'R$' '/mes'

* (**O que fazer para mudar**)
  - Ao analisar os dados e pensar numa proposta para apresentalos, as faixas acima de 20mil poderiam muito bem ser agrupdados, de "20k a 30k" e "30k a 40k"
      - ser 1k<; 1k-2k; 3k-4k para simplifiar
      
      

+ Todos os grandes storytellign escreveram muito mais em `markdown` do que em `python`

+ Omita detalhes técnicos. Os gráficos são como uma paida, devem ser auto-explicativos

+ **RETIRE TODOA INFORMAÇÂO INÚTIL DO GRÁFICO, MENOS É MAIS**
  - ![](https://images.squarespace-cdn.com/content/v1/56713bf4dc5cb41142f28d1f/1450306653111-70K5IT30R69NWPDIE1ZJ/data-ink.gif?format=750w)

+ Siga a metodologia STAR para qualquer StoryTelling

````
If you are asked a question when you are asked to tell about a past experience, you should frame the question using the STAR methodology. STAR is an acronym for (Situation, Task, Action, and Result).

Situation: What is the context to your story? Set the scene for your interviewer. Be sure to include who, what, when, where, and how of the situation. Provide enough context early on so that the interviewer will be able to follow your story

Task: Describe the task at hand and your involvement, keep it specific and concise and be sure to highlight the challenges with the task at hand.

Action: Describe what you did to accomplish the task. Specify skills, tools, characteristics, behaviors, and any conflicts.

Result: Share the outcome of the situation and specifically how you contributed to the outcome. 
````

## Trechos de Kernels para ter ideia do que escrever

+ Introdução de Kernel
  - https://www.kaggle.com/code/ceruttivini/cientista-ou-analista-de-dados-qual-a-diferen-a/notebook

````
Introdução

Com a popularidade da ciência de dados, várias pessoas estão buscando conhecimentos nesta área. Contudo, há uma quantidade enorme de informações disponibilizadas na internet referente a este assunto e isso pode gerar uma confusão desde termos técnicos até definição de papeis da área. Esta análise, tem como objetivo de mostrar a diferença entre uma posição de cientista e analista de dados utilizando dados da pesquisa do state of data 2021.

Aviso! Foi desconsiderado respondentes que se consideram desempregados, apenas estudantes, e que preferiram não informar a situação atual de trabalho.
````



+ Saindo de um tópico há outro
  - Fonte: https://www.kaggle.com/code/ericvpmendes/novos-talentos-um-estudo-sobre-pessoas-j-nior

```
# Exploração do conjunto de dados

"""
print(
O Júnior no Brasil é do gênero Masculino e possui 26 anos de idade.
Mora na região Sudeste, é formado em Computação / Engenharia de Software / Sistemas de Informação/ TI, e possui Graduação/Bacharelado.
)
"""

Chamo atenção para a questão de gênero:

\# MOSTRA GRÁFICO

Vamos começar respondendo à seguinte pergunta: quem é o júnior no Brasil?

\# Manutenção de bons funcionários júnior

Já vimos então quem são, e qual a importância da contratação de pessoas no nível júnior. Vamos ver agora o que valorizam e do que são críticos em uma empresa para que não sejam apenas atraídos, mas também sejam lapidados e bem geridos hoje, para se tornarem os gestores que a área de dados precisará amanhã

Note como a remuneração é o fator mais importante tanto para pessoas júnior como para pessoas sênior. Então nada de oferecer "salário emocional" só porque a pessoa está começando agora na carreira!

Chamo atenção também para como critérios que levam em conta crescimento profissional são dois dos três mais importantes para as pessoas de nível júnior. Noto em redes sociais corporativas por aí como algumas empresas ainda tem uma ideia chata e ultrapassada de que júnior só entra pra fazer o trabalho que um sênior não quer ou não pode.
```



# Andre Sionek Kernel Tips



## Andre Sionek Metodologia 

https://www.kaggle.com/code/andresionek/one-chart-many-answers-kaggle-surveys-in-slopes

+ AndreSinoek2020 - Venceu aplicando um filtro apra smente os profissionais nao dataset da kaggle. Fazer um recorte e conta ruma boa história é melhor do que um pairplot gignate
+ Renomeou todoas as variáveis, e deve também ter feito o replace já de início. Isso evitar ter que fazer preprocessamento a toda hora
+ Como inicia a bordagem de um tema

````
\# The Gender Gap

I wanted to start with something simple and important at the same time. So I questioned myself: over the past three years, did the proportion of Men and Women change? I knew there was a gap, but I would like to see it decreasing (and a lot) in the recent years.


--------- Code --------------
\#grafico
GenderProportionPlot(
    metric=metric,
    yaxes_title='% of Respondents per Survey Year',
    shared_yaxes=True,
    yticks=[20, 40, 60, 80],
    yticks_template='{}%',
    hover_template='%{y:0.1f}%',
    annotation_template='{:0.1f}%',
    x_nticks=3,
    title='<b>Gender Gap: Kaggle members are mostly men. </b><br>And there are no signs of increase in women participation since 2018.'\
          '<br><span style="font-size:14px;color:lightgrey"><i>Percentage of professional respondents per country</i></span>'
).show()
--------- /Code --------------

Unfortunately, there is a considerable gap in professionals participation in Kaggle: 84% of men against 16% of women.

And what is worse than that is that women participation did not increase over the past three years. I saw some other notebooks that showed an increase in female students. Maybe this will cause an increase in data professionals next year, but need a lot more women to close this gap.
Maybe Kaggle could host women only competitions, in a bid to attract more of them to the platform (and to Data Science).

If we zoom-in using the same chart, we can see which countries are getting more women into Data over the past few years.

--------- Code --------------
\#grafico
--------- /Code --------------
````




+ Ele primeiro aprsenta o gráfico e depois fala sbre ele

````
\#grafico

Jupyter/IPython is very popular with Beginners and Modern Data Scientists, and less popular with coders and ML Veterans. Interesting to note that regular use of Ipython is slowly decreasing over time an giving way to IDEs traditionally used by Software Developers. Here it's important to highlight the increase in Visual Studio adoption in 2020. I believe this movement is due to the native integration with notebooks released by mid 2020.

Do you wanna try a proper IDE that has all good features such as code-completion, variable inspection, debugging, etc and still work on your loved notebook environment? Then I suggest you follow the lead and give a try to Visual Studio Code.
````

## Andre Sionek Configurar plotly

+ Suas funções expecifica o retorno da tpipagem

````
def filter_question_columns(columns: List[str], question: str) -> List[str]:

select_questions(self) -> pd.DataFrame:

__init__(self) -> None:
````

+ **COMO SÃO SEUS GRÁFICOS**: Tudo é meio cinza clara, que tem pouco contraste com o branco. Ele faz isso  para que a informaçâo principal fique evidencianda pelas cores.
+ **PINTE TUDO DE QUASE BRANCO OU APAGA E DEIXA O PRINCIPAL COLORICO: !!!!!ABSOLEMTNATMEN TUDO""**

+ **TODO TEXTO EM PLOTLY É HTML, ENTAO, VOCÊ PODE POR ENTRE UMA DICV E CONFIGURAR O CSS**
 + AdnreSimok consegue titulos grandes fazendo isso

  - Exmeplo de por 3 titulos e progressivamente a cada '/' o texto fica mais fraco

    ```
    self.figure.add_annotation(
                xref="paper", 
                yref="paper",
                font=dict(
                    size=11,
                    color='lightgrey'
                ),
                align='left',
                x=-0.07, 
                xanchor='left',
                y=-0.13,
                yanchor='bottom',
                text='<b>Source:</b> Kaggle surveys from 2018 to 2020.',
                showarrow=False
            )
    ```



## Andre Sionek Markdown 

https://www.kaggle.com/code/andresionek/one-chart-many-answers-kaggle-surveys-in-slopes

Padronizaçao do markdown

````
<div style="font-family:Helvetica Neue; font-size:16px; line-height:1.7; color:slategray;">
    Each line in this chart represents a country. This information is available in the subtitle and also when you hover your mouse over the data points.

<img src="https://i.imgur.com/1g0LdeL.png" align="left" style="width:600px;"/>
    </div>
````

ALERT

````
<div style="font-family:Helvetica Neue; font-size:16px; line-height:1.7; color:slategray;">

<div class="alert alert-warning">
  <strong>Warning!</strong> For all charts in this study we applied a filter to select only Professionals (people who are actively working).
</div>
</div>
<br>
````

VERDE

````
<div class="alert alert-success">Maybe Kaggle could host women only competitions, in a bid to attract more of them to the platform (and to Data Science).</div>

<div class="alert alert-success"><b>Let's do something to close the gap?</b> <br>Give more opportunities for women to ingress data careers even if they don't have all the required experience. And please, pay women the same you pay men for consistent education level and experience.</div>
````

TRECHO MARKADO DE AMARELO

````
<mark>India is the country that is closing the gap faster</mark>
````

AZUL

````
<div class="alert alert-info">If there are more professionals available, their market price will drop. <b>Simple economics.</b></div>
````

## Mapemanto de valores, replaces e categorias

````python
from enum import Enum
import numpy as np


class Mapping(Enum):
    """
    Contains dicts mapping values found in the surveys to values we want to replace with.
    """
    COMPENSATION={ 
        '$0-999': '0-10k',
        '1,000-1,999': '0-10k',
 ',
        '300-400,000': '300-500k',
        '400-500,000': '300-500k',
        '500,000+': np.nan,
        'I do not wish to disclose my approximate yearly compensation': np.nan
    }
    JOB_TITLE={
        'Data Scientist': 'Data Scientist',
        'Software Engineer': 'Software Engineer',
        'Data Analyst': 'Data Analyst',
        'Other': 'Other',
        'Research Scientist': 'Research Scientist/Statistician',
        'Business Analyst': 'Business Analyst',
 
        'Principal Investigator': 'Research Scientist/Statistician',
        'Data Journalist': 'Other',
        'Currently not employed': 'Currently not employed', 
        'Student': 'Student'
    } 
    GENDER={
        'Male': 'Men',
        'Female': 'Women',
        'Man': 'Men',
        'Woman': 'Women',
        'Prefer not to say': np.nan, # Very few answers on those categories to do any meaningful analysis
        'Prefer to self-describe':  np.nan, # Very few answers on those categories to do any meaningful analysis
        'Nonbinary':  np.nan # Very few answers on those categories to do any meaningful analysis
    }
    AGE={
        '18-21': '18-21', 
        '22-24': '22-24', 
        '25-29': '25-29',

        '70+': '70+',
        '70-79': '70+',
        '80+': '70+'
    }
    EDUCATION={
        'Master’s degree': 'Master’s', 
        'Bachelor’s degree': 'Bachelor’s',
        'Some college/university study without earning a bachelor’s degree': 'Some college',
        'Doctoral degree': 'Doctoral',
        'Professional degree': 'Professional',
        'I prefer not to answer': np.nan,
        'No formal education past high school': 'High school'
    }
    YEARS_WRITING_CODE={
        '3-5 years': '3-5 years',
        '1-2 years': '1-3 years',
        '2-3 years': '1-3 years',
        '5-10 years': '5-10 years',

        'I have never written code': 'None',
        'I have never written code but I want to learn': 'None',
        '20-30 years': '10+ years',
        '30-40 years': '10+ years',
        '40+ years': '10+ years'
    }    
    YEARS_WRITING_CODE_PROFILES={
        '3-5 years': '3-10 years',
        '1-2 years': '1-2 years',
        '2-3 years': '2-3 years',
        '5-10 years': '3-10 years',

        'I have never written code': 'None',
        'I have never written code but I want to learn': 'None',
        '20-30 years': '10+ years',
        '30-40 years': '10+ years',
        '40+ years': '10+ years'
    } 
    RECOMMENDED_LANGUAGE={
        'Python': 'Python',
        'R': 'R',
        'SQL': 'SQL',
        'C++': 'C++',

        'Bash': 'Bash',
        'VBA': 'Other',
        'Go': 'Other',
        'Swift': 'Swift',
        'TypeScript': 'Other'
    } 
    LANGUAGES={
        'SQL': 'SQL', 
        'R': 'R', 
        'Java': 'Java', 

        'Javascript': 'Javascript/Typescript',
        'C': 'C/C++', 
        'TypeScript': 'Javascript/Typescript', 
        'C++': 'C/C++', 
        'Swift': 'Swift'
    }
    YEARS_USING_ML={
        '1-2 years': '1-3 years',
        '2-3 years': '1-3 years',
        '< 1 year': '< 1 year',

        '20 or more years': '5+ years',
        'I have never studied machine learning and I do not plan to': 'None'
    } 
    YEARS_USING_ML_PROFILES={
        '1-2 years': '1-2 years',

        '20 or more years': '10+ years',
        'I have never studied machine learning and I do not plan to': 'None'
    } 
    PRIMARY_TOOL={
        'Local development environments (RStudio, JupyterLab, etc.)': 'Local or hosted development environments',
        'Basic statistical software (Microsoft Excel, Google Sheets, etc.)': 'Basic statistical software',
        'Local or hosted development environments (RStudio, JupyterLab, etc.)': 'Local or hosted development environments',
        'Cloud-based data software & APIs (AWS, GCP, Azure, etc.)': 'Cloud-based data software & APIs',
        'Other': 'Other',
        'Advanced statistical software (SPSS, SAS, etc.)': 'Advanced statistical software',
        'Business intelligence software (Salesforce, Tableau, Spotfire, etc.)': 'Business intelligence software'
    }
    COUNTRY = {
        'India': 'India',
        'United States of America': 'United States',
    
        'Italy': 'Italy',
        'Nigeria': 'Nigeria',
        'Turkey': 'Turkey',
        'Australia': 'Australia'
    }
    IDE={
        'None': 'None', 
        'MATLAB': 'MATLAB', 
        'RStudio': 'RStudio', 

        ' Visual Studio / Visual Studio Code ': 'Visual Studio',
        '  Vim / Emacs  ': 'Vim/Emacs/Atom',
        'Visual Studio Code (VSCode)': 'Visual Studio'
    }
    CLOUD={
        'I have not used any cloud providers': 'None', 
        'Microsoft Azure': 'Azure',
       'Google Cloud Platform (GCP)': 'GCP', 
        'Amazon Web Services (AWS)': 'AWS',
       'IBM Cloud': 'IBM/Red Hat', 
        'Other': 'Other', 
        'Alibaba Cloud': 'Alibaba', 
        np.nan: 'None',
       ' Amazon Web Services (AWS) ': 'AWS', 
        ' Google Cloud Platform (GCP) ': 'GCP',
       ' Microsoft Azure ': 'Azure', 
        'None': 'None', 
        ' Salesforce Cloud ': 'Other',
       ' Red Hat Cloud ': 'IBM/Red Hat', 
        ' VMware Cloud ': 'Other', 
        ' Alibaba Cloud ': 'Alibaba',
       ' SAP Cloud ': 'Other', 
        ' IBM Cloud ': 'IBM/Red Hat', 
        ' Oracle Cloud ': 'Other',
       ' IBM Cloud / Red Hat ': 'IBM/Red Hat',
        ' Tencent Cloud ': 'Other'
    }
    ML_STATUS={ 
ing insights (but do not put working models into production)': 'Use ML for generating insights',
        np.nan: 'Do not use ML / Do not know',
    }
    ML_FRAMEWORKS={
        'None': 'None', 
        'Prophet': 'Prophet', 

 
        ' H2O 3 ': 'H2O', 
        ' MXNet ': 'Other'   
    }
    
    
class Category(Enum):
    COMPENSATION=[
        'Not Disclosed', '0-10k', '10-20k', '20-30k', '30-40k', '40-50k', '50-60k', 
        '60-70k', '70-80k', '80-90k', '90-100k', '100-125k', '125-150k', '150-200k', 
        '200-250k', '300-500k'
    ]
    JOB_TITLE=[
        'Other', 'Manager/C-level', 'Product/Project Manager', 'Business Analyst', 'Data Analyst', 
        'Research Scientist/Statistician', 'Data Scientist', 'Machine Learning Engineer', 
        'Data Engineer/DBA', 'Software Engineer'
    ]  
    GENDER = ['Women', 'Men'] 
    AGE=['18-21', '22-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-69', '70+']
    YEARS_WRITING_CODE=['None', '< 1 year', '1-3 years', '3-5 years', '5-10 years', '10+ years']
    YEARS_USING_ML=['None', '< 1 year', '1-3 years', '3-5 years', '5+ years']
    SURVEY_YEAR=[2018, 2019, 2020]
    EDUCATION=['High school', 'Some college', 'Professional', 'Bachelor’s', 'Master’s', 'Doctoral']
    PROFILES=['Beginners', 'Others', 'Modern DS', 'Coders', 'ML Veterans']

COLORS = {
    'India': '#FE9933', 
    'Brazil': '#179B3A',
    'United States': '#002366', 
    'China': '#ED2124', 
    'Average': 'blueviolet',
    'Canada': '#F60B00',
    'Data Scientist': '#13A4B4',
    'Product/Project Manager': '#D70947',
    
}
````
