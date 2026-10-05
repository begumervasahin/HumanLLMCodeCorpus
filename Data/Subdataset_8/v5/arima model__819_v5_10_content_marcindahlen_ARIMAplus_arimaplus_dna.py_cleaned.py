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
        self.population_size = 15
        self.dna_generation = []
        self.generation = []
        self.results = []
        self.current_generation_nr = 1
        self.max_generations = 50
        self.default_dna_codes = [
            "00010011010010110010110010110010100001001010100000000000000000000000000000000000000000",
            "00100010000011000000100101001011001101111100010110001000110000000000000000000000000000",
            "10000000000000000000000000000000010000010011110110001011000000000000000000000001011000",
            "11010101000100010010000100010001010110000001100000001011000000000011110000000001011000"
        ]
        self.dna_generation.extend(self.default_dna_codes)
        while len(self.dna_generation) != self.population_size:
            self.dna_generation.append(self.generate_random_dna())
    def evaluate(self, input_data=[]):
        print("Evaluation:")
        print(input_data)
        self.results = []
        for dna_code in self.dna_generation:
            self.generation.append(Entity(dna_code))
        for entity in self.generation:
            self.results.append(entity.forecasting(input_data))
    def evolve(self, input_data=[]):
        self.average_rmse = sum([entity.rmse for entity in self.generation]) / len(self.generation)
        self.deviated_rmse = ap_math.deviation([entity.rmse for entity in self.generation])
        for i, entity in enumerate(self.generation):
            if entity.rmse > (self.average_rmse + self.deviated_rmse):
                del self.generation[i]
        self.generation.sort(key=lambda x: x.rmse, reverse=False)
        if self.generation[0].rmse < ap_math.deviation(input_data) or self.current_generation_nr >= self.max_generations:
            return True
        else:
            if len(self.generation) >= 2:
                while len(self.generation) < math.ceil(self.population_size / 2):
                    self.generation.append(self.mutate(self.cross_over(self.generation[0], self.generation[1])))
                while len(self.generation) <= self.population_size:
                    self.generation.append(self.generate_random_dna())
            else:
                while len(self.generation) <= self.population_size:
                    self.generation.append(self.generate_random_dna())
            self.current_generation_nr += 1
            return False
    def generate_random_dna(self):
        code = ""
        for _ in range(0, 86):
            code += "1" if random.randint(0, 100) % 2 == 0 else "0"
        return code
    def mutate(self, dna_code):
        dna_list = list(dna_code)
        for i, c in enumerate(dna_list):
            dna_list[i] = c if random.randint(0, len(dna_list)) != 0 else ("1" if c == "0" else "0")
        return ''.join(dna_list)
    def cross_over(self, dna_code_A, dna_code_B):
        cross_no = random.randint(1, math.floor(self.population_size / 2))
        cross_point = sorted(set(random.gauss(len(dna_code_A) / 2, len(dna_code_B) / 6) for _ in range(cross_no)))
        code_C = ""
        last_cross_point = 0
        for cross in cross_point:
            code_C += dna_code_A[last_cross_point:cross]
            last_cross_point = cross
            dna_code_A, dna_code_B = dna_code_B, dna_code_A
        code_C += dna_code_A[last_cross_point:]
        return code_C
    def save_best_dna(self):
        best_dna = self.generation[0].dna
        with open(os.path.expanduser("~/the_dna.txt"), 'w') as f:
            f.write(best_dna)
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
        self.decode_dna(dna)
        print("Created entity with topology:")
        print(self.topology)
    def decode_dna(self, dna):
        dna_parts = [dna[i:i+7] for i in range(0, len(dna), 7)]
        dna_int = lambda x: int(x, 2)
        self.forecast_type = dna_int(dna[:3])
        self.typ_AR = dna_int(dna[3:5])
        self.typ_I = dna_int(dna[5:7])
        for i, part in enumerate(dna_parts[2:7]):
            self.typ_coefA += dna_int(part) * math.pow(2, i * 4)
        self.typ_coefA /= 10
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
        print("Forecasting data normalised:")
        print(self.data_in)
        if self.forecast_type == 0:
            self.data_median = forecasting.ARIMA(self.typ_AR, self.typ_MA, self.typ_coefA, self.typ_coefB,
                                                 self.typ_coefC, self.typ_errorA, self.typ_errorB, self.typ_errorC,
                                                 self.data_in)
            self.data_out = [el[0] for el in self.data_median]
            self.rmse = ap_math.rmse(self.data_in, self.data_out)
            return self.data_out
        elif self.forecast_type == 1:
            pass
        elif self.forecast_type == 2:
            pass
    def DifferentiationType(self):
        return self.typ_I
def main():
    pop = Population()
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pop.evaluate(data)
    while not pop.evolve(data):
        pass
    pop.save_best_dna()
if __name__ == "__main__":
    main()