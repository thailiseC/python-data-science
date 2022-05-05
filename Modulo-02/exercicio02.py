import pandas as pd
import plotly_express as px

data = pd.read_csv('datasets/kc_house_data.csv')
print(data.head())

print('1. Crie uma nova coluna chamada: “house_age”. \n- Se o valor da coluna “date” for maior que 2015-01-01 => ‘new_house’. \n- Se o valor da coluna “date” for menor que 2015-01-01 => ‘old_house’')
# 1 - mudar o tipo de variável da data; 2 - criar a coluna house_age; 3 - comparar a data e classificar o imóvel na nova coluna.
#data['date'] = pd.to_datetime(data['date'])
#data['house_age'] = 'standard'
#data.loc[data['date'] > '2015-01-01', 'house_age'] = 'new_house'
#data.loc[data['date'] < '2015-01-01', 'house_age'] = 'old_house'
#print(data.head())

# versão do professor:
data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')
data['house_age'] = data['date'].apply(lambda x: 'new_house' if x > pd.to_datetime('2015-01-01', format='%Y-%m-%d') else 'old_house')
print(data.head())

print('2. Crie uma nova coluna chamada: “dormitory_type”. \n- Se o valor da coluna “bedrooms” for igual à 1 => ‘studio’; \n- Se o valor da coluna “bedrooms” for igual a 2 => ‘apartament’; \n- Se o valor da coluna “bedrooms” for maior que 2 => “house“')

#data['dormitory_type'] = 'standard'
#data.loc[data['bedrooms'] == 1, 'dormitory_type' ] = 'studio'
#data.loc[data['bedrooms'] == 2, 'dormitory_type' ] = 'apartment'
#data.loc[data['bedrooms'] > 2, 'dormitory_type' ] = 'house'
#print(data[['id', 'bedrooms', 'dormitory_type']].head())

#ou (o jeito que o professor fez)

data['dormitory_type'] = data['bedrooms'].apply(lambda x: 'studio' if x == 1 else 'apartment' if x == 2 else 'house' if x > 2 else 'NA')
print(data[['id', 'date', 'bedrooms', 'house_age','dormitory_type']].head())

print('3. Crie uma nova coluna chamada: “condition_type”: \n- Se o valor da coluna “condition” for menor ou igual à 2 => “bad“; \n- Se o valor da coluna “condition” for igual à 3 ou 4 => “regular“; \n- Se o valor da coluna “condition” for igual à 5 => “good“')

#print(data['condition'].unique())
#data['condition_type'] = data['condition'].apply(lambda x: 'bad' if x <= 2 else 'regular' if x <= 4 else 'good' if x == 5 else 'NA')
#print(data[['id', 'date', 'bedrooms', 'house_age','dormitory_type','condition','condition_type']].head())

#ou

data['condition_type'] = data['condition'].apply(lambda x: 'bad' if x <= 2 else 'regular' if (x == 3) | (x == 4) else 'good')
print(data[['id', 'date', 'bedrooms', 'house_age','dormitory_type','condition','condition_type']].head())

print('4. Modifique o tipo da coluna "condition" pra STRING.')

data['condition'] = data['condition'].astype('str')
print(data.dtypes)

print('5. Delete as colunas: “sqft_living15” e “sqft_lot15”.')

data = data.drop(['sqft_living15', 'sqft_lot15'], axis=1)

print(data.columns)

# outro jeito: data = data.drop(columns=['sqft_living15', 'sqft_lot15'])

print('6. Modifique o TIPO a Coluna “yr_built” para DATE.')

#data['yr_built'] = data['yr_built'].astype('datetime64[ns]')
#print(data.dtypes)
#o professor fez:
data['yr_built'] = pd.to_datetime(data['yr_built'], format='%Y')
print(data.dtypes)

print('7. Modifique o TIPO a Coluna “yr_renovated” para DATE.')

