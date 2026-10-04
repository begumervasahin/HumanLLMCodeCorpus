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
    for count, user in enumerate(b1, b4 = 1):
        fonk5(count, b3)
        b5 = b1[user]["Reach_Time"]
        for time in b5:
            b6 = b5[time].keys()
            b2.update(b6)
    b7 = len(b2)
    print(f'\nTotal number of b2: {b7}')
def fonk3(user_time_file):
    print('Processing time group...')
    with open(user_time_file) as f:
        b8 = json.load(f)
    a1 = 0
    b3 = len(b8)
    for count, user in enumerate(b8, b4 = 1):
        fonk5(count, b3)
        b9 = b8[user]
        _, b10 = analysis_Time(user, b9)
        a1 += len(b10)
    print(f'\nTotal number of time intervals: {a1}')
def fonk4(user_info_file):
    print('Processing features...')
    with open(user_info_file) as f:
        b1 = json.load(f)
    a2 = 0
    a3 = 0
    b3 = len(b1)
    for count, user in enumerate(b1, b4 = 1):
        fonk5(count, b3)
        b5 = b1[user]["Reach_Time"]
        for time in b5:
            for user_detail in b5[time]:
                a2 += len(b5[time][user_detail]["Keyword"])
                a3 += len(b5[time][user_detail]["Device_IP"])
    b11 = a2 / b3
    b12 = a3 / b3
    print(f'\nTotal keywords: {a2}')
    print(f'Average keywords per user: {b11:.2f}')
    print(f'Total IP addresses: {a3}')
    print(f'Average IP addresses per user: {b12:.2f}')
def fonk5(count, total):
    b13 = 100 * count / total
    sys.stdout.write(f'\r>> Processing Users............ {b13:.2f} %')
    sys.stdout.flush()
def fonk6():
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
    fonk6()