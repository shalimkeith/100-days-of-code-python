# import smtplib
#
# my_email = "keithfigures2@gmail.com"
# password = "oifx fwed ytli snaa"
#
# with smtplib.SMTP('smtp.gmail.com',587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="shalimkeith@proton.me",
#         msg = "Subject:Hello,Good Day.\n\n Happy Birthday!"
#     )


import datetime as dt

date = dt.datetime.now()

year = date.year
month = date.month
day = date.day
weekday = date.weekday


date_of_birth = dt.datetime(year=1978, month=10, day=10)
print(date_of_birth)

