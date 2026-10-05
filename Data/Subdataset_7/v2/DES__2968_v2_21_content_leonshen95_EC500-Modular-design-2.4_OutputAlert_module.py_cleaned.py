import numpy as np
from AI_module import AI_module
def fonk1(Signal_Loss, Shock_Alert, Oxygen_Supply, Fever, Hypotension, Hypertension):
    b1 = {
        'Signal_Loss': False,
        'Shock_Alert': False,
        'Oxygen_Supply': False,
        'Fever': False,
        'Hypotension': False,
        'Hypertension': False
    }
    if Signal_Loss:
        b1['Signal_Loss'] = True
    if Shock_Alert:
        b1['Shock_Alert'] = True
    if Oxygen_Supply:
        b1['Oxygen_Supply'] = True
    if Fever:
        b1['Fever'] = True
    if Hypotension:
        b1['Hypotension'] = True
    if Hypertension:
        b1['Hypertension'] = True
    return b1
def fonk2():
    b2 = Blood_pressure =
    b3 = pressure_predict_result, oxygen_predict_result, Pulse_predict_result = AI_module.AI_Module(b2, Blood_pressure, b3)
    print('Blood pressure prediction:')
    print(pressure_predict_result)
    print('Blood oxygen prediction:')
    print(oxygen_predict_result)
    print('Pulse prediction:')
    print(Pulse_predict_result)
b4 = fonk1(True, False, True, False, True, False)
fonk2()