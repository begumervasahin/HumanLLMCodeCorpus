import math
def calculate_e_numbers(start, end):
    for i in range(start, end):
        result = math.exp(1) ** i
        print(result)
def main():
    start_value = 1
    end_value = 100000
    calculate_e_numbers(start_value, end_value)
if __name__ == "__main__":
    main()