import sys
def auc(labels, predicted_ctr):
    sorted_indices = sorted(range(len(predicted_ctr)), key=lambda i: predicted_ctr[i], reverse=True)
    auc_score = 0.0
    tp = fp = tp_prev = fp_prev = 0.0
    last_value = predicted_ctr[sorted_indices[0]]
    for idx in sorted_indices:
        if labels[idx] > 0:
            tp += 1
        else:
            fp += 1
        if predicted_ctr[idx] != last_value:
            auc_score += (tp + tp_prev) * (fp - fp_prev) / 2.0
            tp_prev, fp_prev = tp, fp
            last_value = predicted_ctr[idx]
    auc_score += (tp + tp_prev) * (fp - fp_prev) / 2.0
    return auc_score / (tp * fp)
def evaluate(ids, true_values, predicted_values):
    labels = [int(value) for value in true_values]
    predicted_ctr = [float(value) for value in predicted_values]
    return auc(labels, predicted_ctr)
def read_input_file(file_path):
    ids, true_values, predicted_values = [], [], []
    with open(file_path, 'r') as file:
        for line in file:
            seg = line.strip().split(',')
            ids.append(seg[0])
            true_values.append(seg[1])
            predicted_values.append(seg[2])
    return ids, true_values, predicted_values
def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    ids, true_values, predicted_values = read_input_file(input_file)
    auc_score = evaluate(ids, true_values, predicted_values)
    print(f"AUC Score: {auc_score:.6f}")
if __name__ == "__main__":
    main()