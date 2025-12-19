import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# 1. Load Environment Variables
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 2. UI Enhancement: Custom CSS
def apply_custom_css():
    st.markdown("""
        <style>
            .stApp { background-color: #000; }
            .stChatMessage { border-radius: 12px; border: 1px solid #e0e0e0; margin-bottom: 10px; }
            .stChatInputContainer { padding-bottom: 20px; }
            h1 { color: #1E3A8A; font-family: 'Helvetica', sans-serif; }
        </style>
    """, unsafe_allow_html=True)

st.set_page_config(page_title="TalentScout Assistant", page_icon="👔")
apply_custom_css()

st.title("TalentScout Hiring Assistant")
st.caption("Advanced AI Screening with Sentiment Analysis & Multilingual Support")

# 3. Advanced System Prompt
# Includes instructions for sentiment analysis and multilingual handling
SYSTEM_PROMPT = {
    "role": "system",
    "content": """You are 'TalentScout Assistant', a high-end professional recruitment bot.
    
    TASKS:
    1. GATHER INFO: Name, Email, Phone, Experience, Position, Location, and Tech Stack (ONE BY ONE).
    2. TECHNICAL ASSESSMENT: After getting the Tech Stack, ask 3-5 specific technical questions.
    3. SENTIMENT ANALYSIS: Monitor the candidate's tone. If they seem nervous, give encouragement. If confused, simplify.
    4. MULTILINGUAL: Detect the user's language and respond in that language immediately.
    
    RULES:
    - Stay professional and empathetic. 
    - Refer to the candidate by name once provided.
    - If they want to 'exit', provide a summary and thank them."""
}

# 4. State Management
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome to TalentScout! I'm here to help you through the first step of our hiring process. Could you please start with your **Full Name**?"}
    ]

# 5. Display Conversation History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. Chat Logic with Performance Optimization
if prompt := st.chat_input("Reply here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing response..."): # UX enhancement
            try:
                # Using llama-3.3-70b for high performance
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[SYSTEM_PROMPT] + st.session_state.messages,
                    temperature=0.6, # Low temp for consistency
                    max_tokens=1024
                )
                full_response = response.choices[0].message.content
                st.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            except Exception as e:
                st.error(f"Performance Error: {str(e)}")