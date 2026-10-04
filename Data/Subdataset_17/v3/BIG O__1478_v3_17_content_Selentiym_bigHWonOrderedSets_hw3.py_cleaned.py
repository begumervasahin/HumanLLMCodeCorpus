import csv
from bondartsev_nikita.classes import paramClasses, Context, Object
config = ["RealParam"] * 14
data_filename = "hw3.csv"
def create_object(config, data_line, label='') -> 'Object':
    params = [getattr(paramClasses, config[ind]).instantiate(value) for ind, value in enumerate(data_line)]
    return Object(params, label)
def read_csv_data(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return list(reader)
def initialize_context(config, data_lines):
    main_param_set = create_object(config, ['__head' for _ in config]).dash()
    context = Context(main_param_set)
    for counter, data_line in enumerate(data_lines, start=1):
        obj = create_object(config, data_line, str(counter))
        context.addObject(obj)
    return context
def print_objects(objects):
    sorted_objects = sorted(objects, key=lambda x: str(x))
    print(','.join(f'o{obj}' for obj in sorted_objects))
def count_fc(used: set, to_use: set, context: Context) -> int:
    if not to_use:
        param = None
        for obj in used:
            if param is None:
                param = obj.dash()
            else:
                param = param.intersect(obj.dash())
        if param is None:
            return 0
        closed = context.dash(param)
        if len(closed) == len(used):
            print_objects(used)
            return 1
        return 0
    new_el = to_use.pop()
    used_with_new_el = used.copy()
    used_with_new_el.add(new_el)
    return count_fc(used.copy(), to_use.copy(), context) + count_fc(used_with_new_el, to_use.copy(), context)
def main():
    data_lines = read_csv_data(data_filename)
    context_main = initialize_context(config, data_lines)
    count_fc(set(), set(context_main.getObjects()), context_main)
    objs = list(context_main.getObjects())
    print('\n')
    print_objects([objs[0], objs[1]])
    print()
    print_objects(context_main.dash(objs[0].dash().intersect(objs[1].dash())))
if __name__ == "__main__":
    main()