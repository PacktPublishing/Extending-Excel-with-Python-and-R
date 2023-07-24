library(basictabler)

# Create a data frame
data <- data.frame(
  name = c("John Doe", "Jane Doe"),
  age = c(30, 25),
  salary = c(100000, 50000)
)

# Plain table
table_plain <- qhtbl(data, theme = "largeplain")
table_plain

# Create a basictabler object
table <- qhtbl(data,
  theme = "largeplain",
  tableStyle = list("border-color" = "maroon"),
  headingStyle = list(
    "color" = "cornsilk", "background-color" = "maroon",
    "font-style" = "italic", "border-color" = "maroon"
  ),
  cellStyle = list(
    "color" = "maroon", "background-color" = "cornsilk",
    "border-color" = "maroon"
  )
)

# Render the table to HTML
table

# A longer example
library(TidyDensity)
tn <- tidy_normal(.n = 10)

tbl <- BasicTable$new()
# formatting values (explained in the introduction vignette)
columnFormats <- list(
  NULL,
  NULL,
  "%.4f",
  "%.4f",
  "%.4f",
  "%.4f",
  "%.4f"
)
tbl$addData(tn,
  firstColumnAsRowHeaders = TRUE,
  explicitColumnHeaders = c("Simulation", "x", "y", "dx", "dy", "p", "q"),
  columnFormats = columnFormats
)
tbl$renderTable()

# Add some conditional formatting
cells <- tbl$getCells(rowNumbers = 2:11, columnNumbers = 3:7, matchMode = "combinations")

tbl$mapStyling(
  cells = cells, styleProperty = "background-color", valueType = "color",
  mapType = "logic",
  mappings = list(
    "v<=-3", "red",
    "-3<v<=-2", "orange",
    "-2<v<=-1", "pink",
    "-1<v<= 0", "white",
    "0<v<=1", "white",
    "1<v<=2", "lightgreen",
    "2<v<=3", "lightblue",
    "3<v", "green"
  )
)

tbl$renderTable()

# Write styled table out to excel
library(openxlsx)

# Create Workbook
wb <- createWorkbook()
# Add a sheet called Data
addWorksheet(wb, "Data")
# Use basictabler to write the tbl to excel
tbl$writeToExcelWorksheet(
  wb = wb, 
  wsName = "Data",
  topRowNumber = 1, 
  leftMostColumnNumber = 1, 
  applyStyles = TRUE
)
# Use openxlsx to save the file
saveWorkbook(
  wb, 
  file="chapter5/basictabler_excel.xlsx", 
  overwrite = TRUE
)

