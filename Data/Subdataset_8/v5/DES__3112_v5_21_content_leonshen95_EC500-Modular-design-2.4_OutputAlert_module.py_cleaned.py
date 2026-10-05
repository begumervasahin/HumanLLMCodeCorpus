import numpy as np
from AI_module import AI_module
def receive_basic_input_data(signal_loss, shock_alert, oxygen_supply, fever, hypotension, hypertension):
    basic_result = {
        'Signal_Loss': signal_loss,
        'Shock_Alert': shock_alert,
        'Oxygen_Supply': oxygen_supply,
        'Fever': fever,
        'Hypotension': hypotension,
        'Hypertension': hypertension
    }
    return basic_result
def display_AI_input_data(blood_oxygen, blood_pressure, pulses):
    pressure_predict_result, oxygen_predict_result, pulse_predict_result = AI_module.AI_Module(blood_oxygen, blood_pressure, pulses)
    print('Blood pressure prediction:')
    print(pressure_predict_result)
    print('Blood oxygen prediction:')
    print(oxygen_predict_result)
    print('Pulse prediction:')
    print(pulse_predict_result)
input_data = receive_basic_input_data(True, False, True, False, True, False)
blood_oxygen =
blood_pressure =
pulses =
display_AI_input_data(blood_oxygen, blood_pressure, pulses)