import pickle
import os
import utils.parameter as parameter
import utils.process_data as process_data
def fonk1():
    print("  >> It will take about one minute. please wait.......")
    b1 = fonk2()
    b5, b2 = fonk3(b1)
    print ("  >> Resul1: {}".format(b5))
    print ("  >> Resul2: {}".format(b2))
def fonk2():
    b1, b3 = parameter.load_parameter()
    fonk4('b1.bin', b1)
    return b1
def fonk3(b1):
    b4 = process_data.Data(b1)
    b4.data_preprocessing()
    fonk4("b4.bin", b4)
    b5 = len(b4.train_data)
    b2 = b4.check_flag
    return b5, b2
def fonk4(filename, info):
    b6 = os.path.join('Pickle', filename)
    with open(b6, "wb") as f:
        pickle.dump(info, f)
if b7 = = '__main__':
    fonk1()