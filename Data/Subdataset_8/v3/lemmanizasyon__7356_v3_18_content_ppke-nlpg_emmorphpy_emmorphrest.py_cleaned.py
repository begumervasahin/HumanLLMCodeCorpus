
from xtsv import pipeline_rest_api, singleton_store_factory
em_morph_stem_config = {
    'task': 'stem',
    'source_fields': {'form'},
    'target_fields': ['anas']
}
em_morph_analyze_config = {
    'task': 'analyze',
    'source_fields': {'form'},
    'target_fields': ['anas']
}
em_morph_dstem_config = {
    'task': 'dstem',
    'source_fields': {'form'},
    'target_fields': ['anas']
}
em_morph_tools = [
    ('emmorphpy.emmorphpy', 'EmMorphPy', 'stem', (), em_morph_stem_config),
    ('emmorphpy.emmorphpy', 'EmMorphPy', 'analyze', (), em_morph_analyze_config),
    ('emmorphpy.emmorphpy', 'EmMorphPy', 'dstem', (), em_morph_dstem_config)
]
api_config = {
    'conll_comments': False,
    'form_title': 'emMorph demo',
    'form_type': 'radio',
    'doc_link': 'https:
}
pipeline_api = pipeline_rest_api(
    'emMorph',
    em_morph_tools,
    {},
    **api_config,
    singleton_store=singleton_store_factory()
)
if __name__ == '__main__':
    pipeline_api.run(debug=False)