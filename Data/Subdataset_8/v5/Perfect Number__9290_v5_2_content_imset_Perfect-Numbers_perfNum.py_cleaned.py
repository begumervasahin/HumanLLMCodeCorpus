import sys
def check_perfect_number(num):
    factor_list = []
    factor_chk = 1
    while factor_chk < num:
        if num % factor_chk == 0:
            factor_list.append(factor_chk)
        factor_chk += 1
    factor_sum = sum(factor_list)
    return factor_sum == num
def perf_check(action, num):
    if action.lower() not in ['check', 'iterate']:
        print("Invalid action:", action)
        return
    num_chk = int(num) if action.lower() == 'check' else 2
    while num_chk <= int(num):
        if check_perfect_number(num_chk):
            print(str(num_chk) + " is perfect!")
        else:
            print(str(num_chk) + " is not perfect!")
        if action.lower() == 'check':
            break
        else:
            num_chk += 1
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py [check/iterate] [number]")
    else:
        perf_check(sys.argv[1], sys.argv[2])