# Lib pandas-profiling

**O que faz:** Gera relatório sobre o data frame de forma profissional. Combinando com uma limpeza pelo `missingo` podemos tirar vários *insights* sobre a usabilidade de *features*

### Instalação

```
pip install pandas-profiling

conda install pandas-profiling
```

#### Importando

`import pandas_profiling`

##### Link do Git

https://github.com/pandas-profiling/pandas-profiling

##### Exemplo real de como sai

http://nbviewer.jupyter.org/github/JosPolfliet/pandas-profiling/blob/master/examples/meteorites.ipynb

Para mais exemplos, consulte aki.

##### Usando no Jupyter

````python
# Gera na linha de output
pandas_profiling.ProfileReport(df) 

# Salvar o Arquivo (HTML)
pfr = pandas_profiling.ProfileReport(df)
pfr.to_file("/tmp/example.html")
````



