import numpy as np
import scipy.io
import math
import datetime
def read_matfile(matlab_file):
    mat = scipy.io.loadmat(matlab_file)
    data_values = mat.get("DATA", [])
    doy = data_values[:, 0]
    hour = data_values[:, 1]
    minute = data_values[:, 2]
    pwv = data_values[:, 12]
    invalid_pwv_indices = [i for i, value in enumerate(pwv) if math.isnan(value)]
    invalid_minute_indices = [i for i, value in enumerate(minute) if value % 5 != 0]
    removable_indices = np.union1d(invalid_pwv_indices, invalid_minute_indices)
    pwv = np.delete(pwv, removable_indices)
    doy = np.delete(doy, removable_indices)
    hour = np.delete(hour, removable_indices)
    minute = np.delete(minute, removable_indices)
    year = 2010
    timestamps = [
        datetime.datetime(year, 1, 1) + datetime.timedelta(days=int(day) - 1, hours=int(h), minutes=int(m))
        for day, h, m in zip(doy, hour, minute)
    ]
    print(f'Processed {len(pwv)} valid PWV entries.')
    return timestamps, pwv
def main():
    matlab_file = './data/PWV_2010from_WS_2_withGradient.mat'
    timestamps, pwv = read_matfile(matlab_file)
    for ts, value in zip(timestamps[:5], pwv[:5]):
        print(f'Timestamp: {ts}, PWV: {value}')
if __name__ == '__main__':
    main()