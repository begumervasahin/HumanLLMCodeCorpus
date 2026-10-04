import math
DIRECTION_UNKNOWN = 0
DIRECTION_UP = 1
DIRECTION_DOWN = 2
R = 0.1
def choose_peak(data, max_d):
    peak_values = [data[0]]
    peak_indices = [0]
    current_dir = DIRECTION_UNKNOWN
    d0 = 0.0
    for index in range(1, len(data)):
        if current_dir == DIRECTION_UNKNOWN:
            if data[index] > data[index - 1]:
                current_dir = DIRECTION_UP
            elif data[index] < data[index - 1]:
                current_dir = DIRECTION_DOWN
            continue
        if current_dir == DIRECTION_UP and data[index] < data[index - 1]:
            current_dir = DIRECTION_DOWN
            d0 = (data[index - 1] - peak_values[-1]) / max_d
            if d0 >= R:
                peak_values.append(data[index - 1])
                peak_indices.append(index - 1)
            continue
        if current_dir == DIRECTION_DOWN and data[index] > data[index - 1]:
            current_dir = DIRECTION_UP
            d0 = (peak_values[-1] - data[index - 1]) / max_d
            if d0 >= R:
                peak_values.append(data[index - 1])
                peak_indices.append(index - 1)
            continue
    return peak_values, peak_indices
def calc_slope(peak):
    slopes = []
    for index in range(1, len(peak[0])):
        slope = (peak[0][index] - peak[0][index - 1]) / (peak[1][index] - peak[1][index - 1])
        slopes.append(slope)
    return slopes
def calc_mean(data, peak):
    means = []
    for i in range(1, len(peak[0])):
        segment_sum = sum(data[peak[1][i-1]:peak[1][i]])
        mean_value = segment_sum / (peak[1][i] - peak[1][i-1])
        means.append(mean_value)
    return means
def calc_dist(slopes, peaks, means):
    distances = []
    for index in range(1, len(slopes)):
        distance = math.sqrt(
            (slopes[index] - slopes[index - 1]) ** 2 +
            (peaks[1][index] - peaks[1][index - 1]) ** 2 +
            (means[index] - means[index - 1]) ** 2
        )
        distances.append(distance)
    return distances
data0 = [10.0, 11.0, 14.0, 13.0, 40.0, 39.0, 38.0, 60.0, 59.0, 62.0, 80.0, 81.0, 79.0, 78.0, 50.0, 52.0, 51.0, 53.0, 10.0, 9.0, 8.0, 50.0]
peaks = choose_peak(data0, max_d=100.0)
slopes = calc_slope(peaks)
means = calc_mean(data0, peaks)
distances = calc_dist(slopes, peaks, means)
print(distances)