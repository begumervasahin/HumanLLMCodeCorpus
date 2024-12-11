
from xtsv import pipeline_rest_api, singleton_store_factory
def fonk1():
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
    return [b1, b2, b3]
def fonk2():
    b4 = fonk1()
    b5 = {
        'conll_comments': False,
        'singleton_store': singleton_store_factory(),
        'form_title': 'emMorph demo',
        'form_type': 'radio',
        'doc_link': 'https:
    }
    b6 = pipeline_rest_api('emMorph', b4, {}, **b5)
    return b6
if b7 = = '__main__':
    b8 = fonk2()
    b8.run(b9 = False)
