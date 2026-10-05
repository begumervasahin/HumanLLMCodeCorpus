import sys
import re
DI_ONLY = True
ANSWERS_ONLY = False
def build_fields(line):
    match = re.match('^(\S+)\s+(\S+)\s+(\S+)(?:\s+(\S+))?', line)
    if match:
        return match.groups()
    else:
        print('Error: Unable to parse line:', line)
        sys.exit(1)
def build_key(fields):
    return ' '.join(fields[:3])
def process_input(file_obj):
    state = 0
    buf = ""
    data_dict = {}
    key = ""
    fields = ()
    for line in file_obj:
        if line.strip():
            text = line.rstrip()
            if text.endswith('\\'):
                if state != 1:
                    if key:
                        data_dict[key] = (fields, buf)
                    key = ""
                    buf = ""
                    fields = ()
                buf += line
                state = 1
            else:
                if text[0].isalpha():
                    if state == 2:
                        if key:
                            data_dict[key] = (fields, buf)
                        key = ""
                        buf = ""
                        fields = ()
                    fields = build_fields(text)
                    key = build_key(fields)
                    buf += line
                    state = 2
                else:
                    if text[0] == ' ' or text[0] == '\t':
                        buf += line
                        state = 3
                    else:
                        state = 4
    if key:
        data_dict[key] = (fields, buf)
    return data_dict
def print_sorted_output(data_dict):
    new_dict = {}
    for key, value in data_dict.items():
        new_key = value[0][1]
        if new_key in new_dict:
            new_dict[new_key].append(value)
        else:
            new_dict[new_key] = [value]
    sorted_keys = sorted(new_dict.keys())
    for a_key in sorted_keys:
        for item in new_dict[a_key]:
            if DI_ONLY:
                if item[0][0] == 'd-i':
                    print(item[1])
            else:
                print(item[1])
if __name__ == '__main__':
    file_path = sys.argv[1] if len(sys.argv) > 1 else None
    input_file = open(file_path, 'r') if file_path else sys.stdin
    input_data = process_input(input_file)
    print_sorted_output(input_data)