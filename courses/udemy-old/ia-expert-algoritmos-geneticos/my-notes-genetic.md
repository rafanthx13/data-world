# My Notes - Algoritmos Genéticos

## Log

- **Data de Inicio**: 18/06/2018
- **Data de Fim**: 24/06/2018
- **Site Udemy**: https://www.udemy.com/algoritmos-geneticos-em-python/learn/v4/
- O curso é **Uma base para entrar em DeepLearning**, dando uma boa base de rede neurias simples e multicamada
- **Avaliação:** 



## IDE SPyder

- Depurar
  - Digite `F12` para por um momento em que fara a pausa. Apartir desse ponto, voce pode exeuctar passo a passo (asism, evita fazer tudo)
  - `CTRL+F10`: Executar linha por linha, semelhante ao Jupyter
  - Comece a Depurar e depois deixa em Continuar `CRL+F12` para ir executando direto até o ponto que voc eescolheu para parar
  - Limpe o campo de varaiveis quando for depurar e executar denovo
- **Atualizar quando terminar o curso o de rede neurais**
- Voce pode acessar  a aba `Ver` para gerencias as janelas que sâo mostradas a direita
- `CTRL+ENTER`

## Indivíduo/Cromossomo

+ Representam uma solução possivel para o problema
+ Chamado de cormossomo pois, como nos, cada itme da lsita defini a solução
+ **O indivíduo pode ser o próprio cromossomo (nesse caso, o problema é simples, ou pode conter o cromossomo como atributo**
+ **Exemplo**: No nosso exemplo, o inidivido tera o cromossomo com atributo
+ é interresante um inidivudo ser uma classe, de forma a ter uma coleçâo de informaçôes própria dele

## Função de Avaliação/fitness

+ Medida de qualidade par ao inividuo (a solução). Tambem chamada de Fitness.
+ No caso, queremos entâo por fim encontrar o indivíduo com max ou min fitness

## Op. Genético: Seleção

+ Para selecionar os pais, deveremos simular o processo de seleçâo natural:

  + **Indivíduos mais aptos terão chances maiores de reproduzir do que os menos aptos**

+ Perceba que é chance, e que, essa chance será proporcional a seu *fitness*

+ Se  privilegiar inidividuos com somente avaliação alta, não haverá diversidade, e, é essa diversidade que permmite o bom funcionamento de algoritmos genéticos.

+ **Método Roleta Viciada:** 

  + Imagina um gráfico de pizza (Círculo), dividido em pedaços, cada pedaço será proporcional ao fitness

  + O método da roleta é girála e escolher eses pedaço, da forma como ela foi definida anteriormente, então:

    + Indivíduos mais aptos terao mais chances de serem selecionados do que inidividuos menos aptos, ao mesmo tempo que não os descartamos

    ![](C:\Users\Rafael\Google Drive\Private Studies\Computer Advanced\udemy-Algoritmos-Geneticos\imgs\img02.png)



## Op. Genético : Reprodução/Crossover

+ Combina pedaços dos cromossomos, geranco, de dois pais e gera dois filhos
+ Na operação usada no udemy, é selecionado pontos de corte
+ A ideia é de ser fazer isso é, os individuos bons, vão ser selecionados e produzirao soluções que dendem a ter o fitness melhor que o dos pais
+ Questão de corte:
  + Imagine o Gene: 1|0|1|1|0|1, eu escolho um dos '|' e escolhe um dos lados (direita ou esquerda). Enfim, o lado escolhido é feito um swith gerando assim os dois filhos.
    + Perceba que esse é um método bem simples





## Op. Genético: Mutação

+ Serve para criar diversidade, mudando genes alertórios de forma aleartoria.
+ Não é algo que deva ser feito toda hora, como ocorre na natureza





## Algotimo Genetico: Esquema

![](C:\Users\Rafael\Google Drive\Private Studies\Computer Advanced\udemy-Algoritmos-Geneticos\imgs\img01.png)

+ No final, vai tender a  melhor soluçâo, mas, nâo quer dizer que é a melhor possivel para o problema
+ Observação: Uma coisa gritante é que, por conta da questão aleartória ocorre muito de os gráficos ficarem bem dispares de uma execuçâo para outra





## DEAP (Distributed Evolucionary)