import numpy as np

# Create a sample dataset with missing values (using np.nan)
data = np.array([[1, 2, np.nan, 4],
                 [5, np.nan, 7, 8],
                 [9, 10, 11, np.nan],
                 [np.nan, 14, 15, 16]])

print("Original Data:")
print(data)

# 1. Identify missing data
missing_mask = np.isnan(data)
print("\nMissing Data Mask:")
print(missing_mask)

# 2. Count the number of missing values
missing_count = np.sum(missing_mask)
print("\nNumber of Missing Values:", missing_count)

# 3. Fill missing values with a specified value (e.g., 0)
filled_data_0 = np.where(missing_mask, 0, data)
print("\nData with Missing Values Filled with 0:")
print(filled_data_0)

# 4. Fill missing values with the mean of the column
col_means = np.nanmean(data, axis=0)  # Calculate column means ignoring NaN
for i in range(data.shape[1]):
    data[:, i] = np.where(np.isnan(data[:, i]), col_means[i], data[:, i])

print("\nData with Missing Values Filled with Column Means:")
print(data)

# 5. Drop rows with any missing values
dropped_rows = data[~np.isnan(data).any(axis=1)]
print("\nData after Dropping Rows with Missing Values:")
print(dropped_rows)
