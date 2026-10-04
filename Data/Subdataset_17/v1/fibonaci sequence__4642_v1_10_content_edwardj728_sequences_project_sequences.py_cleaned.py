def main():
    user_input = input("Type in 5 integers of any sequence separated by commas. Example: 1,2,3,4,5: ")
    list_input = user_input.split(",")
    list_int = list(map(int, list_input))
    if len(list_int) != 5:
        print("Please enter exactly 5 integers.")
        return
    list_arith = list_int[1] - list_int[0]
    if all(list_int[i] == list_int[i-1] + list_arith for i in range(1, 5)):
        print("Arithmetic Sequence")
    if all(list_int[i] == list_int[i-1] * 2 for i in range(1, 5)):
        print("This is a Geometric Sequence")
    list_quad1 = list_int[1] - list_int[0]
    list_quad2 = list_int[2] - list_int[1]
    list_diff = list_quad2 - list_quad1
    if list_int[1] == list_int[0] + list_quad1 and list_int[2] == list_int[1] + list_quad2:
        print("This is a Quadratic Sequence")
    cub1 = list_int[1] - list_int[0]
    cub2 = list_int[2] - list_int[1]
    cub3 = list_int[3] - list_int[2]
    cub_r1 = cub3 - cub2
    cub_r2 = cub2 - cub1
    if cub_r1 == cub_r2:
        print("This is a Cubic Sequence")
    fib_chck1 = list_int[0] + list_int[1]
    fib_chck2 = list_int[1] + list_int[2]
    if list_int[2] == fib_chck1 and list_int[3] == fib_chck2:
        print("Fibonacci Sequence")
if __name__ == "__main__":
    main()