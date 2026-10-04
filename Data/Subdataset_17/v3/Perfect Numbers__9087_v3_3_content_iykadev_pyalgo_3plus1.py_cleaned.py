def collatz_sequence_steps(n: int) -> None:
    step_count = 0
    while n > 1:
        step_count += 1
        if n % 2 == 0:
            n
        else:
            n = 3 * n + 1
        print(f"Step {step_count}: {n}")
def main(start_value: int) -> None:
    print(f"Starting Collatz sequence with initial value: {start_value}")
    collatz_sequence_steps(start_value)
if __name__ == "__main__":
    start_value = 15000
    main(start_value)