import os
import numpy as np
import requests
from flask import Flask, render_template, request
app = Flask(__name__, template_folder='web', static_folder='static')
x_coords = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
def predict_temperature(*temps):
    coefficients = np.polyfit(x_coords, temps, 2)
    polynomial = np.poly1d(coefficients)
    predicted_temp = round(polynomial(1), 2)
    return predicted_temp
@app.route('/', methods=["GET", "POST"])
def index():
    city = request.values.get('test', 'London')
    api_url = f"http:
    response = requests.get(api_url)
    json_data = response.json()
    temp_data = [
        round(json_data['list'][i]['main']['temp'] - 273.15, 1)
        for i in range(0, 30, 3)
    ]
    if len(temp_data) < 10:
        return "Not enough data to make predictions"
    predicted_temp = predict_temperature(*temp_data[:10])
    current_weather = json_data['list'][0]['weather'][0]['description'].capitalize()
    return render_template('index.html', t=temp_data[0], w=current_weather, n=predicted_temp)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)