# Google Colab Tips

### ShortCuts

+ Add Cell Down : CTRL + M + B
+ Add Cell Up : CTRL + M + A
+ Delete Cell : CTRL + M + D
+ Exec Cell: CTRL + ENTER / SHIFT + ENTER
+ Code to Text : CTRL+ M + Y
+ Text to Code : CTRL + M + M

## Links

+ https://www.kdnuggets.com/2020/06/google-colab-deep-learning.html

## Porque usar Colab

There are several benefits of using Colab over using your own local machines. Some of the benefits of Colab are

+ You do not require to do an environment setup. It comes with important packages pre-installed and ready to use.
+ Provides browser-based Jupyter Notebooks.
+ Free GPU
+ Store Notebooks on Google Drive
+ Importing Notebooks from Github
+ Document code with Markdown
+ Load Data from Drive

## Hardware Selection (GPU or TPU)

Colab’s biggest advantage is that it provides free support to GPU and TPU. You can easily select GPU or TPU for your program by Runtime > Change runtime type.

## Como saber se tem CPU Pytorch


````python
# check
torch.cuda.is_available()

# use
device = 'cuda' if torch.cuda.is_available() else 'cpu'
device

#send data to cpu/tpu/gpu
regressor.to(device)
````

**Processamento da rede**

````python
for epoch in range(2000):
    ...
    for i, data in enumerate(train_loader):
        inputs, labels = data
		# indica para usar cuda
        inputs, labels = inputs.to(device), labels.to(device)
	...

````

**Pegando dados que estão sendo usado na GPU**

````python
# colocando dadaso para serem prcessados pela GPU
previsores = previsores.to(device)
# Aplicando a rede neural
previsoes = regressor.forward(previsores)
# tirando da gpu e pegando
previsoes.cpu().detach().numpy()
````

## Instalar pip packages

````python
!pip install skorch
````

## Fazer Upload de Arquivos

A pasta raiz no FyleSystem do Colab é content, entâo, para acessar após um simples upload na raiz é 

````python
previsores = pd.read_csv('/content/entradas_breast.csv')
classe = pd.read_csv('/content/saidas_breast.csv')
````

LINK : https://medium.com/@tuewithmorris/google-colab-notebooks-keyboard-shortcuts-aa6a008fb91b

### Acessar a MV
+ A VM (Virtual Machine) é linux, você pode executar comandos linux nela pelo Colab através de !.

````python
!head train.csv
!apt-get install libgeos-3.5.0
!apt-get install libgeos-dev
!pip install https://github.com/matplotlib/basemap/archive/master.zip

````

### Acessar o GDrive
 Acessar o seu Drive para pegar os arquivos

````python
from google.colab import drive
drive.mount('/content/drive')
````
Vai abrir um link, pelo qual você acessa com sua conta Google
Depois, você pega  um codigo_de_autorizaçâo e insere embaixo
No final,, deve ter na pasta /content/drive/ as coisas do seu drive



