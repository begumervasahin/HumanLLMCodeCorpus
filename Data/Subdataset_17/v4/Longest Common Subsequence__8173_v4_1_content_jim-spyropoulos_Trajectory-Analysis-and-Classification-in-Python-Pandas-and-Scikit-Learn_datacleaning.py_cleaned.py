import os
import random
import pandas as pd
from auxiliaryfunctions import compute_distances, plot_traj
df = pd.read_csv('train_set.csv')
df = df[pd.notnull(df['journeyPatternId'])]
pd.set_option('display.max_rows', None)
df['route'] = df['vehicleID'].map(str) + df['timestamp'].map(str)
df = df.sort_values(by=['route']).reset_index(drop=True)
print("Ready for cleaning. (Completed sorting and creation of route)")
df['timestamp_longitude_latitude'] = df[['timestamp', 'longitude', 'latitude']].values.tolist()
df_cleaned = pd.DataFrame(columns=['TripId', 'JourneyPatternId', 'timestamp_longitude_latitude'])
trip_locs = []
count = 0
for index, row in df.iterrows():
    trip_locs.append(row['timestamp_longitude_latitude'])
    if (index + 1) == df.shape[0] or row['journeyPatternId'] != df.loc[index + 1, 'journeyPatternId']:
        df_cleaned = df_cleaned.append({
            'TripId': count,
            'JourneyPatternId': row['journeyPatternId'],
            'timestamp_longitude_latitude': trip_locs
        }, ignore_index=True)
        count += 1
        trip_locs = []
df_cleaned.to_pickle('TripId.df')
df_cleaned = pd.read_pickle('TripId.df')
initial_count = len(df_cleaned)
print(f'Initially, we had {initial_count} trajectories')
df_final = pd.DataFrame(columns=['TripId', 'JourneyPatternId', 'timestamp_longitude_latitude', 'total_distance', 'max_distance'])
totaldrop = 0
maxdrop = 0
for index, row in df_cleaned.iterrows():
    total_distance, max_distance = compute_distances(row['timestamp_longitude_latitude'])
    if total_distance <= 2:
        totaldrop += 1
        continue
    if max_distance >= 2:
        maxdrop += 1
        continue
    df_final = df_final.append({
        'TripId': row['TripId'],
        'JourneyPatternId': row['JourneyPatternId'],
        'timestamp_longitude_latitude': row['timestamp_longitude_latitude'],
        'total_distance': total_distance,
        'max_distance': max_distance
    }, ignore_index=True)
print(f'We dropped {totaldrop} trajectories due to total distance.')
print(f'We dropped {maxdrop} trajectories due to max distance.')
final_count = len(df_final)
print(f'Finally, we have {final_count} trajectories')
df_final.to_csv('final_cleaned.csv')
df_final.to_pickle('final_cleaned.df')
df_gm = pd.read_pickle('final_cleaned.df')
random_indices = random.sample(range(len(df_gm)), 5)
os.mkdir("Random_Images")
for i, idx in enumerate(random_indices, start=1):
    traj = df_gm['timestamp_longitude_latitude'].iloc[idx]
    plot_traj(traj, f"./Random_Images/RandomImage{i}")
print("Random trajectory images saved.")