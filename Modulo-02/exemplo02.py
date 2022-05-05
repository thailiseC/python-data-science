 #Novas perguntas do CEO:
#1. Qual a data do imóvel mais antigo no portfólio?
#2. Quantos imóveis possuem o número máximo de andares?
#3. Criar uma classificação para os imóveis, separando-os em baixo e alto padrão, de acordo com preço. Acima de R$ 540.000 -> alto padrão
#Abaixo de R$ 540.000 -> baixo padrão
#4. Gostaria de um relatório ordenado pelo preço e contento as seguintes informações:
#( id do imóvel, data que o imóvel ficou disponível para compra, o número de quartos, o tamanho total to terreno, o preço, a classificação do imóvel
#( alto e baixo padrão )
#5. Gostaria de um Mapa indicando onde as casas estão localizadas geograficamento.

import pandas as pd
import plotly_express as px

data = pd.read_csv( 'datasets/kc_house_data.csv')



print("1. Qual a data do imóvel mais antigo no portfólio?  ")
print("Solução: \n - Mudar a varável data de string para data \n - Ordenar o conjunto de dados pela menor data.\n")
data['date'] = pd.to_datetime( data['date'])
maisantigo = data[['id', 'date']].sort_values('date', ascending=True).reset_index(drop=True).loc[0,'date']
print('R: A casa mais antiga é da data {}' .format(maisantigo),'.\n\n')
print( data.sort_values('date', ascending=True) )

print("2. Quantos imóveis possuem o número máximo de andares?")
print("Solução: \n- Encontrar os números de andares e determinar o maior \n - Contar quantos imóveis eu tenho por andar.\n")
maisandares = data[['id', 'floors']].sort_values('floors', ascending=False).reset_index(drop=True).loc[0,'floors']
print('O maior número de andares é {}' .format(maisandares),'.\n\n')
print( data['floors'].unique() )
print(data[data['floors']==3.5][['floors','id']])
print('R: O número de imóveis com 3.5 andares é ', data[data['floors']==3.5].shape[0],'.\n')


print("3. Criar uma classificação para o imóveis, separando-os em baixo e alto padrão, de acordo com preço.\n Acima de R$ 540.000 -> alto padrão ( high_standard ) \n Abaixo de R$ 540.000 -> baixo padrão ( low_standard ).")
print("Solução: \n- Criar uma nova coluna no conjunto de dados chamada “standard” \n- Para cada linha, eu vou comparar a coluna “price”\n - Se “price” for maior que 540.000, eu vou escrever “high_standard” na coluna “standard” \n - Se “price” for menor que 540.000, eu vou escrever “low_standard” na coluna “standard”\n")
data['level'] = 'standard'
#print(data.columns)


data.loc[data['price'] > 540000, 'level' ] = 'high_level'
data.loc[data['price'] < 540000, 'level' ] = 'low_level'
print(data.head())

print("4. Gostaria de um relatório ordenado pelo preço e contento as seguintes informações: ( id do imóvel, data que o imóvel ficou disponível para compra, o número de quartos, o tamanho total to terreno, o preço, a classificação do imóvel ( alto e baixo padrão )")
print("Solução: \n- Selecionar as colunas desejadas/demandas. \n- Deletar as colunas não desejadas/demandas.\n")
report = data[['id', 'date', 'price', 'bedrooms', 'sqft_lot', 'level']].sort_values('price',ascending=False)
print(report.head())

report.to_csv('datasets/report_aula02.csv', index=False)

print("5. Gostaria de um Mapa indicando onde as casas estão localizadas geograficamente.")
print("Solução: \n- Procurar uma biblioteca em Python que armazena uma função que desenha mapa. \n- Aprender a usar a função que desenha mapas.")

# A função se chama Plotly, uma biblioteca que armazena uma função que desenha mapas.
#Scatter MapBox - Função que desenha um mapa

data_mapa = data[['id','lat','long','price']]
#print(data_mapa)
mapa = px.scatter_mapbox( data_mapa, lat='lat', lon= 'long', hover_name='id', hover_data=['price'],color_discrete_sequence=['fuchsia'],zoom=3,height=300)

mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height=600, margin={'r':0,'t':0,'l':0,'b':0})
mapa.show()

mapa.write_html('datasets/mapa_house_rocket.html')
