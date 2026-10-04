def is_valid_day(day):
    return 1 <= day <= 31
def is_valid_month(month):
    return 1 <= month <= 12
def is_valid_year(year):
    return year >= 1582
def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
def get_days_in_month(month, year):
    days_in_month = {
        1: 31, 2: 29 if is_leap_year(year) else 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    return days_in_month.get(month, 0)
def is_valid_date(day, month, year):
    if not (is_valid_day(day) and is_valid_month(month) and is_valid_year(year)):
        print("La fecha digitada es inválida.")
        return
    if day > get_days_in_month(month, year):
        print("La fecha digitada es inválida.")
    else:
        print("La fecha digitada es válida.")
def main():
    try:
        day = int(input("Digite el día: "))
        month = int(input("Digite el mes: "))
        year = int(input("Digite el año: "))
    except ValueError:
        print("Por favor, ingrese valores enteros válidos para el día, mes y año.")
        return
    is_valid_date(day, month, year)
if __name__ == "__main__":
    main()