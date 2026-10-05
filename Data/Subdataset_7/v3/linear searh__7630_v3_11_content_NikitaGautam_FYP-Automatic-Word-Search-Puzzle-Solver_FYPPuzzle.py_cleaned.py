import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from PIL import Image
import MainServices
import MainImplementation
import SolutionImplementation
b1 = Flask(b10)
b1.config['UPLOAD_FOLDER'] = '/Users/Nikita/PycharmProjects/FYPPuzzle/static/pics/'
b1.config['ALLOWED_EXTENSIONS'] = set(['png', 'tiff'])
def fonk1(b3):
    return '.' in b3 and b3.rsplit('.', 1)[1] in b1.config['ALLOWED_EXTENSIONS']
@b1.route('/')
def fonk2():
    MainServices.clean_dir()
    return render_template('index.html')
@b1.route('/upload', b2 = ['POST'])
def fonk3():
    global b3
    MainServices.clean_dir()
    b3 = None
    b4 = request.files['b4']
    if b4 and fonk1(b4.b3):
        b3 = secure_filename(b4.b3)
        b5 = os.path.join(b1.config['UPLOAD_FOLDER'], b3)
        b4.save(b5)
        MainImplementation.cropImage(b5)
    return render_template('retrieveM.html', b6 = '', displayVal=False, originalFile=b3)
@b1.route('/retrieve', b2 = ['POST'])
def fonk4():
    global b7
    b7 = MainImplementation.detect_chars()
    SolutionImplementation.process_grid(b7)
    return render_template("showDetectedGrid.html", b7 = b7, grid=False, originalFile=b3, matchedWords=[], matchedMeaning=[], b8=[], b9=[])
@b1.route('/solutionL', b2 = ['POST'])
def fonk5():
    matchedWords, matchedMeaning, b8 = SolutionImplementation.LinearSearchImplementation()
    b9 = ["YES" if item in SolutionImplementation.correctWords else "NO" for item in matchedWords]
    return render_template("showDetectedGrid.html", b7 = b7, grid=True, originalFile=b3, matchedWords=enumerate(matchedWords), matchedMeaning=matchedMeaning, b8=b8, b9=b9)
@b1.route('/solutionB', b2 = ['POST'])
def fonk6():
    matchedWords, matchedMeaning, b8 = SolutionImplementation.binarySearchImplementation()
    b9 = ["YES" if item in SolutionImplementation.correctWords else "NO" for item in matchedWords]
    return render_template("showDetectedGrid.html", b7 = b7, grid=True, originalFile=b3, matchedWords=enumerate(matchedWords), matchedMeaning=matchedMeaning, b8=b8, b9=b9)
@b1.route('/solutionT', b2 = ['POST'])
def fonk7():
    matchedWords, matchedMeaning, b8 = SolutionImplementation.TriesImplementation()
    b9 = ["YES" if item in SolutionImplementation.correctWords else "NO" for item in matchedWords]
    return render_template("showDetectedGrid.html", b7 = b7, grid=True, originalFile=b3, matchedWords=enumerate(matchedWords), matchedMeaning=matchedMeaning, b8=b8, b9=b9)
@b1.errorhandler(Exception)
def fonk8(error):
    return render_template('error.html')
if b10 = = '__main__':
    b1.run(b11 = True)