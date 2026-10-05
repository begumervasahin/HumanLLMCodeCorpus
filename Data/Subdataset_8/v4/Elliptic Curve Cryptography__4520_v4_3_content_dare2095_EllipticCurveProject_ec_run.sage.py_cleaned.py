from sage.all import *
prime_modulus = 29579385439865947694694684968492467204765870577
curve_parameters = [32934893483948394, 593439483948394349]
data_path = '/home/landondare/EllipticCurveProject/data.txt'
with open(data_path, 'r') as file:
    lines = file.readlines()
input_values = lines[-1].split(' ')
e, x1, lowest_x2, lowest_y2, lowest_e = map(int, input_values)
field = GF(prime_modulus)
curve = EllipticCurve(GF(prime_modulus), curve_parameters)
start_point = curve.lift_x(x1)
test_point = e * start_point
print("Input values:")
print(f"\te = {e}")
print(f"\tx1 = {x1}")
print(f"\tlowest_x2 = {lowest_x2}")
print(f"\tlowest_y2 = {lowest_y2}")
print(f"\tlowest_e = {lowest_e}")
run_block = 2000000000
write_block = 100000000
while e < run_block:
    if test_point[1] < lowest_y2:
        lowest_x2 = test_point[0]
        lowest_y2 = test_point[1]
        lowest_e = e
        print("New lowest y2 found:")
        print(test_point)
        print(e)
        with open(data_path, "a") as data_file:
            data_file.write("\n\nNew lowest found: " + str(e) + "\n")
            data_file.write(f"{e} {x1} {lowest_x2} {lowest_y2} {lowest_e}")
    if e % write_block == 0:
        with open(data_path, "a") as data_file:
            data_file.write(f"\n\nBlock {e}\n")
            data_file.write(f"{e} {x1} {lowest_x2} {lowest_y2} {lowest_e}")
    e += 1
    test_point += start_point