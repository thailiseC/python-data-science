#carregue o conjunto de dados chamado kc_house_data.csv do HD para a memória

#função - read_csv()
#biblioteca - pandas

import numpy as np
import pandas as pd

data = pd.read_csv( 'datasets/kc_house_data.csv')

#RESPONDENDO ÀS PERGUNTAS DO CEO

print('1. Quantas casas estão disponíveis para compra?')
print('R: Estão disponíveis para compra', data.shape[0], 'casas.\n')

print('Solução do Professor: 1 - selecionar a coluna id;\n 2 - contar o número de valores únicos.')
houses = len(data['id'].unique())
print('R: O número de casas disponíveis é de {}' .format(houses),'.\n\n')

print('2. Quantos atributos as casas possuem?')
print('R: As casas possuem', data.shape[1], 'atributos.\n' )

print('Solução do Professor: 1 -  O numero de colunas representam os atributos do apartamento;\n 2 - id e date não são atributos do apartamento.')
atributos = len(data.drop(['id','date'], axis=1).columns)
print('R: O número de atributos é {}' .format(atributos),'.\n\n')

print('3. Quais são os atributos das casas?')
print('R: Os atributos das casas são', data.columns, '.\n')

print('Solução do Professor: 1 -  O numero de colunas representam os atributos do apartamento;\n 2 - id e date não são atributos do apartamento.')
print('R: Os atributos são:', data.drop(['id','date'], axis=1).columns.tolist(),'.\n\n')

print('4. Qual a casa mais cara (casa com o maior valor de venda?')
print('R: A casa mais cara custa R$', data['price'].max(), '.')
print('Se encontra na linha:', data[data['price'].isin([data['price'].max()])], '.\n')

print('Solução do Professor: 1 -  Ordenar da casa mais cara à mais barata;\n 2 - pegar o primeiro elemento da coluna id depois de resetar os indices.')
maiscara = data[['id', 'price']].sort_values('price', ascending=False).reset_index(drop=True).loc[0,'id']
print('R: A casa mais cara tem o número de identificação {}' .format(maiscara),'.\n\n')

print('5. Qual a casa com maior número de quartos?')
print('R: A casa que possui mais quartos possui', data['bedrooms'].max(), 'quartos.')
print('Se encontra na linha:', data[data['bedrooms'].isin([data['bedrooms'].max()])], '.\n')

print('Solução do Professor: 1 -  Ordenar da casa com maior numero de quartos à de menos;\n 2 - pegar o primeiro elemento da coluna id depois de resetar os indices.')
maisquartos = data[['id', 'bedrooms']].sort_values('bedrooms', ascending=False).reset_index(drop=True).loc[0,'id']
print('R: A casa mais cara tem o número de identificação {}' .format(maisquartos),'.\n\n')

print('6. Qual a soma total de quartos do conjunto de dados?')
print('R: A soma total de quartos do conjunto de dados é', data['bedrooms'].sum(), '.\n')

print('Igual eu fiz. :D\n\n')

print('7. Quantas casas possuem 2 banheiros?')
print('R: ', len(data[data['bathrooms'] == 2]), ' casas possuem 2 banheiros.\n')

print('Solução do Professor: 1 - filtrar somente os id cujo valor da coluna bathroom é 2;\n 2 -  selecionar as colunas id e bathrooms;\n 3 - contar o numero de valores da coluna id.')
doisbanheiros = len(data.loc[data['bathrooms'] == 2, ['id','bathrooms']])
print('R: O número de casas com 2 banheiros é {}' .format(doisbanheiros),'.\n\n')

print('8. Qual o preço médio de todas as casas no conjunto de dados?')
a = data['price'].sum()
b = data.shape[0]
print('R: A soma total dos preços das casas é R$', a,', e o número total de casas é', b,'. Então o preço médio de todas as casas é R$', a/b, '.')
print('Usando a função mean() se obtém como preço médio R$', data['price'].mean(),'.\n')

print('Solução do Professor: 1 - utilizar o comando do panda mean();\n 2 - selecionar quantos números depois da virgula utilizando uma função do numpy.')
print('O preço médio das casas é R$', np.round(data['price'].mean(), 2),'.\n\n')

