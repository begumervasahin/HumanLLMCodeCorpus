from decorator import decorator
import sys
import pandas as pd
import requests
import lxml.html as lh
@decorator
def fonk1(func, *args, **b6):
    if b6:
        try:
            if b6.get('Start'):
                if 'Verbose' in b6.get('Settings', {}):
                    if b6['Settings']['Verbose']:
                        print(f"Starting function: {func.b8}")
                b1 = func(*args, **b6)
                return b1
            else:
                b6['Start'] = False
                print(f"{func.b8} DID NOT START")
                return b6
        except Exception as e:
            print('NODE ERROR OCCURRED TRYING TO START NODE FUNCTION:')
            print('===========================================')
            print(f"{func.b8}:", e)
            print('===========================================')
            print('LAST STATE SET TO:')
            print('===========================================')
            print(b6)
            print('===========================================')
            print('LAST NODE FUNCTION SET TO:')
            print('===========================================')
            print(func.b8)
            print('===========================================')
            global b2
            global b3
            b2 = b6
            b3 = func
            print('HALTING')
            raise
    else:
        print('Empty b6')
        return ()
def fonk2():
    return {'Start': True, 'Settings': {'Verbose': True}, 'Status': {}}
@on_start
def fonk3(*args, **b6):
    b4 = requests.get('https:
    b6['Data'] = lh.fromstring(b4.content)
    return b6
@on_start
def fonk4(*args, **b6):
    b6['Data'] = b6['Data'].get_element_by_id('customers')
    return b6
@on_start
def fonk5(*args, **b6):
    b6['Data'] = pd.read_html(lh.tostring(b6['Data']))[0]
    print(b6['Data'])
    return b6
@on_start
def fonk6(*args, **b6):
    b6['Data'].to_excel('test.xlsx', b5 = False)
    return b6
@on_start
def fonk7(*args, **b6):
    print('exiting')
    sys.exit()
class class1:
    def fonk8(self):
        pass
    def fonk9(self, *args, **b6):
        self.b6 = fonk7(
            **fonk6(
                **fonk5(
                    **fonk4(
                        **fonk3(**b6)
                    )
                )
            )
        )
        return self.b6
class class2:
    def fonk10(self):
        self.b7 = "pending"
    def fonk11(self, expname):
        self.b1 = fonk7(
            **fonk6(
                **fonk5(
                    **fonk4(
                        **fonk3(**fonk2())
                    )
                )
            )
        )
        self.b7 = "completed"
        return self.b7
if b8 = = '__main__':
    b9 = class2()
    b9.fonk11('Local')