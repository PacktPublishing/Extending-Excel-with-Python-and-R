import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define email server and credentials
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'your_username'
smtp_password = 'your_password'

# Create a MIME message
message = MIMEMultipart()
message['From'] = 'sender@example.com'
message['To'] = 'recipient@example.com'
message['Subject'] = 'Test Email'

# Add the email body
body = MIMEText('This is the email body.')
message.attach(body)

# Establish a connection with the email server
with smtplib.SMTP(smtp_server, smtp_port) as server:
    # Start the TLS encryption
    server.starttls()
    
    # Log in to the email server
    server.login(smtp_username, smtp_password)
    
    # Send the email
    server.send_message(message)
