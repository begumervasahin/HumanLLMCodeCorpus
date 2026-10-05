def fonk1(b3):
  b1 = []
  a1 = 0
  a2 = 0
  a3 = 0
  for b2 in range(1, b3):
    if b2 = = 1:
      b1.append(a1)
      a1 = a1 + 1
      b1.append(a1)
      a3 = a2
      a2 = a1
    else:
      a1 = a3 + a2
      b1.append(a1)
      a3 = a2
      a2 = a1
  print b1
while True:
  try:
    b3 = int(raw_input("How many Fibonacci numbers do you want to see?"))
  except ValueError:
    print "Sorry, I did not understand that input, please input a whole b3."
    continue
  if b3 <= 0:
    print "Sorry, seems like that is not a positive integer, try again please."
    continue
  else:
    print "Producing %s Fibonacci numbers..." % b3
    fonk1(b3)
    break