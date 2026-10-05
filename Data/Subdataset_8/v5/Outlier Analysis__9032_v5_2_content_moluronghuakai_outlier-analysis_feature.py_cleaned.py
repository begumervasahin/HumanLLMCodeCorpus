from math import sqrt
DIRECTION_UNKNOWN = 0
DIRECTION_UP = 1
DIRECTION_DOWN = 2
def find_peaks(data, max_distance):
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
            distance = (data[index - 1] - peak_values[-1]) / max_distance
            if distance >= R:
                peak_values.append(data[index - 1])
                peak_indices.append(index - 1)
            continue
        if current_direction == DIRECTION_DOWN and data[index] > data[index - 1]:
            current_direction = DIRECTION_UP
            distance = (peak_values[-1] - data[index - 1]) / max_distance
            if distance >= R:
                peak_values.append(data[index - 1])
                peak_indices.append(index - 1)
            continue
    return peak_values, peak_indices
def calculate_slope(peaks):
    slopes = []
    for index in range(1, len(peaks[0])):
        slope = (peaks[0][index] - peaks[0][index - 1]) / (peaks[1][index] - peaks[1][index - 1])
        slopes.append(slope)
    return slopes
def calculate_mean(data, peaks):
    means = []
    for i in range(1, len(peaks[0])):
        total = 0.0
        for j in range(peaks[1][i-1], peaks[1][i]):
            total += data[j]
        mean = total / (peaks[1][i] - peaks[1][i-1])
        means.append(mean)
    return means
def calculate_distances(slopes, peaks, means):
    distances = []
    for index in range(1, len(slopes)):
        distance = sqrt((slopes[index] - slopes[index - 1]) ** 2 +
                        (peaks[1][index] - peaks[1][index - 1]) ** 2 +
                        (means[index] - means[index - 1]) ** 2)
        distances.append(distance)
    return distances
data = (10.0, 11.0, 14.0, 13.0, 40.0, 39.0, 38.0, 60.0, 59.0, 62.0, 80.0, 81.0, 79.0, 78.0, 50.0, 52.0, 51.0, 53.0, 10.0, 9.0, 8.0, 50.0)
max_distance = 100
R = 0.1
peaks = find_peaks(data, max_distance)
slopes = calculate_slope(peaks)
means = calculate_mean(data, peaks)
distances = calculate_distances(slopes, peaks, means)
print(distances)