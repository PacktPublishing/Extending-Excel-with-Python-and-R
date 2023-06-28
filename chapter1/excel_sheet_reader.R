read_excel_sheets <- function(filename, single_tbl = FALSE) {
  sheets <- readxl::excel_sheets(filename)
  
  if (single_tbl){
    x <- purrr::map_df(sheets, readxl::read_excel, path = filename)
  } else {
    x <- purrr::map(sheets, ~ readxl::read_excel(filename, sheet = .x))
    purrr::set_names(x, sheets)
  }
  
  x
}

f <- "chapter1/iris_data.xlsx"

read_excel_sheets(f, F)
