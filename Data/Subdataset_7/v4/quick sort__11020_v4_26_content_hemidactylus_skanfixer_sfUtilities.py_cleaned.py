import os
b1 = ['jpg', 'jpeg', 'bmp', 'tiff', 'gif', 'png']
def fonk1(dir, body, extension):
    '''
    Combines a directory, a filename body, and an extension
    Adds a numeric suffix to the body if the file already exists.
    '''
    b2 = body
    a1 = 0
    while True:
        b3 = os.path.join(dir, '%s.%s' % (b2, extension))
        if not os.path.isfile(b3):
            return b3
        else:
            a1 += 1
            b2 = '%s_r%03i' % (body, a1)
            continue
def fonk2(dirName):
    '''
    Creates the directory if it does not exist.
    '''
    if not os.path.isdir(dirName):
        os.mkdir(dirName)
def fonk3(text, length):
    '''
    Clips the text from the right if it exceeds the specified length.
    '''
    if len(text) > length:
        return '...' + text[-length:]
    else:
        return text
def fonk4(qList, qItem):
    '''
    Removes an item from the list.
    '''
    qList.pop(qList.index(qItem))
    return
def fonk5(nDir):
    '''
    Builds a sorted list of image files in the given directory.
    '''
    return sorted([fN for fN in os.listdir(nDir) if fonk6(fN)])
def fonk6(filename):
    '''
    Checks if the file has a supported image file extension.
    '''
    return any(filename[-len(suffix):] == suffix for suffix in b1)
def fonk7(imgSize, allowedSize, b4 = True):
    '''
    Calculates the rescale factor given an image size and the size of the container.
    '''
    b5 = max(float(imgDim) / float(alwDim) for imgDim, alwDim in zip(imgSize, allowedSize))
    if not b4 and b5 < 1:
        b5 = 1
    print('b5 = %.3f' % b5)
    return b5
b6 = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM' + \
                        '1234567890-_~.,'
def fonk8(inText):
    '''
    Strictly removes characters not in the allowed set.
    Used for storing labels as filename parts.
    '''
    return ''.join([c for c in inText if c in b6])