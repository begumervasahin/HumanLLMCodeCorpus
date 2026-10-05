
from LSBSteg import LSBSteg
import cv2
from flask import Flask, render_template, request
import numpy as np
app = Flask(__name__, instance_relative_config=True)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'secret_xxx'
@app.route('/')
def index():
    return render_template("index.html")
def encode_text_into_image(file, text):
    img_array = np.fromstring(file.read(), np.uint8)
    image = cv2.imdecode(img_array, cv2.IMREAD_UNCHANGED)
    steg = LSBSteg(image)
    encoded_image = steg.encode_text(text)
    cv2.imwrite("my_new_image.png", encoded_image)
    return "berhasil menyisipkan"
@app.route('/api/encode', methods=['POST'])
def encode():
    if request.method == 'POST':
        file = request.files['file_gambar']
        text = request.form['text']
        message = encode_text_into_image(file, text)
        return render_template("index.html", pesan=message)
def decode_text_from_image(file):
    img_array = np.fromstring(file.read(), np.uint8)
    image = cv2.imdecode(img_array, cv2.IMREAD_UNCHANGED)
    steg = LSBSteg(image)
    decoded_text = steg.decode_text().decode("utf-8")
    return decoded_text
@app.route('/api/decode', methods=['POST'])
def decode():
    file = request.files['file_gambar']
    decoded_message = decode_text_from_image(file)
    print(decoded_message)
    return render_template("index.html", pesan=decoded_message)
if __name__ == '__main__':
    app.run()
