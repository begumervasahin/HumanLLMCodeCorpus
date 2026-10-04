def main():
    TOTAL_MINUTES_IN_DAY = 24 * 60
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
    total_used_minutes = (working_minutes + sleeping_minutes + eating_minutes +
                          driving_minutes + cleaning_minutes)
    remaining_minutes = TOTAL_MINUTES_IN_DAY - total_used_minutes
    sessions = remaining_minutes
    thoughtful_minutes = remaining_minutes % 60
    print(f"{thoughtful_minutes} minutes available today to do something thoughtful for someone.")
    print(f"{sessions} sessions available today for creating something!")
if __name__ == "__main__":
    main()