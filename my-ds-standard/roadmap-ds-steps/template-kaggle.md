# Como fazer Kaggle Kernels Templates

## Titulo

<h1 align="center"> User Cars: EDA and Regression </h1>

<img src="https://mystrongad.com/MTS_MillerToyota/MTS_Interactive/Used/Used-Car-Toyota.png" width="50%" />

Created: 2020-09-01

Last updated: 2020-09-01

Kaggle Kernel made by 🚀 <a href="https://www.kaggle.com/rafanthx13"> Rafael Morais de Assis</a>


## Kaggle Description

````
/## Kaggle Description

/### Data Description

/### The Goal

/### File Description

/### DataSet Description
````

## TOC

````
\## Table Of Content (TOC) <a id="top"></a>

\## Import Libs and DataSet
````

=======================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

import warnings
warnings.filterwarnings("ignore")

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Configs
pd.options.display.float_format = '{:,.4f}'.format
sns.set(style="whitegrid")
plt.style.use('seaborn')
seed = 42
np.random.seed(seed)
random.seed(seed)

========================================================================

sns.set_palette("Set3") 
\# default seabon: deep || default matplotlib: tab10 || Set1, Set2, Set3, Paired, muted, Accent, Spectral, CMRmap # https://medium.com/@morganjonesartist/color-guide-to-seaborn-palettes-da849406d44f


sns.set(style="whitegrid")
\# https://python-graph-gallery.com/104-seaborn-themes/
\# Ohters Themes: darkgrid, whitegrid, dark, white, and ticks

========================================================================

file_path = '/kaggle/input/wine-reviews/winemag-data_first150k.csv'
df = pd.read_csv(file_path)
print("DataSet = {:,d} rows and {} columns".format(df.shape[0], df.shape[1]))

print("\nAll Columns:\n=>", df.columns.tolist())

quantitative = [f for f in df.columns if df.dtypes[f] != 'object']
qualitative = [f for f in df.columns if df.dtypes[f] == 'object']

print("\nStrings Variables:\n=>", qualitative,
      "\n\nNumerics Variables:\n=>", quantitative)

df.head()
=======================================================================

dfs = df.describe(include='all').T.fillna('').rename(columns={'freq': 'freq of top'})
dfs['dtypes'] = df.dtypes
dfs['Missing'] = df.isnull().sum().values
dfs

=======================================================================


## ORDEM

+ Titulo
  - date created, last update, languages, author
+ Kaggle Descripiton
+ Abstract
  - Para ser mais entendível é necessário, eu achei, ter um asbtract como o de um artigo. Ele terá: descriçâo do dataset, o significado de cada linha (nao é features, é row mesmo). O que foivisto, como foi resolvido, métrico, cuirosidesde do processo e por fim a pontuaçâo final e como foi feita
+ Brief Summary (data-length) of dataset
  - em formato de tabela markdown
  - Se for muito grande, nao colocar
+ TableOfContent

---

**Conclusion**

🇺🇸

🇧🇷

-- script

https://medium.com/@researchplex/the-easiest-way-to-convert-jupyter-ipynb-to-python-py-912e39f16917

convert .ipynb to .html

ipython nbconvert — to script abc.ipynb 

convert .ipynb to .py

ipython nbconvert us-police-shooting-eda-with-maps-visualisation.ipynb --to python


## Ter em cada subtitulo

MEDICAL COST

