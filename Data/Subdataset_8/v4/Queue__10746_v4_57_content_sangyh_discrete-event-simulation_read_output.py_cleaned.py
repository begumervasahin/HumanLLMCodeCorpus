import matplotlib.pyplot as plt
with open("Sample_output-5.txt", mode='r') as file:
    Parrival_times = []
    Pboard_times = []
    busdep_times = []
    brdgrp_length = []
    tobrdque_length = []
    for line in file.readlines():
        if line.startswith('PASSENGER ARRIVAL EVENT'):
            segments = line.split(' ')
            parr_time = float(segments[-1].rstrip())
            Parrival_times.append(parr_time)
        elif line.startswith('PASSENGER BOARDING EVENT'):
            segments = line.split(' ')
            pbrd_time = float(segments[-1].rstrip())
            Pboard_times.append(pbrd_time)
        elif line.startswith('BUS DEPARTURE EVENT'):
            segments = line.split(' ')
            bdep_time = float(segments[-1].rstrip())
            busdep_times.append(bdep_time)
        elif line.startswith('Len of boarded group'):
            segments = line.split(' ')
            bd_grp = int(segments[-1].rstrip())
            brdgrp_length.append(bd_grp)
        elif line.startswith('Len of ToBoard_Que'):
            segments = line.split(' ')
            tobd_q = int(segments[-1].rstrip())
            tobrdque_length.append(tobd_q)
plt.plot(range(len(tobrdque_length)), tobrdque_length, 'o', label='Pass to board que')
plt.legend()
plt.show()