from decorator import decorator
import sys
import pandas as pd
import requests
import lxml.html as lh
@decorator
def fonk1(func,*args, **b5):
    if b5 !={}:
        try:
            if b5['Start']:
                if 'Verbose' in b5['Settings']:
                    if b5['Settings']['Verbose']:
                        print(func)
                        pass
                b1 = func(*args,**b5)
                return b1
            else:
                b5['Start'] = False
                print(func,"DID NOT START")
                return(b5)
        except Exception as e:
            print('NODE ERROR OCCURED TRYING TO START NODE FUNCTION:')
            print('===========================================')
            print(func,e)
            print('===========================================')
            print('LAST STATE SET TO:')
            print('===========================================')
            print('b2')
            print('===========================================')
            print('LAST NODE FUNCTION SET TO:')
            print('===========================================')
            print('b3')
            print('===========================================')
            global b2
            global b3
            b2 = b5
            b3 = func
            print('HALTING')
            raise
    else:
        print('Empty b5')
        return ()
def fonk2():
    return {'Start':True,'Settings':{'Verbose':True},'Status':{}}
@on_start
def fonk3(*args,**b5):
    b4 = requests.get('https:
    b5['Data'] = lh.fromstring(b4.content)
    return b5
@on_start
def fonk4(*args,**b5):
    b5['Data'] = b5['Data'].get_element_by_id('customers')
    return b5
@on_start
def fonk5(*args,**b5):
    b5['Data']=pd.read_html(lh.tostring(b5['Data']))[0]
    print(b5['Data'])
    return b5
@on_start
def fonk6(*args,**b5):
    b5['Data'].to_excel(''+'test.xlsx')
    return b5
@on_start
def fonk7(*args,**b5):
    print('exiting')
    sys.exit()
class class1:
    def fonk8(self):
        pass
    def fonk9(self,*args,**b5):
        self.b5 = fonk7(**fonk6(**fonk5(**fonk4(**fonk3(**b5)))))
        return (self.b5)
class class2:
    def fonk10(self):
        self.b6 = "pending"
    def fonk11(self,expname):
        self.b1 = fonk7(**fonk6(**fonk5(**fonk4(**fonk3(**fonk2())))))
        self.b6 = "completed"
        return(self.b6)
if b7 = = '__main__':
    b8 = class2()
    b8.fonk11('Local')