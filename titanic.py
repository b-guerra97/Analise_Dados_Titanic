import datetime
from datetime import timedelta
from datetime import datetime
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
print('-'*65)
print("Verificação de valores nulos ")
print('-'*65)
print(df.isnull().sum())

#Preenchimento de valores nulos com 0
print('-'*65)
print("Preenchimento dos valores nulos com 0")
print('-'*65)
df_filled = df.fillna(0)

print(df_filled)

#Converter coluna idade de float para inteiro
print('-'*65)
print("Converter coluna idade de float para inteiro")
print('-'*65)
df_filled['Age'] = df_filled['Age'].astype(int)
print(df_filled['Age'])

#Coluna Idade_Milissegundos
print('-'*65)
print("Coluna em Milissegundos")
print('-'*65)

'''
Nova coluna criada; aplicada função lambda a cada valor da coluna age;
cada valor da coluna é passado à função | 365.25 considera os anos bissextos | num horas por dia
minutos por hora | segundos por minuto | milissegundos em um segundo
o produto de todos os fatores é a idade em milissegundos - que vai ser convertido num numéro inteiro e
armazenado na nova coluna
'''
df_filled['Idade_Milissegundos'] = df_filled['Age'].apply(
    lambda age: int(age * 365.25 * 24 * 60 * 60 * 1000)
)
print(df_filled[['Age', 'Idade_Milissegundos']])


#Análise e manipulação de dados

#Calcular a taxa de sobrevivência por classe (Pclass) e sexo (Sex)
# Analisar a relação entre idade (Age) e sobrevivência




#Visualização de dados




#Exportação dos resultados




#Armazenamento numa Base de Dados




#Análise adicional
