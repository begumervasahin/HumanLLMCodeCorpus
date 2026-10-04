import sys
def fonk1(b5, b6):
    b1 = sorted(range(len(b6)), key=lambda i: b6[i], reverse=True)
    a1 = 0.0
    b2 = fp = tp_prev = b4 = 0.0
    b3 = b6[b1[0]]
    for i in range(len(b5)):
        if b5[b1[i]] > 0:
            b2 += 1
        else:
            fp += 1
        if b3 != b6[b1[i]]:
            a1 += (b2 + tp_prev) * (fp - b4) / 2.0
            tp_prev, b4 = b2, fp
            b3 = b6[b1[i]]
    a1 += (b2 + tp_prev) * (fp - b4) / 2.0
    return a1 / (b2 * fp)
def fonk2(ids, true_values, predict_values):
    b5 = [int(value) for value in true_values]
    b6 = [float(value) for value in predict_values]
    return fonk1(b5, b6)
def fonk3(file_path):
    ids, true_values, b7 = [], [], []
    with open(file_path, 'r') as file:
        for line in file:
            b8 = line.strip().split(',')
            ids.append(b8[0])
            true_values.append(b8[1])
            b7.append(b8[2])
    return ids, true_values, b7
def fonk4():
    if len(sys.argv) != 2:
        print("Usage: python script.py <b9>")
        sys.exit(1)
    b9 = sys.argv[1]
    ids, true_values, b7 = fonk3(b9)
    a1 = fonk2(ids, true_values, b7)
    print(f"AUC Score: {a1:.6f}")
if b10 = = "__main__":
    fonk4()