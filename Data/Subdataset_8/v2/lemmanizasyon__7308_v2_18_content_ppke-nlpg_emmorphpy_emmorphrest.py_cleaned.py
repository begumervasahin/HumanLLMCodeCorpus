
from xtsv import pipeline_rest_api, singleton_store_factory
em_morph_stem = (
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
em_morph_analyze = (
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
em_morph_dstem = (
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
tools = [
    (em_morph_stem, ('stem',)),
    (em_morph_analyze, ('analyze',)),
    (em_morph_dstem, ('dstem',))
]
api_config = {
    'conll_comments': False,
    'form_title': 'emMorph demo',
    'form_type': 'radio',
    'doc_link': 'https:
}
app = pipeline_rest_api(
    'emMorph',
    tools,
    {},
    **api_config,
    singleton_store=singleton_store_factory()
)
if __name__ == '__main__':
    app.run(debug=False)