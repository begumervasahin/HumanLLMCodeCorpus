import re
import sys
def subtoken_instance_generator(token_instance_generator):
    for token_instance in token_instance_generator:
        subtokens = []
        for token in token_instance:
            if re.search('[a-zA-Z]', token) is None:
                subtokens.append(token)
            else:
                stokens = split_to_subtokens(token)
                subtokens.extend(stokens)
        yield subtokens
def instance_generator(data_file):
    with open(data_file, 'rb') as instances:
        for instance in instances:
            tokens = []
            for wh_token in instance.split():
                if wh_token == b'.':
                    tokens.append(wh_token.decode('utf-8'))
                else:
                    for token in re.split(b'(\.)', wh_token):
                        tokens.append(token.decode('utf-8'))
            yield tokens
def split_to_subtokens(identifier):
    subtokens = []
    matches = re.finditer(r'.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    camel_subtokens = [m.group(0) for m in matches]
    for camel_subtoken in camel_subtokens:
        for subtoken in re.split(r'(_)', camel_subtoken):
            subtokens.append(subtoken + '@@')
    if subtokens:
        subtokens[-1] = subtokens[-1][:-2]
    else:
        print(f'Error: Unable to split identifier: {identifier}')
    return subtokens
def export_to_file(subtoken_instance_gen, export_file):
    with open(export_file, 'w') as f:
        for subtoken_instance in subtoken_instance_gen:
            f.write(' '.join(subtoken_instance))
            f.write('\n')
if __name__ == "__main__":
    data_paths = [
        '/mnt/datastore/inf/groups/cdt_ds/mpatsis/PhD/rafaelository/data/Miltos/tokenized/',
        '/mnt/datastore/inf/groups/cdt_ds/mpatsis/PhD/rafaelository/data/codeCorpora/python/tokenized/',
        '/mnt/datastore/inf/groups/cdt_ds/mpatsis/PhD/rafaelository/data/codeCorpora/c/tokenized/'
    ]
    file_sets = [
        ('validation/java_validation_slp_pre', 'validation/java_validation_slp_pre_sub'),
        ('test/java_test_slp_pre', 'test/java_test_slp_pre_sub'),
        ('training/java_training_slp_pre', 'training/java_training_slp_pre_sub'),
        ('training/java_training_slp_huge_pre', 'training/java_training_slp_huge_pre_sub'),
        ('validation_set_pre', 'validation_set_pre_sub'),
        ('test_set_pre', 'test_set_pre_sub'),
        ('small_training_set_pre', 'small_training_set_pre_sub'),
        ('full_training_set_pre', 'full_training_set_pre_sub')
    ]
    for datapath in data_paths:
        for original_file, sub_file in file_sets:
            tokens_file = f"{datapath}{original_file}"
            export_file = f"{datapath}{sub_file}"
            export_to_file(subtoken_instance_generator(instance_generator(tokens_file)), export_file)