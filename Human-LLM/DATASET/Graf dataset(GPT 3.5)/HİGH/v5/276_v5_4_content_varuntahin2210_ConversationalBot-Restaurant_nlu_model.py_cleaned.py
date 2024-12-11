from rasa_nlu.b2 import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer, Metadata, Interpreter
from rasa_nlu import config
from rasa_nlu.components import ComponentBuilder
b1 = ComponentBuilder(use_cache=True)
def fonk1(data_path, config_file, model_dir):
    b2 = load_data(data_path)
    b3 = Trainer(config.load(config_file), b1)
    b3.train(b2)
    b3.persist(model_dir, b4 = 'restaurantnlu')
def fonk2(model_dir, query):
    b5 = Interpreter.load(model_dir, b1)
    print(b5.parse(query))
if b6 = = '__main__':
    fonk1('./data/data.json', 'config_spacy.json', './models/nlu')
    fonk2('./models/nlu/default/restaurantnlu', "can you please suggest food")