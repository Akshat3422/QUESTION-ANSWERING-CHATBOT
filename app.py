import streamlit as st
import requests
import os

st.title("Groq LLM Chatbot")

api_key = os.getenv("GROQ_API_KEY")

st.subheader("Chat With Model")

user_query = st.text_input("Enter your query here")

if st.button("Get Response"):
    if not user_query.strip():
        st.warning("Please enter a query")
    else:
        res = requests.post(
            "http://127.0.0.1:8000/get_response",
            json={"query": user_query}
        )

        if res.status_code == 200:
            st.success(res.json()["response"])
        else:
            st.error("Backend error")
