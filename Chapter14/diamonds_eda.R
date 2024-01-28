# Library Install
install.packages('scattermore')

# Library Load
library(tidyverse)
library(healthyverse)
library(readxl)
library(scattermore)

# Read data
file_path <- paste0(getwd(), "/Chapter14/")
diamonds <- read_excel(
  path = paste0(file_path, "diamonds.xlsx"),
)

# Visualize Data
hist(diamonds$price)
breaks <- tibble(x = diamonds$price) |>
  opt_bin(x) |>
  pull(value)
hist(diamonds$price, breaks = breaks)

diamonds |>
  ggplot(aes(x = carat, y = price, color = cut)) +
  geom_point(alpha = 0.328) +
  geom_scattermore() +
  facet_wrap(~ clarity, scales = "free") +
  theme_minimal() +
  labs(
    x = "Carat",
    y = "Price",
    title = "Diamonds Data",
    color = "Cut"
  ) +
  hr_scale_color_colorblind()

diamonds |>
  ggplot(aes(x = carat, y = price, fill = cut)) +
  geom_boxplot(alpha = 0.328) +
  facet_wrap(~ clarity, scales = "free") +
  theme_minimal() +
  labs(
    x = "Carat",
    y = "Price",
    title = "Diamonds Data",
    fille = "Cut"
  ) +
  hr_scale_color_colorblind()

diamonds |>
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

diamonds |>
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

diamonds |>
  ggplot(aes(x = price)) +
  geom_histogram(breaks = breaks, fill = "lightblue",
                 color = "black") +
  theme_minimal() +
  facet_wrap(~ cut, ncol = 2, scales = 'free')
