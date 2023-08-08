import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, recipient_email, subject, message):
    #SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    #Get the sender password from an environment variable
    sender_password = os.environ.get('EMAIL_PASSWORD')

    if not sender_password:
        print("Error: Email password not set in environment variable.")
        return

    # Create the email message
    email = MIMEMultipart()
    email['From'] = sender_email
    email['To'] = recipient_email
    email['Subject'] = subject

    # Create a MIMEText object with HTML content
    html_content = '''
    <html>
    <body>
        <h1>{}</h1>
        <p>{}</p>
        <p>This is a <strong>bold</strong> example.</p>
        <p>This is an <em>italic</em> example.</p>
    </html>
    </body>
    '''.format(subject, message)

    email.attach(MIMEText(html_content, 'html'))
    
    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, recipient_email, email.as_string())

    # Close the connection
    server.quit()

# Example usage 
sender_email = 'yskomartin@gmail.com'
recipient_email = 'roldhapatacsil09767@gmail.com'
subject = 'Hello form Python email script'
message = 'This is an automated email sent using Python. F _zapier!'

send_email(sender_email, recipient_email, subject, message)