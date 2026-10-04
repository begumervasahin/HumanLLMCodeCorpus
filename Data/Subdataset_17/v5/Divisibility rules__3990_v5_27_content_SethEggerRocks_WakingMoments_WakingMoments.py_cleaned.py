def get_minutes(prompt):
    hours = float(input(prompt))
    return hours * 60
def main():
    TOTAL_MINUTES_IN_DAY = 24 * 60
    activities = {
        "work": "How many hours will you work today?\n",
        "sleep": "How many hours will you sleep today?\n",
        "eat": "How many hours will you spend eating today?\n",
        "drive": "How many hours will you spend driving today?\n",
        "clean": "How many hours will you spend cleaning today?\n"
    }
    total_used_minutes = sum(get_minutes(prompt) for prompt in activities.values())
    remaining_minutes = TOTAL_MINUTES_IN_DAY - total_used_minutes
    sessions = remaining_minutes
    thoughtful_minutes = remaining_minutes % 60
    print(f"{thoughtful_minutes} minutes available today to do something thoughtful for someone.")
    print(f"{sessions} sessions available today for creating something!")
if __name__ == "__main__":
    main()