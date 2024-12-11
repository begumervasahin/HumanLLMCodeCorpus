
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import utils
import pandas as pd
import numpy as np
from itertools import cycle, islice
import matplotlib.pyplot as plt
from pandas.tools.plotting import parallel_coordinates
%matplotlib inline
b1 = pd.read_csv('./weather/minute_weather.csv')
b1.shape
b1.head()
b2 = b1[(b1['rowID'] % 10) == 0]
b2.shape
b2.describe().transpose()
b2[b2['rain_accumulation'] == 0].shape
b2[b2['rain_duration'] == 0].shape
del b2['rain_accumulation']
del b2['rain_duration']
b3 = b2.shape[0]
b2 = b2.dropna()
b4 = b2.shape[0]
b3 - b4
b2.columns
b5 = ['air_pressure', 'air_temp', 'avg_wind_direction', 'avg_wind_speed', 'max_wind_direction',
        'max_wind_speed','relative_humidity']
b6 = b2[b5]
b6.columns
b6
b7 = StandardScaler().fit_transform(b6)
b7
b8 = KMeans(n_clusters=12)
b9 = b8.fit(b7)
print("b9\n", b9)
b10 = b9.cluster_centers_
b10
def fonk1(featuresUsed, b10):
	b11 = list(featuresUsed)
	b11.append('prediction')
	b12 = [np.append(A, index) for index, A in enumerate(b10)]
	b13 = pd.DataFrame(b12, columns=b11)
	b13['prediction'] = b13['prediction'].astype(int)
	return b13
def fonk2(b1):
	b14 = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(b1)))
	plt.figure(b15 = (15,8)).gca().axes.set_ylim([-3,+3])
	parallel_coordinates(b1, 'prediction', b16 = b14, marker='o')
b13 = fonk1(b5, b10)
b13
fonk2(b13[b13['relative_humidity'] < -0.5])
fonk2(b13[b13['air_temp'] > 0.5])
fonk2(b13[(b13['relative_humidity'] > 0.5) & (b13['air_temp'] < 0.5)])