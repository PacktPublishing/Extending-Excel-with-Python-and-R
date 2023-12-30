library(ggplot2)
library(dplyr)

# Sample data
data <- data.frame(
  Category = c("A", "B", "C", "D"),
  Initial = c(10, 15, 8, 12),
  Final = c(18, 22, 14, 16)
)

# Calculate the midpoint for positioning the dots and lines
data <- data %>%
  mutate(Midpoint = (Initial + Final) / 2)

# Create the dumbbell plot using ggplot2
dumbbell_plot <- ggplot(data, aes(x = Category, xend = Category, 
                                  y = Initial, yend = Final)) +
  geom_segment(color = "gray50") +  # Lines connecting dots
  geom_point(color = "blue", size = 3) +  # Initial values
  geom_point(aes(y = Final), color = "red", size = 3) +  # Final values
  geom_point(aes(y = Midpoint), color = "green", size = 3) + # Midpoint Values
  geom_text(aes(label = Midpoint), 
            y = data$Midpoint, vjust = -.5, size = 3) +  # Midpoint labels
  labs(title = "Dumbbell Plot",
       x = "Category",
       y = "Values") +
  theme_minimal()

# Print the plot
dumbbell_plot
