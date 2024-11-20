def get_top_n_recommendations(model, reviews_df, user_id, n=5):
    # Get all unique items
    all_items = reviews_df['work_encoded'].unique()
    
    # Get items the user has already rated
    user_items = reviews_df[reviews_df['user_encoded'] == user_id]['work_encoded']
    unseen_items = [item for item in all_items if item not in user_items]

    # Predict ratings for all unseen items
    predictions = [model.predict(user_id, item) for item in unseen_items]
    
    # Sort predictions by estimated rating in descending order
    top_recommendations = sorted(predictions, key=lambda x: x.est, reverse=True)[:n]
    return top_recommendations

# # Example usage
# user_id = 123  # Replace with a valid user ID
# top_recommendations = get_top_n_recommendations(user_id)
# for rec in top_recommendations:
#     print(f"Item ID: {rec.iid}, Predicted Rating: {rec.est}")
