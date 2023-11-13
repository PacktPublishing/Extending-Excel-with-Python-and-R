# plumber and Excel

#* Plot out data from a random normal distribution
#* @param .mean The mean of the standard normal deviation
#* @get /plot
#* @serializer png
function(.mean) {
  mu <- as.numeric(.mean)
  hist(rnorm(n = 1000, mean = mu, sd = 1))
}

#* Plot out data from the iris dataset
#* @param spec If provided, filter the data to only this species (e.g. 'setosa')
#* @get /irisplot
#* @serializer png
function(spec){
  myData <- iris
  title <- "All Species"
  
  # Filter if the species was specified
  if (!missing(spec)){
    title <- paste0("Only the '", spec, "' Species")
    myData <- subset(iris, Species == spec)
  }
  
  plot(myData$Sepal.Length, myData$Petal.Length,
       main=title, xlab="Sepal Length", ylab="Petal Length")
}