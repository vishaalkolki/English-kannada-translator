# English to Kannada Translator

A Streamlit-based application that translates English text into Kannada using a local LLM (TranslateGemma via Ollama) and also provides Romanized Kannada (transliteration) for easier reading.

---

## Features

- English → Kannada translation
- Kannada script output (native script)
- Kannada transliteration (Romanized output for easy reading)
- Runs fully offline using Ollama
- Simple Streamlit UI

---

## How it works

1. User enters English text
2. LLM (TranslateGemma via Ollama) translates it into Kannada
3. Transliteration library converts Kannada script into English letters (Roman Kannada)

## Pipeline:
English Text
->
LLM (TranslateGemma)
->
Kannada Script
->
Transliteration (Aksharamukha / IndicXlit)
->
Roman Kannada Output

Note: Roman Kannada means writing the Kannada language using the English (Latin) alphabet instead of Kannada script.


## Tech Stack

- Python
- Streamlit
- LangChain
- Ollama
- TranslateGemma (or Gemma models)
- Aksharamukha (for transliteration)

---

## Installation

```bash
pip install -r requirements.txt
```

## Example query: 
How is the weather in Bengaluru today and what are the famous food items I can try there?