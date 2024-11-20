import streamlit as st
import pandas as pd
import pickle
from recommendations import get_top_n_recommendations 
from Analysis import temporal_analysis, user_behavior_analysis, item_popularity_analysis, model_performance_analysis
from utils import add_header, add_footer, top_navigation
from about import about_section


# top_navigation()

# # Load Data
# reviews_df = pd.read_csv('Files/reviews_processed_time.csv')
# user_mapping = dict(zip(reviews_df['user'], reviews_df['user_encoded']))

# # Function to Load Models Dynamically
# @st.cache_resource
# def load_model(model_name):
#     with open(f'Saved-Models/cf-time-decay.pkl', 'rb') as file:
#         return pickle.load(file)

# # Navigation
# st.sidebar.title("Navigation")
# navigation = st.sidebar.radio("Go to", ["Recommendations", "Analysis"])

# # Recommendation Logic
# if navigation == "Recommendations":
#     st.title("Personalized Recommender System")

#     # Select Model
#     model_choice = st.selectbox(
#         "Select Recommendation Model",
#         options=[
#             "Collaborative Filtering", 
#             "CF with Time Decay", 
#             "CF with Sentiment Analysis",
#             "CF with Graph Analysis",
#             "Hybrid Model"
#         ]
#     )

#     # Map Model Choice to File Names
#     model_files = {
#         "Collaborative Filtering": "cf-model",
#         "CF with Time Decay": "cf-time-decay",
#         "CF with Sentiment Analysis": "cf-sentiment",
#         "CF with Graph Analysis": "cf-graph",
#         "Hybrid Model": "cf-hybrid"
#     }

#     # Load the Selected Model Dynamically
#     selected_model_name = model_files[model_choice]
#     selected_model = load_model(selected_model_name)

#     # User Input
#     username = st.selectbox("Select User", options=list(user_mapping.keys()))
#     user_id = user_mapping[username]

#     if st.button("Get Recommendations"):
#         # Get Top Recommendations for Selected Model
#         top_recommendations = get_top_n_recommendations(selected_model, reviews_df, user_id, n=5)

#         st.subheader(f"Top Recommendations using {model_choice}:")
#         for idx, rec in enumerate(top_recommendations):
#             st.write(f"{idx+1}. Item ID: {rec.iid} - Predicted Rating: {rec.est:.2f}")

# elif navigation == "Analysis":
#     st.title("Recommendation System Analysis")

#     # Analysis Selection
#     analysis_choice = st.selectbox(
#         "Select Analysis Type",
#         options=[
#             "User Behavior", 
#             "Item Popularity", 
#             "Model Performance", 
#             "Temporal Analysis"
#         ]
#     )

#     if analysis_choice == "User Behavior":
#         user_behavior_analysis(reviews_df)

#     elif analysis_choice == "Item Popularity":
#         item_popularity_analysis(reviews_df)

#     elif analysis_choice == "Model Performance":
#         model_performance_analysis()

#     elif analysis_choice == "Temporal Analysis":
#         temporal_analysis(reviews_df)







# # Add Footer
# add_footer()

















# Add Header
add_header()

# Add Top Navigation and Get Selected Tab
selected_tab = top_navigation()

# Load Data
reviews_df = pd.read_csv('Files/reviews_processed_time.csv')
user_mapping = dict(zip(reviews_df['user'], reviews_df['user_encoded']))

# Function to Load Models Dynamically
@st.cache_resource
def load_model(model_name):
    with open(f'Saved-Models/cf-time-decay.pkl', 'rb') as file:
        return pickle.load(file)


# Recommendation Logic
if selected_tab == "Recommendations":
    # st.title("Personalized Recommender System")

    # Select Model
    model_choice = st.selectbox(
        "Select Recommendation Model",
        options=[
            "Collaborative Filtering", 
            "CF with Time Decay", 
            "CF with Sentiment Analysis",
            "CF with Graph Analysis",
            "Hybrid Model"
        ]
    )

    # Map Model Choice to File Names
    model_files = {
        "Collaborative Filtering": "cf-model",
        "CF with Time Decay": "cf-time-decay",
        "CF with Sentiment Analysis": "cf-sentiment",
        "CF with Graph Analysis": "cf-graph",
        "Hybrid Model": "cf-hybrid"
    }

    # Load the Selected Model Dynamically
    selected_model_name = model_files[model_choice]
    selected_model = load_model(selected_model_name)

    # User Input
    username = st.selectbox("Select User", options=list(user_mapping.keys()))
    user_id = user_mapping[username]

    if st.button("Get Recommendations"):
        # Get Top Recommendations for Selected Model
        top_recommendations = get_top_n_recommendations(selected_model, reviews_df, user_id, n=5)

        st.subheader(f"Top Recommendations using {model_choice}:")
        for idx, rec in enumerate(top_recommendations):
            st.write(f"{idx+1}. Item ID: {rec.iid} - Predicted Rating: {rec.est:.2f}")

elif selected_tab == "Analysis":
    # st.title("Recommendation System Analysis")

    # Analysis Selection
    analysis_choice = st.selectbox(
        "Select Analysis Type",
        options=[
            "User Behavior", 
            "Item Popularity", 
            "Model Performance", 
            "Temporal Analysis"
        ]
    )

    if analysis_choice == "User Behavior":
        user_behavior_analysis(reviews_df)

    elif analysis_choice == "Item Popularity":
        item_popularity_analysis(reviews_df)

    elif analysis_choice == "Model Performance":
        model_performance_analysis()

    elif analysis_choice == "Temporal Analysis":
        temporal_analysis(reviews_df)
elif selected_tab == "About":
    about_section()



# Add Footer
add_footer()
