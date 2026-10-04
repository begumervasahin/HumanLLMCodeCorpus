import os
def fonk1():
    return os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + '/'
def fonk2(base_dir, relative_path):
    return os.path.join(base_dir, relative_path)
b1 = fonk1()
b2 = fonk2(b1, 'csv_files/train-arrays.csv')
b3 = fonk2(b1, 'csv_files/train-target.csv')
b4 = fonk2(b1, 'csv_files/test-arrays.csv')
b5 = 'train_features_data'
b6 = 'test_features_data'
b7 = 'output_features'
b8 = f'sqlite:
b9 = 'xoxb-359976621911-4H0Z3pab9hsjqKzJVdFz9Kx0'
def fonk3():
    b10 = {
        "Base Directory": b1,
        "Training Data Path": b2,
        "Training Target Output Path": b3,
        "Testing Data Path": b4,
        "Database Path": b8,
        "Database Training Features Table": b5,
        "Database Testing Features Table": b6,
        "Database Output Features Table": b7,
        "Slack Token": b9
    }
    for key, value in b10.items():
        print(f"{key}: {value}")
if b11 = = "__main__":
    fonk3()