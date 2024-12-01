import pandas as pd
import matplotlib.pyplot as plt

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
print('-'*65)
print("Taxa de sobrevicência por Classe e Sexo")
print('-'*65)
grupos = df_filled.groupby(['Pclass', 'Sex'])['Survived'].mean() * 100
print(grupos)


# Analisar a relação entre idade (Age) e sobrevivência
print('-'*65)
print("Relação entre idade e sobrevivência")
print('-'*65)
tabela_sobrevivencia = df_filled.groupby('Age')['Survived'].value_counts().unstack(fill_value=0)
tabela_sobrevivencia.columns = ['Não Sobreviventes', 'Sobreviventes']
print(tabela_sobrevivencia)


#Calcular a tarifa média por classe e sexo
print('-'*65)
print("Tarfifa média por classe e sexo")
print('-'*65)
grupo_classe_sexo = df_filled.groupby(['Pclass', 'Sex'])['Fare'].mean().round(2)
print(grupo_classe_sexo)


#Identificar correlações entre a tarifa (Fare) e a sobrevivência
print('-'*65)
print("Relação entre tarifa e sobrevivência")
print('-'*65)
grupo_tarifa_sobrevivencia = df_filled.groupby(['Pclass', 'Fare'])['Survived'].count()
print(grupo_tarifa_sobrevivencia)


#Visualização de dados

#TendênciasTemporais: Criar gráficos debarra ou linha para mostrar a distribuição de sobreviventes por classe e sexo
grupo_classe_sexo.plot(kind='bar', figsize=(12, 6), stacked=True, color=['salmon', 'skyblue'])
plt.title('Média de Tarifa por Classe e Sexo', fontsize=16)
plt.xlabel('Classe | Sexo', fontsize=12)
plt.ylabel('Média de Tarifa', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# Correlação entre Variáveis: Utilizar gráficos de dispersão (scatter plots) para analisar a correlação entre Age, Fare e Survived

# DistribuiçãodasVariáveis: CriarhistogramasparavisualizaradistribuiçãodeAge, Fare, eSurvived

#Exportação dos resultados
#Guardar o DataFrame atualizado num novo ficheiro Excel, incluindo todas as colunas novas criadas durante a análise
#Exportar também gráficos relevantes para um relatório final


#Armazenamento numa Base de Dados
#Criar uma tabela onde cada coluna corresponde a uma das variáveis no conjunto de dados
# Inserir o conjunto de dados na tabela criada, assegurando que a nova coluna Idade_Milissegundos esteja formatada corretamente


#Análise adicional



