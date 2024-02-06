# Library Load
library(tidyverse)
library(healthyverse)
library(readxl)

# Source Functions
source(paste0(getwd(),"/chapter1/excel_sheet_reader.R"))

# Read data
file_path <- paste0(getwd(), "/Chapter14/")

df <- read_excel_sheets(
  filename = paste0(file_path, "diamonds_split.xlsx"),
  single_tbl = TRUE
)

# Visualize Data
# Create optimal binning via the opt_bin() function from healthyR
breaks <- tibble(x = df$price) |>
  opt_bin(x) |>
  pull(value)

par(mfrow = c(1, 2))
hist(df$price, main = "Price Histogram - Default binning",
     xlab = "Price", ylab = "Frequency")
hist(df$price, breaks = breaks, main = "Price Histogram - Optimal binning",
     xlab = "Price", ylab = "Frequency")
par(mfrow = c(1, 1))

df |>
  ggplot(aes(x = carat, y = price, fill = cut)) +
  geom_hex(bins = length(breaks), alpha = 1/5) +
  facet_wrap(~ clarity, scales = "free") +
  theme_minimal() +
  labs(
    x = "Carat",
    y = "Price",
    title = "Diamonds Data",
    fill = "Cut"
  ) +
  hr_scale_color_colorblind()

df |>
  ggplot(aes(x = carat, y = price, fill = cut)) +
  geom_boxplot(alpha = 1/5, outlier.color = "lightgrey") +
  facet_wrap(~ clarity, scales = "free") +
  theme_minimal() +
  labs(
    x = "Carat",
    y = "Price",
    title = "Diamonds Data",
    fille = "Cut"
  ) +
  hr_scale_color_colorblind()

df |>
  summarize(m = mean(price), .by = c(clarity, cut)) |> 
  ggplot(aes(x = clarity, y = m, group = cut, color = cut)) +
  geom_point() +
  geom_line() +
  geom_smooth() +
  facet_wrap(~cut, ncol = 2) +
  labs(x= "Clarity", 
       y = "Mean Price", 
       title = "Mean Price by Clarity and Cut",
       color = "Cut") +
  theme_minimal() +
  hr_scale_color_colorblind()

df |>
  summarize(m = mean(price/carat), .by = c(cut, color, clarity)) |>
  ggplot(aes(x = color, y = m, group = clarity, color = clarity)) +
  geom_point() +
  geom_line() +
  facet_wrap(~ cut, ncol = 2, scales = "free") +
  labs(x= "Clarity", 
       y = "Mean Price", 
       title = "Mean Price per Carat by Clarity, Color and Cut",
       color = "Cut") +
  theme_minimal() +
  hr_scale_color_colorblind()

df |>
  ggplot(aes(x = price)) +
  geom_histogram(breaks = breaks, fill = "lightblue",
                 color = "black") +
  theme_minimal() +
  facet_wrap(~ cut, ncol = 2, scales = 'free') +
  labs(x = "Price", y = "Frequency", title = "Price Histogram by Cut")

