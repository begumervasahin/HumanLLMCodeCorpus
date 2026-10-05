import arimaplus_neurony as ann
import arimaplus_przewidywanie as forecasting
import arimaplus_math as ap_math
import math
import sys
import random
import os.path
import struct
class Population:
    def __init__(self):
        self.quantity = 15
        self.dna_generation = []
        self.generation = []
        self.results = []
        self.generation_nr = 1
        self.max_generation = 50
        self.mod_pureARIMA = "00010011010010110010110010110010100001001010100000000000000000000000000000000000000000"
        self.mod_pureANN = "00100010000011000000100101001011001101111100010110001000110000000000000000000000000000"
        self.mod_ANNreg = "10000000000000000000000000000000010000010011110110001011000000000000000000000001011000"
        self.mod_ARIMANN = "11010101000100010010000100010001010110000001100000001011000000000011110000000001011000"
        self.dna_generation.extend([self.mod_pureANN, self.mod_ANNreg, self.mod_ARIMANN, self.mod_pureARIMA])
        while len(self.dna_generation) != self.quantity:
            self.dna_generation.append(self.code_generation())
    def evaluation(self, data_in=[]):
        print("Evaluation:")
        print(data_in)
        self.results = []
        for dna_code in self.dna_generation:
            self.generation.append(Entity(dna_code))
        for entity in self.generation:
            self.results.append(entity.forecasting(data_in))
    def anagenesis(self, data_in=[]):
        average_rmse = sum([entity.rmse for entity in self.generation]) / len(self.generation)
        deviated_rmse = ap_math.deviation([entity.rmse for entity in self.generation])
        for i in range(len(self.generation) - 1, -1, -1):
            if self.generation[i].rmse > (average_rmse + deviated_rmse):
                del self.generation[i]
        self.generation.sort(key=lambda x: x.rmse)
        if self.generation[0].rmse < ap_math.deviation(data_in) or self.generation_nr >= self.max_generation:
            return True
        else:
            if len(self.generation) >= 2:
                while len(self.generation) < math.ceil(self.quantity / 2):
                    self.generation.append(self.mutate(self.inheritance(self.generation[0], self.generation[1])))
                while len(self.generation) <= self.quantity:
                    self.generation.append(self.code_generation())
            else:
                while len(self.generation) <= self.quantity:
                    self.generation.append(self.code_generation())
            self.generation_nr += 1
            return False
    def code_generation(self):
        code = ""
        for _ in range(0, 86):
            p = random.randint(0, 100)
            code += "1" if p % 2 == 0 else "0"
        return code
    def mutate(self, code):
        mutated_code = list(code)
        for i, _ in enumerate(mutated_code):
            if random.randint(0, len(code)) == 0:
                mutated_code[i] = "1" if code[i] == "0" else "0"
        return "".join(mutated_code)
    def inheritance(self, code_A, code_B):
        cross_no = random.randint(1, math.floor(self.quantity / 2))
        cross_point = sorted(random.sample(range(len(code_A)), cross_no))
        code_C = ""
        last_point = 0
        for point in cross_point:
            code_C += code_A[last_point:point] if random.randint(0, 2) == 0 else code_B[last_point:point]
            last_point = point
        code_C += code_A[last_point:] if random.randint(0, 2) == 0 else code_B[last_point:]
        return code_C
    def save_dna(self):
        with open(os.path.expanduser("~/the_dna.txt"), "w") as f:
            f.write(self.generation[0].dna)
