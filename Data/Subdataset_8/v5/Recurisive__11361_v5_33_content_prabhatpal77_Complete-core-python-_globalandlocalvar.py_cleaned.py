
global_variable_a = 1000
global_variable_b = 2000
def function_f1():
    local_variable_p = 3000
    local_variable_q = 4000
    print("Variables accessible in function_f1:")
    print("global_variable_a:", global_variable_a)
    print("global_variable_b:", global_variable_b)
    print("local_variable_p:", local_variable_p)
    print("local_variable_q:", local_variable_q)
def function_f2():
    local_variable_x = 5000
    local_variable_y = 6000
    print("\nVariables accessible in function_f2:")
    print("global_variable_a:", global_variable_a)
    print("global_variable_b:", global_variable_b)
    print("local_variable_x:", local_variable_x)
    print("local_variable_y:", local_variable_y)
function_f1()
function_f2()