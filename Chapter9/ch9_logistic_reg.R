
# Library Load ------------------------------------------------------------


library(tidyverse)

df <- Titanic |>
  as.data.frame() |>
  uncount(Freq)


# Splits ------------------------------------------------------------------

# Split the data into training and test sets
set.seed(123)
train_index <- sample(nrow(df), floor(nrow(df) * 0.8), replace = FALSE)
train <- df[train_index, ]
test <- df[-train_index, ]

# Train a model -----------------------------------------------------------

# Train the logistic regression model
model <- glm(Survived ~ Sex + Age + Class, data = train, family = "binomial")

# Predict -----------------------------------------------------------------

# Evaluate the model on the test set
predictions <- predict(model, newdata = test, type = "response")
pred_resp <- ifelse(predictions <= 0.5, "No", "Yes")

# Calculate the accuracy of the model
accuracy <- mean(pred_resp == test$Survived)

# Print the accuracy of the model
print(accuracy)

# Print the confusion matrix
table(pred_resp, test$Survived)
