import requests

def test_recipe1() :
    result = requests.get("http://localhost:5000/api/v1/recipes?CleanedIngredients=Mango&Cuisine=Indian").json()
    assert len(result['recipes']) != 0

def test_recipe2() :
    result = requests.get("http://localhost:5000/api/v1/recipes?CleanedIngredients=Mango&Cuisine=Mexican").json()
    assert len(result['recipes']) != 0

def test_recipe3() :
    result = requests.get("http://localhost:5000/api/v1/recipes?CleanedIngredients=Mango&Cuisine=Indian").json()
    assert result['recipes'][0]['TotalTimeInMins'] != 0
    
