import json
import random
import pyttsx3
import streamlit as st
"""
TTS
"""
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def load_vocab(file_path='vocab.json'):
    with open(file_path, 'r') as f:
        return json.load(f)

vocab = load_vocab()
words = list(vocab.keys())
random.shuffle(words)

st.title("🧠 Language Learning Assistant")
st.write("Practice your vocabulary!")

word = st.selectbox("Pick a word to translate:", words)
if st.button("Speak Word"):
    speak(word)

user_input = st.text_input("What is the translation?")

if user_input:
    if user_input.lower().strip() == vocab[word].lower():
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Incorrect. The correct translation is: {vocab[word]}")





