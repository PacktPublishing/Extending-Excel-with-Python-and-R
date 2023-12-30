# Import the necessary package
install.packages("svDialogs")
library(svDialogs)

# Create a message box
name <- dlg_input(message = "What is your name? ")

# Print the name that the user entered
print(name$res)

