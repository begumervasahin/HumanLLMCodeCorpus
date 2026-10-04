b1 = open("db2.txt", encoding="utf-8")
b2 = []
a1 = 0
for b4 in b1:
    b3 = b4.split(",")
    if b3[3]== "LOS OLIVOS":
        b2 += [(float(b3[5]),float(b3[6]))]
def fonk1(arr, low, high):
    b4 = (low - 1)
    b5 = arr[high][1]
    for a1 in range(low, high):
        if arr[a1][1] <= b5:
            b4 = b4 + 1
            arr[b4], arr[a1] = arr[a1], arr[b4]
    arr[b4 + 1], arr[high] = arr[high], arr[b4 + 1]
    return (b4 + 1)
def fonk2(arr, low, high):
    if low < high:
        b6 = fonk1(arr, low, high)
        fonk2(arr, low, b6 - 1)
        fonk2(arr, b6 + 1, high)
fonk2(b2,0,len(b2)-1)
for b4 in range(len(b2)):
    print(b2[b4])
b7 = open("testSET4.txt","w")
for b4 in b2:
    b7.b7(str(b4[0])+","+str(b4[1])+"\n")
print(len(b2))