import pandas as pd
def load_data(data_name):
    loaded_data = pd.read_csv(data_name)
    return loaded_data