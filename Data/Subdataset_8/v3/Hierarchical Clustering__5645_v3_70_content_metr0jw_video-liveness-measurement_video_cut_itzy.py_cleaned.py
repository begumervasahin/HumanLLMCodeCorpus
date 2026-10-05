import pandas as pd
prediction_data = pd.read_csv("y_prediction_itzy.csv").values
predictions = list(prediction_data)
start_times = []
end_times = []
idx = 0
while idx < len(predictions) - 1:
    segment_length = 0
    most_dyn_count = 0
    if predictions[idx] == 0.5 or predictions[idx] == 1:
        start_time = idx
        while predictions[idx] == 0.5 or predictions[idx] == 1:
            idx += 1
            segment_length += 1
            if predictions[idx] == 1:
                most_dyn_count += 1
        end_time = idx
        if segment_length > 3 and most_dyn_count > 0:
            start_times.append(start_time)
            end_times.append(end_time)
    idx += 1
start_times_df = pd.DataFrame(start_times, columns=["Start Time"])
end_times_df = pd.DataFrame(end_times, columns=["End Time"])
time_data = pd.concat([start_times_df, end_times_df], axis=1)
time_data.to_csv("timedata_itzy.csv", mode='w', index=False)