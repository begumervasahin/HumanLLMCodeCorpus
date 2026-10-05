import sys
import re
import os
di_only = True
answers_only = False
def build_fields(line):
    fields = ()
    match = re.match('^(\S+)\s+(\S+)\s+(\S+)\s+(\S+)', line)
    if match:
        fields = (match.group(1), match.group(2), match.group(3), match.group(4))
    else:
        match = re.match('^(\S+)\s+(\S+)\s+(\S+)', line)
        if match:
            fields = (match.group(1), match.group(2), match.group(3), '')
        else:
            print('Broken line:', line)
            os._exit(0)
    if len(fields) != 4:
        print('Broken fields:', fields)
        os._exit(0)
    return fields
def build_key(fields):
    return fields[0] + ' ' + fields[1] + ' ' + fields[2]
f = sys.stdin
if len(sys.argv) > 1:
    f = open(sys.argv[1])
state = 0
buf = ""
data_dict = {}
key = ""
fields = ()
for line in f:
    if len(line.strip()) == 0:
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
    if new_key in new_dict:
        new_dict[new_key] += [data_dict[akey]]
    else:
        new_dict[new_key] = [data_dict[akey]]
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