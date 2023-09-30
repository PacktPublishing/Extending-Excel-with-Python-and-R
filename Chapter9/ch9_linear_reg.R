
# Library Load ------------------------------------------------------------

library(readxl)


# Get Data ----------------------------------------------------------------

df <- read_xlsx(
  path = "chapter1/iris_data.xlsx",
  sheet = "iris"
)

head(df)

# Split the dataset by species
iris_split <- split(df, df$species)

# Define the dependent variable and independent variables
dependent_variable <- "petal_length"
independent_variables <- c("petal_width", "sepal_length", "sepal_width")

# Create a function to perform linear regression on each subset
perform_linear_regression <- function(data) {
  lm_model <- lm(
    formula(paste(dependent_variable, "~", paste(independent_variables, collapse = " + "))), 
    data = data
  )
  return(lm_model)
}

# Apply the linear regression to each subset using lapply
results <- lapply(iris_split, perform_linear_regression)

# Get the summary of each linear model
lapply(results, summary)

# Plot the model performance
par(mfrow = c(2,2))
lapply(results, plot)
par(mfrow = c(1, 1))
