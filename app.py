import json
import random
import pyttsx3
import streamlit as st
"""
TTS
"""
# ---------------------------
# Function: Text-to-Speech
# ---------------------------
def speak(text):
    """
    Uses pyttsx3 to speak the given text aloud.
    
    Parameters:
        text (str): The text to speak.
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
# ---------------------------
# Function: Load Vocabulary
# ---------------------------
def load_vocab(file_path='vocab.json'):
    """
    Loads vocabulary words from a JSON file.
    
    Parameters:
        file_path (str): Path to the vocabulary JSON file.
    
    Returns:
        dict: Dictionary of words and their translations.
    """
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





