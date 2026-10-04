import os
import random
import pandas as pd
from auxiliaryfunctions import compute_distances, plot_traj
b1 = pd.read_csv('train_set.csv')
b1 = b1[pd.notnull(b1['journeyPatternId'])]
pd.set_option('display.max_rows', None)
b1['route'] = b1['vehicleID'].map(str) + b1['timestamp'].map(str)
b1 = b1.sort_values(by=['route']).reset_index(drop=True)
print("Ready for cleaning. (Completed sorting and creation of route)")
b1['timestamp_longitude_latitude'] = b1[['timestamp', 'longitude', 'latitude']].values.tolist()
b2 = pd.DataFrame(columns=['TripId', 'JourneyPatternId', 'timestamp_longitude_latitude'])
b3 = []
a1 = 0
for index, row in b1.iterrows():
    b3.append(row['timestamp_longitude_latitude'])
    if (index + 1) == b1.shape[0] or row['journeyPatternId'] != b1.loc[index + 1, 'journeyPatternId']:
        b2 = b2.append({
            'TripId': a1,
            'JourneyPatternId': row['journeyPatternId'],
            'timestamp_longitude_latitude': b3
        }, b4 = True)
        a1 += 1
        b3 = []
b2.to_pickle('TripId.b1')
b2 = pd.read_pickle('TripId.b1')
b5 = len(b2)
print(f'Initially, we had {b5} trajectories')
b6 = pd.DataFrame(columns=['TripId', 'JourneyPatternId', 'timestamp_longitude_latitude', 'total_distance', 'b7'])
a2 = 0
a3 = 0
for index, row in b2.iterrows():
    total_distance, b7 = compute_distances(row['timestamp_longitude_latitude'])
    if total_distance <= 2:
        a2 += 1
        continue
    if b7 >= 2:
        a3 += 1
        continue
    b6 = b6.append({
        'TripId': row['TripId'],
        'JourneyPatternId': row['JourneyPatternId'],
        'timestamp_longitude_latitude': row['timestamp_longitude_latitude'],
        'total_distance': total_distance,
        'b7': b7
    }, b4 = True)
print(f'We dropped {a2} trajectories due to total distance.')
print(f'We dropped {a3} trajectories due to max distance.')
b8 = len(b6)
print(f'Finally, we have {b8} trajectories')
b6.to_csv('final_cleaned.csv')
b6.to_pickle('final_cleaned.b1')
b9 = pd.read_pickle('final_cleaned.b1')
b10 = random.sample(range(len(b9)), 5)
os.mkdir("Random_Images")
for i, idx in enumerate(b10, b11 = 1):
    b12 = b9['timestamp_longitude_latitude'].iloc[idx]
    plot_traj(b12, f"./Random_Images/RandomImage{i}")
print("Random trajectory images saved.")