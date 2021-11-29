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
    
def test_recipe4() :
    result = requests.get("http://localhost:5000/api/v1/recipes?CleanedIngredients=Mango&Cuisine=Indian").json()
    assert result['recipes'][0]['Restaurant'] != 0

def test_recipe5() :
    result = requests.get("http://localhost:5000/api/v1/recipes?CleanedIngredients=Mango&Cuisine=Indian").json()
    assert len(result['recipes'][0]['Diet-type']) != 0

    
def test_recipe6() :
    result = requests.get("http://localhost:5000/api/v1/recipes?CleanedIngredients=Mango&Cuisine=Indian").json()
    assert (result['recipes'][0]['Restaurant-Location']) != 0        
    
def test_recipe7() :
    result = requests.get("http://localhost:5000/api/v1/recipes?CleanedIngredients=Mango&Cuisine=Indian").json()
    assert (result['recipes'][0]['image-url']) != 0        
