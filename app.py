import gradio as gr
from deep_translator import GoogleTranslator

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

def translate(text, source, target):
    if text.strip() == "":
        return ""

    return GoogleTranslator(
        source=languages[source],
        target=languages[target]
    ).translate(text)

with gr.Blocks(
    title="LAD-AI",
    theme=gr.themes.Soft(primary_hue="blue")
) as app:

    gr.Markdown(
    """
    # 🌍 LAD-AI

    ### Language Acquisition Device

    #### Breaking Language Barriers with Artificial Intelligence
    """
    )

    with gr.Row():

        source = gr.Dropdown(
            choices=list(languages.keys()),
            value="English",
            label="Source Language"
        )

        target = gr.Dropdown(
            choices=list(languages.keys()),
            value="French",
            label="Target Language"
        )

    input_text = gr.Textbox(
        label="Enter Text",
        lines=8,
        placeholder="Type your sentence here..."
    )

    translate_btn = gr.Button(
        "🚀 Translate",
        variant="primary"
    )

    output = gr.Textbox(
        label="Translation",
        lines=8
    )

    translate_btn.click(
        translate,
        inputs=[input_text, source, target],
        outputs=output
    )

app.launch()