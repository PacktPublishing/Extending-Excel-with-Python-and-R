import matplotlib.pyplot as plt

### labels and titles

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

# Create a scatter plot
plt.scatter(x, y)

# Customize labels and titles
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Custom Title')
plt.suptitle('Subtitle for Additional Context')

# Save the plot to a file (e.g., .png)
plt.savefig('matplotlib_labels.png')

# Display the plot
plt.show()

### axes and legend

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

# Create a line plot
plt.plot(x, y, label='Data Series A')

# Customize axes and legend
plt.xlim(0, 6)
plt.ylim(0, 40)
plt.xticks([1, 2, 3, 4, 5])
plt.yticks([0, 10, 20, 30, 40])
plt.legend()

# Save the plot to a file (e.g., .png)
plt.savefig('matplotlib_axes_legends.png')

# Display the plot
plt.show()

### themes

# Apply a different theme
plt.style.use('ggplot')

# Sample data and plot
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]
plt.plot(x, y)

# Save the plot to a file (e.g., .png)
plt.savefig('matplotlib_themes.png')

# Display the plot
plt.show()

### text formatting

# Sample data and plot
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]
plt.plot(x, y)

# Customize text formatting
plt.title('Custom Title', fontsize=16, fontweight='bold', color='blue')
plt.xlabel('X-axis Label', fontsize=12, fontstyle='italic', color='green')
plt.ylabel('Y-axis Label', fontsize=12, fontweight='bold', color='red')

# Save the plot to a file (e.g., .png)
plt.savefig('matplotlib_text_formatting.png')

# Display the plot
plt.show()
