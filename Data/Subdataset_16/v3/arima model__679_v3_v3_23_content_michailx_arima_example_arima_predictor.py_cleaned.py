import numpy as np
from statsmodels.tsa.arima.model import ARIMA
def fonk1(b6, b1 = (4, 1, 1), start_index=16, end_index=19):
    b2 = ARIMA(b6, b1=b1)
    b3 = b2.fit()
    b4 = b3.predict(start=start_index, end=end_index, typ='levels')
    return b4
if b5 = = "__main__":
    b6 = np.array([16, 20, 32, 40, 20, 18, 11, 21, 4, 6, 31, 48, 43, 49, 37])
    b7 = (4, 1, 1)
    b8 = fonk1(b6, b1=b7)
    print("Predicted values for the next 4 time points:", b8)