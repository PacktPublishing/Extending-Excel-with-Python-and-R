# Scatter Plot:

from plotnine import ggplot, aes, geom_point, geom_bar, geom_histogram, geom_boxplot, geom_tile, geom_violin, theme_minimal, labs
import pandas

# Sample data
data = pandas.DataFrame({'x': [1, 2, 3, 4, 5],
                         'y': [2, 4, 1, 3, 5]})

# Create a scatter plot
gg = ggplot(aes(x='x', y='y'), data) + geom_point()
print(gg)

# Bar Chart:

# Sample data
data = pandas.DataFrame({'category': ['A', 'B', 'C', 'D'],
                         'value': [10, 25, 15, 30]})

# Create a bar chart
gg = ggplot(aes(x='category', y='value'), data) + geom_bar(stat='identity')
print(gg)

# Histogram:

# Sample data
data = pandas.DataFrame({'values': [1, 2, 2, 3, 3, 3, 4, 4, 5]})

# Create a histogram
gg = ggplot(aes(x='values'), data) + geom_histogram(binwidth=1, fill='blue', color='black', alpha = 0.5)
print(gg)

# Box Plot:

# Sample data
data = pandas.DataFrame({'category': ['A', 'A', 'B', 'B', 'C', 'C'],
                         'value': [10, 15, 20, 25, 30, 35]})

# Create a box plot
gg = ggplot(aes(x='category', y='value'), data) + geom_boxplot()
print(gg)

# Heatmap:

# Sample data
data = {
    'x': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D'],
    'y': ['W', 'X', 'Y', 'Z', 'W', 'X', 'Y', 'Z', 'W', 'X', 'Y', 'Z', 'W', 'X', 'Y', 'Z'],
    'value': [10, 15, 5, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
}

# Convert data to a DataFrame
data = pandas.DataFrame(data)

# Create a heatmap
gg = (ggplot(data, aes(x='x', y='y', fill='value'))
      + geom_tile()
      + theme_minimal()
      + labs(title='Heatmap Example', x='X-Axis', y='Y-Axis', fill='Values'))
print(gg)

# Violin Plot:

# Sample data
data = {
    'Category': ['A', 'A', 'B', 'B', 'B', 'C', 'C', 'D', 'D', 'D'],
    'Value': [10, 15, 25, 30, 35, 45, 50, 65, 70, 75]
}

# Convert data to a DataFrame
df = pandas.DataFrame(data)

# Create a violin plot
gg = (ggplot(df, aes(x='Category', y='Value', fill='Category'))
      + geom_violin()
      + theme_minimal()
      + labs(title='Violin Plot Example', x='Category', y='Value', fill='Category'))
print(gg)
