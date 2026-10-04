def get_minutes(prompt):
    hours = float(input(prompt))
    return hours * 60
def main():
    TOTAL_MINUTES_IN_DAY = 24 * 60
    prompts = [
        "How many hours will you work today?\n",
        "How many hours will you sleep today?\n",
        "How many hours will you spend eating today?\n",
        "How many hours will you spend driving today?\n",
        "How many hours will you spend cleaning today?\n"
    ]
    total_used_minutes = sum(get_minutes(prompt) for prompt in prompts)
    remaining_minutes = TOTAL_MINUTES_IN_DAY - total_used_minutes
    sessions = remaining_minutes
    thoughtful_minutes = remaining_minutes % 60
    print(f"{thoughtful_minutes} minutes available today to do something thoughtful for someone.")
    print(f"{sessions} sessions available today for creating something!")
if __name__ == "__main__":
    main()