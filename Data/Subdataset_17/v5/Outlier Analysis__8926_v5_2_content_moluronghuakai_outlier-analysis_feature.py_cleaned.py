import math
DIRECTION_UNKNOWN = 0
DIRECTION_UP = 1
DIRECTION_DOWN = 2
R = 0.1
def choose_peak(data, max_d):
    peak_values = [data[0]]
    peak_indices = [0]
    current_dir = DIRECTION_UNKNOWN
    for index in range(1, len(data)):
        if current_dir == DIRECTION_UNKNOWN:
            if data[index] > data[index - 1]:
                current_dir = DIRECTION_UP
            elif data[index] < data[index - 1]:
                current_dir = DIRECTION_DOWN
            continue
        if current_dir == DIRECTION_UP and data[index] < data[index - 1]:
            current_dir = DIRECTION_DOWN
            if (data[index - 1] - peak_values[-1]) / max_d >= R:
                peak_values.append(data[index - 1])
                peak_indices.append(index - 1)
            continue
        if current_dir == DIRECTION_DOWN and data[index] > data[index - 1]:
            current_dir = DIRECTION_UP
            if (peak_values[-1] - data[index - 1]) / max_d >= R:
                peak_values.append(data[index - 1])
                peak_indices.append(index - 1)
            continue
    return peak_values, peak_indices
def calc_slope(peaks):
    peak_values, peak_indices = peaks
    slopes = [
        (peak_values[i] - peak_values[i - 1]) / (peak_indices[i] - peak_indices[i - 1])
        for i in range(1, len(peak_values))
    ]
    return slopes
def calc_mean(data, peaks):
    peak_values, peak_indices = peaks
    means = [
        sum(data[peak_indices[i - 1]:peak_indices[i]]) / (peak_indices[i] - peak_indices[i - 1])
        for i in range(1, len(peak_values))
    ]
    return means
def calc_dist(slopes, peaks, means):
    _, peak_indices = peaks
    distances = [
        math.sqrt(
            (slopes[i] - slopes[i - 1]) ** 2 +
            (peak_indices[i] - peak_indices[i - 1]) ** 2 +
            (means[i] - means[i - 1]) ** 2
        )
        for i in range(1, len(slopes))
    ]
    return distances
data0 = [
    10.0, 11.0, 14.0, 13.0, 40.0, 39.0, 38.0, 60.0, 59.0, 62.0, 80.0, 81.0,
    79.0, 78.0, 50.0, 52.0, 51.0, 53.0, 10.0, 9.0, 8.0, 50.0
]
peaks = choose_peak(data0, max_d=100.0)
slopes = calc_slope(peaks)
means = calc_mean(data0, peaks)
distances = calc_dist(slopes, peaks, means)
print(distances)