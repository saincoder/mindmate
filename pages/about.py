import streamlit as st
# Set page configuration
st.set_page_config(page_title=" MindMate", page_icon="books")

# Load and display an image from the local directory
image_path = "images/MM22.jpg"  # Replace with your local image path
st.sidebar.image(image_path, use_column_width=True, caption=" ")
# Sidebar PDF Actions selection
st.sidebar.header("Welcome!")


st.title("About MindMate")
st.write(""" MindMate is a mental health companion application that utilizes the OpenAI GPT-4 
         API to provide mood tracking, symptom-based recommendations, and interactive chatbot
         functionality. This application does not use any external data storage; all interactions
         are handled in real-time using the OpenAI API. The application consists of a backend 
         implemented with Flask, and a frontend using streamlit/gradio. Sensitive information
         like the OpenAI API key is securely managed using environment variables stored in an .env 
         file.
""")
st.title ("Features:")
st.write("""
1. Symptom Tracking and Recommendations: Users can input their mood and symptoms to
receive personalized recommendations based on predefined rules.
         
2. Chatbot Interaction: Users can interact with a chatbot powered by OpenAI GPT-4 to
receive responses and mental health information.
         
3. `python-dotenv` package for environment variable managemen
         """)

st.write('Contact us:')

# Adding links to social accounts
st.markdown("[Saima Hassan](https://www.linkedin.com/in/drsaima-hassan)")
st.markdown("[Shahid Hussain](https://www.researchgate.net/profile/Saima_Hassan)")
st.markdown("[Nauman Khalid](https://www.linkedin.com/in/naumankhalid773)")
st.markdown("[Wasif](https://www.researchgate.net/profile/Saima_Hassan)")
st.markdown("[Mehrun Nisa](https://www.researchgate.net/profile/Saima_Hassan)")