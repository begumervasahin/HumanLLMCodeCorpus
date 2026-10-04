
colors = {
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "green": (0, 255, 0)
}
def print_colors():
    for color_name, rgb_values in colors.items():
        print(f"{color_name.capitalize()}: {rgb_values}")
def main():
    print_colors()
if __name__ == "__main__":
    main()