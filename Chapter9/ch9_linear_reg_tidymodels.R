
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
# Create The Model
lm_mod <- linear_reg(mode = "regression", engine = "lm")

# Make the workflow
wf <- workflow() |>
  add_model(lm_mod)

# Make the function that will get mapped
lm_fit_list <- function(df) {
  #create recipe
  recipe_train <- recipe(f_x, data = df) %>%
    step_normalize(all_predictors())
  
  #fit workflow on the data
  fit_wf <- wf |>
    add_recipe(recipe_train) |>
    fit(data = df)

  fit_wf
}

# Map the linear model ----------------------------------------------------

model_list <- map(iris_list, lm_fit_list)
lapply(model_list, tidy)
lapply(model_list, glance)

# Check the Model
model_list |>
  map(extract_fit_engine) |> 
  map(check_model) 

# Alternate Nested Method
nested_lm <- df |>
  nest(data = -species) |>
  mutate(split = map(data, ~ initial_split(., prop = 8/10)),
         train = map(split, ~ training(.)),
         test  = map(split, ~ testing(.)),
         fit   = map(train, ~ lm(f_x, data = .)),
         pred  = map2(.x = fit, .y = test, ~ predict(object = .x, newdata = .y)))

nested_lm |>
  select(species, pred) |>
  unnest(pred)