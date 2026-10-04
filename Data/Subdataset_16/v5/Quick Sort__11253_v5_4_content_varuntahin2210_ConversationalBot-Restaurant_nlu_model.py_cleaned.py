from rasa_nlu.b2 import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer, Interpreter
from rasa_nlu import config
from rasa_nlu.components import ComponentBuilder
b1 = ComponentBuilder(use_cache=True)
def fonk1(b10, b11, b6):
    b2 = load_data(b10)
    b3 = config.load(b11)
    b4 = Trainer(b3, b1)
    b4.train(b2)
    b5 = b4.persist(b6, fixed_model_name='restaurantnlu')
    print(f"Model trained and saved at: {b5}")
def fonk2(b6 = './models/nlu/default/restaurantnlu'):
    b7 = Interpreter.load(b6, b1)
    b8 = b7.parse("can you please suggest food")
    print("Parsed b8:", b8)
if b9 = = '__main__':
    b10 = './data/data.json'
    b11 = 'config_spacy.json'
    b6 = './models/nlu'
    fonk1(b10, b11, b6)
    fonk2(b6)