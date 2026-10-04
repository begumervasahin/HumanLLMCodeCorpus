from bondartsev_nikita.classes import *
import csv
config = ["RealParam"] * 14
data_filename = "hw3.csv"
def create_object(config, data_line, label='') -> 'AObject':
    params = [
        getattr(paramClasses, config[ind]).instantiate(value)
        for ind, value in enumerate(data_line)
    ]
    return Object(params, label)
with open(data_filename, 'r') as file:
    reader = csv.reader(file)
    raw_data_list = list(reader)
main_param_set = create_object(config, ['__head'] * len(config)).dash()
context_main = Context(main_param_set)
for counter, data_line in enumerate(raw_data_list, start=1):
    obj = create_object(config, data_line, str(counter))
    context_main.addObject(obj)
def print_objects(objects):
    sorted_objects = sorted(objects, key=lambda x: str(x))
    print(','.join('o' + str(obj) for obj in sorted_objects))
def count_formal_concepts(used: set, to_use: set) -> int:
    if not to_use:
        param = None
        for obj in used:
            param = obj.dash() if param is None else param.intersect(obj.dash())
        if param:
            closed = context_main.dash(param)
            if len(closed) == len(used):
                print_objects(used)
                return 1
        return 0
    new_element = to_use.pop()
    return (
        count_formal_concepts(used.copy(), to_use.copy()) +
        count_formal_concepts(used | {new_element}, to_use.copy())
    )
count_formal_concepts(set(), set(context_main.getObjects()))
objects = list(context_main.getObjects())
print("\n")
print_objects([objects[0], objects[1]])
print_objects(context_main.dash(objects[0].dash().intersect(objects[1].dash())))