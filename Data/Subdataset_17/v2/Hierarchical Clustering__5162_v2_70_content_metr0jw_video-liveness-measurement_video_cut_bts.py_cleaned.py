import pandas as pd
def load_prediction_data(file_path):
    return pd.read_csv(file_path).values.flatten().tolist()
def find_valid_sequences(pred_data, min_length=4):
    cut_start_data = []
    cut_end_data = []
    idx = 0
    data_length = len(pred_data)
    while idx < data_length:
        count = 0
        most_dyn_count = 0
        if pred_data[idx] in [0.5, 1]:
            start_idx = idx
            while idx < data_length and pred_data[idx] in [0.5, 1]:
                if pred_data[idx] == 1:
                    most_dyn_count += 1
                count += 1
                idx += 1
            end_idx = idx
            if count >= min_length and most_dyn_count > 0:
                cut_start_data.append(start_idx)
                cut_end_data.append(end_idx)
        else:
            idx += 1
    return cut_start_data, cut_end_data
def save_time_data(start_data, end_data, output_file):
    time_data = pd.DataFrame({
        "Start Time": start_data,
        "End Time": end_data
    })
    time_data.to_csv(output_file, mode='w', index=False)
def main():
    pred_data = load_prediction_data("y_prediction_bts.csv")
    cut_start_data, cut_end_data = find_valid_sequences(pred_data)
    save_time_data(cut_start_data, cut_end_data, "timedata_bts.csv")
if __name__ == "__main__":
    main()