import random
import pickle
limit = 30
Dupes = 0
def LoadRes():
    array = []
    twoeM = []
    threeeM = []
    foureM = []
    fiveeM = []
    sixeM = []
    seveneM = []
    Win = []
    with open("Win.txt", 'rb') as f:
        Win = pickle.load(f)
    with open("Two.txt", 'rb') as f:
        twoeM = pickle.load(f)
    with open("Three.txt", 'rb') as f:
        threeeM = pickle.load(f)
    with open("Four.txt", 'rb') as f:
        foureM = pickle.load(f)
    with open("Five.txt", 'rb') as f:
        fiveeM = pickle.load(f)
    with open("Six.txt", 'rb') as f:
        sixeM = pickle.load(f)
    with open("Seven.txt", 'rb') as f:
        seveneM = pickle.load(f)
    return array, twoeM, threeeM, foureM, fiveeM, sixeM, seveneM, Win
def GenerateNumbers(limit):
    N = []
    for x in ["a","b","c","d","e","f","g","h","i"]:
        tmp = False
        while tmp == False:
            globals()[x] = random.randint((limit * -1), limit)
            if ((globals()[x] in N) == False) and ((globals()[x] < limit)):
                N.append(globals()[x])
                tmp = True
    return a, b, c, d, e, f, g, h, i
def most_common(lst, lstt, array, twoeM, threeeM, foureM, fiveeM, sixeM, seveneM, Win, goal):
    Occ = 0
    mcn = max(set(lst), key=lst.count)
    for i in lst:
        if i == mcn:
            Occ += 1
    if Occ == 1:
        array.append(lstt)
    elif Occ == 2:
        twoeM.append(lstt)
    elif Occ == 3:
        threeeM.append(lstt)
    elif Occ == 4:
        foureM.append(lstt)
    elif Occ == 5:
        fiveeM.append(lstt)
    elif Occ == 6:
        sixeM.append(lstt)
    elif Occ == 7:
        seveneM.append(lstt)
    elif Occ == 8:
        Win.append(lstt)
    print(((len(array))+(len(twoeM))+(len(threeeM))+(len(foureM))+(len(fiveeM))+(len(sixeM))+(len(seveneM))+(len(Win))), "/", goal)
    return array, twoeM, threeeM, foureM, fiveeM, sixeM, seveneM, Win
def Calculate(array, twoeM, threeeM, foureM, fiveeM, sixeM, seveneM, Win, a, b, c, d, e, f, g, h, i, goal):
    aa = a * a
    bb = b * b
    cc = c * c
    dd = d * d
    ee = e * e
    ff = f * f
    gg = g * g
    hh = h * h
    ii = i * i
    h1 = aa + bb + cc
    h2 = dd + ee + ff
    h3 = gg + hh + ii
    v1 = aa + dd + gg
    v2 = bb + ee + hh
    v3 = cc + ff + ii
    d1 = aa + ee + ii
    d2 = gg + ee + cc
    SqNumbers = [a, b, c, d, e, f, g, h, i]
    awnsers = [h1, h2, h3, v1, v2, v3, d1, d2]
    array, twoeM, threeeM, foureM, fiveeM, sixeM, seveneM, Win = most_common(awnsers, SqNumbers, array, twoeM, threeeM, foureM, fiveeM, sixeM, seveneM, Win, goal)
    return array, twoeM, threeeM, foureM, fiveeM, sixeM, seveneM, Win
def endingg(array, twoeM, threeeM, foureM, fiveeM, sixeM, seveneM, Win):
    print("Two:")
    print(len(twoeM))
    print("Three:")
    print(len(threeeM))
    print("Four:")
    print(len(foureM))
    print("Five:")
    print(len(fiveeM))
    print(fiveeM)
    print("Six:")
    print(len(sixeM))
    print(sixeM)
    print("Seven:")
    print(len(seveneM))
    print(seveneM)
    print("Win:")
    print(len(Win))
    print(Win)
    print(Dupes, "Where dupes")
    print("Saving Results")
    with open("Win.txt", 'wb') as f:
        pickle.dump(Win, f)
    with open("Two.txt", 'wb') as f:
        pickle.dump(twoeM, f)
    with open("Three.txt", 'wb') as f:
        pickle.dump(threeeM, f)
    with open("Four.txt", 'wb') as f:
        pickle.dump(foureM, f)
    with open("Five.txt", 'wb') as f:
        pickle.dump(fiveeM, f)
    with open("Six.txt", 'wb') as f:
        pickle.dump(sixeM, f)
    with open("Seven.txt", 'wb') as f:
        pickle.dump(seveneM, f)
