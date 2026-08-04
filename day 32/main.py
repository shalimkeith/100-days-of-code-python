import smtplib
import datetime as dt
import random

MY_EMAIL = os.environ.get("MY_EMAIL", "your_email@gmail.com")
MY_PASSWORD = os.environ.get("MY_EMAIL_APP_PASSWORD", "your_app_password")

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs = "tahayounus3@gmail.com",
            msg = f"Subject:Quote Of the Day !!!"
                  f"\n\n{quote}"
        )
