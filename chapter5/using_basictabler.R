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

# A longer example
library(TidyDensity)
tn <- tidy_normal(.n = 10)

tbl <- BasicTable$new()
# formatting values (explained in the introduction vignette)
columnFormats=list(
  NULL, 
  NULL, 
  "%.4f",
  "%.4f",
  "%.4f",
  "%.4f",
  "%.4f"
)
tbl$addData(tn, firstColumnAsRowHeaders=TRUE,
            explicitColumnHeaders=c("Simulation","x","y","dx","dy","p","q"),
            columnFormats = columnFormats)
tbl$renderTable()
