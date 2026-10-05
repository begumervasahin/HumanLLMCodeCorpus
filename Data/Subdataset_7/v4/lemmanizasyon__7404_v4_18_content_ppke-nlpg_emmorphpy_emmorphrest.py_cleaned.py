
from xtsv import pipeline_rest_api, singleton_store_factory
b1 = (
    'emmorphpy.emmorphpy',
    'EmMorphPy',
    'stem',
    (),
    {
        'task': 'stem',
        'source_fields': {'form'},
        'target_fields': ['anas']
    }
)
b2 = (
    'emmorphpy.emmorphpy',
    'EmMorphPy',
    'analyze',
    (),
    {
        'task': 'analyze',
        'source_fields': {'form'},
        'target_fields': ['anas']
    }
)
b3 = (
    'emmorphpy.emmorphpy',
    'EmMorphPy',
    'dstem',
    (),
    {
        'task': 'dstem',
        'source_fields': {'form'},
        'target_fields': ['anas']
    }
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
