# Load Libraries
pkgs <- c("openxlsx", "xlsx", "readxl")
lapply(pkgs, library, character.only = TRUE)

f_path <- "Chapter1/iris_data.xlsx"

# Use openxlsx
openxlsx::read.xlsx(f_path) |> head(5)
openxlsx::read.xlsx(f_path, sheet = "iris") |> head(5)

# Use xlsx
xlsx::read.xlsx(file = f_path, sheetIndex = 1) |> head(5)
xlsx::read.xlsx(file = f_path, sheetName = "iris") |> head(5)

# Use readxl
readxl::read_excel(f_path) |> head(5)
readxl::read_excel(f_path, "iris") |> head(5)
