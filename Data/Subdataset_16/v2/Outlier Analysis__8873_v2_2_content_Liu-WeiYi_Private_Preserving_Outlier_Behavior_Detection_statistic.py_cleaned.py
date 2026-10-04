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
    b3 = len(b1)
    for count, user in enumerate(b1.keys(), b4 = 1):
        b5 = 100 * count / b3
        sys.stdout.write('\r>> Processing Users............ %.2f %%' % b5)
        sys.stdout.flush()
        b6 = b1[user]["Reach_Time"]
        for time in b6.keys():
            b7 = b6[time].keys()
            b2.update(b7)
    b8 = len(b2)
    print(f'\nTotal number of b2: {b8}')
def fonk3(user_time_file):
    print('Processing time group...')
    with open(user_time_file) as f:
        b9 = json.load(f)
    a1 = 0
    b3 = len(b9)
    for count, user in enumerate(b9.keys(), b4 = 1):
        b5 = 100 * count / b3
        sys.stdout.write('\r>> Processing Users............ %.2f %%' % b5)
        sys.stdout.flush()
        b10 = b9[user]
        _, b11 = analysis_Time(user, b10)
        a1 += len(b11)
    print(f'\nTotal number of time intervals: {a1}')
def fonk4(user_info_file):
    print('Processing features...')
    with open(user_info_file) as f:
        b1 = json.load(f)
    a2 = 0
    a3 = 0
    b3 = len(b1)
    for count, user in enumerate(b1.keys(), b4 = 1):
        b5 = 100 * count / b3
        sys.stdout.write('\r>> Processing Users............ %.2f %%' % b5)
        sys.stdout.flush()
        b6 = b1[user]["Reach_Time"]
        for time in b6.keys():
            for user_detail in b6[time].keys():
                a2 += len(b6[time][user_detail]["Keyword"])
                a3 += len(b6[time][user_detail]["Device_IP"])
    b12 = a2 / b3
    b13 = a3 / b3
    print(f'\nTotal keywords: {a2}')
    print(f'Average keywords per user: {b12:.2f}')
    print(f'Total IP addresses: {a3}')
    print(f'Average IP addresses per user: {b13:.2f}')
def fonk5():
    if len(sys.argv) < 2:
        print("Please provide an argument (0, 1, or 2).")
        return
    b14 = sys.argv[1]
    if b14 = = '0':
        fonk2('b1.json')
    elif b14 = = '1':
        fonk3('user_time_info.json')
    elif b14 = = '2':
        fonk4('b1.json')
    else:
        print("Invalid b14. Please provide 0, 1, or 2.")
if b15 = = "__main__":
    fonk5()