import pandas as pd 
import seaborn as srn
import statistics as sts 
#importar dados
dataset = pd.read_csv("C:\CIENCIAS_DE_DADOS\DADOS\DADOS_TESTE\Churn.csv", sep=";") 
#visualizar
dataset.head()
#tamanho dos corpos dos dados
dataset.shape
#Escreve os nomes da coluna de acordo do conhecimento do dado
dataset.columns = ["Id","Score","Estado","Genero","Idade","Patrimonio","Saldo","Produtos","TemCartCredito",
                    "Ativo","Salario","Saiu" ]
dataset.head()
agrupado = dataset.groupby(['Salario']).size()
agrupado
agrupado.plot.bar(color = 'blue')
agrupado = dataset.groupby(['Salario']).size()
agrupado
agrupado.plot.bar(color = 'red')
#explorar colunas númericas
dataset['Quantidade Distinta de Produtos'].describe()
srn.boxplot(dataset['Salario']).set_title('teste')
srn.displot(dataset['Salario'])
dataset.isnull().sum()
#verifica a mediana 
median = sts.median(dataset['Salario'])
median
#Substituir NAN por Mediana
dataset['Salario'].fillna(median, inplace=True)