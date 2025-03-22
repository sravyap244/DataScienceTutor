import streamlit as st
import google.generativeai as genai
import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # Ensure it's set in Hugging Face Secrets

genai.configure(api_key=GOOGLE_API_KEY)

def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")  # Ensure correct model name
        response = model.generate_content(prompt)
        return response.text if hasattr(response, "text") else " No response received."
    except Exception as e:
        return f" Error: {str(e)}"

st.set_page_config(page_title="AI Data Science Tutor", layout="wide")
st.title("AI Data Science Tutor ")

st.sidebar.header("Instructions")
st.sidebar.write(
    """
    - Ask any question related to Data Science, ML, AI, Python, etc.
    - Click the *Submit* button or press *Enter* to get a response.
    """
)

user_input = st.text_area("Ask a question in Data Science:", "")

if st.button("🚀 Submit") and user_input:
    with st.spinner("Thinking... 🤔"):
        response = get_gemini_response(user_input)
    st.success("Response Generated Successfully!")
    st.subheader("AI's Response:")
    st.write(response)
