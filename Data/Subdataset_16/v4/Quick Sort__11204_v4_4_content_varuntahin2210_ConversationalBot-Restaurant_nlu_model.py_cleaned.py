from rasa_nlu.b2 import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer, Metadata, Interpreter
from rasa_nlu import config
from rasa_nlu.components import ComponentBuilder
b1 = ComponentBuilder(use_cache=True)
def fonk1(data_path, config_path, b5):
    b2 = load_data(data_path)
    b3 = Trainer(config.load(config_path), b1)
    b3.train(b2)
    b4 = b3.persist(b5, fixed_model_name='restaurantnlu')
def fonk2(b5 = './models/nlu/default/restaurantnlu'):
    b6 = Interpreter.load(b5, b1)
    b7 = b6.parse("can you please suggest food")
    print(b7)
if b8 = = '__main__':
    fonk1('./data/data.json', 'config_spacy.json', './models/nlu')
    fonk2()