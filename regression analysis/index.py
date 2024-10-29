import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(0)  # For reproducibility
x = np.random.rand(100) * 10  # 100 random values between 0 and 10
y = 2.5 * x + np.random.normal(0, 2, 100)  # y = 2.5 * x + some noise

# 1. Calculate the regression line
def calculate_regression_line(x, y):
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    # Calculating slope (m) and intercept (c)
    m = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
    c = y_mean - m * x_mean
    return m, c

# Get the slope (m) and intercept (c)
m, c = calculate_regression_line(x, y)
print("Slope:", m)
print("Intercept:", c)

# 2. Make predictions
def predict(x, m, c):
    return m * x + c
# all 
# Predict y values for the regression line
y_pred = predict(x, m, c)

# 3. Calculate Mean Squared Error (MSE)
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# Calculate MSE
mse = mean_squared_error(y, y_pred)
print("Mean Squared Error:", mse)

# 4. Plot the results
plt.scatter(x, y, color="blue", label="Data Points")
plt.plot(x, y_pred, color="red", label="Regression Line")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()
plt.title("Simple Linear Regression")
plt.show()
