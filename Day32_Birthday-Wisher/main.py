### main.py ###

# ==============================================
# 1. Configuration Section
# ==============================================
# This section contains settings for email credentials and file paths.

# 1.1 Email account credentials.
my_email = "nymilitarypolice@gmail.com"  # Sender's email address.
password = "bgkw fsho zqhl gkll"  # Sender's email password or app-specific password.

# 1.2 File paths.
birthday_file = "birthdays.csv"  # Path to the CSV file with birthday data.
template_folder = "letter_templates"  # Path to the folder containing email templates.

# ==============================================
# 2. Import Section
# ==============================================
# This section imports required libraries for the script's functionality.

import smtplib  # For SMTP protocol to send emails.
import socket  # To check internet connectivity.
import datetime as dt  # To work with dates and times.
import random  # To select a random template.
import csv  # To handle CSV file operations.
import os  # To handle file system paths.
from email.mime.text import MIMEText  # To create text-based email parts.
from email.mime.multipart import (
    MIMEMultipart,
)  # To create multipart/alternative email bodies.

# ==============================================
# 3. Helper Functions
# ==============================================
# These functions perform specific tasks to support the main functionality.


# 3.1 Function to read birthdays from the CSV file.
def read_birthdays(filename):
    """Reads birthday data from the given CSV file and returns a list of dictionaries."""
    birthdays = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            birthdays = [row for row in csv_reader]
    except FileNotFoundError:
        print(f"The file {filename} was not found. Check the file path.")
    return birthdays


# 3.2 Function to check for today's birthdays.
def check_todays_birthdays(birthdays):
    """Filters and returns birthdays that match today's date."""
    today = dt.datetime.now()
    return [
        bday
        for bday in birthdays
        if today.month == int(bday["month"]) and today.day == int(bday["day"])
    ]


# 3.3 Function to retrieve a random letter template.
def get_random_letter_template(folder):
    """Selects and returns the content of a random letter template from the specified folder."""
    templates = [
        f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))
    ]
    selected_template = random.choice(templates)
    with open(os.path.join(folder, selected_template), "r", encoding="utf-8") as file:
        content = file.read()
    return content


# 3.4 Function to send an email.
def send_email(to_email, subject, html_content):
    """Composes and sends an email with the given subject and HTML content."""
    try:
        message = MIMEMultipart("alternative")
        message["From"] = my_email
        message["To"] = to_email
        message["Subject"] = subject
        part = MIMEText(html_content, "html")
        message.attach(part)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.send_message(message)
            print(f"Email sent to {to_email} successfully.")
    except Exception as e:
        print(f"An error occurred while sending the email to {to_email}: {e}")


# 3.5 Function to get a random quote.
def get_random_quote(file_path):
    """Reads quotes from the given file and returns a random one."""
    with open(file_path, "r", encoding="utf-8") as file:
        quotes = file.readlines()
    return random.choice(quotes).strip()


# ==============================================
# 4. Main Execution Block
# ==============================================
# The script's main logic for processing and sending birthday emails.

if __name__ == "__main__":
    # 4.1 Read all birthday entries from the CSV file.
    all_birthdays = read_birthdays(birthday_file)

    # 4.2 Check for any birthdays today.
    birthdays_today = check_todays_birthdays(all_birthdays)

    # 4.3 For each birthday match, send a personalized email.
    for birthday in birthdays_today:
        # 4.3.1 Get a random quote.
        quote = get_random_quote("./Day32_Birthday-Wisher/quotes.txt")

        # Fetch the email template and replace placeholder with the name.
        personalized_message = get_random_letter_template(template_folder).replace(
            "[NAME]", birthday["name"]
        )

        # Add the quote to the personalized message.
        personalized_message += f"\n\nHere is a quote for your birthday:\n{quote}"

        # Replace newlines in the personalized message with HTML line breaks.
        personalized_content = personalized_message.replace("\n", "<br>")

        # Define the HTML content for the email.
        html_content = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Happy Birthday!</title>
                <style>
                    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
                    body {{
                        font-family: 'Roboto', sans-serif;
                        margin: 0;
                        padding: 0;
                        background-color: #101010;
                        color: #c1c1c1;
                    }}
                    .email-container {{
                        max-width: 600px;
                        margin: 40px auto;
                        background: linear-gradient(145deg, #1d1d1d, #262626);
                        border-radius: 12px;
                        overflow: hidden;
                        box-shadow: 0 0 15px rgba(0,0,0,0.5);
                    }}
                    .header {{
                        padding: 20px;
                        background: linear-gradient(145deg, #0d47a1, #2196f3);
                        text-align: center;
                    }}
                    .header h1 {{
                        color: #ffffff;
                        font-size: 24px;
                        margin: 0;
                    }}
                    .content {{
                        padding: 20px;
                        text-align: center;
                        background-color: #1d1d1d;
                    }}
                    .content p {{
                        color: #c1c1c1;
                        line-height: 1.5;
                    }}
                    .footer {{
                        font-size: 12px;
                        text-align: center;
                        padding: 10px;
                        background: #0d47a1;
                        color: white;
                    }}
                </style>
            </head>
            <body>
                <div class="email-container">
                    <div class="header">
                        <h1>Happy Birthday, {birthday["name"]}!</h1>
                    </div>
                    <div class="content">
                        <p>{personalized_content}</p>
                    </div>
                    <div class="footer">
                        Sent with love by PyFlow Assistant.
                    </div>
                </div>
            </body>
            </html>
        """.strip()

        # Send the email.
        send_email(birthday["email"], "Happy Birthday!", html_content)
