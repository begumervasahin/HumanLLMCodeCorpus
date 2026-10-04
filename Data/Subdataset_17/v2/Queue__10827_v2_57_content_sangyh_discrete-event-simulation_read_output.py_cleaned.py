
import matplotlib.pyplot as plt
def read_file(file_path):
    passenger_arrival_times = []
    passenger_boarding_times = []
    bus_departure_times = []
    boarded_group_lengths = []
    to_board_queue_lengths = []
    with open(file_path, mode='r') as file:
        for line in file.readlines():
            segments = line.split(' ')
            if line.startswith('PASSENGER ARRIVAL EVENT'):
                arrival_time = float(segments[-1].strip())
                passenger_arrival_times.append(arrival_time)
            elif line.startswith('PASSENGER BOARDING EVENT'):
                boarding_time = float(segments[-1].strip())
                passenger_boarding_times.append(boarding_time)
            elif line.startswith('BUS DEPARTURE EVENT'):
                departure_time = float(segments[-1].strip())
                bus_departure_times.append(departure_time)
            elif line.startswith('Len of boarded group'):
                group_length = int(segments[-1].strip())
                boarded_group_lengths.append(group_length)
            elif line.startswith('Len of ToBoard_Que'):
                queue_length = int(segments[-1].strip())
                to_board_queue_lengths.append(queue_length)
    return (passenger_arrival_times, passenger_boarding_times,
            bus_departure_times, boarded_group_lengths, to_board_queue_lengths)
def plot_to_board_queue_length(to_board_queue_lengths):
    plt.plot(range(len(to_board_queue_lengths)), to_board_queue_lengths, 'o', label='Passengers to board queue')
    plt.xlabel('Time')
    plt.ylabel('Queue Length')
    plt.title('Length of To-Board Queue Over Time')
    plt.legend()
    plt.show()
if __name__ == "__main__":
    file_path = "Sample_output-5.txt"
    (passenger_arrival_times, passenger_boarding_times, bus_departure_times,
     boarded_group_lengths, to_board_queue_lengths) = read_file(file_path)
    plot_to_board_queue_length(to_board_queue_lengths)