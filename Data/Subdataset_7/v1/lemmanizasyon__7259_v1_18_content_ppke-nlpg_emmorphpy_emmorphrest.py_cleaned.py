from xtsv import pipeline_rest_api, singleton_store_factory
b1 = ('emmorphpy.emmorphpy', 'EmMorphPy', 'stem', (), {'task': 'stem', 'source_fields': {'form'}, 'target_fields': ['anas']})
b2 = ('emmorphpy.emmorphpy', 'EmMorphPy', 'analyze', (), {'task': 'analyze', 'source_fields': {'form'}, 'target_fields': ['anas']})
b3 = ('emmorphpy.emmorphpy', 'EmMorphPy', 'dstem', (), {'task': 'dstem', 'source_fields': {'form'}, 'target_fields': ['anas']})
b4 = [(b1, ('stem',)),
         (b2, ('analyze',)),
         (b3, ('dstem',))]
b5 = {
    'conll_comments': False,
    'form_title': 'emMorph demo',
    'form_type': 'radio',
    'doc_link': 'https:
}
b6 = pipeline_rest_api('emMorph', b4, {}, **b5, singleton_store=singleton_store_factory())
if b7 = = '__main__':
    b6.run(b8 = False)