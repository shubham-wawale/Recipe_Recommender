import os
import sys
sys.path.append(os.path.abspath('../../'))

from Recipe_Recommender.Data.csv_reader import restaurant_data 

def test_restaurant_data():
    assert "Punjabi Dhaba" in restaurant_data("Punjabi", "North Indian", "Punjabi Dhaba", "")
    
def test_location_data():
    assert "Raleigh" in restaurant_data("Punjabi", "North Indian", "Raleigh", "")