import streamlit as st
import openai

# Set up OpenAI API key
#openai.api_key = "your-api-key"

st.title("💬 AI Chatbot with Streamlit")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.text_input("Type your message:", key="user_input")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get AI response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages
    )

    ai_message = response["choices"][0]["message"]["content"]
    st.session_state.messages.append({"role": "assistant", "content": ai_message})

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(ai_message)
