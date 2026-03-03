library("tcltk")
tkmessageBox(
  title='Message',
  message = paste0("Hello, it is: ", Sys.time()), 
  type = "ok"
  )
