import datetime
from datetime import timedelta
import pandas as pd
import matplotlib.pyplot as plt
import time

from fontTools.merge.util import current_time

#Leitura e Exploração dos dados
df = pd.read_csv('titanic.csv')
print("5 primeiros registos")
print('-'*65)
print(df.head())

print('-'*65)
print("5 últimos registos")
print('-'*65)
print(df.tail())

print('-'*65)
print("Análise estatística inicial")
print('-'*65)
print(df.describe())

print('-'*65)
print("Informações do DataFrame")
print('-'*65)
print(df.info())

#Limpeza e pré-processamento de dados

#Verificação de valores nulos
print(df.isnull().sum())

#Preenchimento de valores nulos com 0
df_filled = df.fillna(0)

print(df_filled)

#Converter coluna idade de float para inteiro
df_filled['Age'] = df_filled['Age'].astype(int)
print(df_filled['Age'])

#Coluna Idade_Milissegundos
epoch = datetime.datetime(1970, 1, 1)
df_filled['Idade_Milissegundos'] = df_filled['Age'].apply(lambda x: int((epoch + timedelta(days=x * 365.25)).timestamp() * 1000))
print(df_filled['Idade_Milissegundos'])
#Análise e manipulação de dados




#Visualização de dados




#Exportação dos resultados




#Armazenamento numa Base de Dados




#Análise adicional
