import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from PIL import Image
import MainServices
import MainImplementation
import SolutionImplementation
b1 = Flask(b13)
b1.config['UPLOAD_FOLDER'] = '/Users/Nikita/PycharmProjects/FYPPuzzle/static/pics/'
b1.config['ALLOWED_EXTENSIONS'] = set(['png', 'tiff'])
def fonk1(b2):
    return '.' in b2 and b2.rsplit('.', 1)[1] in b1.config['ALLOWED_EXTENSIONS']
@b1.route('/')
def fonk2():
    MainServices.clean_dir()
    return render_template('index.html')
b2 = None
@b1.route('/upload', b3 = ['POST'])
def fonk3():
    global b2
    MainServices.clean_dir()
    b2 = None
    b4 = request.files['b4']
    if b4 and fonk1(b4.b2):
        b2 = secure_filename(b4.b2)
        b4.save(os.path.join(b1.config['UPLOAD_FOLDER'], b2))
    MainImplementation.cropImage()
    return render_template('retrieveM.html', b5 = '', displayVal=False, originalFile=b2)
b6 = []
@b1.route('/retrieve', b3 = ['POST'])
def fonk4():
    global b6
    b6.clear()
    b7 = MainImplementation.neuralNetTrainDetect()
    a1 = 0
    for i in range(15):
        b8 = []
        for j in range(15):
            b8.append(b7[a1])
            a1 = a1 + 1
        b6.append(b8)
    SolutionImplementation.dictionaryProcessing()
    SolutionImplementation.getCombinationWords(b6)
    SolutionImplementation.initializeTrie()
    return render_template("showDetectedGrid.html", b6 = b6, grid=False, originalFile=b2, b9=[], b10=[], b11=[], b12=[])
@b1.route('/solutionL', b3 = ['POST'])
def fonk5():
    global b6
    global b2
    b9 = []
    b10 = []
    b11 = []
    b9, b10, b11 = SolutionImplementation.LinearSearchImplementation()
    b12 = ["YES" if item in SolutionImplementation.correctWords else "NO" for item in b9]
    return render_template("showDetectedGrid.html", b6 = b6, grid=True, originalFile=b2, b9=enumerate(b9), b10=b10, b11=b11, b12=b12)
@b1.route('/solutionB', b3 = ['POST'])
def fonk6():
    global b6
    global b2
    b9 = []
    b10 = []
    b11 = []
    b9, b10, b11 = SolutionImplementation.binarySearchImplementation()
    b12 = ["YES" if item in SolutionImplementation.correctWords else "NO" for item in b9]
    return render_template("showDetectedGrid.html", b6 = b6, grid=True, originalFile=b2, b9=enumerate(b9), b10=b10, b11=b11, b12=b12)
@b1.route('/solutionT', b3 = ['POST'])
def fonk7():
    global b6
    global b2
    b9 = []
    b10 = []
    b11 = []
    b9, b10, b11 = SolutionImplementation.TriesImplementation()
    b12 = ["YES" if item in SolutionImplementation.correctWords else "NO" for item in b9]
    return render_template("showDetectedGrid.html", b6 = b6, grid=True, originalFile=b2, b9=enumerate(b9), b10=b10, b11=b11, b12=b12)
@b1.errorhandler(Exception)
def fonk8(error):
    return render_template('error.html')
if b13 = = '__main__':
    b1.run(b14 = True)