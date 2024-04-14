import os
import random
import datetime as dt
import pandas
import smtplib

my_email = "nameandfamily@gmail.com"
password = "Replace with your APP Password"
folder_path = "./letter_templates"

now = dt.datetime.now()
now_month = now.month
now_day = now.day
now_hour = now.hour
now_minute = now.minute
# print(f"Today is: {now_month}/{now_day} - {now_hour}:{now_minute}")


# List all files in the folder
files = os.listdir(folder_path)
# Filter out only the text files
text_files = [file for file in files if file.endswith(".txt")]
# Select a random text file
random_file = random.choice(text_files)

file_csv_birthdays = pandas.read_csv("birthdays.csv")
data = pandas.DataFrame(file_csv_birthdays)
e = [(row['name'], row['email'], row['year'], row['month'], row['day']) for (index, row) in data.iterrows()]

with open(f"./letter_templates/{random_file}") as file:
    letter_content = file.read()

for name, email, year, month, day in e:
    if month == now_month and day == now_day:
        modified_letter_content = letter_content.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="farjadhesam@gmail.com",
                msg=f"Subject: Happy Birthday \n\n {modified_letter_content}")
