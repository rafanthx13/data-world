# Comandos Básico de Data Science

## Importa DataFrame

file_path = './df_all_predicts_finalize.csv'
df = pd.read_csv(file_path, encoding = 'utf-8', sep=';', header = 0, low_memory = False)

## Exportar DataFrame

df_rdf_r.to_csv('result_LT_to_randomForest_rafael.csv', sep = ';', index = False)

## Filtrar DataFrame por valor de registro de coluna

aux_df = df_diff_zero_predict[ (df_diff_zero_predict['count0'] > 14) & 
                              (df_diff_zero_predict['os_original'] == 0) & 
                              (df_diff_zero_predict['acertou'] == True) ]
aux_df

## Iterar DataFrame

for index, row in rdf_results.iterrows():

## Create DataFrame from List of Lists

// informar lista de colunas, e de @index se precisar
df_rdf_r = pd.DataFrame(data_list, columns =rdf_results_columns)

## COnverter coluna para outro tipo

df_rdf_r[c] = df_rdf_r[c].astype(float)
