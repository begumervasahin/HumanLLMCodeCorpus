def collatz_sequence_steps(n: int) -> None:
    step_count = 0
    while n > 1:
        step_count += 1
        if n % 2 == 0:
            n
        else:
            n = 3 * n + 1
        print(n)
def main(start_value: int) -> None:
    collatz_sequence_steps(start_value)
if __name__ == "__main__":
    main(15000)