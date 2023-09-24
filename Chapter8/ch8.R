# The skimr package
if(!require(skimr)){install.packages("skimr")}
library(skimr)
skim(iris)

if(!require(TidyDensity)){install.packages("TidyDensity")}
tidy_normal() |> skim()

if(!require(GGally)){install.packages("GGally")}
library(GGally)
library(TidyDensity)
tidy_normal(.n = 200) |> 
  ggpairs(columns = c("y","p","q","dx","dy"))

if(!require(DataExplorer)){install.packages("DataExplorer")}
library(DataExplorer)
library(TidyDensity)
library(dplyr)

df <- tidy_normal(.n = 200)

df |>
  introduce() |>
  glimpse()

df |>
  plot_intro() +
  theme_minimal()

df |> 
  plot_qq()

df[c("q","y")] |> 
  plot_qq()
