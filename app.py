import gradio as gr
from deep_translator import GoogleTranslator

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
        return ""

    try:
        return GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)
    except Exception as e:
        return f"Error: {e}"

def clear():
    return "", ""

def swap(source, target):
    if source == "Auto Detect":
        source = "English"
    return target, source

with gr.Blocks(
    title="LAD-AI",
    theme=gr.themes.Soft(primary_hue="blue")
) as app:

    gr.Markdown("""
# 🌍 LAD-AI

### Language Acquisition Device

#### Breaking Language Barriers with Artificial Intelligence
""")

    with gr.Row():
        source = gr.Dropdown(
            list(languages.keys()),
            value="Auto Detect",
            label="From"
        )

        target = gr.Dropdown(
            list(languages.keys()),
            value="French",
            label="To"
        )

    with gr.Row():
        swap_btn = gr.Button("🔄 Swap")
        clear_btn = gr.Button("🗑 Clear")

    input_text = gr.Textbox(
        label="Input",
        lines=8,
        placeholder="Type here..."
    )

    translate_btn = gr.Button(
        "🚀 Translate",
        variant="primary"
    )

    output = gr.Textbox(
        label="Translation",
        lines=8,
        show_copy_button=True
    )

    translate_btn.click(
        translate,
        [input_text, source, target],
        output
    )

    clear_btn.click(
        clear,
        outputs=[input_text, output]
    )

    swap_btn.click(
        swap,
        [source, target],
        [source, target]
    )

app.launch()