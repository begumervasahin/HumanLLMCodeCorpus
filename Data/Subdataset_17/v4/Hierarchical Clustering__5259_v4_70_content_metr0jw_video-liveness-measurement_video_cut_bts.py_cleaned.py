import pandas as pd
data_load = pd.read_csv("y_prediction_bts.csv").values.flatten()
pred_data = list(data_load)
cut_start_data = []
cut_end_data = []
idx = 0
data_length = len(pred_data)
while idx < data_length - 1:
    count = 0
    most_dyn_count = 0
    if pred_data[idx] in [0.5, 1]:
        start_idx = idx
        while idx < data_length and pred_data[idx] in [0.5, 1]:
            count += 1
            if pred_data[idx] == 1:
                most_dyn_count += 1
            idx += 1
            print("TEST")
        end_idx = idx
        if count > 3 and most_dyn_count > 0:
            print("SUCCESS")
            cut_start_data.append(start_idx)
            cut_end_data.append(end_idx)
    idx += 1
cut_start_df = pd.DataFrame(cut_start_data, columns=["Start Time"])
cut_end_df = pd.DataFrame(cut_end_data, columns=["End Time"])
time_data = pd.concat([cut_start_df, cut_end_df], axis=1)
time_data.to_csv("timedata_bts.csv", index=False)