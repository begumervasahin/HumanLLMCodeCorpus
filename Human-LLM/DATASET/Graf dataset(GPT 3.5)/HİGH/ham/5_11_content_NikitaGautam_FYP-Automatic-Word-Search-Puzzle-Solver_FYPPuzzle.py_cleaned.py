import os
from flask import Flask, render_template, request
from Services import MainServices
from werkzeug.utils import secure_filename
import MainImplementation
from PIL import Image
import train
import SolutionImplementation
b1 = Flask(b14)
b1.config['UPLOAD_FOLDER'] = '/Users/Nikita/PycharmProjects/FYPPuzzle/static/pics/'
b1.config['ALLOWED_EXTENSIONS'] = set(['png', 'tiff'])
def fonk1(b3):
    return '.' in b3 and b3.rsplit('.', 1)[1] in b1.config['ALLOWED_EXTENSIONS']
a1 = 0
b2 = ['purple', 'black', 'brown', 'pink', 'yellow', 'orange', 'red', 'blue', 'green', 'white']
@b1.route('/')
def fonk2():
    MainServices.clean_dir()
    return render_template('index.html')
b3 = None
@b1.route('/upload', b4 = ['POST'])
def fonk3():
    global b3
    MainServices.clean_dir()
    b3 = None
    b5 = request.files['b5']
    if b5 and fonk1(b5.b3):
        b3 = secure_filename(b5.b3)
        b5.save(os.path.join(b1.config['UPLOAD_FOLDER'], b3))
    print("here")
    MainImplementation.cropImage()
    print("b3 ---", b3)
    return render_template('retrieveM.html',b6 = '', displayVal = False, originalFile = b3)
b7 = []
@b1.route('/retrieve', b4 = ['POST'])
def fonk4():
    global b7
    b8 = MainImplementation.neuralNetTrainDetect()
    a2 = 0
    for i in range(15):
        b9 = []
        for j in range(15):
            b9.append(b8[a2])
            a2 = a2 + 1
        b7.append(b9)
        print(b9)
        print("
        b9 = []
    print(b7)
    SolutionImplementation.dictionaryProcessing()
    SolutionImplementation.getCombinationWords(b7)
    SolutionImplementation.initializeTrie()
    return render_template("showDetectedGrid.html", b7 = b7, grid = False, originalFile = b3, b10 = [], b11 = [], b12 = [], b13 = [])
@b1.route('/solutionL', b4 = ['POST'])
def fonk5():
    global b7
    global b3
    print("ajshdjasd")
    b10 = []
    b11 = []
    b12 = []
    b10, b11, b12 = SolutionImplementation.LinearSearchImplementation()
    print("Using Linear", len(b10))
    global b2
    b13 = []
    for item in b10:
        if item  not in b2:
            b13.append("NO")
        else:
            b13.append("YES")
    return render_template("showDetectedGrid.html", b7 = b7, grid = True, originalFile = b3, b10 = enumerate(b10), b11 = b11, b12 = b12, b13 = b13)
@b1.route('/solutionB', b4 = ['POST'])
def fonk6():
    global b7
    global b3
    b10 = []
    b11 = []
    b12 = []
    b10, b11, b12 = SolutionImplementation.binarySearchImplementation()
    global b2
    b13 = []
    for item in b10:
        if item  not in b2:
            b13.append("NO")
        else:
            b13.append("YES")
    print("Using Binary", len(b10))
    return render_template("showDetectedGrid.html", b7 = b7, grid=True, b10 = enumerate(b10), b11 = b11, b12 = b12, b13 = b13)
@b1.route('/solutionT', b4 = ['POST'])
def fonk7():
    global b7
    global b3
    b10 = []
    b11 = []
    b12 = []
    b10, b11, b12 = SolutionImplementation.TriesImplementation()
    print("Using TR", len(b10))
    global b2
    b13 = []
    for item in b10:
        if item  not in b2:
            b13.append("NO")
        else:
            b13.append("YES")
    return render_template("showDetectedGrid.html", b7 = b7, grid = True, b10 = enumerate(b10), b11 = b11, b12 = b12, b13 = b13)
@b1.errorhandler(Exception)
def fonk8(error):
    return render_template('error.html')
if b14 = = '__main__':
    b1.run(b15 = True)