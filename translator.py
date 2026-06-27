from deep_translator import GoogleTranslator

LANGUAGES = {
    "French": "fr",
    "Yoruba": "yo",
    "Igbo": "ig",
    "Hausa": "ha"
}

history = []

def translate(text, language):

    if not text.strip():
        return ""

    translated = GoogleTranslator(
        source="en",
        target=LANGUAGES[language]
    ).translate(text)

    history.append({
        "English": text,
        "Language": language,
        "Translation": translated
    })

    return translated


def get_history():

    if not history:
        return [["No translations yet", "", ""]]

    return [
        [
            item["English"],
            item["Language"],
            item["Translation"]
        ]
        for item in history
    ]


def get_statistics():

    return {
        "Total Translations": len(history)
    }