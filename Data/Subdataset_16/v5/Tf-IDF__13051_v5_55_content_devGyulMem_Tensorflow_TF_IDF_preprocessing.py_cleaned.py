import pickle
import os
import utils.parameter as parameter
import utils.process_data as process_data
def fonk1():
    print("  >> It will take about one minute. Please wait.......")
    b1 = fonk2()
    b5, b2 = fonk3(b1)
    print(f"  >> Result1: {b5}")
    print(f"  >> Result2: {b2}")
def fonk2():
    b1, b3 = parameter.load_parameter()
    fonk4('b1.bin', b1)
    return b1
def fonk3(b1):
    b4 = process_data.Data(b1)
    b4.data_preprocessing()
    fonk4("b4.bin", b4)
    b5 = len(b4.train_data)
    b2 = b4.b2
    return b5, b2
def fonk4(filename, data):
    b6 = os.path.join('Pickle', filename)
    os.makedirs(os.path.dirname(b6), b7 = True)
    with open(b6, "wb") as f:
        pickle.dump(data, f)
if b8 = = '__main__':
    fonk1()