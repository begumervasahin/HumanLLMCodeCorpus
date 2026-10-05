import numpy as np
from AI_module import AI_module
def fonk1(Signal_Loss, Shock_Alert, Oxygen_Supply, Fever, Hypotension, Hypertension):
    b1 = {
        'Signal_Loss': Signal_Loss,
        'Shock_Alert': Shock_Alert,
        'Oxygen_Supply': Oxygen_Supply,
        'Fever': Fever,
        'Hypotension': Hypotension,
        'Hypertension': Hypertension
    }
    return b1
def fonk2():
    b2 = Blood_pressure =
    b3 = pressure_predict_result, oxygen_predict_result, pulse_predict_result = AI_module.AI_Module(b2, Blood_pressure, b3)
    print('Blood pressure prediction:')
    print(pressure_predict_result)
    print('Blood oxygen prediction:')
    print(oxygen_predict_result)
    print('Pulse prediction:')
    print(pulse_predict_result)
b4 = fonk1(True, False, True, False, True, False)
fonk2()