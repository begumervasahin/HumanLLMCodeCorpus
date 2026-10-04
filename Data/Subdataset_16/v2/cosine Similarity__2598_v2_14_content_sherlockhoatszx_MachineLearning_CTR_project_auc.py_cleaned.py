import sys
def fonk1(b5, b6):
    b1 = sorted(range(len(b6)), key=lambda i: b6[i], reverse=True)
    a1 = 0.0
    b2 = fp = tp_prev = b4 = 0.0
    b3 = b6[b1[0]]
    for idx in b1:
        if b5[idx] > 0:
            b2 += 1
        else:
            fp += 1
        if b6[idx] != b3:
            a1 += (b2 + tp_prev) * (fp - b4) / 2.0
            tp_prev, b4 = b2, fp
            b3 = b6[idx]
    a1 += (b2 + tp_prev) * (fp - b4) / 2.0
    return a1 / (b2 * fp)
def fonk2(ids, true_values, b7):
    b5 = [int(value) for value in true_values]
    b6 = [float(value) for value in b7]
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
if b9 = = "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <b10>")
        sys.exit(1)
    b10 = sys.argv[1]
    ids, true_values, b7 = fonk3(b10)
    a1 = fonk2(ids, true_values, b7)
    print(f"AUC Score: {a1:.6f}")