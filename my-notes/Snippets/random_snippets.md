# Random Snippets of Kaggle

## Template

````python

````

## Não mostrar nada desnecessário

````python
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline
````

## 

## Zoom HeartMap most important correlation

````python
k = 10 #number of variables for heatmap
# get the 'k' largest correlations values columns with 'SalePrice'
cols = corrmat.nlargest(k, 'SalePrice')['SalePrice'].index
cm = np.corrcoef(df_train[cols].values.T)
sns.set(font_scale=1.25)
hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)
plt.show()
# The heartmap is order_by correlation value with 'Sale Price' in row of 'Sale Price'
````

##  pairplot: scaterplot and histogram in diagonal


````python
#scatterplot
sns.set()
cols = ['SalePrice', 'OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt']
sns.pairplot(df_train[cols], size = 2.5)
plt.show();
````


### Missing Data

````python
#missing data
total = df_train.isnull().sum().sort_values(ascending=False) # Qtd of missing Values
percent = (df_train.isnull().sum()/df_train.isnull().count()).sort_values(ascending=False) # Make Percentage of missing_values
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent']) # concat in DataFrame
missing_data.head(20) # View the top '20' coluns with most missing_values


#dealing with missing data
df_train = df_train.drop((missing_data[missing_data['Total'] > 1]).index,1) # drop coluns with more of 1 missing_values
df_train = df_train.drop(df_train.loc[df_train['Electrical'].isnull()].index) # drop rows
df_train.isnull().sum().max() #just checking that there's no missing data missing...
````

#### Seaborn e printar dados faltantes em gráfico

````python
# set up aesthetic design
plt.style.use('seaborn')
sns.set_style('whitegrid')

# create NA plot for train data
plt.subplots(0,0,figsize = (15,3)) # positioning for 1st plot
train.isnull().mean().sort_values(ascending = False).plot.bar(color = 'blue')
plt.axhline(y=0.1, color='r', linestyle='-')
plt.title('Missing values average per columns in TRAIN data', fontsize = 20)
plt.show()
````

## Acessar diretorio e listar arquivos

````python
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
````

/input/house-prices-advanced-regression-techniques/data_description.txt
````
## Categorical Data

````python
# get categorical columns
categorical_cols = [col for col in train.columns if train[col].dtypes == "object"]
print("number of categorical columns is: ")
print(len(categorical_cols))
print("categorical columns:\n", categorical_cols)
````

## Fill Mising data

### Fill Categorical MIssing Data

````python
# fill NA value by missing
for col in categorical_cols:
    df[col] = df[col].fillna("missing")
````

## Cálculo de RMLSE

````python
def rmsle(y_true, y_pred):
    return 'RMSLE', np.sqrt(np.mean(np.power(np.log1p(y_pred) - np.log1p(y_true), 2))), False
````

## Como usar parâmetros de GridSearchCV

````python
svr_model = SVR(**clf.best_params_)
````

## View Importance Features of XGBoost

````python
xgb_feature_importances = xgb_model.feature_importances_
xgb_feature_importances = pd.Series(
    xgb_feature_importances, index=X_train.columns.values
    ).sort_values(ascending=False).head(15)

fig, ax = plt.subplots(figsize=(7, 5))
sns.barplot(x=xgb_feature_importances, 
            y=xgb_feature_importances.index, 
            color="#003f5c");
plt.xlabel('Feature Importance');
plt.ylabel('Feature');
````

````python
rf_feature_importances = pd.Series(
    rf_feature_importances, index=X_train.columns.values
    ).sort_values(ascending=False).head(15)

fig, ax = plt.subplots(figsize=(7,5))
sns.barplot(x=rf_feature_importances, 
            y=rf_feature_importances.index, 
            color="#ffa600");
plt.xlabel('Feature Importance');
plt.ylabel('Feature');
````
