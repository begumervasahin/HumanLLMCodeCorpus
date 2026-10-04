from __future__ import with_statement
def fonk1(file):
    with open(file, 'rb') as fid:
      b1 = fid.read(1)
      b2 = list(b1)
      while b1:
          b1 = fid.read(1)
          b2 = b2 + list(b1)
    fid.close()
    return b2
if b3 = = "__main__":
    fonk1()