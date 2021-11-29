import requests

def test_1() :
    result = requests.get("http://localhost:5000/api/v1/recipes?CleanedIngredients=Tomato").text
    assert result.find("Tomato") != -1

def test_2() :
    result = requests.get("http://localhost:5000/api/v1/recipes?CleanedIngredients=pear").text
    assert result.find("pear") != -1    
def test_3() :
    result = requests.get("http://localhost:5000/api/v1/recipes?CleanedIngredients=peach").text
    assert result.find("peach") != -1

    
