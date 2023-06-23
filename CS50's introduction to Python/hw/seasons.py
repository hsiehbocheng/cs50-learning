from datetime import date
import inflect
from datetime import datetime, timedelta
import sys

p = inflect.engine()

def main():
    try:
        birthday = input("Date of Birth: ")
        year, month, day = birthday.split("-")
    except ValueError:
        sys.exit("Invalid Date")

    print(cal(year, month, day))

def cal(year, month, day):
    today = date.today()
    try:
        bday = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid Date")

    diff = today - bday
    minutes = int(diff.total_seconds() / 60)
    msg = p.number_to_words(minutes, andword="") + " minutes"
    return msg.capitalize()






if __name__ == '__main__':
    main()