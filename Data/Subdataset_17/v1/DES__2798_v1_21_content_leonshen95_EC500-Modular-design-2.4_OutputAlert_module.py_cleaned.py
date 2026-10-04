import numpy as np
from AI_module import AI_module
def receive_basic_input_data(Signal_Loss, Shock_Alert, Oxygen_Supply, Fever, Hypotension, Hypertension):
    basic_result = {
        'Signal_Loss': False,
        'Shock_Alert': False,
        'Oxygen_Supply': False,
        'Fever': False,
        'Hypotension': False,
        'Hypertension': False
    }
    if Signal_Loss:
        basic_result['Signal_Loss'] = True
    if Shock_Alert:
        basic_result['Shock_Alert'] = True
    if Oxygen_Supply:
        basic_result['Oxygen_Supply'] = True
    if Fever:
        basic_result['Fever'] = True
    if Hypotension:
        basic_result['Hypotension'] = True
    if Hypertension:
        basic_result['Hypertension'] = True
    return basic_result
def display_AI_input_data(Blood_oxygen, Blood_pressure, Pulses):
    ai_module = AI_module()
    pressure_predict_result = ai_module.AI_Module(Blood_pressure)
    oxygen_predict_result = ai_module.AI_Module(Blood_oxygen)
    pulse_predict_result = ai_module.AI_Module(Pulses)
    print('Blood pressure prediction:')
    print(pressure_predict_result)
    print('Blood oxygen prediction:')
    print(oxygen_predict_result)
    print('Pulse prediction:')
    print(pulse_predict_result)
if __name__ == "__main__":
    basic_input_data = receive_basic_input_data(
        Signal_Loss=True,
        Shock_Alert=False,
        Oxygen_Supply=True,
        Fever=False,
        Hypotension=True,
        Hypertension=False
    )
    print(basic_input_data)
    Blood_oxygen = np.array([95, 96, 97])
    Blood_pressure = np.array([120, 122, 119])
    Pulses = np.array([75, 78, 77])
    display_AI_input_data(Blood_oxygen, Blood_pressure, Pulses)