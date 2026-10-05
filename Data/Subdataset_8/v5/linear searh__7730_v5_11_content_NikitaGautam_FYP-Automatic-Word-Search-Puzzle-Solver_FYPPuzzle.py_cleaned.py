import os
from flask import Flask, render_template, request
from Services import MainServices
import MainImplementation
import SolutionImplementation
from PIL import Image
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/Users/Nikita/PycharmProjects/FYPPuzzle/static/pics/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'tiff'}
trained = 0
correctWords = {'purple', 'black', 'brown', 'pink', 'yellow', 'orange', 'red', 'blue', 'green', 'white'}
@app.route('/')
def index():
    MainServices.clean_dir()
    return render_template('index.html')
@app.route('/upload', methods=['POST'])
def upload():
    global filename
    MainServices.clean_dir()
    filename = None
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    print("File uploaded")
    MainImplementation.cropImage()
    print("Filename:", filename)
    return render_template('retrieveM.html', message='', displayVal=False, originalFile=filename)
@app.route('/retrieve', methods=['POST'])
def getMsg():
    global detected
    detected = []
    charsDetected = MainImplementation.neuralNetTrainDetect()
    k = 0
    for i in range(15):
        new_row = []
        for j in range(15):
            new_row.append(charsDetected[k])
            k += 1
        detected.append(new_row)
    print(detected)
    SolutionImplementation.dictionaryProcessing()
    SolutionImplementation.getCombinationWords(detected)
    SolutionImplementation.initializeTrie()
    return render_template("showDetectedGrid.html", detected=detected, grid=False, originalFile=filename, matchedWords=[], matchedMeaning=[], matchedDirection=[], yesNoList=[])
def search_solution(implementation):
    global detected, filename
    matchedWords = []
    matchedMeaning = []
    matchedDirection = []
    matchedWords, matchedMeaning, matchedDirection = implementation()
    print("Using", implementation.__name__)
    print("Number of Matches:", len(matchedWords))
    yesNoList = ["YES" if item in correctWords else "NO" for item in matchedWords]
    return render_template("showDetectedGrid.html", detected=detected, grid=True, originalFile=filename, matchedWords=enumerate(matchedWords), matchedMeaning=matchedMeaning, matchedDirection=matchedDirection, yesNoList=yesNoList)
@app.route('/solutionL', methods=['POST'])
def solutionL():
    return search_solution(SolutionImplementation.LinearSearchImplementation)
@app.route('/solutionB', methods=['POST'])
def solutionB():
    return search_solution(SolutionImplementation.binarySearchImplementation)
@app.route('/solutionT', methods=['POST'])
def solutionT():
    return search_solution(SolutionImplementation.TriesImplementation)
@app.errorhandler(Exception)
def all_exception_handler(error):
    return render_template('error.html')
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
if __name__ == '__main__':
    app.run(debug=True)