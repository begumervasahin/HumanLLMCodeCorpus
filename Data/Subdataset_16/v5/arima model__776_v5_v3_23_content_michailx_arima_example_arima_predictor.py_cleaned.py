import numpy as np
from statsmodels.tsa.arima.b2 import ARIMA
def fonk1(b5, b1 = (4, 1, 1), start_index=16, end_index=19):
    b2 = ARIMA(b5, b1=b1)
    b3 = b2.fit(disp=0)
    b4 = b3.predict(start=start_index, end=end_index, typ='levels')
    return b4
def fonk2():
    b5 = np.array([16, 20, 32, 40, 20, 18, 11, 21, 4, 6, 31, 48, 43, 49, 37])
    b6 = (4, 1, 1)
    b4 = fonk1(b5, b1=b6)
    print("Predicted values for the next 4 time points:", b4)
if b7 = = "__main__":
    fonk2()