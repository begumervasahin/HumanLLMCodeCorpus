
from xtsv import pipeline_rest_api, singleton_store_factory
b1 = {
    'task': 'stem',
    'source_fields': {'form'},
    'target_fields': ['anas']
}
b2 = {
    'task': 'analyze',
    'source_fields': {'form'},
    'target_fields': ['anas']
}
b3 = {
    'task': 'dstem',
    'source_fields': {'form'},
    'target_fields': ['anas']
}
b4 = [
    ('emmorphpy.emmorphpy', 'EmMorphPy', 'stem', (), b1),
    ('emmorphpy.emmorphpy', 'EmMorphPy', 'analyze', (), b2),
    ('emmorphpy.emmorphpy', 'EmMorphPy', 'dstem', (), b3)
]
b5 = {
    'conll_comments': False,
    'form_title': 'emMorph demo',
    'form_type': 'radio',
    'doc_link': 'https:
}
b6 = pipeline_rest_api(
    'emMorph',
    b4,
    {},
    **b5,
    b7 = singleton_store_factory()
)
if b8 = = '__main__':
    b6.run(b9 = False)