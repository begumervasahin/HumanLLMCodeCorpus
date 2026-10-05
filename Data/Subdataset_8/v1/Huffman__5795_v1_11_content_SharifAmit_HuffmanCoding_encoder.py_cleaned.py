
with open("input.txt", "r") as f:
    s = f.readline().lower()
t = list(set(s))
print("The String:", s)
print("The char list:", t)
b = [0] * len(t)
for x in s:
    count = s.count(x)
    y = t.index(x)
    if b[y] == 0:
        b[y] = count
print("Frequency Table before sorting:")
print(b)
new = []
newchar = []
while b:
    max_freq = max(b)
    index = b.index(max_freq)
    new.append(max_freq)
    newchar.append(t[index])
    b.pop(index)
    t.pop(index)
print("Frequency Table after sorting:")
print(new)
print(newchar)
k = sum(1 for x in new if x != 0)
j = 2 * k - 1
print("Number of nodes in the tree:", j)
print("Number of leafs in the tree:", k)
encoder = ["null"] * k
bintree = list(new)
strtree = list(newchar)
while len(bintree) > 1:
    right = min(bintree)
    rightstr = strtree[bintree.index(right)]
    bintree.remove(right)
    strtree.remove(rightstr)
    left = min(bintree)
    leftstr = strtree[bintree.index(left)]
    bintree.remove(left)
    strtree.remove(leftstr)
    summation = right + left
    strsum = leftstr + rightstr
    strtree.append(strsum)
    bintree.append(summation)
    for char in rightstr:
        ci = newchar.index(char)
        encoder[ci] = "0" + encoder[ci]
    for char in leftstr:
        ci = newchar.index(char)
        encoder[ci] = "1" + encoder[ci]
print("Encoder:", encoder)
encoded_string = ""
for char in s:
    index = newchar.index(char)
    encoded_string += encoder[index]
print("Encoded String:", encoded_string)
with open("output.txt", "w") as g:
    g.write(encoded_string)
with open("dictionary.txt", "w") as p:
    for i in range(len(encoder)):
        q = newchar[i]
        t = encoder[i]
        w = q + "=" + t
        print(w)
        p.write(w + "\n")