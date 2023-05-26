library(rbenchmark)
library(xlsx)
library(writexl)
library(openxlsx)
library(dplyr)

n <- 5

benchmark(
  "writexl" = {
    writexl::write_xlsx(iris, tempfile())
  },
  "openxlsx" = {
    openxlsx::write.xlsx(iris, tempfile())
  },
  "xlsx" = {
    xlsx::write.xlsx(iris, paste0(tempfile(),".xlsx"))
  },
  replications = n,
  columns = c(
    "test","replications","elapsed","relative","user.self","sys.self")
) |>
  arrange(relative)
