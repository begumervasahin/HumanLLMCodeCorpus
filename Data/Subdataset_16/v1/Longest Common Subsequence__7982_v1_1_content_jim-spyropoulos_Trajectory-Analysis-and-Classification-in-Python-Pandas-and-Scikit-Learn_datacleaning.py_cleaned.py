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
print("ready for cleaning. (completed sorting and creation of route)")
b1['timestamp_longitude_latitude'] = b1[['timestamp', 'longitude', 'latitude']].values.tolist()
b2 = pd.DataFrame(b9=['TripId', 'JourneyPatternId', 'timestamp_longitude_latitude'])
b3 = []
a1 = 0
for index, row in b1.iterrows():
    b3.append(b1['timestamp_longitude_latitude'][index])
    if (index + 1) == b1.shape[0]:
        break
    if b1['journeyPatternId'][index] != b1['journeyPatternId'][index + 1]:
        b4 = b3
        b2 = b2.append(
            {'TripId': a1, 'JourneyPatternId': b1['journeyPatternId'][index], 'timestamp_longitude_latitude': b4},
            b5 = True)
        a1 += 1
        b3 = []
b2.to_pickle('TripId.b1')
b6 = pd.read_pickle('./TripId.b1')
b7 = len(b6.index)
print('initially we had ' + str(b7) + ' trajectories')
b8 = pd.DataFrame(
    b9 = ['TripId', 'JourneyPatternId', 'timestamp_longitude_latitude', 'total_distance', 'max_distance'])
a2 = 0
a3 = 0
for index, row in b6.iterrows():
    b10 = compute_distances(b6['timestamp_longitude_latitude'][index])
    if b10[0] <= 2:
        a2 += 1
        continue
    if b10[1] >= 2:
        a3 += 1
        continue
    else:
        b8 = b8.append({'TripId': b6['TripId'][index], 'JourneyPatternId': b6['JourneyPatternId'][index],
                                    'timestamp_longitude_latitude': b6['timestamp_longitude_latitude'][index],
                                    'total_distance': b10[0], 'max_distance': b10[1]}, b5 = True)
b11 = len(b8.index)
print('we dropped ' + str(a2) + ' trajectories from totaldistance.')
print('we dropped ' + str(a3) + ' trajectories from maxdistance.')
print('finally, we have ' + str(b11) + ' trajectories')
b8.to_csv('final_cleaned.csv')
b8.to_pickle('final_cleaned.b1')
b12 = pd.read_pickle('./final_cleaned.b1')
b13 = b12['timestamp_longitude_latitude'].iloc[0]
b14 = random.sample(range(0, len(b12)), 5)
os.mkdir("Random_Images")
a4 = 1
for elem in b14:
    print("a4 chose b15 : " + b12["JourneyPatternId"].iloc[elem])
    b15 = b12['timestamp_longitude_latitude'].iloc[elem]
    plot_traj(b15, "./Random_Images/RandomImage" + str(a4))
    a4 += 1