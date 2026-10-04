
import matplotlib.pyplot as plt
def parse_file(file_path):
    with open(file_path, mode='r') as file:
        arrival_times = []
        boarding_times = []
        bus_departure_times = []
        boarded_group_lengths = []
        to_board_queue_lengths = []
        for line in file.readlines():
            segments = line.split(' ')
            if line.startswith('PASSENGER ARRIVAL EVENT'):
                arrival_time = float(segments[-1].rstrip())
                arrival_times.append(arrival_time)
            elif line.startswith('PASSENGER BOARDING EVENT'):
                boarding_time = float(segments[-1].rstrip())
                boarding_times.append(boarding_time)
            elif line.startswith('BUS DEPARTURE EVENT'):
                departure_time = float(segments[-1].rstrip())
                bus_departure_times.append(departure_time)
            elif line.startswith('Len of boarded group'):
                group_length = int(segments[-1].rstrip())
                boarded_group_lengths.append(group_length)
            elif line.startswith('Len of ToBoard_Que'):
                queue_length = int(segments[-1].rstrip())
                to_board_queue_lengths.append(queue_length)
    return arrival_times, boarding_times, bus_departure_times, boarded_group_lengths, to_board_queue_lengths
def plot_queue_lengths(queue_lengths):
    plt.plot(range(len(queue_lengths)), queue_lengths, 'o', label='Pass to board queue')
    plt.legend()
    plt.xlabel('Event Index')
    plt.ylabel('Queue Length')
    plt.title('To-Board Queue Length Over Time')
    plt.show()
if __name__ == '__main__':
    input_file_path = "Sample_output-5.txt"
    arrival_times, boarding_times, bus_departure_times, boarded_group_lengths, to_board_queue_lengths = parse_file(input_file_path)
    plot_queue_lengths(to_board_queue_lengths)