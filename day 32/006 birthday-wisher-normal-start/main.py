import datetime as dt
import pandas
import smtplib
import random

MY_EMAIL = "keithfigures2@gmail.com"
MY_PASSWORD = "oifx fwed ytli snaa"

today = dt.datetime.now()
today_tuple = (today.month,today.day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}


if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path= f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as f:
        contents = f.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        # Notice: NO connection.starttls() here!
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}",
        )



