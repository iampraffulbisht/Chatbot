import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configure the Gemini API
genai.configure(api_key="*****")
model = genai.GenerativeModel('gemini-1.5-flash')

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 10px;
    }
    .title {
        color: #4CAF50;
        font-family: 'Arial', sans-serif;
    }
    
    </style>
""", unsafe_allow_html=True)

# Title and Persona
st.markdown("<h1 class='title'>AI Chatbot</h1>", unsafe_allow_html=True)
st.sidebar.title("Welcome to the AI Chatbot")


# Optionally add a logo/image to the sidebar
image = Image.open('chatbot_logo.png')  # Replace with your image path
st.sidebar.image(image, caption='Chatbot', use_column_width=True)

persona = """ You are a chatbot, so answer questions accordingly. """
st.write("Hello, I am your AI chatbot. How can I assist you today?")

# Layout with Columns
col1, col2 = st.columns([3, 1])

with col1:
    # Input for user's question
    user_question = st.text_input("Ask your question:", "")
    
    if st.button("Ask", use_container_width=True):
        if user_question.strip() != "":
            # Generating the response
            prompt = persona + " Now, the question is: " + user_question
            response = model.generate_content(prompt)
            
            # Display the response
            st.markdown("<div class='chat-box'><strong>Bot:</strong> " + response.text + "</div>", unsafe_allow_html=True)
        else:
            st.warning("Please ask a question before submitting.")
    
    st.write(" ")



st.write(" ")
