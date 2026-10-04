from rasa_nlu.b2 import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer, Interpreter
from rasa_nlu import config
from rasa_nlu.components import ComponentBuilder
b1 = ComponentBuilder(use_cache=True)
def fonk1(b9, b10, b11):
    b2 = load_data(b9)
    b3 = config.load(b10)
    b4 = Trainer(b3, b1)
    b4.train(b2)
    b4.persist(b11, b5 = 'restaurantnlu')
def fonk2():
    b6 = Interpreter.load('./models/nlu/default/restaurantnlu', b1)
    b7 = b6.parse("can you please suggest food")
    print(b7)
if b8 = = '__main__':
    b9 = './data/data.json'
    b10 = 'config_spacy.json'
    b11 = './models/nlu'
    fonk1(b9, b10, b11)
    fonk2()