from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer, Interpreter
from rasa_nlu import config
from rasa_nlu.components import ComponentBuilder
builder = ComponentBuilder(use_cache=True)
def train_nlu(data_path, config_path, model_dir):
    training_data = load_data(data_path)
    training_config = config.load(config_path)
    trainer = Trainer(training_config, builder)
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name='restaurantnlu')
    print(f"Model trained and saved at: {model_directory}")
def run_nlu(model_dir='./models/nlu/default/restaurantnlu'):
    interpreter = Interpreter.load(model_dir, builder)
    result = interpreter.parse("can you please suggest food")
    print("Parsed result:", result)
if __name__ == '__main__':
    data_path = './data/data.json'
    config_path = 'config_spacy.json'
    model_dir = './models/nlu'
    train_nlu(data_path, config_path, model_dir)
    run_nlu(model_dir)