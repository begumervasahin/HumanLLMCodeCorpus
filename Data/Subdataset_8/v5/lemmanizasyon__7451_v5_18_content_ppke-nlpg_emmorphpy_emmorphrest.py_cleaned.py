
from xtsv import pipeline_rest_api, singleton_store_factory
def define_tasks():
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
    return [em_morph_stem, em_morph_analyze, em_morph_dstem]
def setup_pipeline():
    tools = define_tasks()
    api_config = {
        'conll_comments': False,
        'singleton_store': singleton_store_factory(),
        'form_title': 'emMorph demo',
        'form_type': 'radio',
        'doc_link': 'https:
    }
    app = pipeline_rest_api('emMorph', tools, {}, **api_config)
    return app
if __name__ == '__main__':
    pipeline_app = setup_pipeline()
    pipeline_app.run(debug=False)
