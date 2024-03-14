import numpy
import pandas
import matplotlib.pyplot as plt

### scatter plot
data = {
    'Height': [155, 162, 168, 173, 179],
    'Weight': [50, 56, 61, 65, 72]
}

df = pandas.DataFrame(data)

# Create a scatter plot
df.plot.scatter(x='Height', y='Weight', title='Scatter Plot of Height versus Weight')

# Save the plot to a file (e.g., .png) in your working directory 
plt.savefig('matplotlib_scatter_plot.png')

# Show the plot
plt.show()


### bar chart

data = {'Category': ['A', 'B', 'C', 'D', 'E'],
        'Values': [15, 28, 24, 20, 32]}

df = pandas.DataFrame(data)

# Create a basic bar chart
plt.figure(figsize=(8, 6))
plt.bar(df['Category'], df['Values'], color='skyblue')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Basic Bar Chart')

# Save the plot to a file (e.g., .png) in your working directory 
plt.savefig('matplotlib_bar_chart.png')

plt.show()

### histogram

# Generate some random data for the histogram
data = numpy.random.normal(0, 1, 1000)

import matplotlib.pyplot as plt

# Create a basic histogram
plt.figure(figsize=(8, 6))
plt.hist(data, bins=20, color='lightblue', edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Basic Histogram')

# Save the plot to a file (e.g., .png)
plt.savefig('matplotlib_histogram.png')

plt.show()

### box plot

# Generate some random data for the box plot
data = [numpy.random.normal(0, 1, 100) for _ in range(3)]  # Three sets of random data

# Create a basic box plot
plt.figure(figsize=(8, 6))
plt.boxplot(data, vert=False, labels=['Set 1', 'Set 2', 'Set 3'])
plt.xlabel('Values')
plt.ylabel('Datasets')
plt.title('Basic Box Plot')

# Save the plot to a file (e.g., .png)
plt.savefig('matplotlib_boxplot.png')

plt.show()

### heatmap

# Generate some random data for the heatmap
numpy.random.seed(42)
data = numpy.random.rand(5, 5)  # Create a 5x5 matrix of random values

# Create a heatmap
plt.figure(figsize=(8, 6))
heatmap = plt.imshow(data, cmap='viridis', interpolation='nearest')
plt.colorbar(heatmap)
plt.title('Heatmap Example')

# Save the plot to a file (e.g., .png)
plt.savefig('matplotlib_heatmap.png')

plt.show()

### violinplot

# Generate some random data for the violin plot
numpy.random.seed(42)
data = [numpy.random.normal(0, std, 100) for std in range(1, 4)]

# Create a violin plot
plt.figure(figsize=(8, 6))
plt.violinplot(data, showmedians=True)
plt.title('Violin Plot Example')
plt.xticks([1, 2, 3], ['Group 1', 'Group 2', 'Group 3'])
plt.xlabel('Groups')
plt.ylabel('Values')

# Save the plot to a file (e.g., .png)
plt.savefig('matplotlib_violinplot.png')

plt.show()
