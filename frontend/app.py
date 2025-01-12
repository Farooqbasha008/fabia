import streamlit as st

# Set up the title and description
st.title("FABIA - Your App Planning Assistant")
st.write("Welcome to FABIA - Focus, Aim, Build, Invent and Achieve -  I’m here to help you plan and refine your app idea.")

# Add Groq API key input in the sidebar
groq_api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")
if not groq_api_key:
    st.sidebar.write("Don't have a Groq API key? Get it from [GroqCloud](https://console.groq.com/keys).")

# Chat interface
user_input = st.text_input("Describe your app idea or ask FABIA for help:")

if user_input and groq_api_key:
    # Call the backend API (FastAPI) to process the user input
    import requests
    backend_url = "https://fabia-backend.onrender.com"  # Replace with your Render backend URL
    response = requests.post(backend_url, json={"user_input": user_input, "api_key": groq_api_key})
    if response.status_code == 200:
        st.write(f"FABIA: {response.json()['response']}")
    else:
        st.write("Sorry, something went wrong. Please try again.")
elif user_input and not groq_api_key:
    st.write("Please enter your Groq API key to continue.")
