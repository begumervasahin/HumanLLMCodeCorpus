import math
def main():
    today_minutes = 24 * 60
    working_minutes = float(input("How many hours will you work today?\n")) * 60
    sleeping_minutes = float(input("How many hours will you sleep today?\n")) * 60
    eating_minutes = float(input("How many hours will you spend eating today?\n")) * 60
    driving_minutes = float(input("How many hours will you spend driving today?\n")) * 60
    cleaning_minutes = float(input("How many hours will you spend cleaning today?\n")) * 60
    what_is_left = today_minutes - (working_minutes + sleeping_minutes + eating_minutes +
                                    driving_minutes + cleaning_minutes)
    artistic_windows = 45
    artistic_breaks = 15
    a_wab = 60
    sessions = what_is_left
    thoughtful_minutes = what_is_left % a_wab
    print(f"{thoughtful_minutes} minutes available today to do something thoughtful for someone.")
    print(f"{sessions} sessions available today for creating something!")
if __name__ == "__main__":
    main()