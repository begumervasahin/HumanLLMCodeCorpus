from rasa_nlu.b2 import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter
from rasa_nlu import config
from rasa_nlu.components import ComponentBuilder
b1 = ComponentBuilder(use_cache=True)
def fonk1(data, config_file, model_dir):
    b2 = load_data(data)
    b3 = Trainer(config.load(config_file), b1)
    b3.train(b2)
    b4 = b3.persist(model_dir, fixed_model_name='restaurantnlu')
def fonk2():
    b5 = Interpreter.load('./models/nlu/default/restaurantnlu', b1)
    print(b5.parse("can you please suggest food"))
if b6 = = '__main__':
    fonk1('./data/data.json', 'config_spacy.json', './models/nlu')
    fonk2()