from ../Data/csv-reader import restaurant_data 

def test_restaurant_data():
    assert restaurant_data("Punjabi", "North Indian", "Punjabi Dhaba", "") == "Punjabi Dhaba"