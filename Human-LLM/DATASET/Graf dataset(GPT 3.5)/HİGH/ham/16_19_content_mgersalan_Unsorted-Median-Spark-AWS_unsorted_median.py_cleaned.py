% pyspark
from pyspark import SparkContext
import sys
import os
import random
import math
def fonk1(fn):
  b1 = sc.textFile(fn)
  b2 = b1.map(lambda s: float(s))
  b2.cache()
  return b2
def fonk2(b2):
  b3 = b2.sum() / b2.count()
  return b3
def fonk3(b2):
  b4 = b2.min()
  return b4
def fonk4(b2):
  b5 = b2.max()
  return b5
def fonk5(b2):
  b6 = b2.b6()
  return b6
def fonk6(b2):
  b7 = b2.count()
  b8 = round(b7 / 2) + 1
  if (b7 % 2 != 0):
    b9 = fonk7(b2, b8)
    return b9
  else:
    b10 = fonk7(b2, b8)
    b11 = fonk7(b2, b8 - 1)
    print("b12 = " + str(b10))
    print("b13 = " + str(b11))
    b9 = (b10 + b11) / 2
    return b9
def fonk7(Set, b8):
  b7 = Set.count()
  b14 = Set.takeSample(False, 1, seed=0)
  b15 = b14[0]
  b16 = Set.filter(lambda x: x < b15)
  b17 = Set.filter(lambda x: x > b15)
  if b8 = = (b16.count() + 1):
    return b15
  if b8 <= (b16.count()):
    b18 = fonk7(b16, b8)
    return b18
  if b8 > (b16.count() + 1):
    b18 = fonk7(b17, b8 - (b16.count() + 1))
    return b18
b19 = fonk1('/Users/Gur/Desktop/b1-1.txt')
b3 = fonk2(b19)
b20 = "The average of b1 set is " + str(b3)
print(b20)
b21 = fonk3(b19)
b22 = "The minimum of b1 set is " + str(b21)
print(b22)
b23 = fonk4(b19)
b24 = "The maximum of b1 set is " + str(b23)
print(b24)
b25 = fonk5(b19)
b26 = "The b6 of b1 set is " + str(b25)
print(b26)
b27 = fonk6(b19)
print("Median is equal to " + str(b27))