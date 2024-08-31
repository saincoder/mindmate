import streamlit as st
import base64
import uuid
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Function to generate recommendation based on mood and symptoms
def generate_recommendation(mood, symptoms, behaviors):
    client = Groq(api_key=GROQ_API_KEY)
    if mood == 'sad':
        return 'Consider talking to a mental health professional or practicing mindfulness techniques such as meditation.'
    elif 'anxious' in mood:
        return 'Try breathing exercises or consider reaching out to a counselor to discuss your anxiety.'
    elif 'headache' in symptoms:
        return 'Ensure you are hydrated and have enough rest. If it persists, consult a doctor.'
    elif 'insomnia' in symptoms:
        return 'Establish a regular sleep schedule and avoid screen time before bed. If it continues, see a healthcare provider.'
    else:
        return 'Keep tracking your symptoms and consider speaking with a professional if needed.'

# Function to chat with bot using Groq API
def chat_with_bot(user_message):
    client = Groq(api_key=GROQ_API_KEY)
    user_message_lower = user_message.lower()

    # Greetings response
    if user_message_lower in ["hi", "hello", "hey"]:
        return "Hi! How can I help you? I'm your assistant to give you healthy tips."

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": user_message}
        ],
        model="llama-3.1-70b-versatile",
    )

    response_content = chat_completion.choices[0].message.content

    # Check if the question is unrelated to mental health
    if not is_health_related(user_message_lower):
        return "I'm your health assistant. Please ask me something related to health, and I'll do my best to help!"
    
    # Return the chatbot's natural language response if it's health-related
    return response_content

# Helper function to check if the user message is health-related
def is_health_related(user_message):
    health_keywords = ["stress", "anxiety", "depression", "mental health", "cbt", "dbt", "symptoms", "headache", "insomnia", "mood", "therapy", "counseling", "meditation", "well-being", "emotions"]
    return any(keyword in user_message for keyword in health_keywords)

# Function to generate a unique ID for each message
def generate_message_id():
    return str(uuid.uuid4())

# Function to generate a unique CSS class for message alignment
def message_class(role):
    return "user-message" if role == "user" else "bot-message"

def main():
    st.set_page_config(page_title="MindMate", page_icon="books")
    st.title('MindMate: Your Mental Health Companion')

    # Sidebar Intro
    st.sidebar.header("About MindMate")
    st.sidebar.write(
        """
        **MindMate** helps you track your mood, symptoms, and behaviors. 
        Get personalized recommendations and chat with our mental health chatbot for information and resources.
        """
    )

    # Load and display an image from the local directory
    image_path = "images/MM22.jpg"  # Replace with your local image path
    st.sidebar.image(image_path, use_column_width=True, caption=" ")

    # Symptom Tracking Section
    st.header('Track Your Mood and Symptoms')
    mood = st.text_input('Mood', placeholder="e.g., sad, anxious, happy")
    symptoms = st.text_input('Symptoms', placeholder="e.g., headache, insomnia, fatigue")
    behaviors = st.text_input('Behaviors', placeholder="e.g., overeating, sleeping late")

    if st.button('Get Recommendation'):
        recommendation = generate_recommendation(mood, symptoms, behaviors)
        st.write('Recommendation:', recommendation)

    # Chatbot Section
    st.header('Chat with MindMate')
    user_message = st.text_area('Ask MindMate a question about mental health', placeholder="e.g., How to deal with stress?")
    
    if st.button('Send'):
        bot_response = chat_with_bot(user_message)
        
        # Add messages to session state
        if 'messages' not in st.session_state:
            st.session_state.messages = []
        
        st.session_state.messages.append({
            'id': generate_message_id(),
            'role': 'user',
            'content': user_message
        })
        st.session_state.messages.append({
            'id': generate_message_id(),
            'role': 'bot',
            'content': bot_response
        })

    # Display chat messages
    if 'messages' in st.session_state:
        for message in st.session_state.messages:
            if message['role'] == 'user':
                st.markdown(f"""
                <div class="message user-message">
                    <div class="message-icon"><img src="https://img.icons8.com/?size=100&id=YtnFdkYn0RsE&format=png&color=000000" alt="User Icon"/></div>
                    <div class="message-content">{message['content']}</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="message bot-message">
                    <div class="message-icon"><img src="https://img.icons8.com/?size=100&id=uZrQP6cYos2I&format=png&color=000000" alt="Bot Icon"/></div>
                    <div class="message-content">{message['content']}</div>
                </div>
                """, unsafe_allow_html=True)

    # Inject CSS for the dark theme chat design
    st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: white;
    }
    .chat-container {
        display: flex;
        flex-direction: column;
        margin: 20px;
    }
    .message {
        display: flex;
        flex-direction: row; /* Ensure icon appears at the start */
        align-items: flex-start;
        margin: 10px 0;
        padding: 10px;
        border-radius: 20px;
        max-width: 80%;
        font-size: 16px;
        color: white;
    }
    .user-message {
        background-color: #1f1f1f;
        align-self: flex-end;
        justify-content: flex-end;
        border-radius: 20px 20px 0 20px;
    }
    .bot-message {
        background-color: #333;
        align-self: flex-start;
        justify-content: flex-start;
        border-radius: 20px 20px 20px 0;
    }
    .message-icon {
        margin-right: 10px; /* Place icon at the start */
    }
    .message-icon img {
        width: 30px;
        height: 30px;
    }
    .message-content {
        flex: 1; /* Allow text to take up remaining space */
    }
    </style>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
