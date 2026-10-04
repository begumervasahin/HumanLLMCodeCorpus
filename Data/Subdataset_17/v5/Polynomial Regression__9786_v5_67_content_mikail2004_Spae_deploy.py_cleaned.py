import os
import numpy as np
import requests
from flask import Flask, render_template, request
app = Flask(__name__, template_folder='web', static_folder='static')
x_values = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
def predict_temperature_from_values(temperature_values):
    coefficients = np.polyfit(x_values, temperature_values, 2)
    polynomial = np.poly1d(coefficients)
    predicted_value = round(polynomial(1), 2)
    return predicted_value
@app.route('/', methods=["GET", "POST"])
def index():
    city = request.values.get('test', type=str)
    api_key = "8da365f65510cd3b548ab105287b6f28"
    url = f"http:
    response = requests.get(url)
    json_data = response.json()
    temperature_list = [
        round(json_data['list'][i]['main']['temp'] - 273.15, 1)
        for i in [0, 1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
    ]
    current_temperature = temperature_list[0]
    future_temperatures = temperature_list[1:]
    predicted_value = predict_temperature_from_values(future_temperatures)
    weather_description = json_data['list'][0]['weather'][0]['description'].capitalize()
    return render_template('index.html', t=current_temperature, w=weather_description, n=predicted_value)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)