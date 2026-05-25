import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("Spam Message Classifier")

message = st.text_area("Enter your message : ")

if st.button("Predict"):

    transformed = vectorizer.transform([message])

    prediction = model.predict(transformed)

    if prediction[0] == 1: 
        st.error("Spam message")
    else:
        st.success("Not Spam message")