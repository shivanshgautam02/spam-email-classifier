import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

def load_model():
    try:
        with open("models/spam_classifier.pkl", "rb") as model_file:
            vectorizer, model = pickle.load(model_file)
        return vectorizer, model
    except FileNotFoundError:
        st.error("Model file not found. Please train and save the model first.")
        return None, None


vectorizer, model = load_model()

def predict_email(text):
    if vectorizer and model:
        text_tfidf = vectorizer.transform([text])
        prediction = model.predict(text_tfidf)[0]
        return "Spam" if prediction == 1 else "Not-Spam"
    return "Error: Model not loaded"


st.title("📧 Spam Email Detector")
st.write("Enter an email below to check if it's spam or not.")

email_text = st.text_area("Type or paste the email content here:")

if st.button("Check Spam"): 
    if email_text.strip():
        prediction = predict_email(email_text)
        if prediction.startswith("Error"):
            st.error(prediction)
        else:
            st.success(f"Prediction: {prediction}")
    else:
        st.warning("Please enter some email content to check.")
