def get_minutes(prompt):
    hours = float(input(prompt))
    return hours * 60
def main():
    TOTAL_MINUTES_IN_DAY = 24 * 60
    working_minutes = get_minutes("How many hours will you work today?\n")
    sleeping_minutes = get_minutes("How many hours will you sleep today?\n")
    eating_minutes = get_minutes("How many hours will you spend eating today?\n")
    driving_minutes = get_minutes("How many hours will you spend driving today?\n")
    cleaning_minutes = get_minutes("How many hours will you spend cleaning today?\n")
    total_used_minutes = (
        working_minutes +
        sleeping_minutes +
        eating_minutes +
        driving_minutes +
        cleaning_minutes
    )
    remaining_minutes = TOTAL_MINUTES_IN_DAY - total_used_minutes
    sessions = remaining_minutes
    thoughtful_minutes = remaining_minutes % 60
    print(f"{thoughtful_minutes} minutes available today to do something thoughtful for someone.")
    print(f"{sessions} sessions available today for creating something!")
if __name__ == "__main__":
    main()