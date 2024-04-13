"""
Understaning the use of python library Matplotlib
Matplotlib is a popular open-source data visualization library for Python. It provides a wide range of tools for creating static, animated, and interactive visualizations in Python.
Matplotlib is built on top of NumPy, a library for numerical computation in Python, and provides a high-level interface for creating common types of plots, such as line plots, scatter plots, bar charts, histograms, and more. It also provides tools for customizing the appearance of plots, including the colors, labels, titles, and axes.

One of the key strengths of Matplotlib is its flexibility. It provides a low-level interface for creating custom plots and visualizations, which can be used to create complex and sophisticated plots. Additionally, Matplotlib can be used in conjunction with other libraries for data analysis, such as Pandas, Seaborn, and Plotly, to create more advanced visualizations.

Matplotlib provides a wide range of functionality for creating different types of plots and visualizations. Some of the key features of Matplotlib include:

1. Line plots: used to plot continuous data as a series of connected points.
2. Scatter plots: used to plot data points as individual dots or markers.
3. Bar charts: used to plot categorical data as bars.
4. Histograms: used to plot the distribution of a set of continuous data.
5. Heatmaps: used to plot data as a color-coded grid.
6. Contour plots: used to plot data as a series of contours or lines.

Matplotlib is a powerful and flexible library for creating visualizations in Python. Its wide range of functionality, combined with its intuitive and easy-to-use interface, make it a popular choice for data scientists, researchers, and developers who need to create informative and visually appealing plots and visualizations.
"""
import matplotlib.pyplot as plt # same as: from matplotlib import pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Line plot of sin(x)')
plt.show()

# Scatter plot:
import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(100)
y = np.random.randn(100)
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter plot of random data')
plt.show()

# Bar chart:
import matplotlib.pyplot as plt
x = ["Apples", "Bananas", "Oranges"]
y = [10, 7, 15]
plt.bar(x, y)
plt.xlabel("Fruits")
plt.ylabel("Quantities")
plt.title("Bar chart of fruit quantities")
plt.show()

# Histogram:
import matplotlib.pyplot as plt
import numpy as np
data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of random data")
plt.show()

# Subplots:
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y1 = np.cos(x)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
ax1.plot(x, y1)
ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)')
ax1.set_title('Line plot of sin(x)')

ax2.plot(x, y1)
ax2.set_xlabel('x')
ax2.set_ylabel('cos(x)')
ax2.set_title('Line plot of cos(x)')

plt.tight_layout()
plt.show()