print('9. Qual o preço médio das casas com 2 banheiros?')
#pegar a soma total do preço das casas com 2 banheiros, c, e dividir pelo número de casas que tem 2 banheiros, d.
c = data[data['bathrooms'].isin(data['bathrooms'] == 2)]
d = c['price'].sum()
e = len(data[data['bathrooms'] == 2])
print('R: A soma total dos preços das casas com 2 banheiros é R$', d, ' e o número total de casas de 2 banheiros é', e,'. Então preço médio das casas com 2 banheiros é R$', d/e , '.')
print('Usando a função mean() se obtém como preço médio das casas de 2 banheiros R$', c['price'].mean(),'.\n')

print('Solução do Professor: 1 - selecionar as colunas com bathrooms igual a 2 e preço;\n 2 - utilizar o comando do panda mean();\n 3 - reduzir as casas decimais.\n')
print('A soma total dos preços das casas com 2 banheiros é R$', np.round(data.loc[data['bathrooms'] == 2, 'price'].mean(), 2),'.\n\n')

print('10. Qual o preço mínimo entre as casas com 3 quartos?')
detresquartos = data[data['bedrooms'].isin(data['bedrooms'] == 3)]
print('R: O preço mínimo de uma casa com 3 quartos é R$', detresquartos['price'].min(), '.\n')

print('Solução do Professor: 1 - selecionar as colunas com bedrooms igual a 3 e preço;\n 2 - utilizar o comando min();')
print('O preço mínimo de uma casa com 3 quartos é R$', data.loc[data['bedrooms'] == 3, 'price'].min(),'.\n\n')

print('11. Quantas casas possuem mais de 300 metros quadrados na sala de estar?')
print('R: ', len(data[data['sqft_living'] > 300]), 'possuem mais de 300 metros quadrados na sala de estar.\n')

print('Solução do Professor: 1 - passar de foot pra m²;\n 2 - selecionar as linhas em que o m² da sala de estar é maior que 300.;')
data['m2'] = data['sqft_living'] * 0.093
print('R: ', len(data.loc[data['m2'] > 300, 'id']), ' casas possuem mais de 300 metros quadrados na sala de estar.\n\n')

print('12. Quantas casas tem mais de 2 andares?')
print('R: ', len(data[data['floors'] > 2]), 'casas tem mais de 2 andares.\n')

print('Solução do Professor: 1 - selecionar as linhas em que floor é maior que 2.')
print('R: ', len(data.loc[data['floors'] > 2, 'id']), ' casas possuem mais de 2 andares.\n\n')

print('13. Quantas casas tem vista para o mar?')
print('R: ', len(data[data['waterfront'] == 1]), 'casas têm vista para o mar.\n')

print('Solução do Professor: 1 - selecionar as linhas em que waterfront é 1.')
print('R: ', len(data.loc[data['waterfront'] == 1, 'id']), 'casas têm vista para o mar.\n\n')

print('14. Das casas com vista para o mar, quantas tem 3 quartos?')
vistamar = data[data['waterfront'] == 1]
print('R: ', len(vistamar[vistamar['bedrooms'] == 3]), 'casas com vista para o mar têm 3 quartos.\n')

print('Solução do Professor: 1 - selecionar as linhas em que waterfront é 1; 2 - selecionar as linhas com bedrooms igual a 3.')
print('R: ', len(data.loc[(data['waterfront'] == 1) & (data['bedrooms'] == 3), 'id']), 'casas com vista para o mar têm 3 quartos.\n\n')

print('15. Das casas mais de 300 metros quadrados na sala de estar, quantas tem mais de 2 banheiros?')
maisde300 = data[data['sqft_living'] > 300]
print('R: ', len(maisde300[maisde300['bathrooms'] > 2]), 'casas com mais de 300 metros quadrados na sala de estar possuem mais de 2 banheiros.\n')

print('Solução do Professor: 1 - selecionar as linhas em que m2 é maior que 300; 2 - selecionar as linhas com bathrooms maior que 2.')
print('R: ', len(data.loc[(data['m2'] > 300) & (data['bathrooms'] > 2), 'id']), 'casas com mais de 300 metros quadrados na sala de estar possuem mais de 2 banheiros.\n\n')



