import numpy as np
from AI_module import AI_module
def fonk1(signal_loss, shock_alert, oxygen_supply, fever, hypotension, hypertension):
    b1 = {
        'Signal_Loss': signal_loss,
        'Shock_Alert': shock_alert,
        'Oxygen_Supply': oxygen_supply,
        'Fever': fever,
        'Hypotension': hypotension,
        'Hypertension': hypertension
    }
    return b1
def fonk2(b4, blood_pressure, b5):
    pressure_predict_result, oxygen_predict_result, b2 = AI_module.AI_Module(b4, blood_pressure, b5)
    print('Blood pressure prediction:')
    print(pressure_predict_result)
    print('Blood oxygen prediction:')
    print(oxygen_predict_result)
    print('Pulse prediction:')
    print(b2)
b3 = fonk1(True, False, True, False, True, False)
b4 = blood_pressure =
b5 = fonk2(b4, blood_pressure, b5)