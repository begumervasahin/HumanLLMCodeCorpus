import os
import random
import pandas as pd
from auxiliaryfunctions import compute_distances, plot_traj
df = pd.read_csv('train_set.csv')
df = df[pd.notnull(df['journeyPatternId'])]
pd.set_option('display.max_rows', 1000000000)
df['route'] = df['vehicleID'].map(str) + df['timestamp'].map(str)
df = df.sort_values(by=['route'])
df = df.reset_index(drop=True)
print("Ready for cleaning. (completed sorting and creation of route)")
df['timestamp_longitude_latitude'] = df[['timestamp', 'longitude', 'latitude']].values.tolist()
df_2 = pd.DataFrame(columns=['TripId', 'JourneyPatternId', 'timestamp_longitude_latitude'])
TripId_LOCS = []
count = 0
for index, row in df.iterrows():
    TripId_LOCS.append(df['timestamp_longitude_latitude'][index])
    if (index + 1) == df.shape[0]:
        break
    if df['journeyPatternId'][index] != df['journeyPatternId'][index + 1]:
        df_2 = df_2.append(
            {
                'TripId': count,
                'JourneyPatternId': df['journeyPatternId'][index],
                'timestamp_longitude_latitude': TripId_LOCS
            },
            ignore_index=True
        )
        count += 1
        TripId_LOCS = []
df_2.to_pickle('TripId.df')
df3 = pd.read_pickle('TripId.df')
init_counter = len(df3.index)
print(f'Initially, we had {init_counter} trajectories')
df_final = pd.Dat