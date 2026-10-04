import pickle
import os
import utils.parameter as parameter
import utils.process_data as process_data
def preprocessing():
    print("  >> It will take about one minute. Please wait.......")
    parameters = parameter_setting()
    res1, res2 = dataset_setting(parameters)
    print(f"  >> Result1: {res1}")
    print(f"  >> Result2: {res2}")
def parameter_setting():
    parameters, conf_parameters = parameter.load_parameter()
    save_to_pickle('parameters.bin', parameters)
    return parameters
def dataset_setting(parameters):
    data_info = process_data.Data(parameters)
    data_info.data_preprocessing()
    save_to_pickle("data_info.bin", data_info)
    res1 = len(data_info.train_data)
    res2 = data_info.check_flag
    return res1, res2
def save_to_pickle(filename, data):
    dir_path = os.path.join('Pickle', filename)
    with open(dir_path, "wb") as f:
        pickle.dump(data, f)
if __name__ == '__main__':
    preprocessing()