A = 'A'
space = ' '
print("ord(A) = ", hex(ord(A)))
print("ord(space) = ", hex(ord(space)))
axorb = chr(ord(A) ^ ord(space))
print("chr(ord(A) ^ ord(space)) = ", axorb)