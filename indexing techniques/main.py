import numpy as np

# Create a sample 2D array
data = np.array([[10, 20, 30, 40],
                  [50, 60, 70, 80],
                  [90, 100, 110, 120],
                  [130, 140, 150, 160]])

print("Original Data Array:")
print(data)

# 1. Boolean Indexing
# Create a boolean mask for values greater than 70
mask = data > 70
filtered_data = data[mask]
print("\nFiltered Data (Values > 70):")
print(filtered_data)

# 2. Fancy Indexing
# Use a list of indices to extract specific elements
row_indices = np.array([0, 2, 3])  # Rows to select
col_indices = np.array([1, 3, 2])  # Columns to select
fancy_indexed_data = data[row_indices, col_indices]
print("\nFancy Indexed Data (Selected Elements):")
print(fancy_indexed_data)

# 3. Combining Boolean and Fancy Indexing
# Extract rows where the first column is greater than 50, and only get columns 1 and 3
combined_filtered = data[data[:, 0] > 50][:, [1, 3]]
print("\nCombined Indexing (Rows where first column > 50, Columns 1 and 3):")
print(combined_filtered)

# 4. Modifying Values Using Boolean Indexing
# Set all values greater than 100 to 0
data[data > 100] = 0
print("\nData After Setting Values > 100 to 0:")
print(data)
