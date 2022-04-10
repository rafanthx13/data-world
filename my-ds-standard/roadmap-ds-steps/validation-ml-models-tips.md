---------------------------------------------------------------

### Resumo do `classification_report` e `confusion_matrix`

````

Matrix de Confusao    Nomenclatura das partes
 [[65  3]              [[TP  FP ]
 [ 3 29]]              [ FN  TN]]
 
-------------------------------------------------------

               precision    recall  f1-score   support

Not Purchased       0.96      0.96      0.96        68
    Purchased       0.91      0.91      0.91        32

     accuracy                           0.94       100
    macro avg       0.93      0.93      0.93       100
 weighted avg       0.94      0.94      0.94       100
 
-------------------------------------------------------
 
    Métricas por Classe 
    
OBS: É a matriz de confusâo particular para cada classe
    
Precision: Numero total de positivos do total dos classificados como posititovos par uma classe
    Precision = TP / TP + FP
    
Recall: Número de Positivos que foram devidamente identificados par auma classe
    Recall = TP / TP + FN
    
F1-Score: Média Harmonica entre precisao e recall
    F1-Score = 2 * Recall * Precision / Recall + Precision
    
Support: Quantidade de itens por classe
    Support = TP + FP
    
    Métricas Geral
    
Acurracy: O quanto acertou do total
    TP + TN / TP + FP + FN + TN
    

````

---------------------------------------------------------------



## Forma normal de divir a base, classificar a de teste e avaliar

A forma mais normal que fazemos, dividimos a base treinamentos com uma e com a outra testamos

````python
### WHERE
## "classificador" é o classificador do SciKItLearning
## "previsores" é um numpy.array das features
## "classe" é um numpy.array das classes

# DIVIDIR A BASE
from sklearn.model_selection import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(
    previsores, classe, test_size=0.25, random_state=0)

# CLASSIFICADOR E TREINAMENTO
classificador = ...Classify()
classificador.fit(previsores_treinamento, classe_treinamento)
previsoes = classificador.predict(previsores_teste)

# AVALIANDO
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
precisao = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)
print("Accuracy\n", precisao, "\n")
print("Matrix de Confusao\n",matriz, "\n")
print("Matrix de Confusao Porcentagem\n",matriz/matriz.sum(), "\n")
print(classification_report(classe_teste,previsoes))
````

---------------------------------------------------------------

## Fazer Cross Validation

````python
# Com Scikit-learning você só precisa do classificador e das bases
# separadas. O cross_val vai retornar a acurácia/precisão para cada cv
# Depois dissovocê tira a média e o desvio padrâo
# .mean(): É o valor final mesmo
# .stv(): QUanto maior significa que a escolha de dados de teste/train # 	impcataram muito na nota
### WHERE
## "classificador" é o classificador do SciKItLearning
## "previsores" é um numpy.array das features
## "classe" é um numpy.array das classes
from sklearn.model_selection import cross_val_score
resultados = cross_val_score(classificador, previsores, classe, cv = 10)
````
---------------------------------------------------------------

## StratifiedKFold

==> Em artigos científicos geralmente é feito 30 testes. Um corss validation com K=10 variando 3 vezes o seed

````python
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score, confusion_matrix
kfold = StratifiedKFold(n_splits = 10, shuffle = True, random_state = 3)

resultados = []
matrizes = []
for indice_treinamento, indice_teste in kfold.split(previsores,
                                                    np.zeros(shape=(previsores.shape[0], 1))):
    # print('==>Índice treinamento: ', indice_treinamento, '\n Índice teste: ', indice_teste)
    classificador = GaussianNB()
    classificador.fit(previsores[indice_treinamento], classe[indice_treinamento]) 
    previsoes = classificador.predict(previsores[indice_teste])
    precisao = accuracy_score(classe[indice_teste], previsoes)
    matrizes.append(confusion_matrix(classe[indice_teste], previsoes))
    resultados.append(precisao)

# Fazemos a média das 10 matrizes de confunsão em uma só
matriz_final = np.mean(matrizes, axis = 0)
print(matriz_final)

resultados = np.asarray(resultados)
print(resultados.mean())
print(resultados.std())

--------------------------------------------------------------------

## HyperParams GridSearchCV

````python

# Get Classify
from sklearn.ensemble import RandomForestClassifier
classify = RandomForestClassifier()

# Get all HyperParameters to tuning
classify.get_params().keys()

# Chose params to tuning
param_grids = {'criterion': ['gini', 'entropy'], 'max_depth': [2, 4, 6, 8]}

# 
from sklearn.model_selection import GridSearchCV

# scoring pode mudar, é a métrica para escolher o melhor
grid_search = GridSearchCV(estimator = classify, param_grid = param_grids, scoring = 'accuracy', cv = 5, n_jobs = -1)

grid_search = grid_search.fit(X_train, y_train)

# Show best Score (de acordo com "scoring")
best_scorre = grid_search.best_score_

# Melhores HyperParâmetros
best_parameters = grid_search.best_params_
best_parameters

# Analisar os resultados de cada combinação ordenado por score

(pd.DataFrame(grid_search.cv_results_)).sort_values(by=['rank_test_score'])
