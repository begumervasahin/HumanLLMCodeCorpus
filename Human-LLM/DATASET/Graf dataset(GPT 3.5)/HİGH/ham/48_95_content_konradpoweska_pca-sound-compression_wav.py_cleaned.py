import numpy as np
import wave, struct
b1 = {
  1: 'b',
  2: 'h'
}
def fonk1(filename):
  b2 = wave.fonk1(filename, 'r')
  b3 = b2.getnchannels()
  b4 = b2.getsampwidth()
  b5 = b2.getframerate()
  b6 = b2.getnframes()
  b7 = b3, b4, b5, b6
  b8 = "<{0}{1}".format(b6, b1[b4])
  b9 = b2.readframes(b6)
  b10 = np.array(struct.unpack(b8, b9))
  b2.close()
  return b7, b10
def fonk2(filename, b7, b10):
  b2 = wave.fonk1(filename, 'w')
  b3, b4, b5, b6 = b7
  b2.setnchannels(b3)
  b2.setsampwidth(b4)
  b2.setframerate(b5)
  b2.setnframes(b6)
  b10 = np.clip(b10[:b6], -2**(b4*8-1), 2**(b4*8-1)-1)
  b8 = "<{0}{1}".format(b6, b1[b4])
  b9 = struct.pack(b8, *b10)
  b2.writeframes(b9)
  b2.close()