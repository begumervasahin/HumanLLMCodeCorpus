import numpy as np
import scipy.io
import math
import datetime
def read_matfile(matlab_file):
    mat = scipy.io.loadmat(matlab_file)
    data_values = mat.get("DATA", [])
    (no_of_obs, no_of_features) = data_values.shape
    doy = data_values[:, 0]
    hour = data_values[:, 1]
    minute = data_values[:, 2]
    temperature = data_values[:, 3]
    solar_radiation = data_values[:, 4]
    relative_humidity = data_values[:, 5]
    rain = data_values[:, 6]
    dew_point_temp = data_values[:, 7]
    pwv = data_values[:, 12]
    removable_index1 = np.where(np.isnan(pwv))[0]
    removable_index2 = np.where(minute % 5 != 0)[0]
    removable_index = np.union1d(removable_index1, removable_index2)
    pwv = np.delete(pwv, removable_index)
    doy = np.delete(doy, removable_index)
    hour = np.delete(hour, removable_index)
    minute = np.delete(minute, removable_index)
    year = 2010
    timestamp = []
    for i, item in enumerate(doy):
        dummy = datetime.datetime(year, 1, 1) + datetime.timedelta(item - 1)
        sw = datetime.datetime(dummy.year, dummy.month, dummy.day, int(hour[i]), int(minute[i]))
        timestamp.append(sw)
    return timestamp, pwv
matlab_file = './data/PWV_2010from_WS_2_withGradient.mat'
timestamps, pwv = read_matfile(matlab_file)
print("Length of timestamps:", len(timestamps))
print("Length of pwv:", len(pwv))