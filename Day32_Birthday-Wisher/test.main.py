### 1. Import necessary libraries
import smtplib
import socket
import datetime as dt
import random
import time  # Import the time module for sleep functionality
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

### 2. Define email parameters and read quotes
my_email = "nymilitarypolice@gmail.com"
their_email = "networkdoctor@live.com"
password = "bgkw fsho zqhl gkll"  # Use an App Password if 2FA is enabled


def read_quotes(filename="quotes.txt"):
    with open(filename, "r", encoding="utf-8") as file:
        quotes = file.readlines()
    return [quote.strip() for quote in quotes]


### 3. Function to send the email
def send_motivational_email():
    try:
        quotes = read_quotes()
        selected_quote = random.choice(quotes)

        ### 3.1 Check Internet connection
        socket.create_connection(("www.google.com", 80))
        print("Internet connection successful.")

        ### 3.2 Establish connection to SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            print("Connecting to SMTP server...")
            connection.starttls()  # Secure the connection
            print("Connection secured with TLS.")

            ### 3.3 Attempt login
            connection.login(user=my_email, password=password)
            print("Logged in successfully.")

            ### 3.4 Create and send the email message with HTML formatting
            message = MIMEMultipart("alternative")
            message["From"] = my_email
            message["To"] = their_email
            message["Subject"] = "Your Motivational Quote of the Day"

            # HTML Content with a surprise
            html = f"""\
            <html>
              <body>
                <p>Here's your motivational quote for today:<br>
                   <blockquote>"{selected_quote}"</blockquote>
                </p>

              </body>
            </html>
            """
            part = MIMEText(html, "html")
            message.attach(part)

            ### 3.5 Send the email
            connection.send_message(message)
            print("Email with a surprise sent successfully.")

    except Exception as e:
        ### 3.6 Handle any errors that occur during the email sending process
        print(f"An error occurred: {e}")


### 4. Loop to send the email continuously until manually stopped
while True:
    send_motivational_email()
    print("Waiting for the next iteration...")
    time.sleep(60)  # Wait for 60 seconds (1 minute) before the next email
