library(taskscheduleR)

# Create a task scheduler job that runs the script every hour
taskscheduler_create(
  taskname = "Hello World Hourly",
  rscript = "hello_world.R",
  schedule = "0 * * * *"
)

# Create a task scheduler job that runs the script once a day at 10:00 AM
taskscheduler_create(
  taskname = "Hello World Daily",
  rscript = "hello_world.R",
  schedule = "0 10 * * *"
)
