# Library Load
library(plumber)

# Set dir and file path
wd <- getwd()
sub_dir <- paste0("/Chapter11/")
full_dir <- paste0(wd, sub_dir)
f <- "plumber_api.R"
f_path <- paste0(full_dir, f)

# Initiate root
root <- pr(f_path)
root

root |> pr_run()
