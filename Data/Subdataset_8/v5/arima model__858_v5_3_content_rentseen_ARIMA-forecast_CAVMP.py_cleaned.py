from __future__ import print_function
import numpy as np
import pandas as pd
import random
import math
import time
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARIMA
VM_RANGE = 15
PM_NUMBER = 20
NVM_NUMBER = 150
U_MEAN = 0.06111
SLICE_NUMBER = 20
RAND_RANGE = 0.6
RACK_NUMBER = 16
P = 3
Q = 1
def arima_predict(origin_data):
    p, q = P, Q
    log_data = np.log(origin_data)
    predict_data = [-1]
    for i in range(p, -1, -1):
        for j in range(q, -1, -1):
            try:
                model = ARIMA(log_data, order=(i, 0, j))
                results_arima = model.fit(disp=-1)
                predict_data = np.exp(results_arima.predict(len(log_data), len(log_data), dynamic=True))
                if not math.isnan(predict_data[0]):
                    return predict_data[0] + 0.008
            except:
                continue
    return predict_data[0] + 0.008
def generate_u():
    base = random.randrange(6)
    return [(math.sin(base + t) + 1 + RAND_RANGE * random.random()) * U_MEAN for t in range(SLICE_NUMBER)]
class VM:
    def __init__(self):
        self.usage = generate_u()
    def predict_load(self):
        return arima_predict(self.usage)
class PM:
    def __init__(self, rack_id):
        self.vm_count = random.randrange(VM_RANGE - 5, VM_RANGE)
        self.vms = [VM() for _ in range(self.vm_count)]
        self.rack_id = rack_id
        self.load = -1
    def calculate_load(self):
        self.load = min(1, sum(vm.predict_load() for vm in self.vms))
class Rack:
    def __init__(self, rack_id):
        self.pms = [PM(rack_id) for _ in range(PM_NUMBER)]
class NVM:
    def __init__(self):
        self.utilization = 0.07 + 0.06 * random.random()
        self.destinations = []
    def add_destination(self, pm_id):
        self.destinations.append(pm_id)
def simulate():
    racks = [Rack(rack_id) for rack_id in range(RACK_NUMBER)]
    nvms = sorted([NVM() for _ in range(NVM_NUMBER)], key=lambda nvm: nvm.utilization, reverse=True)
def main():
    start_time = time.time()
    simulate()
    end_time = time.time()
    print("Simulation completed in {:.2f} seconds.".format(end_time - start_time))
if __name__ == "__main__":
    main()