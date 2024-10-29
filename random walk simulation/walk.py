import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_steps = 1000  # Number of steps in the random walk

# 1. One-Dimensional Random Walk
def random_walk_1d(num_steps):
    steps = np.random.choice([-1, 1], size=num_steps)  # Step left or right
    position = np.cumsum(steps)  # Cumulative sum to get position over time
    return position

# Simulate 1D random walk
position_1d = random_walk_1d(num_steps)

# Plot 1D random walk
plt.figure(figsize=(12, 4))
plt.plot(position_1d, label="1D Random Walk")
plt.xlabel("Step")
plt.ylabel("Position")
plt.title("1D Random Walk Simulation")
plt.legend()
plt.show()

# 2. Two-Dimensional Random Walk
def random_walk_2d(num_steps):
    x_steps = np.random.choice([-1, 1], size=num_steps)  # Steps along x-axis
    y_steps = np.random.choice([-1, 1], size=num_steps)  # Steps along y-axis
    x_position = np.cumsum(x_steps)
    y_position = np.cumsum(y_steps)
    return x_position, y_position

# Simulate 2D random walk
x_position, y_position = random_walk_2d(num_steps)

# Plot 2D random walk
plt.figure(figsize=(6, 6))
plt.plot(x_position, y_position, label="2D Random Walk")
plt.scatter(0, 0, color='red', label="Start", zorder=5)  # Mark the starting point
plt.scatter(x_position[-1], y_position[-1], color='green', label="End", zorder=5)  # Mark the ending point
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.title("2D Random Walk Simulation")
plt.legend()
plt.show()

# 3. Calculate Average Distance from Starting Point
def average_distance(x, y):
    distances = np.sqrt(x**2 + y**2)  # Calculate distance from (0,0) for each step
    avg_distance = np.mean(distances)
    return avg_distance

# Calculate and print the average distance for the 2D random walk
avg_distance = average_distance(x_position, y_position)
print("Average Distance from Start in 2D Random Walk:", round(avg_distance, 2))
