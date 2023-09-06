# Convert the dataset to a data frame
df <- as.data.frame(UCBAdmissions)
# Create a contingency table using xtabs()
xtabs(Freq ~ Gender + Admit, df)

# The gt package
if(!require(gt)){install.packages("gt", dependencies = TRUE)}
library(dplyr)
library(tibble)

tab <- mtcars |>
  rownames_to_column() |>
  arrange(factor(cyl), mpg) |>
  group_by(cyl) |>
  slice(1:3) |>
  gt() 

tab <- tab |>
  tab_spanner(
    label = "Performance",
    columns = c(mpg, disp, hp, drat, wt, qsec)
  ) 

tab <- tab |>
  tab_spanner(
    label = "Specs",
    columns = c(vs, am, gear, carb)
  ) 

tab <- tab |>
  tab_header(
    title = md("The Cars of **mtcars**"),
    subtitle = "These are some fine automobiles"
  )

tab
