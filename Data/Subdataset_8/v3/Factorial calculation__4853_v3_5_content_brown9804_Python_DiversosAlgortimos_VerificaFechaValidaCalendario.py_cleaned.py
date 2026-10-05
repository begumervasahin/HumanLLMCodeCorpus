def is_valid_day(day):
    return 1 <= day <= 31
def is_valid_month(month):
    return 1 <= month <= 12
def is_valid_year(year):
    return year >= 1582
def is_leap_year(year):
    return (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))
def is_valid_date(day, month, year):
    if is_valid_day(day) and is_valid_month(month) and is_valid_year(year):
        if (month in [4, 6, 9, 11]) and day == 31:
            print("The date is invalid.")
        elif month == 2 and (day == 30 or day == 31):
            print("The date is invalid.")
        elif month == 2 and day == 29 and not is_leap_year(year):
            print("The date is invalid.")
        else:
            print("The date is valid.")
    else:
        print("The date is invalid.")
def get_user_input():
    day = int(input("Enter the day: "))
    month = int(input("Enter the month: "))
    year = int(input("Enter the year: "))
    return day, month, year
def main():
    day, month, year = get_user_input()
    is_valid_date(day, month, year)
if __name__ == "__main__":
    main()