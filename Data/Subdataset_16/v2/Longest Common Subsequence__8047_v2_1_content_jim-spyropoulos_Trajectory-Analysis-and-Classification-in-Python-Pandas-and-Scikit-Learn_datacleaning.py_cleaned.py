import os
import random
import pandas as pd
from auxiliaryfunctions import compute_distances, plot_traj
b1 = pd.read_csv('train_set.csv')
b1 = b1[pd.notnull(b1['journeyPatternId'])]
pd.set_option('display.max_rows', 1000000000)
b1['route'] = b1['vehicleID'].map(str) + b1['timestamp'].map(str)
b1 = b1.sort_values(by=['route'])
b1 = b1.reset_index(drop=True)
print("Ready for cleaning. (completed sorting and creation of route)")
b1['timestamp_longitude_latitude'] = b1[['timestamp', 'longitude', 'latitude']].values.tolist()
b2 = pd.DataFrame(columns=['TripId', 'JourneyPatternId', 'timestamp_longitude_latitude'])
b3 = []
a1 = 0
for index, row in b1.iterrows():
    b3.append(b1['timestamp_longitude_latitude'][index])
    if (index + 1) == b1.shape[0]:
        break
    if b1['journeyPatternId'][index] != b1['journeyPatternId'][index + 1]:
        b2 = b2.append(
            {
                'TripId': a1,
                'JourneyPatternId': b1['journeyPatternId'][index],
                'timestamp_longitude_latitude': b3
            },
            b4 = True
        )
        a1 += 1
        b3 = []
b2.to_pickle('TripId.b1')
b5 = pd.read_pickle('TripId.b1')
b6 = len(b5.index)
print(f'Initially, we had {b6} trajectories')
b7 = pd.Dat