#data['yr_renovated'] = data['yr_renovated'].astype('datetime64[ns]')
#print(data.dtypes)
#o professor fez:
data['yr_renovated'] = data['yr_renovated'].apply(lambda x: pd.to_datetime('1900-01-01', format='%Y-%m-%d') if x == 0 else pd.to_datetime(x, format='%Y'))
print(data.dtypes)

print('8. Qual a data mais antiga de construção de um imóvel?')

#maisantiga = data[['id', 'yr_built']].sort_values('yr_built', ascending=True).reset_index(drop=True).loc[0,'yr_built']
#print('R: A data mais antiga de construção é {}' .format(maisantiga),'.\n')

#o professor fez:
print('O professor fez:', data['yr_built'].min())

print('9. Qual a data mais antiga de renovação de um imóvel?')

#maisantigar = data[['id', 'yr_renovated']].sort_values('yr_renovated', ascending=True).reset_index(drop=True).loc[0,'yr_renovated']
#print('R: A data mais antiga de renovação é {}' .format(maisantigar),'.\n')

#o professor fez:
print(data.loc[data['yr_renovated'] > pd.to_datetime('1900-01-01', format='%Y-%m-%d'), 'yr_renovated'].min())

print('10. Quantos imóveis tem 2 andares?')
print(data.loc[data['floors'] == 2, 'id'].size)

print('11. Quantos imóveis estão com a condição igual a “regular” ?')
print(data.loc[data['condition_type'] == 'regular', 'id'].size)

print('12. Quantos imóveis estão com a condição igual a “bad”e possuem “vista para água” ?')
print(data.loc[(data['condition_type'] == 'bad') & (data['waterfront'] == 1), 'id'].size)

print('13. Quantos imóveis estão com a condição igual a “good” e são “new_house”?')
print(data.loc[(data['condition_type'] == 'good') & (data['house_age'] == 'new_house'), 'id'].size)

print('14. Qual o valor do imóvel mais caro do tipo “studio” ?')
print(data.loc[data['dormitory_type'] == 'studio','price'].max())

print('15. Quantos imóveis do tipo “apartment” foram reformados em 2015 ?')
print(data.loc[(data['dormitory_type'] == 'apartment') & (data['yr_renovated'] == pd.to_datetime('2015-01-01')), 'id'].size)

print('16. Qual o maior número de quartos que um imóvel do tipo “house” possui ?')
print(data.loc[data['dormitory_type'] == 'house', 'bedrooms'].max())

print('17. Quantos imóveis “new_house” foram reformados no ano de 2014?')
print(data.loc[(data['house_age'] == 'new_house') & (data['yr_renovated'] == pd.to_datetime('2014-01-01', format='%Y-%m-%d')), 'id'].size)

print('18. Selecione as colunas: “id”, “date”, “price”, “floors”, “zipcode” pelo método: \n 10.1. Direto pelo nome das colunas.\n 10.2. Pelos Índices. \n 10.3. Pelos Índices das linhas e o nome das colunas \n 10.4. Índices Booleanos')
print('Nomes: \n', data[['id', 'date', 'price', 'floors', 'zipcode']])
print(data.columns)
print('Índices: \n', data.iloc[:, [0, 1, 2, 7, 16]])
i = [True, True, True, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False, ]
print('Booleanos: \n', data.iloc[:, i])

print('19. Salve um arquivo .csv com somente as colunas novas adicionadas.')
data[['house_age', 'dormitory_type', 'condition_type']].to_csv('datasets/exercicio_19.csv')

print('20. Modifique a cor dos pontos no mapa de “pink” para “verde-escuro”')
data_mapa = data[['id','lat','long','price']]
mapa = px.scatter_mapbox( data_mapa, lat='lat', lon= 'long', hover_name='id', hover_data=['price'],color_discrete_sequence=['darkgreen'],zoom=3,height=300)

mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height=600, margin={'r':0,'t':0,'l':0,'b':0})
mapa.show()

mapa.write_html('datasets/mapa_house_rocket2.html')