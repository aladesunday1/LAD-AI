import gradio as gr

from translator import translate, get_history, get_statistics
from dictionary import dictionary_data
from favorites import add_favorite, get_favorites

last_translation = {
    "english": "",
    "language": "",
    "translation": ""
}


def translate_and_store(text, language):
    translated = translate(text, language)

    last_translation["english"] = text
    last_translation["language"] = language
    last_translation["translation"] = translated

    return translated


def save_translation():
    return add_favorite(
        last_translation["english"],
        last_translation["language"],
        last_translation["translation"]
    )


with gr.Blocks(title="LAD-AI") as app:

    gr.Markdown("""
# 🌍 LAD-AI

## Language Acquisition Device

### Breaking Language Barriers with Artificial Intelligence
""")

    with gr.Tabs():

        # ==========================
        # HOME
        # ==========================
        with gr.Tab("🏠 Home"):

            gr.Markdown("""
## Welcome to LAD-AI

LAD-AI is an AI-powered language translation application.

### Features

- 🌍 Translate English to French
- 🇳🇬 Translate English to Yoruba
- 🇳🇬 Translate English to Igbo
- 🇳🇬 Translate English to Hausa
""")

        # ==========================
        # TRANSLATOR
        # ==========================
        with gr.Tab("🌍 Translator"):

            english = gr.Textbox(
                label="English Text"
            )

            language = gr.Dropdown(
                choices=[
                    "French",
                    "Yoruba",
                    "Igbo",
                    "Hausa"
                ],
                value="French",
                label="Translate To"
            )

            output = gr.Textbox(
                label="Translation"
            )

            translate_btn = gr.Button("🚀 Translate")
            save_btn = gr.Button("⭐ Save")

            save_status = gr.Textbox(
                label="Status",
                interactive=False
            )

            translate_btn.click(
                fn=translate_and_store,
                inputs=[english, language],
                outputs=output
            )

            save_btn.click(
                fn=save_translation,
                outputs=save_status
            )

        # ==========================
        # DICTIONARY
        # ==========================
        with gr.Tab("📖 Dictionary"):

            gr.Dataframe(
                headers=[
                    "English",
                    "French",
                    "Yoruba",
                    "Igbo",
                    "Hausa"
                ],
                value=dictionary_data,
                interactive=False
            )

        # ==========================
        # FAVORITES
        # ==========================
        with gr.Tab("⭐ Favorites"):

            favorites_table = gr.Dataframe(
                headers=[
                    "English",
                    "Language",
                    "Translation"
                ],
                interactive=False
            )

            refresh_favorites = gr.Button(
                "⭐ Refresh Favorites"
            )

            refresh_favorites.click(
                fn=get_favorites,
                outputs=favorites_table
            )

        # ==========================
        # HISTORY
        # ==========================
        with gr.Tab("📜 History"):

            history_table = gr.Dataframe(
                headers=[
                    "English",
                    "Language",
                    "Translation"
                ],
                interactive=False
            )

            refresh_history = gr.Button(
                "🔄 Refresh History"
            )

            refresh_history.click(
                fn=get_history,
                outputs=history_table
            )

        # ==========================
        # STATISTICS
        # ==========================
        with gr.Tab("📊 Statistics"):

            stats = gr.JSON()

            refresh_stats = gr.Button(
                "📊 Refresh Statistics"
            )

            refresh_stats.click(
                fn=get_statistics,
                outputs=stats
            )

        # ==========================
        # SETTINGS
        # ==========================
        with gr.Tab("⚙️ Settings"):

            gr.Markdown("""
Settings page coming soon.
""")

        # ==========================
        # CONTACT
        # ==========================
        with gr.Tab("📞 Contact"):

            gr.Markdown("""
### Developer

**Name:** Mr-Smile

**Email:** wteam3286@gmail.com

**Phone:** +2349063926739
""")

app.launch()