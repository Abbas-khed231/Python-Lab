"""1. Install matplotlib  & you can use plt.plot() to create a line plot of given data

x = [0, 5, 9, 10, 15, 20, 25] 

y = [0, 1, 2, 3, 4, 5, 6]"""

import matplotlib.pyplot as plt

# Data
x = [0, 5, 9, 10, 15, 20, 25]
y = [0, 1, 2, 3, 4, 5, 6]

# Create a figure and axis
plt.figure(figsize=(8, 5))

# Plot the line chart
plt.plot(x, y, marker='o', linestyle='-', color='b')

# Adding titles and labels
plt.title('Line Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the grid
plt.grid(True)

# Show the plot
plt.show()
