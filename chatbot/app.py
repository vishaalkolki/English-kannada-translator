
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from aksharamukha import transliterate


import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
print("Entered the app.py file")

## Prompt template
prompt=chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system","""You are a helpful assistant that translates English to Kannada
                    Also, return the transliteration of the Kannada text in English
                    Return the Kannada pronunciation using the English alphabet only.
                    Example:
                    Hello -> Namaskara
                    How are you? -> Neevu hegiddira?"""),
        ("user","Input sentence:{input}")
    ]
 )

 ##streamlit framework
st.title("English to Kannada Translator")
st.write("This is a simple English to Kannada translator")

## Input text box
input_text = st.text_area("Enter English text to translate:", height=150)

## LLM model
llm = ChatOllama(
    model="translategemma:4b",
    temperature=0
)

# Output parser
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    with st.spinner("Translating..."):
        # Translate English to Kannada
        kannada_text = chain.invoke({"input": input_text})

        # Transliterate Kannada to English (Roman)
        roman_text = transliterate.process(
            "Kannada",
            "ISO",
            kannada_text
        )

    st.subheader("Kannada")
    st.write(kannada_text)

    st.subheader("Pronunciation")
    st.write(roman_text)