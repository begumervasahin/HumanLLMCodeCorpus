from rasa_nlu.b1 import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Interpreter
def fonk1(training_data_path, config_file_path, model_dir):
    b1 = load_data(training_data_path)
    b2 = Trainer(config.load(config_file_path))
    b2.train(b1)
    b2.persist(model_dir, b3 = 'restaurantnlu')
def fonk2(model_dir):
    b4 = Interpreter.load(model_dir)
    print(b4.parse("can you please suggest food"))
if b5 = = '__main__':
    fonk1('./data/data.json', 'config_spacy.json', './models/nlu')
    fonk2('./models/nlu/default/restaurantnlu')