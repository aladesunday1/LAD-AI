favorites = []

def add_favorite(english, language, translation):

    favorites.append({
        "English": english,
        "Language": language,
        "Translation": translation
    })

    return "✅ Saved to Favorites"


def get_favorites():

    if not favorites:
        return [["No favorites yet", "", ""]]

    return [
        [
            item["English"],
            item["Language"],
            item["Translation"]
        ]
        for item in favorites
    ]