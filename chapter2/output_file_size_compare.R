writexl::write_xlsx(iris, tmp1 <- tempfile())
file.info(tmp1)$size

openxlsx::write.xlsx(iris, tmp2 <- tempfile())
file.info(tmp2)$size

xlsx::write.xlsx(iris, tmp3 <- paste0(tempfile(),".xlsx"))
file.info(tmp3)$size
