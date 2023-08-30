library(TidyDensity)
library(styledTables)
library(xlsx)

st <- tidy_normal() |>
  styled_table(keep_header = TRUE) |>
  set_border_position("all", row_id = 1) |>
  set_bold(row_id = 1) |>
  set_fill_color("#00FF00", col_id = 3, condition = X >= 0.5)

# open new xlsx workbook and create a worksheet
wb <- createWorkbook()
sheet <- createSheet(wb, "tidy_normal")

# insert the styled table in the worksheet
write_excel(sheet, st)

# save the workbook
saveWorkbook(wb, "chapter5/styledTables_test.xlsx")
