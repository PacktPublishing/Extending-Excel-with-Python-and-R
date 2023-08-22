import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def task1():
    # Simulate data processing for task 1
    print("Task 1 in progress...")
    # ... your code here ...
    print("Task 1 completed successfully")

def task2():
    # Simulate data processing for task 2
    print("Task 2 in progress...")
    # ... your code here ...
    print("Task 2 completed successfully")

def send_email_notification(task_name, status):
    sender_email = os.environ.get("from_email")
    recipient_email = os.environ.get("to_email")
    
    # Create a multi-part email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    
    if status == "success":
        subject = f"Task {task_name} completed successfully"
        body = f"The task {task_name} has been completed successfully."
    elif status == "error":
        subject = f"Error in task {task_name}"
        body = f"There was an error while executing task {task_name}. Please check the log files or attachments for more information."
        
        # Attach log files or other relevant attachments
        attachment = MIMEText("... attachment content ...")
        attachment.add_header("Content-Disposition", "attachment", filename="log.txt")
        message.attach(attachment)
    
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    
    # Connect to the SMTP server and send the email
    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login(sender_email, os.environ.get("password"))
        server.send_message(message)

# Usage example
task1()
send_email_notification("task1", "success")

task2()
send_email_notification("task2", "error")
