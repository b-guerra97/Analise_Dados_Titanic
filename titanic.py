from fileinput import close

import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', passwd='123456789', database='titanic')
cursor = conn.cursor()

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
plt.savefig('grafico_sobreviventes.png')
plt.show()


# Correlação entre Variáveis: Utilizar gráficos de dispersão (scatter plots) para analisar a correlação entre Age, Fare e Survived

colors = df_filled['Survived'].map({0: 'red', 1: 'green'})
plt.scatter(df_filled['Age'], df_filled['Fare'], c=colors, alpha=0.6, edgecolor='k')
plt.title('Correlação entre Idade, Tarifa e Sobrevivência')
plt.xlabel('Idade')
plt.ylabel('Tarifa')
plt.grid(linestyle='--', alpha=0.7)
plt.savefig('dispersao_idade_tarifa_sobrevivencia.png')
plt.show()

# Distribuição das Variáveis: Criar histogramas para visualizar a distribuição de Age, Fare, e Survived
media_idade = df_filled['Age'].mean()
plt.figure(figsize=(8, 6))
plt.hist(df_filled['Age'], bins=20, color='skyblue', edgecolor='black', alpha=0.7, label='Idade')
plt.axvline(media_idade, color='red', linestyle='dashed', linewidth=2, label=f'Média = {media_idade:.2f}')
plt.title('Distribuição de Idades')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.legend(fontsize=12)
plt.savefig('distribuicao_idade.png')
plt.show()

media_tarifa = df_filled['Fare'].mean()
plt.figure(figsize=(8, 6))
plt.hist(df_filled['Fare'], bins=20, color='green', edgecolor='black', alpha=0.7, label='Tarifa')
plt.axvline(media_tarifa, color='red', linestyle='dashed', linewidth=2, label=f'Média = {media_tarifa:.2f}')
plt.title('Distribuição de Tarifas')
plt.xlabel('Tarifa')
plt.ylabel('Frequência')
plt.legend(fontsize=12)
plt.savefig('distribuicao_tarifa.png')
plt.show()

nao_sobreviventes = df_filled[df_filled['Survived'] == 0]
sobreviventes = df_filled[df_filled['Survived'] == 1]
plt.figure(figsize=(8, 6))
plt.hist([nao_sobreviventes['Survived'], sobreviventes['Survived']],
         bins=[0, 1],
         color=['red', 'green'],
         edgecolor='black',
         alpha=0.7,
         label=['Não Sobreviveu', 'Sobreviveu'])
plt.title('Distribuição de Sobrevivência')
plt.xlabel('Sobrevivência (0 = Não Sobreviveu, 1 = Sobreviveu)')
plt.ylabel('Frequência')
plt.xticks([0.30,0.70], ['Não Sobreviveu', 'Sobreviveu'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('distribuicao_sobrevivencia.png')
plt.show()

#Exportação dos resultados
#Guardar o DataFrame atualizado num novo ficheiro Excel, incluindo todas as colunas novas criadas durante a análise

df_filled.to_excel('relatorio_titanic.xlsx', index=False, sheet_name='Dados Atualizados')
print("Ficheiro Excel criado: relatorio_titanic.xlsx")

#Exportar também gráficos relevantes para um relatório final


#Armazenamento numa Base de Dados
#Criar uma tabela onde cada coluna corresponde a uma das variáveis no conjunto de dados
#Inserir o conjunto de dados na tabela criada, assegurando que a nova coluna Idade_Milissegundos esteja formatada corretamente
relatorio_titanic = 'relatorio_titanic.xlsx'
df_dados = pd.read_excel(relatorio_titanic)

cursor.execute('CREATE TABLE IF NOT EXISTS dados(PassengerId INT PRIMARY KEY,'
               'Survived BIT, '
               'Pclass INT, '
               'Name VARCHAR(100), '
               'Sex VARCHAR(10), '
               'Age INT, '
               'SibSp INT, '
               'Parch INT, '
               'Ticket VARCHAR(50), '
               'Fare FLOAT, '
               'Cabin VARCHAR(50), '
               'Embarked VARCHAR(1), '
               'Idade_Milissegundos BIGINT(50))')

query = '''INSERT INTO dados(PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked, Idade_Milissegundos) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

try:
    for _, row in df_dados.iterrows():
        values = (row['PassengerId'], row['Survived'], row['Pclass'], row['Name'], row['Sex'], row['Age'], row['SibSp'], row['Parch'], row['Ticket'], row['Fare'], row['Cabin'], row['Embarked'], row['Idade_Milissegundos'])
        cursor.execute(query, values)
except mysql.connector.Error as e:
    print(f'Erro: {e}')

conn.commit()
cursor.close()
conn.close()

#Análise adicional
#Sobreviventes família a bordo

familia_a_bordo = df_filled.groupby('SibSp')['Survived'].count()
plt.figure(figsize=(10, 6))
label_barras = familia_a_bordo.plot(kind='bar', figsize=(12, 6), stacked=True, color=['salmon', 'skyblue'])
for i in label_barras.patches:
    label_barras.annotate(f'{int(i.get_height())}',  # Valor com duas casas decimais
                (i.get_x() + i.get_width() / 2, i.get_height()),  # Localização do rótulo
                ha='center', va='bottom',  # Alinhamento horizontal e vertical
                fontsize=12, color='black', fontweight='bold')
plt.title('Sobrevivência de Passageiros com Irmãos/Cônjuges a Bordo')
plt.xlabel('Número de Irmãos/Cônjuges')
plt.ylabel('Número de sobreviventes')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('sobrevivencia_sibsp.png')
plt.show()

#Sobreviventes crianças
criancas = df_filled[df_filled['Age'] < 18]
sobrevivencia_criancas = criancas['Survived'].sum()
nao_sobrevivencia_criancas = len(criancas) - sobrevivencia_criancas
labels = ['Sobreviventes', 'Não Sobreviventes']
sizes = [sobrevivencia_criancas, nao_sobrevivencia_criancas]
colors = ['darkgreen', 'darkred']
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, textprops={'fontsize': 20, 'color': 'darkgrey'})
plt.title('Sobrevivência de Crianças a Bordo')
plt.axis('equal')
plt.tight_layout()
plt.savefig('sobrevivencia_criancas.png')
plt.show()