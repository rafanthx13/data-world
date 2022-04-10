# Lib missigno

### Instalação

````
pip install missingno
````

### Link do Git

https://github.com/ResidentMario/missingno

Para mais exemplos, consulte aki.



### Ideia para tratar dados

mapear valores inválidos para null

+ No DW_Clientes quero saber se os dados são ou não válidos. Infelizmente, os dados são categóricos.

+ O missigno trata dados `null` mas não vai saber a diferença entre 'algo' e '-1' pois na algar, -1 indica que é inválido como `Null`.

  **Solução:** Mapear para cada coluna todos os valores possíveis e analisar um por um qual deles indica que é `null` e converter o `dataframe` para `null`.