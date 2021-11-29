import requests

def test() :
    result = requests.get("http://localhost:5000/api/v1/recipes?CleanedIngredients=Mango&Cuisine=Indian").json()
    assert len(result['recipes'][0]['TranslatedIngredients']) != 0
