import re
import sys
def fonk1(token_instance_generator):
    for token_instance in token_instance_generator:
        b1 = []
        for token in token_instance:
            if re.search('[a-zA-Z]', token) is None:
                b1.append(token)
            else:
                b2 = fonk3(token)
                b1.extend(b2)
        yield b1
def fonk2(data_file):
    with open(data_file, 'rb') as instances:
        for instance in instances:
            b3 = []
            for b4 in instance.split():
                if b4 = = b'.':
                    b3.append(b4.decode('utf-8'))
                else:
                    for token in re.split(b'(\.)', b4):
                        b3.append(token.decode('utf-8'))
            yield b3
def fonk3(identifier):
    b1 = []
    b5 = re.finditer(r'.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    b6 = [m.group(0) for m in b5]
    for camel_subtoken in b6:
        for subtoken in re.split(r'(_)', camel_subtoken):
            b1.append(subtoken + '@@')
    if b1:
        b1[-1] = b1[-1][:-2]
    else:
        print(f'Error: Unable to split identifier: {identifier}')
    return b1
def fonk4(subtoken_instance_gen, b11):
    with open(b11, 'w') as f:
        for subtoken_instance in subtoken_instance_gen:
            f.write(' '.join(subtoken_instance))
            f.write('\n')
if b7 = = "__main__":
    b8 = [
        '/mnt/datastore/inf/groups/cdt_ds/mpatsis/PhD/rafaelository/data/Miltos/tokenized/',
        '/mnt/datastore/inf/groups/cdt_ds/mpatsis/PhD/rafaelository/data/codeCorpora/python/tokenized/',
        '/mnt/datastore/inf/groups/cdt_ds/mpatsis/PhD/rafaelository/data/codeCorpora/c/tokenized/'
    ]
    b9 = [
        ('validation/java_validation_slp_pre', 'validation/java_validation_slp_pre_sub'),
        ('test/java_test_slp_pre', 'test/java_test_slp_pre_sub'),
        ('training/java_training_slp_pre', 'training/java_training_slp_pre_sub'),
        ('training/java_training_slp_huge_pre', 'training/java_training_slp_huge_pre_sub'),
        ('validation_set_pre', 'validation_set_pre_sub'),
        ('test_set_pre', 'test_set_pre_sub'),
        ('small_training_set_pre', 'small_training_set_pre_sub'),
        ('full_training_set_pre', 'full_training_set_pre_sub')
    ]
    for datapath in b8:
        for original_file, sub_file in b9:
            b10 = f"{datapath}{original_file}"
            b11 = f"{datapath}{sub_file}"
            fonk4(fonk1(fonk2(b10)), b11)