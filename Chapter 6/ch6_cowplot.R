# Install Libraries
install.packages("ggplot2")
install.packages("cowplot")

# Load required libraries
library(ggplot2)
library(cowplot)

# Load the Iris dataset
data(iris)

# Create separate histograms for each species
histograms <- list()
for (species in unique(iris$Species)) {
  data_subset <- iris[iris$Species == species, ]
  
  histogram <- ggplot(data_subset, aes(x = Sepal.Width)) +
    geom_histogram(binwidth = 0.1, fill = "lightblue", color = "black") +
    labs(title = paste("Sepal Width Histogram for", species)) +
    labs(x = "", y = "") +
    theme_minimal()
  
  histograms[[species]] <- histogram
}

# Create histogram for all species combined
all_species_hist <- ggplot(iris, aes(x = Sepal.Width)) +
  geom_histogram(binwidth = 0.1, fill = "lightblue", color = "black") +
  labs(title = "Sepal Width Histogram for All Species") +
  theme_minimal()

# Arrange histograms using cowplot
plot_grid(
  histograms[["setosa"]], 
  histograms[["versicolor"]], 
  histograms[["virginica"]], 
  all_species_hist,
  ncol = 2,
  align = "hv"
)

histograms <- lapply(unique(iris$Species), function(species) {
  data_subset <- iris[iris$Species == species, ]
  
  histogram <- ggplot(data_subset, aes(x = Sepal.Width)) +
    geom_histogram(binwidth = 0.1, fill = "lightblue", color = "black") +
    labs(title = paste("Sepal Width Histogram for", species)) +
    labs(x = "", y = "") +
    theme_minimal()
  
  return(histogram)
})

histograms
