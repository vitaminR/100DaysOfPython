import smtplib

my_email = "nymilitarypolice@gmail.com"
their_email = "networkdoctor@live.com"
password = "bgkw fsho zqhl gkll"
their_message = "Subject:Hello\n\nThis is the body of my email."

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs=their_email, msg=their_message)
connection.close()
