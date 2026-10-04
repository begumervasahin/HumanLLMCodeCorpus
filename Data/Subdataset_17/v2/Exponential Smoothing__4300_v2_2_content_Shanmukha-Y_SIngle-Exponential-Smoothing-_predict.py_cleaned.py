import matplotlib.pyplot as plt
def read_data(file_path):
    with open(file_path, 'r') as file:
        data = list(map(float, file.read().strip().split("\n")))
    return data
def simple_exponential_smoothing(data, alpha):
    smoothed_data = [data[0], data[1]]
    for i in range(2, len(data)):
        smoothed_value = alpha * data[i - 1] + (1 - alpha) * smoothed_data[i - 2]
        smoothed_data.append(round(smoothed_value, 3))
    return smoothed_data
def calculate_mean_absolute_error(data, smoothed_data):
    total_error = sum(abs(data[i] - smoothed_data[i]) for i in range(len(data)))
    mean_error = total_error / len(data)
    return mean_error
def plot_data(original_data, smoothed_data):
    plt.plot(original_data, color="blue", label="Original Data")
    plt.plot(smoothed_data, color="red", label="Smoothed Data")
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Original vs Smoothed Data')
    plt.show()
def main():
    file_path = "data.txt"
    alpha = 0.98
    data = read_data(file_path)
    smoothed_data = simple_exponential_smoothing(data, alpha)
    mean_error = calculate_mean_absolute_error(data, smoothed_data)
    print(f"Mean Absolute Error: {mean_error}")
    plot_data(data, smoothed_data)
if __name__ == "__main__":
    main()