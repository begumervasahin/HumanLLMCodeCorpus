import re
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
    with open(data_file, 'r') as instances:
        for instance in instances:
            b3 = []
            for b4 in instance.split():
                if b4 = = '.':
                    b3.append(b4)
                else:
                    for token in re.split('(\.)', b4):
                        b3.append(token)
            yield b3
def fonk3(identifier):
    b1 = []
    b5 = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    b6 = [m.group(0) for m in b5]
    for camel_subtoken in b6:
        for subtoken in re.split('(_)', camel_subtoken):
            b1.append(subtoken + '@@')
    b1[-1] = b1[-1][:-2]
    if len(b1) == 0:
        print('error:', identifier)
    return b1
def fonk4(subtoken_instance_generator, b11):
    with open(b11, 'w') as f:
        for subtoken_instance in subtoken_instance_generator:
            f.write(' '.join(subtoken_instance))
            f.write('\n')
if b7 = = "__main__":
    b8 = '/mnt/datastore/inf/groups/cdt_ds/mpatsis/PhD/rafaelository/data/Miltos/tokenized/'
    b9 = ['validation/java_validation_slp_pre', 'test/java_test_slp_pre',
                  'training/java_training_slp_pre', 'training/java_training_slp_huge_pre']
    for java_file in b9:
        b10 = b8 + java_file
        b11 = b8 + java_file + '_sub'
        fonk4(fonk1(fonk2(b10)), b11)
    b12 = '/mnt/datastore/inf/groups/cdt_ds/mpatsis/PhD/rafaelository/data/codeCorpora/python/tokenized/'
    b13 = ['validation_set_pre', 'test_set_pre', 'small_training_set_pre', 'full_training_set_pre']
    for python_file in b13:
        b10 = b12 + python_file
        b11 = b12 + python_file + '_sub'
        fonk4(fonk1(fonk2(b10)), b11)
    b14 = '/mnt/datastore/inf/groups/cdt_ds/mpatsis/PhD/rafaelository/data/codeCorpora/c/tokenized/'
    b15 = ['validation_set_pre', 'test_set_pre', 'small_training_set_pre', 'full_training_set_pre']
    for c_file in b15:
        b10 = b14 + c_file
        b11 = b14 + c_file + '_sub'
        fonk4(fonk1(fonk2(b10)), b11)