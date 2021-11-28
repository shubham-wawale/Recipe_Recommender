import requests

def test_1() :
    result = requests.get("http://localhost:5000/api/v1/recipes?CleanedIngredients=Tomato").text
    assert result.find("Tomato") != -1

