from xtsv import pipeline_rest_api, singleton_store_factory
def create_task(module_path, class_name, method_name, task_name, source_fields, target_fields):
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
em_morph_stem = create_task(
    'emmorphpy.emmorphpy',
    'EmMorphPy',
    'stem',
    'stem',
    {'form'},
    ['anas']
)
em_morph_analyze = create_task(
    'emmorphpy.emmorphpy',
    'EmMorphPy',
    'analyze',
    'analyze',
    {'form'},
    ['anas']
)
em_morph_dstem = create_task(
    'emmorphpy.emmorphpy',
    'EmMorphPy',
    'dstem',
    'dstem',
    {'form'},
    ['anas']
)
tools = [
    (em_morph_stem, ('stem',)),
    (em_morph_analyze, ('analyze',)),
    (em_morph_dstem, ('dstem',)),
]
app = pipeline_rest_api(
    'emMorph',
    tools,
    {},
    conll_comments=False,
    singleton_store=singleton_store_factory(),
    form_title='emMorph demo',
    form_type='radio',
    doc_link='https:
)
if __name__ == '__main__':
    app.run(debug=False)
