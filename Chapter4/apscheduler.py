from apscheduler.schedulers.blocking import BlockingScheduler

# Create a scheduler instance
scheduler = BlockingScheduler()

# Define a task function
def send_email():
    # Code to send an email
    print("Email sent!")

# Schedule the task to run every hour
scheduler.add_job(send_email, 'interval', hours=1)

# Start the scheduler
scheduler.start()
