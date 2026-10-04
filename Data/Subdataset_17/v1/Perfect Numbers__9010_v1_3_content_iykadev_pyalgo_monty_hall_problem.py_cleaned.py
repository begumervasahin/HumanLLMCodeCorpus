import random
stay = 0
switch = 0
for _ in range(1000):
    lst = [1, 0, 0]
    random.shuffle(lst)
    ran = random.randrange(3)
    user_choice = lst[ran]
    del lst[ran]
    for i in range(len(lst)):
        if lst[i] == 0:
            del lst[i]
            break
    if user_choice == 1:
        stay += 1
    if lst[0] == 1:
        switch += 1
print("Stay =", stay)
print("Switch =", switch)