def FibGen(number):
  FibList = []
  curr = 0
  prev1 = 0
  prev2 = 0
  for i in range(1, number):
    if i == 1:
      FibList.append(curr)
      curr = curr + 1
      FibList.append(curr)
      prev2 = prev1
      prev1 = curr
    else:
      curr = prev2 + prev1
      FibList.append(curr)
      prev2 = prev1
      prev1 = curr
  print FibList
while True:
  try:
    number = int(raw_input("How many Fibonacci numbers do you want to see?"))
  except ValueError:
    print "Sorry, I did not understand that input, please input a whole number."
    continue
  if number <= 0:
    print "Sorry, seems like that is not a positive integer, try again please."
    continue
  else:
    print "Producing %s Fibonacci numbers..." % number
    FibGen(number)
    break