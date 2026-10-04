from decorator import decorator
import sys
import pandas as pd
import requests
import lxml.html as lh
@decorator
def fonk1(func, *args, **b7):
    try:
        if b7.get('Start', False):
            if b7.get('Settings', {}).get('Verbose', False):
                print(f"Starting function: {func.b9}")
            b1 = func(*args, **b7)
            return b1
        else:
            b7['Start'] = False
            print(f"Function {func.b9} DID NOT START")
            return b7
    except Exception as e:
        fonk2(func, b7, e)
def fonk2(func, b7, exception):
    print('NODE ERROR OCCURRED TRYING TO START NODE FUNCTION:')
    print('===========================================')
    print(func, exception)
    print('===========================================')
    print('LAST STATE SET TO:')
    print('===========================================')
    print(b7)
    print('===========================================')
    print('LAST NODE FUNCTION SET TO:')
    print('===========================================')
    print(func)
    print('===========================================')
    global b2, b3
    b2 = b7
    b3 = func
    print('HALTING')
    raise
def fonk3():
    return {'Start': True, 'Settings': {'Verbose': True}, 'Status': {}}
@on_start
def fonk4(*args, **b7):
    b4 = 'https:
    b5 = requests.get(b4)
    b7['Data'] = lh.fromstring(b5.content)
    return b7
@on_start
def fonk5(*args, **b7):
    b7['Data'] = b7['Data'].get_element_by_id('customers')
    return b7
@on_start
def fonk6(*args, **b7):
    b6 = lh.tostring(b7['Data'])
    b7['Data'] = pd.read_html(b6)[0]
    print(b7['Data'])
    return b7
@on_start
def fonk7(*args, **b7):
    b7['Data'].to_excel('test.xlsx')
    return b7
@on_start
def fonk8(*args, **b7):
    print('Exiting')
    sys.exit()
class class1:
    def fonk9(self):
        pass
    def fonk10(self, *args, **b7):
        self.b7 = fonk8(**fonk7(**fonk6(**fonk5(**fonk4(**b7)))))
        return self.b7
class class2:
    def fonk11(self):
        self.b8 = "pending"
    def fonk12(self, expname):
        self.b1 = fonk8(**fonk7(**fonk6(**fonk5(**fonk4(**fonk3())))))
        self.b8 = "completed"
        return self.b8
if b9 = = '__main__':
    b10 = class2()
    b10.fonk12('Local')