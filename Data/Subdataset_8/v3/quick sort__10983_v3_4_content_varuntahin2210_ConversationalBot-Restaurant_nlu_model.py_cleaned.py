from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Interpreter
def train_nlu(training_data_path, config_file_path, model_dir):
    training_data = load_data(training_data_path)
    trainer = Trainer(config.load(config_file_path))
    trainer.train(training_data)
    trainer.persist(model_dir, fixed_model_name='restaurantnlu')
def run_nlu(model_dir):
    interpreter = Interpreter.load(model_dir)
    print(interpreter.parse("can you please suggest food"))
if __name__ == '__main__':
    train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')
    run_nlu('./models/nlu/default/restaurantnlu')