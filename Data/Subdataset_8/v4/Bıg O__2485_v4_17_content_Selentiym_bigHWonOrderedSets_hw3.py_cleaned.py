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
mainParamSet = createObject(config, ['__head' for _ in range(len(config))]).dash()
contMain = Context(mainParamSet)
counter = 0
for dataLine in _rawDataList:
    counter += 1
    obj = createObject(config, dataLine, str(counter))
    contMain.addObject(obj)
def printObjs(used):
    used = list(used)
    used.sort(key=lambda x: x.__str__())
    for obj in used:
        print('o' + obj.__str__(), end=',')
def CountFC(used: set, toUse: set):
    if len(toUse) == 0:
        for obj in used:
            try:
                param = param.intersect(obj.dash())
            except UnboundLocalError:
                param = obj.dash()
        try:
            closed = contMain.dash(param)
            if len(closed) == len(used):
                printObjs(used)
                print('')
                return 1
            else:
                return 0
        except UnboundLocalError:
            return 0
    newEl = toUse.pop()
    second = used.copy()
    third = used.copy()
    second.add(newEl)
    copyF1 = toUse.copy()
    copyF2 = toUse.copy()
    return CountFC(third, copyF1) + CountFC(second, copyF2)
CountFC(set(), set(contMain.getObjects()))
objs = list(contMain.getObjects())
print()
print()
printObjs([objs[0], objs[1]])
print()
printObjs(contMain.dash(objs[0].dash().intersect(objs[1].dash())))