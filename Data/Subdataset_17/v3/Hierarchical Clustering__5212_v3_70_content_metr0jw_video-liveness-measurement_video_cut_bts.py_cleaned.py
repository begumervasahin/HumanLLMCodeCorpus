import pandas as pd
def load_prediction_data(file_path):
    return pd.read_csv(file_path).values.flatten().tolist()
def find_valid_sequences(pred_data, min_length=4):
    start_indices = []
    end_indices = []
    idx = 0
    data_length = len(pred_data)
    while idx < data_length:
        count = 0
        ones_count = 0
        if pred_data[idx] in [0.5, 1]:
            start_idx = idx
            while idx < data_length and pred_data[idx] in [0.5, 1]:
                if pred_data[idx] == 1:
                    ones_count += 1
                count += 1
                idx += 1
            end_idx = idx
            if count >= min_length and ones_count > 0:
                start_indices.append(start_idx)
                end_indices.append(end_idx)
        else:
            idx += 1
    return start_indices, end_indices
def save_time_data(start_indices, end_indices, output_file):
    time_data = pd.DataFrame({
        "Start Time": start_indices,
        "End Time": end_indices
    })
    time_data.to_csv(output_file, index=False)
def main():
    pred_data = load_prediction_data("y_prediction_bts.csv")
    start_indices, end_indices = find_valid_sequences(pred_data)
    save_time_data(start_indices, end_indices, "timedata_bts.csv")
if __name__ == "__main__":
    main()