+ [Import Libs and DataSet](#index01) 
+ [Snippets](#index02)
+ [EDA](#index03)
  - [Each feature individually](#index03)
  - [Each Feauture with 'charges'](#index04)
  - [Analyze feature crossover](#index05)
  - [Conclusions of EDA](#index06)
+ [Pre-Processing](#index07)
+ [Correlation](#index08)
+ [Split in Train and Test](#index09)
+ [Develop Models](#index10)
  - [Cross Validation](#index11)
  - [Fit Models](#index12)
  - [Test Models](#index13)
  - [Bests Models](#index14)
+ [Feature Importance](#index15)
+ [Hyperparameter Tuning Best Model](#index16)
+ [Evaluate Best Model to Regression](#index20)
+ [Conclusion](#index25)

+ [Import Libs and DataSet](#index01) 
+ [Snippets](#index02)
+ [Data Cleaning](#index03)
+ [EDA](#index04)
  - [Each feature Individually](#index04)
  - [Target by Features](#index05)
  - [Target by cross Features](#index06)
  - [EDA conclusions](#index50)
+ [Pre-Processing](#index07)
+ [Correlations](#index08)
+ [Split in train and Test](#index09)
+ [Develop Models](#index10)
  - [Prepare ML Models and Training](#index33)
  - [Cross Validation](#index11)
  - [Fit Models](#index12)
  - [Test Models](#index13)
  - [Bests Models](#index14)
+ [Feature Importance](#index15)
+ [Evaluate Best Model to Regression](#index20)
+ [Conclusion](#index25)

+ [Import Libs and DataSet](#index01) 
+ [Snippets](#index02)
+ [Undestand DataSet](#index03)

----

Target by Feaute
+ Year: The bigger the year tends to be the higher the price
+ Name: Some Names values more than others
+ Location: Coimbatore and Bangalore has more than others
+ Fuel_Type: Diesel has more price than PEtrol, and the others have few examples to check better
+ Kilometers_Driven: Few Influence
+ Milege: Few Influence
+ Engine: Linear Infleunce
+ Power: Linear INfluence
+ Seats: Has2 places has more mean than others

Target by cross Features
+ Transmission: Tem influencia em Power, a parrtir de Power 200 so ha tramnissao automatica e tem os maiores preços. Ocorre de forma parecida com Engine. Analsisando 4 features nuemricas (Engine, Power, Mileage, Kilometres_Drive) vemos que ser transmisaao automatiac da de acrra um grande preço



df['message'] = df['message'].apply(lambda x: clean_contractions(x, contraction_mapping))

df['message'] = df['message'].apply(lambda x: correct_spelling(x, mispell_dict))

df['new_message'] = df['message'].apply(clean_message)

df['new_message'] = df['new_message'].apply(lambda x: lematizer(x))

+ [1. Intro to NLP](#index01)
  - [1.1 Theory: Intro to NLP](#index02)
  - [1.2 Exercise: Basic Text Processing with Spacy](#index03)
+ [2. Text Classification](#index04)
  - [2.1 Theory: Text Classification with SpaCy](#index05)
  - [2.2 Exercise: Natural Language Classification](#index06)
+ [3. Word Embedding](#index07)
  - [3.1 Theory: Word Embedding](#index08)
  - [3.2 Exercise: Vectorizing Language](#index09)


+ [Import Libs and DataSet](#index01)
+ [Snippets](#index02)
+ [Data Cleaning](#index03)
+ [EDA](#index04)
  - [Each feature individually](#index05)
  - [Feature by Target: Response](#index06)
+ [Corr](#index07)
  - [Corr to PolicySalesChannel as Categorical Feature](#index08)
  - [Corr to RegionCode as Categorical Feature](#index09)
  - [All Corr](#index10)
+ [Pre-Processing](#index11)
+ [Split Train and Test](#index12)
+ [Handle Unbalanced DataSet](#index13)
+ [Develop Model](#index14)
  - [CV, Fitting and Testing](#index15)
  - [CatBoost](#index16)
  - [Super Leaner](#index17)
+ [Submission](#index18)
+ [Conclusion](#index19)

0	de RS 8.001/mês a RS 12.000/mês	479
1	de RS 4.001/mês a RS 6.000/mês	403
2	de RS 6.001/mês a RS 8.000/mês	393
3	de RS 12.001/mês a RS 16.000/mês	263
4	de RS 3.001/mês a RS 4.000/mês	183
5	de RS 2.001/mês a RS 3000/mês	180
6	de RS 16.001/mês a RS 20.000/mês	129
7	de RS 1.001/mês a RS 2.000/mês	126
8	de RS 20.001/mês a RS 25.000/mês	62
9	de RS 25.001/mês a RS 30.000/mês	43
10	de RS 30.001/mês a RS 40.000/mês	38
11	Acima de RS 40.001/mês	34
12	Menos de RS 1.000/mês	32



<a id="top"></a>

<a id='index02'></a> <a href="#top" class="btn btn-primary btn-sm" role="button" aria-pressed="true" style="color:white; margin-left: 20px;" data-toggle="popover">Go to TOC</a>

<span style='font-size: 15pt'>Analyse_dangerous_measurements_of_each_pollutant</span>


--------------

### Feedback
This Kernel is still under development. I would highly appreciate your feedback for improvement and, of course, if you like it, please upvote it!



<a id='index01'></a> <a href="#top" style="background-color: #20beff; border: none; color: white;  padding: 15px 30px;  font-family: sans-serif;  border-radius: 12px;  text-align: center;  text-decoration: none;  display: inline-block;  font-size: 16px;  margin: 4px 2px;  cursor: pointer;" >Go to TOC</a>

+ [Import Libs and DataSet](#index01) 
+ [Snippets](#index02)
+ [Data Cleaning](#index03)
+ [EDA](#index04)
  - [Each feature Individually](#index04)
  - [Target by Features](#index05

+ [Import Libs](#index01) 
+ [Snippets](#index02)
+ [Import DataSet](#index03)
+ [Import GeoJson Of World](#index04)
+ [EDA: Map of Count Medals on World](#index05)
+ [Web Scraping of Country Population](#index06)
+ [EDA: Medals by Population](#index07)

----------

EXEPLO DE TÍTULO = Time Series AnALYSIS kAGGLE (Grande exemplod e bem estilizado)

# <p style="background-color:skyblue; font-family:newtimeroman; font-size:180%; text-align:center">TimeSeries 📈 ARIMA, Prophet, ADF, PACF... 📚 Beginner to Pro</p>

# <p style="background-color:skyblue; font-family:newtimeroman; font-size:150%; text-align:center">3. Feature engineering 🔧</p>
