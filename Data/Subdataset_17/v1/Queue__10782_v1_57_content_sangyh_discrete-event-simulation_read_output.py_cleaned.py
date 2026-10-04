
import matplotlib.pyplot as plt
def read_file(file_path):
    Parrival_times = []
    Pboard_times = []
    busdep_times = []
    brdgrp_length = []
    tobrdque_length = []
    with open(file_path, mode='r') as file:
        for line in file.readlines():
            segments = line.split(' ')
            if line.startswith('PASSENGER ARRIVAL EVENT'):
                parr_time = float(segments[-1].rstrip())
                Parrival_times.append(parr_time)
            elif line.startswith('PASSENGER BOARDING EVENT'):
                pbrd_time = float(segments[-1].rstrip())
                Pboard_times.append(pbrd_time)
            elif line.startswith('BUS DEPARTURE EVENT'):
                bdep_time = float(segments[-1].rstrip())
                busdep_times.append(bdep_time)
            elif line.startswith('Len of boarded group'):
                bd_grp = int(segments[-1].rstrip())
                brdgrp_length.append(bd_grp)
            elif line.startswith('Len of ToBoard_Que'):
                tobd_q = int(segments[-1].rstrip())
                tobrdque_length.append(tobd_q)
    return Parrival_times, Pboard_times, busdep_times, brdgrp_length, tobrdque_length
def plot_to_board_queue_length(tobrdque_length):
    plt.plot(range(len(tobrdque_length)), tobrdque_length, 'o', label='Passengers to board queue')
    plt.xlabel('Time')
    plt.ylabel('Queue Length')
    plt.title('Length of To-Board Queue Over Time')
    plt.legend()
    plt.show()
if __name__ == "__main__":
    file_path = "Sample_output-5.txt"
    Parrival_times, Pboard_times, busdep_times, brdgrp_length, tobrdque_length = read_file(file_path)
    plot_to_board_queue_length(tobrdque_length)