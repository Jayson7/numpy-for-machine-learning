import numpy as np

# Sample dataset
data = np.array([23, 76, 45, 89, 12, 34, 57, 78, 90, 21, 67, 45, 89, 55, 41])

# 1. Min-Max Scaling Function
def min_max_scaling(data):
    min_val = np.min(data)
    max_val = np.max(data)
    scaled_data = (data - min_val) / (max_val - min_val)
    return scaled_data

# Applying Min-Max Scaling
min_max_scaled_data = min_max_scaling(data)
print("Min-Max Scaled Data:\n", min_max_scaled_data)

# 2. Z-Score Normalization Function
def z_score_normalization(data):
    mean_val = np.mean(data)
    std_dev = np.std(data)
    normalized_data = (data - mean_val) / std_dev
    return normalized_data

# Applying Z-Score Normalization
z_score_normalized_data = z_score_normalization(data)
print("\nZ-Score Normalized Data:\n", z_score_normalized_data)