# Library Load ------------------------------------------------------------

library(tidymodels)
library(healthyR.ai)

# Convert to a tibble for tidymodels
df <- Titanic |>
  as_tibble() |>
  uncount(n)  |>
  mutate(across(where(is.character), as.factor))

# Splits ------------------------------------------------------------------

# Set seed for reproducibility
set.seed(123)

# Split the data into training and test sets
split <- initial_split(df, prop = 0.8)
train <- training(split)
test <- testing(split)

# Train a model -----------------------------------------------------------

# Create a recipe for pre-processing
recipe <- recipe(Survived ~ Sex + Age + Class, data = train)

# Specify logistic regression as the model
log_reg <- logistic_reg() |>
  set_engine("glm", family = "binomial")

# Combine the recipe and model into a workflow
workflow <- workflow() %>%
  add_recipe(recipe) %>%
  add_model(log_reg)

# Train the logistic regression model
fit <- fit(workflow, data = train)

# Predict -----------------------------------------------------------------

# Predict on the test set
predictions <- predict(fit, new_data = test) |>
  bind_cols(test) |>
  select(Class:Survived, .pred_class)

# Better method
pred_fit_tbl <- fit |>
  augment(new_data = test)

# Accuracy Check ----------------------------------------------------------

# Accuracy metrics for the model to be scored against from the healthyR.ai package
perf <- hai_default_classification_metric_set()

# Calculate the accuracy metrics
perf(pred_fit_tbl, truth = Survived, estimate = .pred_class)

# Print the confusion matrix
predictions |>
  conf_mat(truth = Survived, estimate = .pred_class)

# Use broom to tidy and glance the fitted model
tidy(fit, exponentiate = TRUE, conf.int = TRUE)
glance(fit)

# Visualize' --------------------------------------------------------------

# ROC Curve
roc_curve(pred_fit_tbl, truth = Survived, .pred_Yes, event_level = "second") |> 
  autoplot()