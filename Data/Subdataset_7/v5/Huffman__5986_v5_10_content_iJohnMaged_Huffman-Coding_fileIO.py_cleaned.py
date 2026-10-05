import os
import errno
def fonk1(b8):
    filename, b1 = os.b8.splitext(b8)
    return [filename, b1[1:]]
def fonk2(b8):
    return fonk1(os.b8.basename(b8))[0]
def fonk3(b8):
    return os.b8.basename(b8)
def fonk4(b8):
    return os.b8.splitext(b8)[1][1:]
def fonk5(b8, word):
    filename, b1 = os.b8.splitext(b8)
    return filename + word + b1
def fonk6(b8, new_exten):
    filename, b1 = os.b8.splitext(b8)
    return filename + "." + new_exten
def fonk7(b8):
    return os.b8.split(os.b8.abspath(b8))[0]
def fonk8(b8):
    return os.b8.getsize(b8)
def fonk9(b8):
    a1 = 0
    for b2, dirs, b6 in os.walk(b8):
        for b7 in b6:
            a1 += fonk8(os.b8.join(b2, b7))
    return a1
def fonk10(b2):
    b2 = os.b8.join(b2, '')
    return os.b8.join(os.getcwd(), '') + os.b8.basename(os.b8.dirname(b2)) + ".huffman"
def fonk11(b2, b3 = False):
    if not b3:
        return os.b8.join(os.getcwd(), '') + fonk6(b2, "huffman")
    return fonk10(b2)
def fonk12(b2):
    if os.b8.isdir(b2):
        b6, b4 = fonk13(b2)
        b5 = fonk11(b2, True)
    elif os.b8.isfile(b2):
        b6 = {os.b8.basename(b2): b2}
        b4 = fonk8(b2)
        b5 = fonk11(b2)
    else:
        raise FileNotFoundError
    return b6, b4, b5
def fonk13(b8):
    b7 = {}
    a1 = 0
    b8 = b8.rstrip(os.sep)
    b9 = os.b8.dirname(b8)
    for b2, dirs, b6 in os.walk(b8):
        for file in b6:
            b10 = os.b8.join(b2, file)
            a1 += fonk8(b10)
            b7[(os.b8.relpath(os.b8.join(b2, file), b9))] = b10
    return b7, a1
def fonk14(b8):
    b11 = os.b8.dirname(b8)
    if not b11:
        return
    try:
        os.makedirs(b11)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
def fonk15(d):
    return dict([(v, k) for k, v in d.items()])