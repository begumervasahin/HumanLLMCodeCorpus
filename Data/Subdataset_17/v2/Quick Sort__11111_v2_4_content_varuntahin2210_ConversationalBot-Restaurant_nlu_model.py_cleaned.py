from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer, Interpreter
from rasa_nlu import config
from rasa_nlu.components import ComponentBuilder
builder = ComponentBuilder(use_cache=True)
def train_nlu(data_path, config_path, model_dir):
    training_data = load_data(data_path)
    nlu_config = config.load(config_path)
    trainer = Trainer(nlu_config, builder)
    trainer.train(training_data)
    trainer.persist(model_dir, fixed_model_name='restaurantnlu')
def run_nlu():
    interpreter = Interpreter.load('./models/nlu/default/restaurantnlu', builder)
    result = interpreter.parse("can you please suggest food")
    print(result)
if __name__ == '__main__':
    train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')
    run_nlu()