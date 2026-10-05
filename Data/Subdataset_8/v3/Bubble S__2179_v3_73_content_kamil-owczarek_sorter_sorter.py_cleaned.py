import datetime
from configparser import ConfigParser
CONFIG_FILE = 'config.ini'
INPUT_FILE = 'input.txt'
def read_config():
    config = ConfigParser()
    config.read(CONFIG_FILE)
    return config
def open_input_file(input_file):
    try:
        with open(input_file, "r") as f:
            data = eval(f.readline())
        return data
    except FileNotFoundError:
        print("Input file not found.")
        return None
    except Exception as e:
        print("Error reading input file:", e)
        return None
def bubble_sort(element_list):
    n = len(element_list)
    for i in range(n):
        for j in range(n - i - 1):
            if element_list[j] > element_list[j + 1]:
                element_list[j], element_list[j + 1] = element_list[j + 1], element_list[j]
def quick_sort(element_list, l=0, r=None):
    if r is None:
        r = len(element_list) - 1
def main():
    config = read_config()
    if not config:
        return
    data = open_input_file(INPUT_FILE)
    if not data:
        return
    while True:
        print()
        ans = input().strip()
        if ans == "1":
            print("Bubble Sort:")
            start = datetime.datetime.now()
            bubble_sort(data[:])
            end = datetime.datetime.now()
            print("Sorted:", data)
            print("Sorted in", (end - start).seconds, "seconds.")
        elif ans == "2":
            print("Quick Sort:")
            start = datetime.datetime.now()
            quick_sort(data[:])
            end = datetime.datetime.now()
            print("Sorted:", data)
            print("Sorted in", (end - start).seconds, "seconds.")
        elif ans.lower() == "w":
            print("Goodbye!")
            break
        else:
            print("Unknown option")
if __name__ == '__main__':
    main()