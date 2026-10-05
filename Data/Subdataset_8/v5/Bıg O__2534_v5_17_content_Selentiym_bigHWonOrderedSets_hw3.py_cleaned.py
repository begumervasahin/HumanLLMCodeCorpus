import csv
from bondartsev_nikita.classes import *
config = ["RealParam"] * 14
data_filename = "hw3.csv"
def read_data_from_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        return list(reader)
def create_object(config, data_line, label=''):
    params = []
    for index, value in enumerate(data_line):
        class_name = getattr(paramClasses, config[index])
        params.append(class_name.instantiate(value))
    return Object(params, label)
def print_objects(objects):
    sorted_objects = sorted(objects, key=lambda obj: str(obj))
    for obj in sorted_objects:
        print('o' + str(obj), end=',')
def count_closed_sets(used, to_use, context):
    if len(to_use) == 0:
        params = None
        for obj in used:
            params = obj.dash() if params is None else params.intersect(obj.dash())
        try:
            closed = context.dash(params)
            if len(closed) == len(used):
                print_objects(used)
                print('')
                return 1
            else:
                return 0
        except UnboundLocalError:
            return 0
    new_element = to_use.pop()
    second = used.copy()
    third = used.copy()
    second.add(new_element)
    copy_f1 = to_use.copy()
    copy_f2 = to_use.copy()
    return count_closed_sets(third, copy_f1, context) + count_closed_sets(second, copy_f2, context)
def main():
    raw_data_list = read_data_from_csv(data_filename)
    main_param_set = create_object(config, ['__head' for _ in range(len(config))]).dash()
    context = Context(main_param_set)
    counter = 0
    for data_line in raw_data_list:
        counter += 1
        obj = create_object(config, data_line, str(counter))
        context.addObject(obj)
    objects = set(context.getObjects())
    count_closed_sets(set(), objects.copy(), context)
    print()
    print()
    print_objects([objects[0], objects[1]])
    print()
    intersection = objects[0].dash().intersect(objects[1].dash())
    print_objects(context.dash(intersection))
if __name__ == "__main__":
    main()