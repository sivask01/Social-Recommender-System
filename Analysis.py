
import streamlit as st
import pandas as pd

def user_behavior_analysis(reviews_df):
    st.subheader("User Behavior Analysis")
    
    # Most Active Users (Top 10)
    active_users = reviews_df['user'].value_counts().head(10)
    st.write("Top 10 Most Active Users:")
    st.bar_chart(active_users)

    # Average Ratings Given by Users
    avg_user_rating = reviews_df.groupby('user')['stars'].mean().sort_values(ascending=False).head(10)
    st.write("Top 10 Users by Average Rating Given:")
    st.bar_chart(avg_user_rating)

def item_popularity_analysis(reviews_df):
    st.subheader("Item Popularity Analysis")
    
    # Most Rated Items (Top 10)
    most_rated_items = reviews_df['work_encoded'].value_counts().head(10)
    st.write("Top 10 Most Rated Items:")
    st.bar_chart(most_rated_items)

    # Average Ratings of Items
    avg_item_rating = reviews_df.groupby('work_encoded')['stars'].mean().sort_values(ascending=False).head(10)
    st.write("Top 10 Items by Average Rating:")
    st.bar_chart(avg_item_rating)



def model_performance_analysis():
    st.subheader("Model Performance Comparison")

    # Sample performance metrics (replace with actual results)
    performance_data = {
        "Model": ["Collaborative Filtering", "CF with Time Decay", "CF with Sentiment", "CF with Graph", "Hybrid"],
        "RMSE": [0.81, 0.79, 0.75, 0.78, 0.73]
    }

    performance_df = pd.DataFrame(performance_data)
    st.table(performance_df)

    # Plot RMSE for each model
    st.bar_chart(performance_df.set_index("Model")["RMSE"])


def temporal_analysis(reviews_df):
    st.subheader("Temporal Analysis of Reviews")
    
    # Convert review_date to datetime if not already
    reviews_df['review_date'] = pd.to_datetime(reviews_df['review_date'])
    
    # Reviews per Month
    monthly_reviews = reviews_df.groupby(reviews_df['review_date'].dt.to_period("M")).size()
    st.write("Monthly Review Counts:")
    st.line_chart(monthly_reviews)

    # Reviews per Year
    yearly_reviews = reviews_df.groupby(reviews_df['review_date'].dt.year).size()
    st.write("Yearly Review Counts:")
    st.bar_chart(yearly_reviews)
