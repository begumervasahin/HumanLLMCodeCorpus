import csv
from bondartsev_nikita.classes import paramClasses, Context, Object
config = ["RealParam"] * 14
dataFilename = "hw3.csv"
def createObject(config, dataLine, label='') -> 'Object':
    params = []
    for ind, value in enumerate(dataLine):
        className = getattr(paramClasses, config[ind])
        params.append(className.instantiate(value))
    return Object(params, label)
with open(dataFilename, 'r') as f:
    reader = csv.reader(f)
    _rawDataList = list(reader)
mainParamSet = createObject(config, ['__head' for _ in config]).dash()
contMain = Context(mainParamSet)
counter = 0
for dataLine in _rawDataList:
    counter += 1
    obj = createObject(config, dataLine, str(counter))
    contMain.addObject(obj)
def printObjs(used):
    used = list(used)
    used.sort(key=lambda x: str(x))
    for obj in used:
        print(f'o{obj}', end=',')
def CountFC(used: set, toUse: set) -> int:
    if not toUse:
        param = None
        for obj in used:
            if param is None:
                param = obj.dash()
            else:
                param = param.intersect(obj.dash())
        if param is None:
            return 0
        closed = contMain.dash(param)
        if len(closed) == len(used):
            printObjs(used)
            print('')
            return 1
        else:
            return 0
    newEl = toUse.pop()
    second = used.copy()
    second.add(newEl)
    return CountFC(used.copy(), toUse.copy()) + CountFC(second, toUse.copy())
CountFC(set(), set(contMain.getObjects()))
objs = list(contMain.getObjects())
print('\n')
printObjs([objs[0], objs[1]])
print()
printObjs(contMain.dash(objs[0].dash().intersect(objs[1].dash())))