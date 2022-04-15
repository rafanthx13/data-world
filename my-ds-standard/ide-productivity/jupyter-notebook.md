# Jupyter Notebook Tips & Best Practices

## Links



+ https://www.codingem.com/jupyter-notebook-tricks/

## Convert .ipyn to html

 jupyter nbconvert --to html notebook.ipynb 

## Jupyter ShortCuts

### 

+ `A`: adiciona em cima
+ `B`: Adiciona em baixo
+ `DD`: Deleta
+ `ENTER`: Entra para editar a célula
+ `ESC`: Sai do modo de editar para o de navega??o 
+ `M`: celula Markdown
+ `Y`: celula Code
+ Press key `**x**` — Cut the selected cell(s)
  Press key `**c**` — Copy the selected cell(s)
  Press key `**v**` — Paste the selected cell(s)

**Novos comandos**

+ `CTRL+SHIFT+-` : Dividi a c?lula em 2 no ponto que est? o cursor
+ `SHIFT+M`: junta c?lulas
+ `ESC+F`: Find e Replace nas c?lulas

**Help**

+ Documenta??o do comando: `SHIT+TAB` sobre o m?todo/atrr

**Curiosos**

+ M?ltiplos cursores
  + Aperte `ALT`, arraste com bot?o-esquerdo (clique normal) pelas linhas de c?digo (o curso vai virar uma cruz), vai ficar marcado; solte e comece a escrever
    + Infelizmente nao tem como seleciona exatamente cada lugar das linhas
    + Ou pega na n-posii?ao de todas elas, ou, no final de todas elas
+ `;` Imprimir gr?fico
  + Ao invez de `plt.scatter(x,y)` fa?a `plt.scatter(x,y);` colocando `;` pois em gr?ficos as vezes mostra o tipo de objeto que sai, e n?o queremos isso

**Principais**

+ Exec Cell: `SHIFT + ENTER`
+ Exec and Insert Below: `ALT + ENTER`
+ Insert Cell Below: `ESC + B | B + B (in cell)`
+ Insert Cell Above: `ESC + A | A + A (in cell)`

**Pandas Configs**

+ ```
  pd.set_option('display.max.rows', 3000)
  pd.set_option('display.max.columns', 30)
  pd.set_option('display.max_colwidth', 200)
  ```

  

## Magic Commands on Jupyter

Acess shell (!)

```
!pip install Tkinter
```



```
# Print the current working directory
%pwd

# Show all the files in the current directory
%ls

%cd #change working directory
%ls #show contents in the current directory

# Change the working directory
%ls [PATH_TO_DIR]

# List all the variables
%Who  
%who
% who_ls

%debug — to debug a single line of code; OR
%%debug — to debug the whole cell

%%time
for ...
# retorna tempo de executar a celula

# %load imports.py
$load o que fz: ele ler arquivo python e crrega o seu codigo na celular em que est?

%matplotlib inline
```

### %%

```
%history ? print input history
%lsmagic ? list currently available magic functions
%magic ? print information about the magic function system
%matplotlib ? setting up matplotlib to work interactively
```



## Libs to improve and optimize jupyter

### NbExtentions

```
pip install jupyter_contrib_nbextensions

 jupyter contrib nbextension install 
```

**Comment/Uncomment Hotkey**

ALT + C: COMENTA E DESCOMENTA CÓDIGO, USANDO '#' e colocando um espacinho a mais

**Notify**

+ Serve para mandar uma notificaçâo no browser avisando que um processo acabou quando ele passar mais de x segundos. 
 - Coloque o máximo, assim vai mandar a notificaçâoq uando algo grande tiver completado, com mais de 30 segunods

## Que extesao colocar

+ Autopep8

  + /prettify the contents of code cells

  +  na celula `Alt+A` | `ALT+SHIF+A` no codigo todo

  + ```
    pip install autopep8
    ```

    

+ CodeFolding e no editor

  + Se por exemplo, a classe py tiver muito grande, voce pode colapsala. para apenas uma unica linha ()

+ Collapsible Heading

  + Memsa coisa que o anterio, mas para heading de markdown e todas as celuals abaixo dele.
  + bom para notebooks grnades

+ Execute Time

  + Quanto tempo gasta as celuas.
  + MUITO BOM

+ Hinterland / Tabnine

  + Auto Complete

