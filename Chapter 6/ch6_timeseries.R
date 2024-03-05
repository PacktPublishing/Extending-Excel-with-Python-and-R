plot.ts(AirPassengers)
plot(decompose(AirPassengers))

library(healthyR.ts)

ts_brownian_motion() |>
  ts_brownian_motion_plot(t, y)
