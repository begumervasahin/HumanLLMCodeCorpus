import os
import random
import pandas as pd
from auxiliaryfunctions import compute_distances, plot_traj
def load_and_prepare_data(filepath):
    df = pd.read_csv(filepath)
    df = df[pd.notnull(df['journeyPatternId'])]
    pd.set_option('display.max_rows', 1000000000)
    df['route'] = df['vehicleID'].map(str) + df['timestamp'].map(str)
    df = df.sort_values(by=['route'])
    df = df.reset_index(drop=True)
    df['timestamp_longitude_latitude'] = df[['timestamp', 'longitude', 'latitude']].values.tolist()
    print("Ready for cleaning. (completed sorting and creation of route)")
    return df
def create_trips(df):
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
    return df_2
def clean_data(df):
    df_final = pd.DataFrame(
        columns=['TripId', 'JourneyPatternId', 'timestamp_longitude_latitude', 'total_distance', 'max_distance']
    )
    totaldrop = 0
    maxdrop = 0
    for index, row in df.iterrows():
        td = compute_distances(df['timestamp_longitude_latitude'][index])
        if td[0] <= 2:
            totaldrop += 1
            continue
        if td[1] >= 2:
            maxdrop += 1
            continue
        df_final = df_final.append(
            {
                'TripId': df['TripId'][index],
                'JourneyPatternId': df['JourneyPatternId'][index],
                'timestamp_longitude_latitude': df['timestamp_longitude_latitude'][index],
                'total_distance': td[0],
                'max_distance': td[1]
            },
            ignore_index=True
        )
    return df_final, totaldrop, maxdrop
def save_data(df, csv_path, pickle_path):
    df.to_csv(csv_path)
    df.to_pickle(pickle_path)
def plot_random_trajectories(df, num_samples=5, output_dir="Random_Images"):
    r5 = random.sample(range(0, len(df)), num_samples)
    os.makedirs(output_dir, exist_ok=True)
    for i, elem in enumerate(r5, start=1):
        print(f"I chose traj: {df['JourneyPatternId'].iloc[elem]}")
        traj = df['timestamp_longitude_latitude'].iloc[elem]
        plot_traj(traj, f"{output_dir}/RandomImage{i}")
def main():
    df = load_and_prepare_data('train_set.csv')
    df_trips = create_trips(df)
    df_trips.to_pickle('TripId.df')
    df3 = pd.read_pickle('TripId.df')
    init_counter = len(df3.index)
    print(f'Initially, we had {init_counter} trajectories')
    df_final, totaldrop, maxdrop = clean_data(df3)
    final_counter = len(df_final.index)
    print(f'We dropped {totaldrop} trajectories from total distance.')
    print(f'We dropped {maxdrop} trajectories from max distance.')
    print(f'Finally, we have {final_counter} trajectories')
    save_data(df_final, 'final_cleaned.csv', 'final_cleaned.df')
    df_gm = pd.read_pickle('final_cleaned.df')
    plot_random_trajectories(df_gm)
if __name__ == "__main__":
    main()