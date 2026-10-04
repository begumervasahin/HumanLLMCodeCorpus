from xtsv import pipeline_rest_api, singleton_store_factory
def fonk1(module_path, class_name, method_name, task_name, source_fields, target_fields):
    return (
        module_path,
        class_name,
        method_name,
        (),
        {
            'task': task_name,
            'source_fields': source_fields,
            'target_fields': target_fields
        }
    )
b1 = fonk1(
    'emmorphpy.emmorphpy',
    'EmMorphPy',
    'stem',
    'stem',
    {'form'},
    ['anas']
)
b2 = fonk1(
    'emmorphpy.emmorphpy',
    'EmMorphPy',
    'analyze',
    'analyze',
    {'form'},
    ['anas']
)
b3 = fonk1(
    'emmorphpy.emmorphpy',
    'EmMorphPy',
    'dstem',
    'dstem',
    {'form'},
    ['anas']
)
b4 = [
    (b1, ('stem',)),
    (b2, ('analyze',)),
    (b3, ('dstem',)),
]
b5 = pipeline_rest_api(
    'emMorph',
    b4,
    {},
    b6 = False,
    b7 = singleton_store_factory(),
    b8 = 'emMorph demo',
    b9 = 'radio',
    b10 = 'https:
)
if b11 = = '__main__':
    b5.run(b12 = False)
