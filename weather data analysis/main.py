import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic temperature data for 365 days (1 year)
np.random.seed(0)  # For reproducibility
temperatures = np.random.normal(25, 5, 365)  # Mean of 25°C, standard deviation of 5

# 1. Calculate the average, maximum, and minimum temperature
average_temp = np.mean(temperatures)
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)

print("Average Temperature:", round(average_temp, 2), "°C")
print("Max Temperature:", round(max_temp, 2), "°C")
print("Min Temperature:", round(min_temp, 2), "°C")

# 2. Find the hottest and coldest day of the year
hottest_day = np.argmax(temperatures)  # Day with highest temperature
coldest_day = np.argmin(temperatures)  # Day with lowest temperature

print("Hottest Day:", hottest_day + 1, "with", round(max_temp, 2), "°C")
print("Coldest Day:", coldest_day + 1, "with", round(min_temp, 2), "°C")

# 3. Calculate the moving average (7-day window) to observe temperature trends
def moving_average(data, window_size=7):
    return np.convolve(data, np.ones(window_size) / window_size, mode='valid')

moving_avg_temp = moving_average(temperatures)

# 4. Plot the results
days = np.arange(1, 366)
plt.figure(figsize=(12, 6))
plt.plot(days, temperatures, label="Daily Temperatures", color="lightblue")
plt.plot(days[:len(moving_avg_temp)], moving_avg_temp, label="7-Day Moving Average", color="orange", linewidth=2)
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.title("Weather Data Analysis")
plt.legend()
plt.show()
