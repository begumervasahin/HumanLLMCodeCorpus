def fonk1(b1):
  if b1 < 2:
    return False
  elif b1 = = 2:
    return True
  for b2 in range(2, b1):
    if b1 % b2 = = 0:
      return False
      break
  else:
    return True
print(fonk1(21))
def fonk2(b2):
  if b2 < 2:
    return False
  elif b2 = = 2:
    return False
  else:
    for b3 in range(2, b2):
      print(b3)
      if b2 % b3 = = 0:
        return False
    else:
      return True
print(fonk2(18))
def fonk3(b2):
  if b2 < 2:
    return False
  else:
    for b3 in range(2, b2 - 1):
      if b2 % b3 = = 0:
        return False
    else:
      return True
print(fonk3(15))