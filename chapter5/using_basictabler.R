library(basictabler)

# Create a data frame
data <- data.frame(
  name = c("John Doe", "Jane Doe"),
  age = c(30, 25),
  salary = c(100000, 50000)
)

# Create a basictabler object
table <- qhtbl(data, 
  theme = "largeplain"
)

# Render the table to HTML
table
  