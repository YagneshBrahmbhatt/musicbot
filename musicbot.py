import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = 'sk-proj-5hNgET0mI8PMGw03m5ZdT3BlbkFJv4HRUKI3l2dzgv9NEwoa'

st.title("MusicBot")
st.write("Ask me anything about music!")

if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

user_input = st.text_input("You: ", "")

if st.button("Send"):
    if user_input:
        st.session_state.conversation_history.append({"role": "user", "content": user_input})
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=st.session_state.conversation_history
        )
        bot_response = response['choices'][0]['message']['content'].strip()
        st.session_state.conversation_history.append({"role": "assistant", "content": bot_response})
        
        st.write(f"You: {user_input}")
        st.write(f"MusicBot: {bot_response}")

if st.button("Clear Conversation"):
    st.session_state.conversation_history = []
    st.write("Conversation cleared!")
