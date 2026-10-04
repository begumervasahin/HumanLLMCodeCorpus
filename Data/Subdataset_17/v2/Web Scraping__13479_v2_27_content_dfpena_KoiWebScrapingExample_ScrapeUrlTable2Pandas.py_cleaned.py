from decorator import decorator
import sys
import pandas as pd
import requests
import lxml.html as lh
@decorator
def on_start(func, *args, **kwargs):
    if kwargs:
        try:
            if kwargs.get('Start'):
                if kwargs.get('Settings', {}).get('Verbose'):
                    print(f"Starting function: {func.__name__}")
                return func(*args, **kwargs)
            else:
                kwargs['Start'] = False
                print(f"{func.__name__} DID NOT START")
                return kwargs
        except Exception as e:
            handle_exception(func, e, kwargs)
    else:
        print('Empty kwargs')
        return ()
def handle_exception(func, exception, kwargs):
    print('NODE ERROR OCCURRED TRYING TO START NODE FUNCTION:')
    print('===========================================')
    print(f"{func.__name__}: {exception}")
    print('===========================================')
    print('LAST STATE SET TO:')
    print('===========================================')
    print(kwargs)
    print('===========================================')
    print('LAST NODE FUNCTION SET TO:')
    print('===========================================')
    print(func.__name__)
    print('===========================================')
    global ekwargs, efunc
    ekwargs = kwargs
    efunc = func
    print('HALTING')
    raise
def start():
    return {'Start': True, 'Settings': {'Verbose': True}, 'Status': {}}
@on_start
def lxmlParseUrl1(*args, **kwargs):
    page = requests.get('https:
    kwargs['Data'] = lh.fromstring(page.content)
    return kwargs
@on_start
def lxmlFindAll2(*args, **kwargs):
    kwargs['Data'] = kwargs['Data'].get_element_by_id('customers')
    return kwargs
@on_start
def lxmlTable2Pandas3(*args, **kwargs):
    kwargs['Data'] = pd.read_html(lh.tostring(kwargs['Data']))[0]
    print(kwargs['Data'])
    return kwargs
@on_start
def pandaExcelDump(*args, **kwargs):
    kwargs['Data'].to_excel('test.xlsx', index=False)
    return kwargs
@on_start
def stop(*args, **kwargs):
    print('exiting')
    sys.exit()
class StremeNode:
    def __init__(self):
        pass
    def run(self, *args, **kwargs):
        self.kwargs = stop(
            **pandaExcelDump(
                **lxmlTable2Pandas3(
                    **lxmlFindAll2(
                        **lxmlParseUrl1(**kwargs)
                    )
                )
            )
        )
        return self.kwargs
class LiveProcess:
    def __init__(self):
        self.status = "pending"
    def run(self, expname):
        self.response = stop(
            **pandaExcelDump(
                **lxmlTable2Pandas3(
                    **lxmlFindAll2(
                        **lxmlParseUrl1(**start())
                    )
                )
            )
        )
        self.status = "completed"
        return self.status
if __name__ == '__main__':
    process = LiveProcess()
    process.run('Local')