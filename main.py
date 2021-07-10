# import modules
import smtplib  # for email sending
import random  # for random generating
import pandas  # for csv data reading
import datetime as dt  # for time and date

EMAIL = "your email"
PASSWORD = "your password"
letter_paths = ['letter_templates/letter_1.txt', 'letter_templates/letter_2.txt', 'letter_templates/letter_3.txt']

# genertaing the date
today = dt.datetime.now()
day_today = today.day
month_today = today.month
print(month_today)

# opening the file that have birthday details
data = pandas.read_csv("birthdays.csv")
names = data["name"]
name_list = names.to_list()

# creating a for loop for loop through names in name_list
for name in name_list:
    # extracting datas from csv file
    name_data = data[data.name == name]
    email = name_data["email"].to_string(index=False)
    day = int(name_data["day"].to_string(index=False))
    month = int(name_data["month"].to_string(index=False))

    # checking the dates
    if day == day_today and month == month_today:
        letter_selected = random.choice(letter_paths)

        # opening the random letter and replacing the [NAME] with name
        with open(letter_selected, "r") as letter_data:
            letter = letter_data.read()
            replaced_letter = letter.replace("[NAME]", name)

        with open(letter_selected, "r") as letter_data:
            letter = letter_data.read()
            letter.replace(name, "[NAME]")

        # # creating a smptp connection to send email
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()  # for encryption of the email
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=email,
                            msg=f"Subject:Happy Birthday {name}!!!!! \n\n{replaced_letter}")
        connection.close
