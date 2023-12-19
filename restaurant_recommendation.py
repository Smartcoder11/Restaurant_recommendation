import random

class RestaurantRecommendationSystem:
    def __init__(self):
        self.restaurants = {
            "Italian": ["Trattoria Bella", "Pasta Palace", "Mamma Mia Pizzeria"],
            "Mexican": ["Taco Haven", "Burrito Bliss", "Salsa Fiesta"],
            "Japanese": ["Sushi Samurai", "Ramen Retreat", "Tempura Town"],
            # Add more cuisines and restaurants as needed
        }

    def recommend_restaurants(self, cuisine):
        try:
            restaurants_for_cuisine = self.restaurants[cuisine]
            if not restaurants_for_cuisine:
                return "No restaurants found for the specified cuisine."
            
            # Dummy recommendation algorithm (random selection)
            recommended_restaurants = random.sample(restaurants_for_cuisine, min(3, (restaurants_for_cuisine)))
            return recommended_restaurants
        except KeyError:
            return "Invalid cuisine. Please enter a valid cuisine."

def user_interaction():
    try:
        user_input = input("Enter the type of food you desire: ")
        return user_input.strip()
    except KeyboardInterrupt:
        print("\nExiting the program.")
        exit()

def main():
    recommendation_system = RestaurantRecommendationSystem()

    while True:
        cuisine = user_interaction()
        recommendations = recommendation_system.recommend_restaurants(cuisine)
        print("\nRecommended restaurants:")
        for i, restaurant in enumerate(recommendations, start=1):
            print(f"{i}. {restaurant}")

if __name__ == "__main__":
    main()
