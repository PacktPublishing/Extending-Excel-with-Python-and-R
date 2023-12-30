# Load the openxlsx package
library(openxlsx)

# Set the path to the xlsx file
xlsx_file <- "C:/Users/steve/OneDrive/Desktop/Extending_Excel/ch1/iris_data.xlsx"

# Open the xlsx file
wb <- openxlsx::loadWorkbook(xlsx_file)

# Save the xlsx file as an xlsb file
openxlsx::saveWorkbook(wb, "C:/Users/steve/OneDrive/Desktop/Extending_Excel/ch1/iris_data.xlsb")
