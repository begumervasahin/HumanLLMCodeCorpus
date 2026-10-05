def main():
    MINUTES_PER_HOUR = 60
    ARTISTIC_WINDOW_DURATION = 45
    ARTISTIC_BREAK_DURATION = 15
    working_hours = float(input("How many hours will you work today?\n"))
    sleeping_hours = float(input("How many hours will you sleep today?\n"))
    eating_hours = float(input("How many hours will you spend eating today?\n"))
    driving_hours = float(input("How many hours will you spend driving today?\n"))
    cleaning_hours = float(input("How many hours will you spend cleaning today?\n"))
    working_minutes = working_hours * MINUTES_PER_HOUR
    sleeping_minutes = sleeping_hours * MINUTES_PER_HOUR
    eating_minutes = eating_hours * MINUTES_PER_HOUR
    driving_minutes = driving_hours * MINUTES_PER_HOUR
    cleaning_minutes = cleaning_hours * MINUTES_PER_HOUR
    total_activity_minutes = (
        working_minutes + sleeping_minutes + eating_minutes +
        driving_minutes + cleaning_minutes
    )
    remaining_minutes = 24 * MINUTES_PER_HOUR - total_activity_minutes
    sessions = remaining_minutes
    thoughtful_minutes = remaining_minutes % (ARTISTIC_WINDOW_DURATION + ARTISTIC_BREAK_DURATION)
    print(f"{thoughtful_minutes} minutes available today to do something thoughtful for someone.")
    print(f"{sessions} sessions available today for creating something!")
if __name__ == "__main__":
    main()