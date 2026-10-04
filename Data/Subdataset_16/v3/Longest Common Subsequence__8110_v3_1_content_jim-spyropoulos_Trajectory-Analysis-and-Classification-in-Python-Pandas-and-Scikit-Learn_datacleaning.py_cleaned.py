import os
import random
import pandas as pd
from auxiliaryfunctions import compute_distances, plot_traj
def fonk1(filepath):
    b1 = pd.read_csv(filepath)
    b1 = b1[pd.notnull(b1['journeyPatternId'])]
    pd.set_option('display.max_rows', 1000000000)
    b1['route'] = b1['vehicleID'].map(str) + b1['timestamp'].map(str)
    b1 = b1.sort_values(by=['route'])
    b1 = b1.reset_index(drop=True)
    b1['timestamp_longitude_latitude'] = b1[['timestamp', 'longitude', 'latitude']].values.tolist()
    print("Ready for cleaning. (completed sorting and creation of route)")
    return b1
def fonk2(b1):
    b2 = pd.DataFrame(b6=['TripId', 'JourneyPatternId', 'timestamp_longitude_latitude'])
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
    return b2
def fonk3(b1):
    b5 = pd.DataFrame(
        b6 = ['TripId', 'JourneyPatternId', 'timestamp_longitude_latitude', 'total_distance', 'max_distance']
    )
    a2 = 0
    a3 = 0
    for index, row in b1.iterrows():
        b7 = compute_distances(b1['timestamp_longitude_latitude'][index])
        if b7[0] <= 2:
            a2 += 1
            continue
        if b7[1] >= 2:
            a3 += 1
            continue
        b5 = b5.append(
            {
                'TripId': b1['TripId'][index],
                'JourneyPatternId': b1['JourneyPatternId'][index],
                'timestamp_longitude_latitude': b1['timestamp_longitude_latitude'][index],
                'total_distance': b7[0],
                'max_distance': b7[1]
            },
            b4 = True
        )
    return b5, a2, a3
def fonk4(b1, csv_path, pickle_path):
    b1.to_csv(csv_path)
    b1.to_pickle(pickle_path)
def fonk5(b1, b8 = 5, output_dir="Random_Images"):
    b9 = random.sample(range(0, len(b1)), b8)
    os.makedirs(output_dir, b10 = True)
    for i, elem in enumerate(b9, b11 = 1):
        print(f"I chose b12: {b1['JourneyPatternId'].iloc[elem]}")
        b12 = b1['timestamp_longitude_latitude'].iloc[elem]
        plot_traj(b12, f"{output_dir}/RandomImage{i}")
def fonk6():
    b1 = fonk1('train_set.csv')
    b13 = fonk2(b1)
    b13.to_pickle('TripId.b1')
    b14 = pd.read_pickle('TripId.b1')
    b15 = len(b14.index)
    print(f'Initially, we had {b15} trajectories')
    b5, a2, a3 = fonk3(b14)
    b16 = len(b5.index)
    print(f'We dropped {a2} trajectories from total distance.')
    print(f'We dropped {a3} trajectories from max distance.')
    print(f'Finally, we have {b16} trajectories')
    fonk4(b5, 'final_cleaned.csv', 'final_cleaned.b1')
    b17 = pd.read_pickle('final_cleaned.b1')
    fonk5(b17)
if b18 = = "__main__":
    fonk6()