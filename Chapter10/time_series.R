# Generate a Random Time Series
# Set seed to make results reproducible
set.seed(123)
# Generate Random Points using a gaussian distribution with mean 0 and sd = 1
n <- 25
x <- rnorm(n)
head(x)

# Make x a ts object
ts_obj <- ts(x)

class(ts_obj)
str(ts_obj)
attributes(ts_obj)
plot(ts_obj)

# Change Start
ts(x, start = 1980)
ts(x, start = c(1980, 05))
ts(x, start = 1980, frequency = 12)
ts(x, start = 1980, frequency = 12/3)
# Change End
ts(x, end = 2023)
ts(x, end = 2023, frequency = 12)
ts(x, end = 2023, frequency = 12/3)

# AirPassengers - Plotting, ACF/PACF
library(readxl)
library(writexl)

# Write Out the AirPassengers dataset to Excel as a data.frame object
write_xlsx(AirPassengers |> as.data.frame(), "./chapter10/airpassengers.xlsx")

# Read the airpassengers.xlsx file in and convert to a ts object starting at 1949
ap_ts <- read_xlsx("./chapter10/airpassengers.xlsx") |>
  ts(start = 1949, frequency = 12)

class(ap_ts)

# Plot the ts object
plot(ap_ts)

# Decomposition and Visualization
plot(decompose(ap_ts))
