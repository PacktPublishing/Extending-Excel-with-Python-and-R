#* Plot out data from a random normal distribution
#* @param .mean The mean of the standard normal distribution
#* @get /plot
#* @serializer png
function(.mean) {
  mu <- as.numeric(.mean)
  hist(rnorm(n = 1000, mean = mu, sd = 1))
}