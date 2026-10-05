import numpy as np
from AI_module import AI_module
def receive_basic_input_data(Signal_Loss, Shock_Alert, Oxygen_Supply, Fever, Hypotension, Hypertension):
    BasicResult = {
        'Signal_Loss': Signal_Loss,
        'Shock_Alert': Shock_Alert,
        'Oxygen_Supply': Oxygen_Supply,
        'Fever': Fever,
        'Hypotension': Hypotension,
        'Hypertension': Hypertension
    }
    return BasicResult
def display_AI_input_data(Blood_oxygen, Blood_pressure, Pulses):
    pressure_predict_result, oxygen_predict_result, Pulse_predict_result = AI_module.AI_Module(Blood_oxygen, Blood_pressure, Pulses)
    print('Blood pressure prediction:')
    print(pressure_predict_result)
    print('Blood oxygen prediction:')
    print(oxygen_predict_result)
    print('Pulse prediction:')
    print(Pulse_predict_result)
input_data = receive_basic_input_data(True, False, True, False, True, False)
Blood_oxygen =
Blood_pressure =
Pulses =
display_AI_input_data(Blood_oxygen, Blood_pressure, Pulses)