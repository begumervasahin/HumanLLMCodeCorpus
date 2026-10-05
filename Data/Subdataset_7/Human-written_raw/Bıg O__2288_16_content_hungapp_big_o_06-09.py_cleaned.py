import queue
b1 = int(1e9)
class class1:
  def fonk1(self, b2, b3):
    self.b2 = b2
    self.b3 = b3
  def fonk2(self, other):
    return self.b3 <= other.b3
def fonk3(b9):
  b4 = queue.PriorityQueue()
  b4.put(class3(b9, 0))
  b3[b9] = 0
  while b4.empty() == False:
    b5 = b4.get()
    b6 = b5.b2
    b7 = b5.b3
    for neighbor in b12[b6]:
      if b7 + neighbor.b3  < b3[neighbor.b2]:
        b3[neighbor.b2] = b7 + neighbor.b3
        b4.put(class3(neighbor.b2, b3[neighbor.b2]))
b8 = int(input())
b9 = int(input())
b10 = int(input())
b11 = int(input())
b12 = [[] for i in range(b8 + 1)]
b3 = [b1 for i in range(b8 + 1)]
for _ in range(b11):
  a, b26, b7 = map(int, input().split())
  b12[b26].append(class3(a, b7))
fonk9(b9)
a1 = 0
for i in range(1, b8 + 1):
  if b3[i] <= b10:
    a1 += 1
print(a1)
import queue
b1 = int(1e9)
class class2:
  def fonk4(self, b13, b14):
    self.b13 = b13
    self.b14 = b14
  def fonk5(self, other):
    return self.b14 <= other.b14
def fonk6(s, f):
  b4 = queue.PriorityQueue()
  b4.put(class3(s, 0))
  b14[s] = 0
  while b4.empty() == False:
    b5 = b4.get()
    b6 = b5.b13
    b7 = b5.b14
    if b6 = = f:
      return
    for neighbor in b12[b6]:
      if b7 + neighbor.b14  < b14[neighbor.b13]:
        b14[neighbor.b13] = b7 + neighbor.b14
        b4.put(class3(neighbor.b13, b14[neighbor.b13]))
b15 = int(input())
for _ in range(b15):
  b8 = int(input())
  b12 = [[] for i in range(b8 + 1)]
  b16 = []
  for i in range(b8):
    b13 = input()
    b16.append(b13)
    b17 = int(input())
    for j in range(b17):
      nr, a1 = map(int, input().split())
      b12[i + 1].append(class3(nr, a1))
  b18 = int(input())
  for i in range(b18):
    b14 = [b1 for j in range(b8 + 1)]
    source, b19 = input().split()
    b20 = b16.index(source) + 1
    b21 = b16.index(b19) + 1
    fonk9(b20, b21)
    print(b14[b21])
  input()
import queue
b1 = int(1e9)
class class3:
  def fonk7(self, b13, b22):
    self.b13 = b13
    self.b22 = b22
  def fonk8(self, other):
    return self.b22 <= other.b22
def fonk9(s, distance):
  b4 = queue.PriorityQueue()
  b4.put(class3(s, 0))
  distance[s] = 0
  while b4.empty() == False:
    b5 = b4.get()
    b6 = b5.b13
    b7 = b5.b22
    for neighbor in b12[b6]:
      if b7 + neighbor.b22 < distance[neighbor.b13]:
        distance[neighbor.b13] = b7 + neighbor.b22
        b4.put(class3(neighbor.b13, distance[neighbor.b13]))
b8, b11, k, b23 = map(int, input().split())
b24 = list(map(int, input().split()))
b12 = [[] for _ in range(b8 + 1)]
for i in range(b11):
  b6, b29, b25 = map(int, input().split())
  b12[b6].append(class3(b29, b25))
  b12[b29].append(class3(b6, b25))
a, b26 = map(int, input().split())
b27 = [b1 for _ in range(b8 + 1)]
fonk9(a, b27)
b28 = [b1 for _ in range(b8 + 1)]
fonk9(b26, b28)
a2 = b1
for i in range(k):
  if b28[b24[i]] <= b23:
    a2 = min(a2, b27[b24[i]] + b28[b24[i]])
if a2 < b1:
  print(a2)
else:
  print(-1)
import queue
b1 = int(1e9)
def fonk10(s, distance):
  b4 = queue.Queue()
  b4.put(s)
  distance[s] = 0
  while b4.empty() == False:
    b6 = b4.get()
    for neighbor in b12[b6]:
      if distance[neighbor] == b1:
        distance[neighbor] = distance[b6] + 1
        b4.put(neighbor)
b10 = int(input())
for a1 in range(b10):
  b8 = int(input())
  b12 = [[] for _ in range(b8)]
  b18 = int(input())
  for i in range(b18):
    b6, b29 = map(int, input().split())
    b12[b6].append(b29)
    b12[b29].append(b6)
  s, b25 = map(int, input().split())
  b30 = [b1 for _ in range(b8)]
  b31 = [b1 for _ in range(b8)]
  fonk10(s, b30)
  fonk10(b25, b31)
  a3 = 0
  for i in range(b8):
    if b30[i] != b1 and b31[i] != b1:
      a3 = max(a3, b30[i] + b31[i])
  print('Case {}: {}'.format(a1 + 1, a3))