import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = [[3, 1], [3, -1], [6, 1], [6, -1], [1, 0], [0, 1], [0, 0], [1, 1]]

# Extract x and y values from the data
x = [point[0] for point in data]
y = [point[1] for point in data]

# Calculate the linear regression parameters (slope and intercept) manually
n = len(data)
sum_x = sum(x)
sum_y = sum(y)
sum_x_squared = sum([xi ** 2 for xi in x])
sum_xy = sum([x[i] * y[i] for i in range(n)])

slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
intercept = (sum_y - slope * sum_x) / n


print("slope=",slope)
print("intercept",intercept)

# Generate regression line points
regression_line_x = np.linspace(min(x), max(x), 100)
regression_line_y = [slope * xi + intercept for xi in regression_line_x]

# Plot the data points
plt.scatter(x, y,  color='b')

# Plot the regression line
plt.plot(regression_line_x, regression_line_y,  color='r')

# Add labels and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
#plt.legend()

# Show the plot
plt.show()
