import numpy as np

# Sample data
data = np.array([23, 76, 45, 89, 12, 34, 57, 78, 90, 21, 67, 45, 89, 55, 41])

# 1. Calculate Mean
mean_value = np.mean(data)
print("Mean:", mean_value)

# 2. Calculate Median
median_value = np.median(data)
print("Median:", median_value)

# 3. Calculate Standard Deviation
std_deviation = np.std(data)
print("Standard Deviation:", std_deviation)

# 4. Calculate Variance
variance_value = np.var(data)
print("Variance:", variance_value)

# 5. Calculate Percentiles
percentile_25 = np.percentile(data, 25)
percentile_50 = np.percentile(data, 50)  # This is also the median
percentile_75 = np.percentile(data, 75)
print("25th Percentile:", percentile_25)
print("50th Percentile (Median):", percentile_50)
print("75th Percentile:", percentile_75)
