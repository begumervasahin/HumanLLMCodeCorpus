def main():
    today_minutes = 24 * 60
    working_hours = float(input("How many hours will you work today?\n"))
    sleeping_hours = float(input("How many hours will you sleep today?\n"))
    eating_hours = float(input("How many hours will you spend eating today?\n"))
    driving_hours = float(input("How many hours will you spend driving today?\n"))
    cleaning_hours = float(input("How many hours will you spend cleaning today?\n"))
    working_minutes = working_hours * 60
    sleeping_minutes = sleeping_hours * 60
    eating_minutes = eating_hours * 60
    driving_minutes = driving_hours * 60
    cleaning_minutes = cleaning_hours * 60
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