# Load the library
library(RDCOMClient)

# Set file path
f_path <- "C:/Users/steve/Documents/GitHub/Extending-Excel-with-Python-and-R/"
f_chapter <- "chapter3/"
f_name <- "mult_by_rand_ch3.xlsm"
f <- paste0(f_path, f_chapter, f_name)

# Make Excel App
xl_app <- COMCreate("Excel.Application")
xl_wkbk <- xl_app$Workbooks()$Open(f)
xl_app[['Visible']] <- TRUE

macro_name <- "MultiplyByRandom"

# Run the macro
xl_app$Run(macro_name)

# Save and Quit
xl_wkbk$close(TRUE); xl_app$Quit() 
