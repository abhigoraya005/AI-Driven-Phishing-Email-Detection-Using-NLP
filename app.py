import streamlit as st
import joblib
import nltk
import re
import string
import numpy as np

from scipy.sparse import hstack
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title="AI Phishing Detector",
    page_icon="🛡️",
    layout="wide"
)

# ----------------------------
# Load Model
# ----------------------------

model = joblib.load("models/phishing_detector.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

# ----------------------------
# Preprocessing
# ----------------------------

def preprocess(text):

    text = text.lower()

    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"http\\S+|www\\S+", "", text)
    text = re.sub(r"\\S+@\\S+", "", text)
    text = re.sub(r"\\d+", "", text)

    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    tokens = nltk.word_tokenize(text)

    tokens = [
        word
        for word in tokens
        if word not in stop_words
    ]

    tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
    ]

    return " ".join(tokens)

# ----------------------------
# Feature Extraction
# ----------------------------

def extract_features(message):

    cleaned = preprocess(message)

    tfidf = vectorizer.transform([cleaned])

    metadata = np.array([[
        len(message),
        len(re.findall(r"http|www", message)),
        len(re.findall(r"\\d", message)),
        message.count("!"),
        sum(1 for c in message if c.isupper())
    ]])

    return hstack([tfidf, metadata])

# ----------------------------
# UI
# ----------------------------

st.title("🛡️ AI-Driven Phishing Email Detection")

st.write(
    "Detect whether a message is **Spam** or **Ham** using Machine Learning."
)

message = st.text_area(
    "Enter Message",
    height=200
)

if st.button("Predict"):

    if message.strip() == "":
        st.warning("Please enter a message.")

    else:

        features = extract_features(message)

        prediction = model.predict(features)[0]

        confidence = model.predict_proba(features).max()

        if prediction == 1:

            st.error("🚨 Spam Message")

        else:

            st.success("✅ Legitimate Message")

        st.metric(
            "Confidence",
            f"{confidence:.2%}"
        )