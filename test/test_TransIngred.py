def test() :
    result = requests.get("http://localhost:5000/api/v1/recipes?CleanedIngredients=Mango&Cuisine=Mexican").json()
    assert len(result['TranslatedIngredients']) != 0