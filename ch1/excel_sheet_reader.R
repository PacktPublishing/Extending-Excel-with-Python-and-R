library(readxl)

excel_sheet_reader <- function(filename) {
  sheets <- excel_sheets(filename)
  x <- lapply(sheets, function(X) read_excel(filename, sheet = X))
  names(x) <- sheets
  x
}

f <- "C:/Users/steve/Documents/GitHub/Extending-Excel-with-Python-and-R/ch1/iris_data.xlsx"

excel_sheet_reader(f)