+ hIDE HEADER

  + Esoncde abre o header com `CLTR+H`. Ulti para aproveitar mais expa?o
  + Para por tudo v? em  `View` e ative `Toogle Header` e `Toogle Toolbar`. A toolbar ? a mia simporantte

+ Move Select Cell

  + Alt Up e Down no modo navega?ao nas celulas

+ Noitify

  + Notifica quando uma execu?ao demora demais e ela acaba

+ Skip trace-back

  + Pula aqueles erros gigantes

+ table_beautifur

+ variavle inspector

  + Evitar ter que debugar muita coisa

+ Snippets

+ Table of contens (2)

  + TOC muito bom

  ----

  ## Popular extensions

  - **Scratchpad —** This is awesome. It allows you to create a temporary cell to do quick calculations without creating a new cell in your workbook. This is a huge time saver!
  - **Hinterland** — This enables a code autocompletion menu for every keypress in a code cell instead of just with tab
  - **Snippets** — Adds a drop-down menu to insert snippet cells into the current notebook.
  - **Autopep8** — This is a tool that automatically formats Python code to conform to the PEP 8 style guide. It’s so handy! Make sure you have run `pip install autopep8 --user` on your local machine. This will make sure you’re following the correct python coding conventions.
  - **Split Cells Notebook** — Enables split cells in Jupyter notebooks. Enter command mode and use `Shift + S` to toggle the current cell to either a split cell or full width.
  - **Table of Contents** — This extension enables you to collect all running headers and display them in a floating window, as a sidebar, or with a navigation menu.
  - **A Code Prettifier —** Cleans up, formats, and indents your code, so you don’t have to.
  - **Notify —** This displays a desktop notification when your kernel becomes idle. This is awesome when you’re running code that takes more than a couple of seconds to complete.
  - **Code Folding —** While in edit mode, a triangle appears in the gutter to fold your code. Good when you have large functions you want to hide for readability.
  - **Zen mode —** Makes things a bit less cluttered. Make sure to turn off the backgrounds in the settings.

## `pixiedust`: debuger jupyter

**N?o consegui colcoar**

Para usar coloque no início:

import pixiedust

E na linha que for usálo:

%%pixie_debugger

[link](https://medium.com/ibm-watson-data-lab/the-visual-python-debugger-for-jupyter-notebooks-youve-always-wanted-761713babc62)


ENTER: Edita a célula
B: Adiciona celular embaixo
A: Adiciona celula em cima





. PixieDust uses pyspark; a Python binding for Apache Spark. PixieDust includes a command-line utility for installing new kernels that use pyspark. The command-line utility walks you through the steps of configuring your kernel as well as installing Apache Spark





## Temas para o jupyter

https://github.com/dunovank/jupyter-themes

### Install with pip

```
# install jupyterthemes
pip install jupyterthemes

# upgrade to latest version
pip install --upgrade jupyterthemes
```

### Install with conda

```
# install jupyterthemes
conda install -c conda-forge jupyterthemes

# update to latest version
conda update jupyterthemes
```

Listar temas

```
! jt -l
```

Mudar tema

```
! jt -t chesterish
```

**VOCE TEM QUE REINICAR TODO O JUPYTER**

Restaurar tema

```
!jt -r
```

Outras coisa que pode fazer

```
Changing the font: !jt -t solarizedd -f fira -fs 115

Adjusting cell width: !jt -t chesterish -cellw 90% -linech 170

Cursor width and colour: !jt -t oceans16 -cursc r -cursw 5
```

Exemplo que um cara usa

**Nao costei de nenhum deesse, tem muito zoom**

select theme

- jt -t monokai

I use below setting-

- jt -t monokai -f fira -fs 10 -nf ptsans -nfs 11 -N -kl -cursw 2 -cursc r -cellw 95% -T

I saw that Ashraf Khan used the below setup:
`$ jt -t monokai -f fira -fs 10 -nf ptsans -nfs 11 -N -kl -cursw 2 -cursc r -cellw 95% -T`

but I used the setup:
`$ jt -t monokai -f fira -fs 13 -nf ptsans -nfs 11 -N -kl -cursw 5 -cursc r -cellw 95% -T`





Esse mostra cada coisa

```
jt -t onedork -T -N
```

where `-T` is toolbar visible and `-N` is name & logo visible (you can even display the kernel logo by adding `-kl` to the code above)
