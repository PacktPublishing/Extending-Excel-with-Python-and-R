library(tidyverse)
library(healthyverse)
library(writexl)

file_path <- paste0(getwd(), "/Chapter14/")
diamonds |>
  write_xlsx(paste0(file_path, "diamonds.xlsx"))