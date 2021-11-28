import requests

def test_recipe1() :
    result = requests.get("http://localhost:5000/api/v1/recipes?CleanedIngredients=Mango&Cuisine=Indian").json()
    assert result['filters']['CleanedIngredients'] == "Mango"
