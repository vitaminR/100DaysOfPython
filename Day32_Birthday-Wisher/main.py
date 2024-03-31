###1. Import necessary libraries
import smtplib
import socket
import datetime as dt
import random

###2. Define email parameters
my_email = "nymilitarypolice@gmail.com"
their_email = "networkdoctor@live.com"
password = "bgkw fsho zqhl gkll"  # Use an App Password if 2FA is enabled
their_message = "Subject:Hello\n\nThis is the body of my email."

###3. Attempt to send an email with error handling
try:
    ###3.1 Check Internet connection
    socket.create_connection(("www.google.com", 80))
    print("Internet connection successful.")

    ###3.2 Establish connection to SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        print("Connecting to SMTP server...")
        connection.starttls()  # Secure the connection
        print("Connection secured with TLS.")

        ###3.3 Attempt login
        connection.login(user=my_email, password=password)
        print("Logged in successfully.")

        ###3.4 Send the email
        connection.sendmail(from_addr=my_email, to_addrs=their_email, msg=their_message)
        print("Email sent successfully.")

except socket.gaierror:
    ###3.5 Handle errors related to Internet connection
    print("Failed to connect to the Internet. Please check your connection.")
except smtplib.SMTPServerDisconnected:
    ###3.6 Handle errors related to server disconnection
    print(
        "Failed to connect to the SMTP server. Please check the server address and port."
    )
except smtplib.SMTPAuthenticationError:
    ###3.7 Handle errors related to authentication
    print("Authentication failed. Check your email and password/app password.")
except Exception as e:
    ###3.8 Handle any other SMTP or unforeseen errors
    print(f"An error occurred: {e}")


now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()

print(year, month, day)
print(day_of_week)
