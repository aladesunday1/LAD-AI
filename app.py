import gradio as gr
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

languages = {
    "Auto Detect": "auto",
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

def translate(text, source, target):
    if not text.strip():
        return "", None

    translated = GoogleTranslator(
        source=languages[source],
        target=languages[target]
    ).translate(text)

    tts = gTTS(
        text=translated,
        lang=languages[target]
    )

    filename = "translation.mp3"
    tts.save(filename)

    return translated, filename

def clear():
    return "", "", None

def swap(source, target):
    if source == "Auto Detect":
        source = "English"
    return target, source

with gr.Blocks(theme=gr.themes.Soft()) as app:

    gr.Markdown("""
# 🌍 LAD-AI

## Language Acquisition Device

### AI Translation • Voice • Learning
""")

    with gr.Row():
        source = gr.Dropdown(
            choices=list(languages.keys()),
            value="Auto Detect",
            label="From"
        )

        target = gr.Dropdown(
            choices=list(languages.keys()),
            value="French",
            label="To"
        )

    with gr.Row():
        swap_btn = gr.Button("🔄 Swap")
        clear_btn = gr.Button("🗑 Clear")

    input_text = gr.Textbox(
        lines=8,
        label="Input Text"
    )

    translate_btn = gr.Button(
        "🚀 Translate",
        variant="primary"
    )

    output = gr.Textbox(
        lines=8,
        label="Translation",
        show_copy_button=True
    )

    audio = gr.Audio(
        label="🔊 Listen",
        autoplay=False
    )

    translate_btn.click(
        translate,
        [input_text, source, target],
        [output, audio]
    )

    clear_btn.click(
        clear,
        outputs=[input_text, output, audio]
    )

    swap_btn.click(
        swap,
        [source, target],
        [source, target]
    )

app.launch()