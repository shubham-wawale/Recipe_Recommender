import pandas as pd 
import random

df1 = pd.read_csv('Cleaned_Indian_Food_Dataset.csv')
df2 = pd.read_csv('Cuisine.csv')


cnt = 0

df1 = df1.fillna('')

for ind1, row1 in df1.iterrows():

	cnt+=1
	
	df1.at[ind1, 'Recipe-rating'] = str(random.randrange(1, 5))

	restaurant = ""
	location = ""

	for ind2, row2 in df2.iterrows():

		if row2['Cuisine'] == row1['Cuisine']:
			restaurant = restaurant + str(row2['Restaurant']) + "% "
			location = location + str(row2['Location']) + "% "
		elif row2['Cuisine'] in row1['Cuisine']:
			restaurant = restaurant + str(row2['Restaurant']) + "% "
			location = location + str(row2['Location']) + "% "
		elif row1['Cuisine'] == 'Punjabi' and row2['Cuisine'] == 'North Indian':
			restaurant = restaurant + str(row2['Restaurant']) + "% "
			location = location + str(row2['Location']) + "% "
		elif row1['Cuisine'] == 'Indian' and row2['Cuisine'] in ['South Indian', 'Gujarati', 'North Indian']:
			restaurant = restaurant + str(row2['Restaurant']) + "% "
			location = location + str(row2['Location']) + "% "
		elif row2['Cuisine'] == 'South Indian':
			restaurant = restaurant + str(row2['Restaurant']) + "% "
			location = location + str(row2['Location']) + "% "

	restaurant = restaurant[:len(restaurant)-2]
	location = location[:len(location)-2]

	df1.at[ind1, 'Restaurant'] = restaurant
	df1.at[ind1, 'Restaurant-Location'] = location.strip('\n')

	if 'chicken' in row1['Cleaned-Ingredients'] or 'fish' in row1['Cleaned-Ingredients'] or 'egg' in row1['Cleaned-Ingredients']:
		df1.at[ind1, 'Diet-type'] = "Non-Vegetarian"
	elif 'milk' in row1['Cleaned-Ingredients'] or 'paneer' in row1['Cleaned-Ingredients'] or 'curd' in row1['Cleaned-Ingredients'] or 'butter' in row1['Cleaned-Ingredients'] or 'ghee' in row1['Cleaned-Ingredients']:
		df1.at[ind1, 'Diet-type'] = "Vegetarian"
	else:
		df1.at[ind1, 'Diet-type'] = "Vegan"


df1.to_csv('final_recipe_recommender.csv', index=False)
