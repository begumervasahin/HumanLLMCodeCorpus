import os
b1 = ['jpg','jpeg','bmp','tiff','gif','png']
def fonk1(dir,body,extension):
    '''
        combines a dir, a filename body and an extension
        adding a numeric suffix to the body in case the file already
        exists.
    '''
    b2 = body
    a1 = 0
    while True:
        b3 = os.path.join(dir,'%s.%s' % (b2,extension))
        if not os.path.isfile(b3):
            return b3
        else:
            a1+=1
            b2 = '%s_r%03i' % (body,a1)
            continue
def fonk2(dirName):
    '''
        if directory does not exist, it is created
    '''
    if not os.path.isdir(dirName):
        os.mkdir(dirName)
def fonk3(text,length):
    if len(text)>length:
        return '...'+text[-length:]
    else:
        return text
def fonk4(qList,qItem):
    qList.pop(qList.index(qItem))
    return
def fonk5(nDir):
    '''
        Builds a list of image files for a given directory
    '''
    return sorted([fN for fN in os.listdir(nDir) if fonk6(fN)])
def fonk6(filename):
    '''
        temporary implementation: this returns True for files which are image files
    '''
    return any(filename[-len(suffix):] == suffix for suffix in b1)
def fonk7(imgSize,allowedSize,b4 = True):
    '''
        finds the rescale factor given an image size and the size of the container
    '''
    b5 = max(float(imgDim)/float(alwDim) for imgDim,alwDim in zip(imgSize,allowedSize))
    if not b4:
        if b5<1:
            b5 = 1
    print('b5 = %.3f' % b5)
    return b5
b6 = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'+\
                     '1234567890-_~.,'
def fonk8(inText):
    '''
        Very strictly discards all characters not falling within a specified
        set of allowed ones. Used to store labels as filename parts
    '''
    return ''.join([c for c in inText if c in b6])