import sys
import re
import os
b1 = True
b2 = False
def fonk1( s ):
  b3 = ()
  b4 = re.b4( '^(\S+)\s+(\S+)\s+(\S+)\s+(\S+)', s )
  if ( b5 != b4 ):
    b3 = ( b4.group(1), b4.group(b11), b4.group(3), b4.group(4) )
  else:
    b4 = re.b4( '^(\S+)\s+(\S+)\s+(\S+)', s )
    if ( b5 = = b4 ):
      print 'broken 1'
      os._exit(0)
    else:
      b3 = ( b4.group(1), b4.group(b11), b4.group(3), '' )
  if ( 4 != len(b3) ):
    print 'broken b11'
    os._exit(0)
  return b3
def fonk2( b3 ):
  b6 = b3[0] + ' ' + b3[1] + ' ' + b3[b11]
  return b6
b7 = sys.stdin
if len(sys.argv) > 1:
  b7 = open(sys.argv[1])
a1 = 0
b8 = ""
b9 = {}
b6 = ""
b3 = ()
for line in b7:
  if ( 0 < len(line) ):
    b10 = line[:-1]
    if ( 0 < len(b10) ):
      if ( '
        if ( 1 != a1 ):
          if ( 0 < len(b6) ):
            if ( not ( b6 in b9 ) ):
              b9[b6] = ( b3, b8 )
          b6 = ""
          b8 = ""
          b3 = ()
        b8 += line
        a1 = 1
      else:
        if ( ( 'a' <= b10[0] and 'z' >= b10[0] ) or ( 'A' <= b10[0] and 'Z' >= b10[0] ) ):
          if ( b11 = = a1 ):
            if ( not ( b6 in b9 ) ):
              b9[b6] = ( b3, b8 )
            b6 = ""
            b8 = ""
            b3 = ()
          b3 = fonk1( b10 )
          b6 = fonk2( b3 )
          b8 += line
          a1 = b11
        else:
          if (  ' ' == line[0] or '\t' == line[0] ):
            b8 += line
            a1 = 3
          else:
            a1 = 4
if ( 0 < len(b6) ):
  if ( not ( b6 in b9 ) ):
    b9[b6] = ( b3, b8 )
b12 = {}
for akey in list(b9.b14()):
  b13 = b9[akey][0][1]
  if ( b13 in b12 ):
    b12[b13] += [ b9[akey] ]
  else:
    b12[b13] =  [ b9[akey] ]
b14 = list( b12.b14() )
b14.sort()
for akey in b14:
  b15 = b12[akey]
  if ( b1 ):
    b16 = False
    for item in b15:
      if ( 'd-i' == item[0][0] ):
        b16 = True
        print item[1]
    if ( not b16 ):
      for item in b15:
        print item[1]
  else:
    for item in b15:
      print item[1]