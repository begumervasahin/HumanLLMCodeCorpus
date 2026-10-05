from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer, Metadata, Interpreter
from rasa_nlu import config
from rasa_nlu.components import ComponentBuilder
builder = ComponentBuilder(use_cache=True)
def train_nlu(data_path, config_file, model_dir):
    training_data = load_data(data_path)
    trainer = Trainer(config.load(config_file), builder)
    trainer.train(training_data)
    trainer.persist(model_dir, fixed_model_name='restaurantnlu')
def run_nlu(model_dir, query):
    interpreter = Interpreter.load(model_dir, builder)
    print(interpreter.parse(query))
if __name__ == '__main__':
    train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')
    run_nlu('./models/nlu/default/restaurantnlu', "can you please suggest food")