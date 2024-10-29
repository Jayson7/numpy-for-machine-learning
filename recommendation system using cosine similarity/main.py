import numpy as np
import pandas as pd

# Create a user-item matrix
data = {
    'User1': [5, 4, 0, 0, 2],
    'User2': [0, 0, 4, 5, 0],
    'User3': [2, 3, 0, 0, 0],
    'User4': [0, 0, 0, 0, 1],
    'User5': [3, 4, 0, 0, 0]
}

# Create DataFrame
df = pd.DataFrame(data, index=['Item1', 'Item2', 'Item3', 'Item4', 'Item5'])
print("User-Item Matrix:")
print(df)

# Calculate cosine similarity between users
def cosine_similarity(matrix):
    sim = np.dot(matrix.T, matrix)  # Dot product of the matrix
    norms = np.array([np.sqrt(np.diagonal(sim))])  # Calculate norms
    return sim / norms / norms.T  # Normalize

similarity_matrix = cosine_similarity(df.values)
similarity_df = pd.DataFrame(similarity_matrix, index=df.columns, columns=df.columns)
print("\nCosine Similarity Matrix:")
print(similarity_df)

# Recommend items for a specific user
def recommend_items(user, user_item_matrix, similarity_matrix, n_recommendations=2):
    user_idx = user_item_matrix.columns.get_loc(user)
    similar_users = similarity_matrix[user_idx]
    
    # Get weighted ratings from similar users
    weighted_ratings = user_item_matrix.dot(similar_users) / np.array([np.abs(similar_users).sum()])
    
    # Get already rated items by the user
    already_rated = user_item_matrix.loc[:, user] > 0
    
    # Filter out already rated items
    weighted_ratings[already_rated] = 0
    
    # Recommend top n items
    recommendations = weighted_ratings.nlargest(n_recommendations)
    return recommendations

# Example: Recommend items for User1
user_to_recommend = 'User1'
recommendations = recommend_items(user_to_recommend, df, similarity_matrix)
print(f"\nRecommended Items for {user_to_recommend}:")
print(recommendations)
