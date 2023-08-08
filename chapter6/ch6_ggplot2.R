install.packages("ggplot2")
library(ggplot2)

# Make a histogram of the sepal width for all species
hist(iris$Sepal.Width)

# Make a histogram of the sepal width for each species
par(mfrow = c(2,2))
for (species in unique(iris$Species)) {
  hist(iris$Sepal.Width[iris$Species == species], main = species,
       xlab = species)
}
hist(iris$Sepal.Width, main = "All Species")
par(mfrow = c(1,1))

# Make a histogram of the sepal width for all species
iris |>
ggplot(aes(x = Sepal.Width)) + 
  geom_histogram(alpha = 0.328) +
  theme_minimal()

# Make a histogram of the sepal width for each species
iris |>
ggplot(aes(x = Sepal.Width, fill = Species)) + 
  geom_histogram(alpha = 0.328) +
  theme_minimal()
