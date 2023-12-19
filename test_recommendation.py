import unittest
from restaurant_recommendation import RestaurantRecommendationSystem

class TestRecommendationSystem(unittest.TestCase):
    def setUp(self):
        self.recommendation_system = RestaurantRecommendationSystem()

    def test_valid_cuisine_recommendation(self):
        recommendations = self.recommendation_system.recommend_restaurants("Italian")
        self.assertTrue(recommendations)

    def test_invalid_cuisine_recommendation(self):
        result = self.recommendation_system.recommend_restaurants("Indian")
        self.assertEqual(result, "Invalid cuisine. Please enter a valid cuisine.")

    def test_empty_cuisine_recommendation(self):
        result = self.recommendation_system.recommend_restaurants("")
        self.assertEqual(result, "No restaurants found for the specified cuisine.")

if __name__ == "__main__":
    unittest.main()
