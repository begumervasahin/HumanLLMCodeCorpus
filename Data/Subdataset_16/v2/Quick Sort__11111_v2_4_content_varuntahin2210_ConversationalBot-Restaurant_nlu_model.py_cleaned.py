from rasa_nlu.b2 import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer, Interpreter
from rasa_nlu import config
from rasa_nlu.components import ComponentBuilder
b1 = ComponentBuilder(use_cache=True)
def fonk1(data_path, config_path, model_dir):
    b2 = load_data(data_path)
    b3 = config.load(config_path)
    b4 = Trainer(b3, b1)
    b4.train(b2)
    b4.persist(model_dir, b5 = 'restaurantnlu')
def fonk2():
    b6 = Interpreter.load('./models/nlu/default/restaurantnlu', b1)
    b7 = b6.parse("can you please suggest food")
    print(b7)
if b8 = = '__main__':
    fonk1('./data/data.json', 'config_spacy.json', './models/nlu')
    fonk2()