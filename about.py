import streamlit as st

def about_section():
    # st.title("About the Recommender System")
    st.markdown("""
    ### Overview of Recommendation Models
    Our system leverages advanced recommendation models to provide personalized recommendations:
    
    #### 1. Collaborative Filtering (CF)
    Collaborative Filtering uses user-item interactions to find patterns. It recommends items to a user based on the preferences of similar users.

    #### 2. CF with Time Decay
    Time Decay enhances Collaborative Filtering by giving more weight to recent interactions. This ensures that recent preferences influence the recommendations more.

    #### 3. CF with Sentiment Analysis
    Sentiment Analysis incorporates natural language processing (NLP) to analyze review sentiments. This model considers user emotions expressed in reviews to enhance recommendations.

    #### 4. CF with Graph Analysis
    Graph Analysis leverages social network structures, analyzing relationships between users and items to improve recommendation accuracy.

    #### 5. Hybrid Model
    The Hybrid Model combines multiple techniques, such as Collaborative Filtering, Time Decay, Sentiment Analysis, and Graph Analysis, to provide robust recommendations by addressing the strengths and weaknesses of individual models.
    
    ### How It Works
    - **Data Collection**: The system collects user-item interactions and reviews.
    - **Model Training**: Various models are trained dynamically based on user behavior.
    - **Recommendation Generation**: The selected model generates top recommendations for users.

    Our system aims to deliver accurate, diverse, and personalized recommendations.
    """)
