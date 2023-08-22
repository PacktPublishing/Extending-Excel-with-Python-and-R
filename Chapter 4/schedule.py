import schedule
import time

def job():
    print("This job is executed every day at 8:00 AM.")

# Schedule the job to run every day at 8:00 AM
schedule.every().day.at("08:00").do(job)

# Keep the program running
while True:
    schedule.run_pending()
    time.sleep(1)
