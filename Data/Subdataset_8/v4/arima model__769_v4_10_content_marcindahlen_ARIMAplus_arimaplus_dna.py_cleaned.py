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
    def evaluation(self, dane_in=[]):
        print("Evaluation:")
        print(dane_in)
        self.results = []
        for dna_code in self.dna_generation:
            self.generation.append(Entity(dna_code))
        for entity in self.generation:
            self.results.append(entity.forecasting(dane_in))
    def anagenesis(self, dane_in=[]):
        self.average_rmse = sum([entity.rmse for entity in self.generation]) / len(self.generation)
        self.deviated_rmse = ap_math.deviation([entity.rmse for entity in self.generation])
        for i, entity in enumerate(self.generation):
            if entity.rmse > (self.average_rmse + self.deviated_rmse):
                del self.generation[i]
        self.generation.sort(key=lambda x: x.rmse, reverse=False)
        if self.generation[0].rmse < ap_math.deviation(dane_in) or self.generation_nr >= self.max_generation:
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
    def mutate(self, kod):
        kod_list = list(kod)
        for i, c in enumerate(kod_list):
            kod_list[i] = kod_list[i] if random.randint(0, len(kod_list)) != 0 else ("1" if kod_list[i] == "0" else "0")
        return ''.join(kod_list)
    def inheritance(self, code_A, code_B):
        code_C = ""
        cross_no = random.randint(1, math.floor(self.quantity / 2))
        cross_point = []
        for _ in range(0, cross_no):
            cross_point.append(math.floor(random.gauss(len(code_A) / 2, len(code_B) / 6)))
        cross_point = list(set(cross_point))
        if len(cross_point) == 1:
            code_C = code_A[0:cross_point[0]] + code_B[cross_point[0]:len(code_B)] if random.randint(0, 2) == 0 else code_B[0:cross_point[0]] + code_A[cross_point[0]:len(code_A)]
        else:
            code_C = code_A[0:cross_point[0]] if random.randint(0, 2) == 0 else code_B[0:cross_point[0]]
            for i, n in enumerate(cross_point, start=1):
                code_C += code_A[cross_point[i - 1]:n] if random.randint(0, 2) == 0 else code_B[cross_point[i - 1]:n]
            code_C += code_A[cross_point[len(cross_point) - 1]:] if random.randint(0, 2) == 0 else code_B[cross_point[len(cross_point) - 1]:]
        return code_C
    def save_dna(self):
        with open(os.path.expanduser("~/the_dna.txt"), 'w') as f:
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
                self.topology[self.layer_quantity] = sum(list(map(lambda x: int(x[1]) * math.pow(2, int(x[0])), enumerate(dna[45 + i * 7:45 + i * 7 + 6]))))
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
            if self.neuron_type == 0:
                self.network = ann.simpleNetwork(self.window_length, self.topology, self.forecast_type, self.typ_AR + self.typ_MA)
            elif self.neuron_type == 1:
                self.network = ann.gruNetwork(self.window_length, self.topology, self.forecast_type, self.typ_AR + self.typ_MA)
            elif self.neuron_type == 2:
                self.network = ann.lstmNetwork(self.window_length, self.topology, self.forecast_type, self.typ_AR + self.typ_MA)
            elif self.neuron_type == 3:
                self.network = ann.simpleNetwork(self.window_length, self.topology, self.forecast_type, self.typ_AR + self.typ_MA)
            for i in range(0, int(len(self.data_in) / self.window_length)):
                self.data_median.extend(self.network.forward_pass(self.data_in[i * self.window_length:i * self.window_length + self.window_length]))
                if i < int(len(self.data_in) / self.window_length - 1):
                    self.network.backward_pass(self.data_in[(i + 1) * self.window_length:(i + 1) * self.window_length + self.window_length],
                                               self.learning_lambda, self.data_in[i * self.window_length:i * self.window_length + self.window_length])
            self.rmse = ap_math.rmse(self.data_in, self.data_median)
            return self.data_median
        elif self.forecast_type == 2:
            self.rmse = sys.maxsize
            return 0
        elif self.forecast_type == 3:
            self.rmse = sys.maxsize
            return 0
        elif self.forecast_type == 4:
            coefficients = forecasting.linearRegression(self.window_length, self.data_in)
            if self.neuron_type == 0:
                self.network = ann.simpleNetwork(self.window_length, self.topology, self.forecast_type, self.typ_AR + self.typ_MA)
            elif self.neuron_type == 1:
                self.network = ann.gruNetwork(self.window_length, self.topology, self.forecast_type, self.typ_AR + self.typ_MA)
            elif self.neuron_type == 2:
                self.network = ann.lstmNetwork(self.window_length, self.topology, self.forecast_type, self.typ_AR + self.typ_MA)
            elif self.neuron_type == 3:
                self.network = ann.simpleNetwork(self.window_length, self.topology, self.forecast_type, self.typ_AR + self.typ_MA)
            for i in range(0, int(len(self.data_in) / self.window_length)):
                self.data_median.append(self.network.forward_pass(self.data_in[int(i * self.window_length):int(i * self.window_length + self.window_length)]))
                if i < int(len(self.data_in) / self.window_length - 1):
                    self.network.backward_pass(coefficients[i], self.learning_lambda,
                                               self.data_in[int(i * self.window_length):int(i * self.window_length + self.window_length)])
            mem = 1
            for i in self.data_in:
                mem = mem + 1 if mem < self.window_length else 1
                self.data_out.append(mem * self.data_median[int(i / self.window_length)])
            self.rmse = ap_math.rmse(self.data_in, self.data_out)
            return self.data_out
        elif self.forecast_type == 5:
            coefficients = forecasting.polynomialRegression(self.window_length, 2, self.data_in)
            if self.neuron_type == 0:
                self.network = ann.simpleNetwork(self.window_length, self.topology, self.forecast_type, self.typ_AR + self.typ_MA)
            elif self.neuron_type == 1:
                self.network = ann.gruNetwork(self.window_length, self.topology, self.forecast_type, self.typ_AR + self.typ_MA)
            elif self.neuron_type == 2:
                self.network = ann.lstmNetwork(self.window_length, self.topology, self.forecast_type, self.typ_AR + self.typ_MA)
            elif self.neuron_type == 3:
                self.network = ann.simpleNetwork(self.window_length, self.topology, self.forecast_type, self.typ_AR + self.typ_MA)
            for i in range(0, len(self.data_in) / self.window_length):
                self.data_median.append(self.network.forward_pass(self.data_in[i * self.window_length:i * self.window_length + self.window_length]))
            if i < len(self.data_in) / self.window_length - 1:
                self.network.backward_pass(coefficients[i], self.learning_lambda,
                                           self.data_in[i * self.window_length:i * self.window_length + self.window_length])
            mem = 1
            for i in self.data_in:
                mem = mem + 1 if mem < self.window_length else 1
                self.data_out.append(mem ** 2 * self.data_median[int(i / self.window_length)] + mem * self.data_median[int(i / self.window_length)])
            self.rmse = ap_math.rmse(self.data_in, self.data_out)
            return self.data_out
        elif self.forecast_type == 6 and self.typ_AR != 0:
            self.arima_out = forecasting.ARIMA(self.typ_MA, self.typ_AR, self.typ_coefA, self.typ_coefB,
                                               self.typ_coefC, self.typ_errorA, self.typ_errorB, self.typ_errorC,
                                               self.data_in)
            for i in range(0, len(self.data_in) / self.window_length):
                self.data_median.extend(self.network.forward_pass(self.data_in[i * self.window_length:i * self.window_length + self.window_length]))
                if i < len(self.data_in) / self.window_length - 1:
                    self.network.backward_pass(self.arima_out[i * self.window_length:i * self.window_length + self.window_length][1],
                                               self.learning_lambda, self.data_in[i * self.window_length:i * self.window_length + self.window_length])
                self.data_out.append(self.arima_out[i][0] - self.data_median[i])
            self.rmse = ap_math.rmse(self.data_in, self.data_out)
            return self.data_out
        elif self.forecast_type == 7 and self.typ_AR != 0:
            self.arima_out = forecasting.ARIMA(self.typ_MA, self.typ_AR, self.typ_coefA, self.typ_coefB,
                                               self.typ_coefC, self.typ_errorA, self.typ_errorB, self.typ_errorC,
                                               self.data_in)
            for i in range(0, len(self.data_in) / self.window_length):
                self.data_median.extend(self.network.forward_pass(self.data_in[i * self.window_length:i * self.window_length + self.window_length]))
                if i < len(self.data_in) / self.window_length - 1:
                    self.network.backward_pass(self.arima_out[i * self.window_length:i * self.window_length + self.window_length][1],
                                               self.learning_lambda, self.data_in[i * self.window_length:i * self.window_length + self.window_length])
                self.data_out.append(self.arima_out[i][0] - self.data_median[i])
            self.rmse = ap_math.rmse(self.data_in, self.data_out)
            return self.data_out
    def DifferentiationType(self):
        return self.typ_I
    def drawing(self, bits, *series):
        self.row_no_4 = lambda n: int(math.ceil(n / 4)) * 4
        self.row_no_8 = lambda n: int(math.ceil(n / 8)) * 8
        self.format_short = lambda n: struct.pack("<h", n)
        self.format_int = lambda n: struct.pack("<i", n)
        self.result = []
        for i, el in enumerate(series):
            height = len(el)
            width = int(self.row_no_8(bits) / 8)
            shift = [0] * (self.row_no_4(width) - width)
            size = self.format_int(self.row_no_4(bits) * height + 0x20)
            self.result.append((b"BM" + size + b"\x00\x00\x00\x00\x20\x00\x00\x00\x0C\x00\x00\x00" +
                self.format_short(width) + self.format_short(height) + b"\x01\x00\x01\x00\xff\xff\xff\x00\x00\x00" +
                b"".join([bytes(row + shift) for row in reversed(el)])))