def removedupe(L):
    if L:
       L.sort()
       last = L[-1]
       for i in range(len(L)-2, -1, -1):
           if last == L[i]:
               del L[i]
           else:
               last = L[i]
    return L
array, twoeM, threeeM, foureM, fiveeM, sixeM, seveneM, Win = LoadRes()
Current = ((len(array))+(len(twoeM))+(len(threeeM))+(len(foureM))+(len(fiveeM))+(len(sixeM))+(len(seveneM))+(len(Win)))
print("Don't run too many tests at once, as results are only saved at the end")
target = (int(input("There are %s current tests. How many more? " % ("{:,d}".format(Current))))) + Current
loops = target - Current
while ((len(array))+(len(twoeM))+(len(threeeM))+(len(foureM))+(len(fiveeM))+(len(sixeM))+(len(seveneM))+(len(Win))) < target:
    a, b, c, d, e, f, g, h, i = GenerateNumbers(limit)
    array, twoeM, threeeM, foureM, fiveeM, sixeM, seveneM, Win = Calculate(array, twoeM, threeeM, foureM, fiveeM, sixeM, seveneM, Win, a, b, c, d, e, f, g, h, i, target)
before = ((len(array))+(len(twoeM))+(len(threeeM))+(len(foureM))+(len(fiveeM))+(len(sixeM))+(len(seveneM))+(len(Win)))
print("Before purification:", "{:,d}".format(before))
print("Removing squares with 0 matching rows")
array = []
afterOne = ((len(array))+(len(twoeM))+(len(threeeM))+(len(foureM))+(len(fiveeM))+(len(sixeM))+(len(seveneM))+(len(Win)))
print("{:,d}".format(before - afterOne), " Removed")
print("Removing duplicates 1/7")
twoeM = removedupe(twoeM)
afterTwo = ((len(array))+(len(twoeM))+(len(threeeM))+(len(foureM))+(len(fiveeM))+(len(sixeM))+(len(seveneM))+(len(Win)))
print("{:,d}".format(afterOne - afterTwo), " Removed")
print("Removing duplicates 2/7")
threeeM = removedupe(threeeM)
afterThree = ((len(array))+(len(twoeM))+(len(threeeM))+(len(foureM))+(len(fiveeM))+(len(sixeM))+(len(seveneM))+(len(Win)))
print("{:,d}".format(afterTwo - afterThree), " Removed")
print("Removing duplicates 3/7")
foureM = removedupe(foureM)
afterFour = ((len(array))+(len(twoeM))+(len(threeeM))+(len(foureM))+(len(fiveeM))+(len(sixeM))+(len(seveneM))+(len(Win)))
print("{:,d}".format(afterThree - afterFour), " Removed")
print("Removing duplicates 4/7")
fiveeM = removedupe(fiveeM)
afterFive = ((len(array))+(len(twoeM))+(len(threeeM))+(len(foureM))+(len(fiveeM))+(len(sixeM))+(len(seveneM))+(len(Win)))
print("{:,d}".format(afterFour - afterFive), " Removed")
print("Removing duplicates 5/7")
sixeM = removedupe(sixeM)
afterSix = ((len(array))+(len(twoeM))+(len(threeeM))+(len(foureM))+(len(fiveeM))+(len(sixeM))+(len(seveneM))+(len(Win)))
print("{:,d}".format(afterFive - afterSix), " Removed")
print("Removing duplicates 6/7")
seveneM = removedupe(seveneM)
afterSeven = ((len(array))+(len(twoeM))+(len(threeeM))+(len(foureM))+(len(fiveeM))+(len(sixeM))+(len(seveneM))+(len(Win)))
print("{:,d}".format(afterSix - afterSeven), " Removed")
print("Removing duplicates 7/7")
Win = removedupe(Win)
afterEight = ((len(array))+(len(twoeM))+(len(threeeM))+(len(foureM))+(len(fiveeM))+(len(sixeM))+(len(seveneM))+(len(Win)))
print("{:,d}".format(afterSeven - afterEight), " Removed")
print("Removing duplicates complete")
print("After purification:", "{:,d}".format((len(array))+(len(twoeM))+(len(threeeM))+(len(foureM))+(len(fiveeM))+(len(sixeM))+(len(seveneM))+(len(Win))))
endingg(array, twoeM, threeeM, foureM, fiveeM, sixeM, seveneM, Win)
input("Press enter to close")