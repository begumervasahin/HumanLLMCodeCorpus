import json
import sys
def fonk1(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]
def fonk2(user_info_file):
    print('Processing b2 group...')
    with open(user_info_file) as f:
        b1 = json.load(f)
    b2 = set()
    a1 = 0
    b3 = len(b1.keys())
    for user in b1.keys():
        a1 += 1
        b4 = 100 * a1 / b3
        sys.stdout.write('\r>> Processing Users............ %.2f %%' % b4)
        sys.stdout.flush()
        b5 = b1[user]["Reach_Time"]
        for time in b5.keys():
            b6 = b5[time].keys()
            b2.update(b6)
    b7 = len(b2)
    print(f'\nTotal number of b2: {b7}')
def fonk3(user_time_file):
    print('Processing time group...')
    with open(user_time_file) as f:
        b8 = json.load(f)
    a2 = 0
    a1 = 0
    b3 = len(b8.keys())
    for user in b8.keys():
        a1 += 1
        b4 = 100 * a1 / b3
        sys.stdout.write('\r>> Processing Users............ %.2f %%' % b4)
        sys.stdout.flush()
        b9 = b8[user]
        _, b10 = analysis_Time(user, b9)
        a2 += len(b10.keys())
    print(f'\nTotal number of time intervals: {a2}')
def fonk4(user_info_file):
    print('Processing features...')
    with open(user_info_file) as f:
        b1 = json.load(f)
    a3 = 0
    a4 = 0
    a1 = 0
    b3 = len(b1.keys())
    for user in b1.keys():
        a1 += 1
        b4 = 100 * a1 / b3
        sys.stdout.write('\r>> Processing Users............ %.2f %%' % b4)
        sys.stdout.flush()
        b5 = b1[user]["Reach_Time"]
        for time in b5.keys():
            for user in b5[time].keys():
                a3 += len(b5[time][user]["Keyword"])
                a4 += len(b5[time][user]["Device_IP"])
    b11 = a3 / b3
    b12 = a4 / b3
    print(f'\nTotal keywords: {a3}')
    print(f'Average keywords per user: {b11}')
    print(f'Total IP addresses: {a4}')
    print(f'Average IP addresses per user: {b12}')
def fonk5():
    if len(sys.argv) < 2:
        print("Please provide an argument (0, 1, or 2).")
        return
    b13 = sys.argv[1]
    if b13 = = '0':
        fonk2('b1.json')
    elif b13 = = '1':
        fonk3('user_time_info.json')
    elif b13 = = '2':
        fonk4('b1.json')
    else:
        print("Invalid b13. Please provide 0, 1, or 2.")
if b14 = = "__main__":
    fonk5()