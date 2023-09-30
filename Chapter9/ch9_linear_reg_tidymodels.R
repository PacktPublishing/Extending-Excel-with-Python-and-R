
# Library Load ------------------------------------------------------------

library(readxl)
library(tidymodels)
library(purrr)
library(performance)


# Get Data ----------------------------------------------------------------

df <- read_xlsx(
  path = "chapter1/iris_data.xlsx",
  sheet = "iris"
)

# Split the data by Species -----------------------------------------------

iris_list <- split(df, df$species)

# Specify the Model -------------------------------------------------------

lm_model <- linear_reg(mode = "regression", engine = "lm")

# Define Formula ----------------------------------------------------------

f_x <- formula(paste("petal_width", "~", "petal_length + sepal_width + sepal_length"))

# Perform Linear Regression using purrr -----------------------------------
lm_mod <- linear_reg(mode = "regression", engine = "lm")

wf <- workflow() |>
  add_model(lm_mod)

lm_fit_list <- function(df) {
  #create recipe
  recipe_train <- recipe(f_x, data = df) %>%
    step_normalize(all_predictors())
  
  #fit workflow on train data
  fit_wf <- wf |>
    add_recipe(recipe_train) |>
    fit(data = df)

  fit_wf
}

model_list <- map(iris_list, lm_fit_list)
lapply(model_list, tidy)
lapply(model_list, glance)

model_list |>
  map(extract_fit_engine) |> 
  map(check_model) 
