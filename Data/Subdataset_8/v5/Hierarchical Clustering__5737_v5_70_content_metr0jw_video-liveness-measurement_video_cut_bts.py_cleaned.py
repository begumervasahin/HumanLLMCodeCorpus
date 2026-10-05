import pandas as pd
prediction_data = pd.read_csv("y_prediction_bts.csv").values
predictions = list(prediction_data)
segment_start_times = []
segment_end_times = []
idx = 0
while idx < len(predictions) - 1:
    count = 0
    most_dynamic_count = 0
    if predictions[idx] == 0.5 or predictions[idx] == 1:
        start_idx = idx
        while predictions[idx] == 0.5 or predictions[idx] == 1:
            idx += 1
            count += 1
            if predictions[idx] == 1:
                most_dynamic_count += 1
        end_idx = idx
        if count > 3 and most_dynamic_count > 0:
            segment_start_times.append(start_idx)
            segment_end_times.append(end_idx)
    idx += 1
start_times_df = pd.DataFrame(segment_start_times, columns=["Start Time"])
end_times_df = pd.DataFrame(segment_end_times, columns=["End Time"])
time_data = pd.concat([start_times_df, end_times_df], axis=1)
time_data.to_csv("timedata_bts.csv", mode='w', index=False)