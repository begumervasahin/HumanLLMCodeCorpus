import csv
from bondartsev_nikita.classes import paramClasses, Context, Object
config = ["RealParam"] * 14
data_filename = "hw3.csv"
def create_object(config, data_line, label='') -> 'Object':
    params = []
    for ind, value in enumerate(data_line):
        param_class = getattr(paramClasses, config[ind])
        params.append(param_class.instantiate(value))
    return Object(params, label)
with open(data_filename, 'r') as f:
    reader = csv.reader(f)
    raw_data_list = list(reader)
main_param_set = create_object(config, ['__head' for _ in config]).dash()
context_main = Context(main_param_set)
counter = 0
for data_line in raw_data_list:
    counter += 1
    obj = create_object(config, data_line, str(counter))
    context_main.addObject(obj)
def print_objects(objects):
    sorted_objects = sorted(objects, key=lambda x: str(x))
    for obj in sorted_objects:
        print(f'o{obj}', end=',')
    print()
def count_fc(used: set, to_use: set) -> int:
    if not to_use:
        param = None
        for obj in used:
            if param is None:
                param = obj.dash()
            else:
                param = param.intersect(obj.dash())
        if param is None:
            return 0
        closed = context_main.dash(param)
        if len(closed) == len(used):
            print_objects(used)
            return 1
        else:
            return 0
    new_el = to_use.pop()
    used_with_new_el = used.copy()
    used_with_new_el.add(new_el)
    return count_fc(used.copy(), to_use.copy()) + count_fc(used_with_new_el, to_use.copy())
count_fc(set(), set(context_main.getObjects()))
objs = list(context_main.getObjects())
print('\n')
print_objects([objs[0], objs[1]])
print()
print_objects(context_main.dash(objs[0].dash().intersect(objs[1].dash())))