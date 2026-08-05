import requests
from datetime import datetime, UTC
import smtplib
import os
import time

MY_EMAIL = os.environ.get("MY_EMAIL", "your_email@gmail.com")
MY_PASSWORD = os.environ.get("MY_EMAIL_APP_PASSWORD", "your_app_password")


# NOTE: These are set to match the ISS's live position (as of this test)
# so is_iss_overhead() will return True right now. Replace with your real
# home coordinates for normal use.
MY_LAT = 21.6785
MY_LONG = -141.8920


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now(UTC)

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True
    return False


while True:
    overhead = is_iss_overhead()
    night = is_night()
    print(f"Checked at {datetime.now(UTC)} — ISS overhead: {overhead}, Night: {night}")

    if overhead and night:
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up \n\nThe ISS is above you in the sky!"
        )
        connection.close()
        print("Email sent!")

    time.sleep(60)