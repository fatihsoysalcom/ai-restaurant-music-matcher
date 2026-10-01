import random

# Mock data for restaurants and their associated music genres
RESTAURANTS = {
    "Le Petit Bistro": ["French", "Jazz", "Chanson"],
    "Spice Route": ["Indian", "World Music", "Fusion"],
    "The Blue Note": ["Jazz", "Blues", "Soul"],
    "Sakura Garden": ["Japanese", "Ambient", "Classical"],
    "El Fuego": ["Spanish", "Flamenco", "Latin"],
    "Rockin' Diner": ["American", "Rock", "Pop"],
    "Reggae Vibes": ["Caribbean", "Reggae", "Ska"]
}

# Mock data for user's music preferences
USER_MUSIC_PREFERENCES = {
    "Jazz": 5,
    "French": 3,
    "Ambient": 4,
    "Rock": 1
}

def get_restaurant_recommendation(preferences):
    """Recommends a restaurant based on music preferences."""
    scores = {}

    # Calculate a score for each restaurant based on music genre overlap
    for restaurant, genres in RESTAURANTS.items():
        score = 0
        for genre in genres:
            # If the user likes this genre, add its preference weight to the score
            if genre in preferences:
                score += preferences[genre]
        scores[restaurant] = score

    # Find the restaurant with the highest score
    if not scores:
        return "No restaurants found."

    # Sort restaurants by score in descending order
    sorted_restaurants = sorted(scores.items(), key=lambda item: item[1], reverse=True)

    # Return the top-scoring restaurant
    if sorted_restaurants and sorted_restaurants[0][1] > 0:
        return sorted_restaurants[0][0]
    else:
        # If no strong match, return a random restaurant
        return random.choice(list(RESTAURANTS.keys()))

if __name__ == "__main__":
    print("Welcome to the AI Restaurant Lezzet Avcısı!")
    print("Based on your music taste, we recommend:")

    recommended_restaurant = get_restaurant_recommendation(USER_MUSIC_PREFERENCES)
    print(f"\n-> {recommended_restaurant}")

    print("\nEnjoy your meal and the music!")
