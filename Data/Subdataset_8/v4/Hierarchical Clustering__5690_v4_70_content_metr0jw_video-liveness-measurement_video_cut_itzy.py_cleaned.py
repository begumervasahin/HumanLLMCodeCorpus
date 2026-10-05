import pandas as pd
prediction_data = pd.read_csv("y_prediction_itzy.csv").values
predictions = list(prediction_data)
cut_start_data = []
cut_end_data = []
idx = 0
data_length = len(predictions) - 1
while idx != data_length:
    count = 0
    most_dyn_count = 0
    if predictions[idx] == 0.5 or predictions[idx] == 1:
        start_count = idx
        while predictions[idx] == 0.5 or predictions[idx] == 1:
            idx += 1
            count += 1
            if predictions[idx] == 1:
                most_dyn_count += 1
        last_count = idx
    if count > 3 and most_dyn_count > 0:
        print("SUCCESS")
        cut_start_data.append(start_count)
        cut_end_data.append(last_count)
    idx += 1
cut_start_data = pd.DataFrame(cut_start_data, columns=["Start Time"])
cut_end_data = pd.DataFrame(cut_end_data, columns=["End Time"])
time_data = pd.concat([cut_start_data, cut_end_data], axis=1)
time_data.to_csv("timedata_itzy.csv", mode='w', index=False)