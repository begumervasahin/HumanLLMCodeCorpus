import sys
import re
di_only = True
answers_only = False
def build_fields(line):
    match = re.match('^(\S+)\s+(\S+)\s+(\S+)(?:\s+(\S+))?', line.strip())
    if match:
        return match.groups()
    else:
        print('Broken line:', line.strip())
        sys.exit(1)
def build_key(fields):
    return ' '.join(fields[:3])
input_file = sys.stdin if len(sys.argv) == 1 else open(sys.argv[1])
data_dict = {}
state = 0
buf = ""
key = ""
fields = ()
for line in input_file:
    if not line.strip():
        continue
    text = line.strip()
    if text.startswith("'"):
        if state != 1:
            if key:
                if key not in data_dict:
                    data_dict[key] = (fields, buf)
            key = ""
            buf = ""
            fields = ()
        buf += line
        state = 1
    else:
        if text[0].isalpha():
            if state == 2:
                if key not in data_dict:
                    data_dict[key] = (fields, buf)
                key = ""
                buf = ""
                fields = ()
            fields = build_fields(text)
            key = build_key(fields)
            buf += line
            state = 2
        else:
            if text[0] in [' ', '\t']:
                buf += line
                state = 3
            else:
                state = 4
if key:
    if key not in data_dict:
        data_dict[key] = (fields, buf)
new_dict = {}
for akey in data_dict:
    new_key = data_dict[akey][0][1]
    new_dict.setdefault(new_key, []).append(data_dict[akey])
keys = sorted(new_dict.keys())
for akey in keys:
    alist = new_dict[akey]
    if di_only:
        di_found = False
        for item in alist:
            if item[0][0] == 'd-i':
                di_found = True
                print(item[1])
        if not di_found:
            for item in alist:
                print(item[1])
    else:
        for item in alist:
            print(item[1])
input_file.close()
