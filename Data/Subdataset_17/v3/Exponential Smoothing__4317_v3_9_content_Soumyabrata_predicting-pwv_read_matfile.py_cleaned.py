import numpy as np
import scipy.io
import math
import datetime
def read_matfile(matlab_file):
    mat = scipy.io.loadmat(matlab_file)
    data_values = mat.get("DATA", [])
    doy, hour, minute, pwv = data_values[:, 0], data_values[:, 1], data_values[:, 2], data_values[:, 12]
    invalid_indices = np.union1d(
        np.where(np.isnan(pwv))[0],
        np.where(minute % 5 != 0)[0]
    )
    doy, hour, minute, pwv = map(lambda x: np.delete(x, invalid_indices), [doy, hour, minute, pwv])
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