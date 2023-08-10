import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Define the function f(x) = x^2
def f(x):
    return x**2

# Define the range of x values from 0 to 50
x_values = np.linspace(0, 50, 100)

# Calculate the corresponding y values for the function f(x)
y_values = f(x_values)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot(x_values, y_values, np.zeros_like(x_values), color='b')

# Fill the area under the curve
ax.fill_between(x_values, y_values, np.zeros_like(x_values), color='b', alpha=0.3)

# Set labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('3D Integral of f(x) = x^2 from 0 to 50')

plt.show()


