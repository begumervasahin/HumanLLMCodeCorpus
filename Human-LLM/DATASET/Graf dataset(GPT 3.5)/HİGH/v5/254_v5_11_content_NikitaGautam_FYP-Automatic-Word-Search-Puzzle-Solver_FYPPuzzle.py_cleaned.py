import os
from flask import Flask, render_template, request
from Services import MainServices
import MainImplementation
import SolutionImplementation
from PIL import Image
from werkzeug.utils import secure_filename
b1 = Flask(b14)
b1.config['UPLOAD_FOLDER'] = '/Users/Nikita/PycharmProjects/FYPPuzzle/static/pics/'
b1.config['ALLOWED_EXTENSIONS'] = {'png', 'tiff'}
a1 = 0
b2 = {'purple', 'black', 'brown', 'pink', 'yellow', 'orange', 'red', 'blue', 'green', 'white'}
@b1.route('/')
def fonk1():
    MainServices.clean_dir()
    return render_template('index.html')
@b1.route('/upload', b3 = ['POST'])
def fonk2():
    global b4
    MainServices.clean_dir()
    b4 = None
    b5 = request.files['b5']
    if b5 and fonk9(b5.b4):
        b4 = secure_filename(b5.b4)
        b5.save(os.path.join(b1.config['UPLOAD_FOLDER'], b4))
    print("File uploaded")
    MainImplementation.cropImage()
    print("Filename:", b4)
    return render_template('retrieveM.html', b6 = '', displayVal=False, originalFile=b4)
@b1.route('/retrieve', b3 = ['POST'])
def fonk3():
    global b7
    b7 = []
    b8 = MainImplementation.neuralNetTrainDetect()
    a2 = 0
    for i in range(15):
        b9 = []
        for j in range(15):
            b9.append(b8[a2])
            a2 += 1
        b7.append(b9)
    print(b7)
    SolutionImplementation.dictionaryProcessing()
    SolutionImplementation.getCombinationWords(b7)
    SolutionImplementation.initializeTrie()
    return render_template("showDetectedGrid.html", b7 = b7, grid=False, originalFile=b4, b10=[], b11=[], b12=[], b13=[])
def fonk4(implementation):
    global b7, b4
    b10 = []
    b11 = []
    b12 = []
    b10, b11, b12 = implementation()
    print("Using", implementation.b14)
    print("Number of Matches:", len(b10))
    b13 = ["YES" if item in b2 else "NO" for item in b10]
    return render_template("showDetectedGrid.html", b7 = b7, grid=True, originalFile=b4, b10=enumerate(b10), b11=b11, b12=b12, b13=b13)
@b1.route('/solutionL', b3 = ['POST'])
def fonk5():
    return fonk4(SolutionImplementation.LinearSearchImplementation)
@b1.route('/solutionB', b3 = ['POST'])
def fonk6():
    return fonk4(SolutionImplementation.binarySearchImplementation)
@b1.route('/solutionT', b3 = ['POST'])
def fonk7():
    return fonk4(SolutionImplementation.TriesImplementation)
@b1.errorhandler(Exception)
def fonk8(error):
    return render_template('error.html')
def fonk9(b4):
    return '.' in b4 and b4.rsplit('.', 1)[1] in b1.config['ALLOWED_EXTENSIONS']
if b14 = = '__main__':
    b1.run(b15 = True)