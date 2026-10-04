from decorator import decorator
import sys
import pandas as pd
import requests
import lxml.html as lh
@decorator
def fonk1(func, *args, **b5):
    if not b5:
        print('Empty b5')
        return ()
    try:
        if b5.get('Start'):
            if b5.get('Settings', {}).get('Verbose'):
                print(f"Starting function: {func.b8}")
            return func(*args, **b5)
        else:
            b5['Start'] = False
            print(f"{func.b8} DID NOT START")
            return b5
    except Exception as e:
        fonk2(func, e, b5)
def fonk2(func, exception, b5):
    print('NODE ERROR OCCURRED TRYING TO START NODE FUNCTION:')
    print('===========================================')
    print(f"{func.b8}: {exception}")
    print('===========================================')
    print('LAST STATE SET TO:')
    print('===========================================')
    print(b5)
    print('===========================================')
    print('LAST NODE FUNCTION SET TO:')
    print('===========================================')
    print(func.b8)
    print('===========================================')
    global b1, b2
    b1 = b5
    b2 = func
    print('HALTING')
    raise
def fonk3():
    return {'Start': True, 'Settings': {'Verbose': True}, 'Status': {}}
@on_start
def fonk4(*args, **b5):
    b3 = requests.get('https:
    b5['Data'] = lh.fromstring(b3.content)
    return b5
@on_start
def fonk5(*args, **b5):
    b5['Data'] = b5['Data'].get_element_by_id('customers')
    return b5
@on_start
def fonk6(*args, **b5):
    b5['Data'] = pd.read_html(lh.tostring(b5['Data']))[0]
    print(b5['Data'])
    return b5
@on_start
def fonk7(*args, **b5):
    b5['Data'].to_excel('test.xlsx', b4 = False)
    return b5
@on_start
def fonk8(*args, **b5):
    print('Exiting...')
    sys.exit()
class class1:
    def fonk9(self):
        pass
    def fonk10(self, *args, **b5):
        self.b5 = fonk8(
            **fonk7(
                **fonk6(
                    **fonk5(
                        **fonk4(**b5)
                    )
                )
            )
        )
        return self.b5
class class2:
    def fonk11(self):
        self.b6 = "pending"
    def fonk12(self, expname):
        self.b7 = fonk8(
            **fonk7(
                **fonk6(
                    **fonk5(
                        **fonk4(**fonk3())
                    )
                )
            )
        )
        self.b6 = "completed"
        return self.b6
if b8 = = '__main__':
    b9 = class2()
    b9.fonk12('Local')