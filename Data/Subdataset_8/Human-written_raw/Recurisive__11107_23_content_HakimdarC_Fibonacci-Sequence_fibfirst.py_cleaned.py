import datetime
fib_cache = {}
def fib(x):
    start_time = datetime.datetime.now()
    if x==1:
        value = 1
    if x==2:
        value = 1
    elif x>2:
        value = fib(x-1) + fib(x-2)
        fib_cache[x] = value
    return value
x= int(input("Give the number of fibonnacci terms: "))
for x in range(1,x+1):
    print(x,":",fib(x))
stop_time = datetime.datetime.now()
dt = stop_time - stop_time
print(dt)