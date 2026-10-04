from bondartsev_nikita.classes import *
import csv
config = ["RealParam"] * 14
dataFilename = "hw3.csv"
def createObject(config, dataLine, label='') -> 'AObject':
    params = []
    for ind, value in enumerate(dataLine):
        className = getattr(paramClasses, config[ind])
        params.append(className.instantiate(value))
    return Object(params, label)
with open(dataFilename, 'r') as f:
    reader = csv.reader(f)
    _rawDataList = list(reader)
mainParamSet = createObject(config, ['__head'] * len(config)).dash()
contMain = Context(mainParamSet)
for counter, dataLine in enumerate(_rawDataList, start=1):
    obj = createObject(config, dataLine, str(counter))
    contMain.addObject(obj)
def printObjs(used):
    used = sorted(used, key=lambda x: str(x))
    for obj in used:
        print('o' + str(obj), end=',')
    print()
def CountFC(used: set, toUse: set) -> int:
    if not toUse:
        param = None
        for obj in used:
            param = obj.dash() if param is None else param.intersect(obj.dash())
        if param:
            closed = contMain.dash(param)
            if len(closed) == len(used):
                printObjs(used)
                return 1
        return 0
    newEl = toUse.pop()
    return (
        CountFC(used.copy(), toUse.copy()) +
        CountFC(used | {newEl}, toUse.copy())
    )
CountFC(set(), set(contMain.getObjects()))
objs = list(contMain.getObjects())
print("\n")
printObjs([objs[0], objs[1]])
printObjs(contMain.dash(objs[0].dash().intersect(objs[1].dash())))