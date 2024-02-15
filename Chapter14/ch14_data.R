# Library Load
library(tidyverse)
library(writexl)
library(janitor)

# Write File to disk
file_path <- paste0(getwd(), "/Chapter14/")

# Split data by cut and clean names of the list
df_list <- split(diamonds, diamonds$cut) |>
  clean_names()

# Write to xlsx
df_list |>
  write_xlsx(paste0(file_path, "diamonds_split.xlsx"))