class Entity:
    def __init__(self, dna):
        self.rmse = 0
        self.data_in = []
        self.data_out = []
        self.data_median = []
        self.forecast_type = 0
        self.typ_AR = 0
        self.typ_I = 0
        self.typ_MA = 0
        self.typ_coefA = 1
        self.typ_coefB = 1
        self.typ_coefC = 1
        self.typ_errorA = 1
        self.typ_errorB = 1
        self.typ_errorC = 1
        self.window_length = 0
        self.layer_quantity = 0
        self.neuron_type = 0
        self.learning_lambda = 0.1
        self.topology = {}
        self.create_entity(dna)
    def create_entity(self, dna):
        for i in range(0, 3):
            self.forecast_type += int(dna[i]) * math.pow(2, i)
        for i in range(3, 5):
            self.typ_AR += int(dna[i]) * math.pow(2, i - 3)
        for i in range(5, 7):
            self.typ_I += int(dna[i]) * math.pow(2, i - 5)
        for i in range(7, 9):
            self.typ_MA += int(dna[i]) * math.pow(2, i - 7)
        for i in range(9, 13):
            self.typ_coefA += int(dna[i]) * math.pow(2, i - 9)
        self.typ_coefA = self.typ_coefA / 10
        for i in range(13, 17):
            self.typ_coefB += int(dna[i]) * math.pow(2, i - 13)
        self.typ_coefB = self.typ_coefB / 10
        for i in range(17, 21):
            self.typ_coefC += int(dna[i]) * math.pow(2, i - 17)
        self.typ_coefC = self.typ_coefC / 10
        for i in range(21, 25):
            self.typ_errorA += int(dna[i]) * math.pow(2, i - 21)
        self.typ_errorA = self.typ_errorA / 10
        for i in range(25, 29):
            self.typ_errorB += int(dna[i]) * math.pow(2, i - 25)
        self.typ_errorB = self.typ_errorB / 10
        for i in range(29, 33):
            self.typ_errorC += int(dna[i]) * math.pow(2, i - 29)
        self.typ_errorC = self.typ_errorC / 10
        for i in range(33, 37):
            self.window_length += int(dna[i]) * math.pow(2, i - 33)
        self.window_length = self.window_length + 1
        for i in range(37, 39):
            self.neuron_type += int(dna[i]) * math.pow(2, i - 37)
        for i in range(39, 45):
            self.learning_lambda += int(dna[i]) * math.pow(2, i - 39)
        self.learning_lambda = 1 / (self.learning_lambda + 1)
        for i in range(0, 6):
            if int(dna[45 + i * 7]) == 1:
                self.topology[self.layer_quantity] = sum(
                    list(map(lambda x: int(x[1]) * math.pow(2, int(x[0])), enumerate(dna[45 + i * 7:45 + i * 7 + 6]))))
                self.topology[self.layer_quantity] = self.topology[self.layer_quantity] + 1
                self.layer_quantity += 1
        print("Created entity with topology:")
        print(self.topology)
    def forecasting(self, data=[]):
        self.data_in = data
        print("Forecasting data input:")
        print(self.data_in)
        while len(self.data_in) % self.window_length != 0:
            del self.data_in[0]
        if self.typ_I == 0:
            self.data_in = ap_math.normalise(self.data_in)
        else:
            self.data_in = forecasting.DataDifferentiation(self.typ_I, self.data_in)
        print("Forecasting data normalized:")
        print(self.data_in)
        if self.forecast_type == 0:
            self.data_median = forecasting.ARIMA(self.typ_AR, self.typ_MA, self.typ_coefA, self.typ_coefB,
                                                 self.typ_coefC, self.typ_errorA, self.typ_errorB, self.typ_errorC,
                                                 self.data_in)
            self.data_out = [el[0] for el in self.data_median]
            self.rmse = ap_math.rmse(self.data_in, self.data_out)
            return self.data_out
        elif self.forecast_type == 1:
            if self.neuron_type == 0:
                self.network = ann.simpleNetwork(self.window_length, self.topology, self.forecast_type, self.typ_AR + self.typ_MA)
            elif self.neuron_type == 1:
                self.network = ann.gruNetwork(self.window_length, self.topology, self.forecast_type, self.typ_AR + self.typ_MA)
            elif self.neuron_type == 2:
                self.network = ann.lstmNetwork(self.window_length, self.topology, self.forecast_type, self.typ_AR + self.typ_MA)
            elif self.neuron_type == 3:
                self.network = ann.simpleNetwork(self.window_length, self.topology, self.forecast_type, self.typ_AR + self.typ_MA)
            for i in range(0, int(len(self.data_in) / self.window_length)):
                self.data_median.extend(
                    self.network.forward_pass(self.data_in[i * self.window_length:i * self.window_length + self.window_length]))
                if i < int(len(self.data_in) / self.window_length - 1):
                    self.network.backward_pass(
                        self.data_in[(i + 1) * self.window_length:(i + 1) * self.window_length + self.window_length], self.learning_lambda,
                        self.data_in[i * self.window_length:i * self.window_length + self.window_length])
            self.rmse = ap_math.rmse(self.data_in, self.data_median)
            return self.data_median
        else:
            self.rmse = sys.maxsize
            return 0
def main():
    population = Population()
    data_to_evaluate = []
    population.evaluation(data_to_evaluate)
    while not population.anagenesis(data_to_evaluate):
        population.evaluation(data_to_evaluate)
    population.save_dna()
if __name__ == "__main__":
    main()