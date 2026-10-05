import matplotlib.pyplot as plt
def read_events_from_file(file_name):
    passenger_arrival_times = []
    passenger_boarding_times = []
    bus_departure_times = []
    boarded_group_lengths = []
    to_board_queue_lengths = []
    with open(file_name, mode='r') as file:
        for line in file.readlines():
            if line.startswith('PASSENGER ARRIVAL EVENT'):
                segments = line.split(' ')
                arrival_time = float(segments[-1].rstrip())
                passenger_arrival_times.append(arrival_time)
            elif line.startswith('PASSENGER BOARDING EVENT'):
                segments = line.split(' ')
                boarding_time = float(segments[-1].rstrip())
                passenger_boarding_times.append(boarding_time)
            elif line.startswith('BUS DEPARTURE EVENT'):
                segments = line.split(' ')
                departure_time = float(segments[-1].rstrip())
                bus_departure_times.append(departure_time)
            elif line.startswith('Len of boarded group'):
                segments = line.split(' ')
                group_length = int(segments[-1].rstrip())
                boarded_group_lengths.append(group_length)
            elif line.startswith('Len of ToBoard_Que'):
                segments = line.split(' ')
                queue_length = int(segments[-1].rstrip())
                to_board_queue_lengths.append(queue_length)
    return passenger_arrival_times, passenger_boarding_times, bus_departure_times, \
           boarded_group_lengths, to_board_queue_lengths
def plot_data(data, label):
    plt.plot(range(len(data)), data, 'o', label=label)
    plt.legend()
    plt.show()
def main():
    file_name = "Sample_output-5.txt"
    passenger_arrival_times, passenger_boarding_times, bus_departure_times, \
    boarded_group_lengths, to_board_queue_lengths = read_events_from_file(file_name)
    plot_data(to_board_queue_lengths, 'Passenger Queue Length')
if __name__ == "__main__":
    main()