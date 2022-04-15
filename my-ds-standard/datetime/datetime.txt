https://khuyentran1401.github.io/Efficient_Python_tricks_and_tools_for_data_scientists/Chapter3/date_time.html

## Acessar todos os valore de datetime

Datetime é como uma classe que possui varios atributos:
year, month, day, hour

Voce acessar usando o attr dt na series pandas.Series.dt.

````
import pandas as pd 

df = pd.DataFrame({"date": ["2021/05/13 15:00", "2022-6-20 14:00"], "values": [1, 3]})

df["date"] = pd.to_datetime(df["date"])

print(df["date"].dt.year )
print(df["date"].dt.month )


## filtrar df por data

import pandas as pd 

df = pd.DataFrame(
    {"date": pd.date_range(start="2021-7-19", end="2021-7-23"), "value": list(range(5))}
)
filtered_df = df[df.date <= "2021-07-21"]
filtered_df


==================================

https://towardsdatascience.com/automated-data-cleaning-with-python-94d44d854423
https://github.com/elisemercury/AutoClean/blob/main/AutoClean/Modules.py

Código que automatcimaente converte columns do df para datetime. Ele tenta todas. E tambem, gera todas as possibilidade de datetime


def convert_datetime(self, df):
        # function for extracting of datetime values in the data
        if self.extract_datetime:
            logger.info('Started conversion of DATETIME features... Granularity: {}', self.extract_datetime)
            start = timer()
            cols = set(df.columns) ^ set(df.select_dtypes(include=np.number).columns) 
            for feature in cols: 
                try:
                    # convert features encoded as strings to type datetime ['D','M','Y','h','m','s']
                    df[feature] = pd.to_datetime(df[feature], infer_datetime_format=True)
                    try:
                        df['Day'] = pd.to_datetime(df[feature]).dt.day

                        if self.extract_datetime in ['M','Y','h','m','s']:
                            df['Month'] = pd.to_datetime(df[feature]).dt.month

                            if self.extract_datetime in ['Y','h','m','s']:
                                df['Year'] = pd.to_datetime(df[feature]).dt.year

                                if self.extract_datetime in ['h','m','s']:
                                    df['Hour'] = pd.to_datetime(df[feature]).dt.hour

                                    if self.extract_datetime in ['m','s']:
                                        df['Minute'] = pd.to_datetime(df[feature]).dt.minute

                                        if self.extract_datetime in ['s']:
                                            df['Sec'] = pd.to_datetime(df[feature]).dt.second
                        
                        logger.debug('Conversion to DATETIME succeeded for feature "{}"', feature)

                        try: 
                            # check if entries for the extracted dates/times are non-NULL, otherwise drop
                            if (df['Hour'] == 0).all() and (df['Minute'] == 0).all() and (df['Sec'] == 0).all():
                                df.drop('Hour', inplace = True, axis =1 )
                                df.drop('Minute', inplace = True, axis =1 )
                                df.drop('Sec', inplace = True, axis =1 )
                            elif (df['Day'] == 0).all() and (df['Month'] == 0).all() and (df['Year'] == 0).all():
                                df.drop('Day', inplace = True, axis =1 )
                                df.drop('Month', inplace = True, axis =1 )
                                df.drop('Year', inplace = True, axis =1 )   
                        except:
                            pass          
                    except:
                        # feature cannot be converted to datetime
                        logger.warning('Conversion to DATETIME failed for "{}"', feature)
                except:
                    pass
            end = timer()
            logger.info('Completed conversion of DATETIME features in {} seconds', round(end-start, 4))
        return df
