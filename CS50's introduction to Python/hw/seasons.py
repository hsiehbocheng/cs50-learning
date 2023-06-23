from datetime import date
import inflect
from datetime import datetime, timedelta
import sys


def main():
    try:
        birthday = input("Date of Birth: ")
        year, month, day = birthday.split("-")
    except ValueError:
        sys.exit("Invalid Date")

    cal(year, month, day)
    # today = date.today()
    # print(str(today))
    # print(date.today())

def cal(year, month, day):
    today = date.today()
    try:
        bday = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid Date")

    diff = today - bday
    print(int(diff.total_seconds() / 60))






if __name__ == '__main__':
    main()