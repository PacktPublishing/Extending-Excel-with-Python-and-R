# Import necessary libraries
from plotnine import ggplot, aes, geom_point, xlab, ylab, ggtitle, labs, scale_x_continuous, scale_y_continuous, scale_color_manual, theme_minimal, theme_light, theme, element_text
import pandas

# Sample data
data = pandas.DataFrame({'X': [1, 2, 3, 4, 5],
                     'Y': [10, 15, 5, 20, 25],
                     'Category': ['A', 'B', 'A', 'B', 'A']})

# Create a base scatter plot
gg = (ggplot(data, aes(x='X', y='Y', color='Category')) +
      geom_point())

# Customize labels and titles
gg = gg + xlab("Custom X Label") + ylab("Custom Y Label")
gg = gg + ggtitle("Custom Plot Title") + labs(subtitle="Custom Subtitle")

# Customize axes and legends
gg = gg + scale_x_continuous(breaks=[1, 2, 3, 4, 5], labels=["One", "Two", "Three", "Four", "Five"])
gg = gg + scale_y_continuous(limits=(0, 30))
gg = gg + scale_color_manual(values={'A': 'red', 'B': 'blue'})

# Customize color palettes
# Map the 'category' variable to the 'fill' aesthetic
gg = gg + aes(fill='Category')

# Apply themes
gg = gg + theme_minimal()
gg = gg + theme_light()

# Control text formatting
gg = gg + theme(text=element_text(size=12, family="Arial", face="bold", color="black"),
                axis_text_x=element_text(angle=45, hjust=1))

print(gg)
