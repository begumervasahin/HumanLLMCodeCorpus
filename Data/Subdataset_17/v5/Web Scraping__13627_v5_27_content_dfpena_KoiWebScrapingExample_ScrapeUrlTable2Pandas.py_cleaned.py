from decorator import decorator
import sys
import pandas as pd
import requests
import lxml.html as lh
@decorator
def on_start(func, *args, **kwargs):
    try:
        if kwargs.get('Start', False):
            if kwargs.get('Settings', {}).get('Verbose', False):
                print(f"Starting function: {func.__name__}")
            response = func(*args, **kwargs)
            return response
        else:
            kwargs['Start'] = False
            print(f"Function {func.__name__} DID NOT START")
            return kwargs
    except Exception as e:
        handle_exception(func, kwargs, e)
def handle_exception(func, kwargs, exception):
    print('NODE ERROR OCCURRED TRYING TO START NODE FUNCTION:')
    print('===========================================')
    print(func, exception)
    print('===========================================')
    print('LAST STATE SET TO:')
    print('===========================================')
    print(kwargs)
    print('===========================================')
    print('LAST NODE FUNCTION SET TO:')
    print('===========================================')
    print(func)
    print('===========================================')
    global ekwargs, efunc
    ekwargs = kwargs
    efunc = func
    print('HALTING')
    raise
def start():
    return {'Start': True, 'Settings': {'Verbose': True}, 'Status': {}}
@on_start
def lxml_parse_url(*args, **kwargs):
    url = 'https:
    page = requests.get(url)
    kwargs['Data'] = lh.fromstring(page.content)
    return kwargs
@on_start
def lxml_find_table(*args, **kwargs):
    kwargs['Data'] = kwargs['Data'].get_element_by_id('customers')
    return kwargs
@on_start
def lxml_table_to_pandas(*args, **kwargs):
    table_html = lh.tostring(kwargs['Data'])
    kwargs['Data'] = pd.read_html(table_html)[0]
    print(kwargs['Data'])
    return kwargs
@on_start
def save_to_excel(*args, **kwargs):
    kwargs['Data'].to_excel('test.xlsx')
    return kwargs
@on_start
def stop(*args, **kwargs):
    print('Exiting')
    sys.exit()
class StreamNode:
    def __init__(self):
        pass
    def run(self, *args, **kwargs):
        self.kwargs = stop(**save_to_excel(**lxml_table_to_pandas(**lxml_find_table(**lxml_parse_url(**kwargs)))))
        return self.kwargs
class LiveProcess:
    def __init__(self):
        self.status = "pending"
    def run(self, expname):
        self.response = stop(**save_to_excel(**lxml_table_to_pandas(**lxml_find_table(**lxml_parse_url(**start())))))
        self.status = "completed"
        return self.status
if __name__ == '__main__':
    process = LiveProcess()
    process.run('Local')