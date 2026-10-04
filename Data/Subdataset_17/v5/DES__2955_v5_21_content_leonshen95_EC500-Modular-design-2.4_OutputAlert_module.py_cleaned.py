import numpy as np
from AI_module import AI_module
def receive_basic_input_data(signal_loss, shock_alert, oxygen_supply, fever, hypotension, hypertension):
    return {
        'Signal_Loss': signal_loss,
        'Shock_Alert': shock_alert,
        'Oxygen_Supply': oxygen_supply,
        'Fever': fever,
        'Hypotension': hypotension,
        'Hypertension': hypertension
    }
def display_ai_input_data(blood_oxygen, blood_pressure, pulses):
    ai_module = AI_module()
    pressure_predict_result = ai_module.AI_Module(blood_pressure)
    oxygen_predict_result = ai_module.AI_Module(blood_oxygen)
    pulse_predict_result = ai_module.AI_Module(pulses)
    print('Blood pressure prediction:')
    print(pressure_predict_result)
    print('Blood oxygen prediction:')
    print(oxygen_predict_result)
    print('Pulse prediction:')
    print(pulse_predict_result)
if __name__ == "__main__":
    basic_input_data = receive_basic_input_data(
        signal_loss=True,
        shock_alert=False,
        oxygen_supply=True,
        fever=False,
        hypotension=True,
        hypertension=False
    )
    print("Basic Input Data:")
    print(basic_input_data)
    blood_oxygen = np.array([95, 96, 97])
    blood_pressure = np.array([120, 122, 119])
    pulses = np.array([75, 78, 77])
    print("\nAI Module Predictions:")
    display_ai_input_data(blood_oxygen, blood_pressure, pulses)