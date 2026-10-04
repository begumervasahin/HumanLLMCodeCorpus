import os
PIC_SUFFIXES = ['jpg', 'jpeg', 'bmp', 'tiff', 'gif', 'png']
def safeBuildFileName(dir, body, extension):
    _nbody = body
    _niter = 0
    while True:
        fname = os.path.join(dir, f'{_nbody}.{extension}')
        if not os.path.isfile(fname):
            return fname
        else:
            _niter += 1
            _nbody = f'{body}_r{_niter:03d}'
def ensureDirectoryExists(dirName):
    if not os.path.isdir(dirName):
        os.mkdir(dirName)
def rightClipText(text, length):
    if len(text) > length:
        return '...' + text[-length:]
    else:
        return text
def popItem(qList, qItem):
    qList.pop(qList.index(qItem))
def listImageFiles(nDir):
    return sorted([fN for fN in os.listdir(nDir) if isPicture(fN)])
def isPicture(filename):
    return any(filename.lower().endswith(suffix) for suffix in PIC_SUFFIXES)
def findRescaleFactor(imgSize, allowedSize, allowZoom=True):
    mFactor = max(float(imgDim) / float(alwDim) for imgDim, alwDim in zip(imgSize, allowedSize))
    if not allowZoom and mFactor < 1:
        mFactor = 1
    print(f'mFactor={mFactor:.3f}')
    return mFactor
fileNameAllowedChars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM' + '1234567890-_~.,'
def normalizeString(inText):
    return ''.join([c for c in inText if c in fileNameAllowedChars])
if __name__ == "__main__":
    dir = './test_dir'
    body = 'image'
    extension = 'jpg'
    ensureDirectoryExists(dir)
    unique_filename = safeBuildFileName(dir, body, extension)
    print(f'Unique filename: {unique_filename}')
    image_files = listImageFiles(dir)
    print(f'Image files in directory: {image_files}')
    sample_text = "Hello, World! This is a test."
    normalized_text = normalizeString(sample_text)
    print(f'Normalized text: {normalized_text}')
    img_size = (1920, 1080)
    allowed_size = (800, 600)
    rescale_factor = findRescaleFactor(img_size, allowed_size)
    print(f'Rescale factor: {rescale_factor:.3f}')