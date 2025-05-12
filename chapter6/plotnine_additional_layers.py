from plotnine import ggplot, aes, geom_line, geom_point, geom_errorbar, position_dodge, geom_text, labs, geom_smooth
import pandas
import numpy

### Error bars
# Sample data
data = pandas.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 15, 8, 12, 18],
    'group': ['A', 'A', 'B', 'B', 'C'],
    'error': [1, 2, 1.5, 1, 2.5],
    'label_x': [2, 4, 3, 1, 5],
    'label_y': [16, 11, 6, 13, 17],
    'annotation_text': ['Peak', 'Valley', 'Low', 'High', 'Bottom']
})

# Create a ggplot object
gg = ggplot(data, aes(x='x', y='y', group='group')) + \
    geom_line() + \
    geom_point() + \
    geom_errorbar(aes(ymin='y - error', ymax='y + error'), width=0.1, size=0.5, position=position_dodge(width=0.2)) + \
    geom_text(aes(x='label_x', y='label_y', label='annotation_text'), size=10)

# Draw the plot
print(gg)

### Trendline
# Sample data
data = pandas.DataFrame({
    'X': numpy.arange(1, 21),
    'Y': numpy.random.randint(1, 101, size=20)
})

# Create a base plot
gg = (ggplot(data, aes(x='X', y='Y')) +
      geom_point() +
      labs(title='Scatter Plot with Trendline')
     )

# Add a trendline
gg = gg + geom_smooth(method='lm', se=False, linetype='dashed', color='red', size=1)

print(gg)

### Annotations
# Sample data
data = pandas.DataFrame({
    'X': numpy.arange(1, 11),
    'Y': numpy.random.randint(1, 101, size=10)
})

# Create a base plot
gg = (ggplot(data, aes(x='X', y='Y')) +
      geom_point() +
      labs(title='Scatter Plot with Annotations')
     )

# Add an annotation and adjust the position of the labels along the y-axis using nudge_y by 5 units 
gg = gg + geom_text(aes(label='Y'), nudge_y=5, color='blue')

print(gg)
