from math import sqrt
R = 0.1
DIRECTION_UNKNOWN = 0
DIRECTION_UP = 1
DIRECTION_DOWN = 2
def choose_peak(data, max_d):
    peak_values = [data[0]]
    peak_indices = [0]
    current_direction = DIRECTION_UNKNOWN
    for index in range(1, len(data)):
        if current_direction == DIRECTION_UNKNOWN:
            if data[index] > data[index - 1]:
                current_direction = DIRECTION_UP
            elif data[index] < data[index - 1]:
                current_direction = DIRECTION_DOWN
            continue
        if current_direction == DIRECTION_UP and data[index] < data[index - 1]:
            current_direction = DIRECTION_DOWN
            d0 = (data[index - 1] - peak_values[-1]) / max_d
            if d0 >= R:
                peak_values.append(data[index - 1])
                peak_indices.append(index - 1)
            continue
        if current_direction == DIRECTION_DOWN and data[index] > data[index - 1]:
            current_direction = DIRECTION_UP
            d0 = (peak_values[-1] - data[index - 1]) / max_d
            if d0 >= R:
                peak_values.append(data[index - 1])
                peak_indices.append(index - 1)
            continue
    return peak_values, peak_indices
def calc_slope(peaks):
    peak_values, peak_indices = peaks
    slopes = []
    for index in range(1, len(peak_values)):
        sl = (peak_values[index] - peak_values[index - 1]) / (peak_indices[index] - peak_indices[index - 1])
        slopes.append(sl)
    return slopes
def calc_mean(data, peaks):
    _, peak_indices = peaks
    means = []
    for i in range(1, len(peak_indices)):
        segment_sum = sum(data[peak_indices[i-1]:peak_indices[i]])
        segment_mean = segment_sum / (peak_indices[i] - peak_indices[i-1])
        means.append(segment_mean)
    return means
def calc_dist(slopes, peaks, means):
    _, peak_indices = peaks
    distances = []
    for index in range(1, len(slopes)):
        d1 = sqrt((slopes[index] - slopes[index-1])**2 + (peak_indices[index] - peak_indices[index-1])**2 + (means[index] - means[index-1])**2)
        distances.append(d1)
    return distances
data0 = [10.0, 11.0, 14.0, 13.0, 40.0, 39.0, 38.0, 60.0, 59.0, 62.0, 80.0, 81.0, 79.0, 78.0, 50.0, 52.0, 51.0, 53.0, 10.0, 9.0, 8.0, 50.0]
max_d = 50.0
peaks = choose_peak(data0, max_d)
slopes = calc_slope(peaks)
means = calc_mean(data0, peaks)
distances = calc_dist(slopes, peaks, means)
print("Distances between consecutive slopes, peaks, and means:", distances)