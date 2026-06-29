import gradio as gr
from deep_translator import GoogleTranslator

# -----------------------
# Languages
# -----------------------

languages = {
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Yoruba": "yo",
    "Igbo": "ig",
    "Hausa": "ha",
    "Arabic": "ar",
    "Chinese": "zh-CN"
}

# -----------------------
# Translator
# -----------------------

def translate(text, source, target):
    if not text.strip():
        return ""

    translated = GoogleTranslator(
        source=languages[source],
        target=languages[target]
    ).translate(text)

    return translated

# -----------------------
# UI
# -----------------------

with gr.Blocks(title="LAD-AI") as app:

    gr.Markdown(
        """
        # 🌍 LAD-AI

        ## Language Acquisition Device

        Translate • Learn • Speak • Understand
        """
    )

    with gr.Row():

        source = gr.Dropdown(
            list(languages.keys()),
            value="English",
            label="From"
        )

        target = gr.Dropdown(
            list(languages.keys()),
            value="French",
            label="To"
        )

    text = gr.Textbox(
        lines=8,
        placeholder="Type here..."
    )

    output = gr.Textbox(
        lines=8,
        label="Translation"
    )

    button = gr.Button("🚀 Translate")

    button.click(
        translate,
        inputs=[text, source, target],
        outputs=output
    )

app.launch()