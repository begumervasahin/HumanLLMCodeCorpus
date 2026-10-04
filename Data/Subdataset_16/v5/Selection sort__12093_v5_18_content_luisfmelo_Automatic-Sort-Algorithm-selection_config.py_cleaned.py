import os
def fonk1(b3):
    b1 = {
        "TRAIN_DATA_PATH": os.path.join(b3, 'csv_files/train-arrays.csv'),
        "TRAIN_TARGET_OUTPUT_PATH": os.path.join(b3, 'csv_files/train-target.csv'),
        "TEST_DATA_PATH": os.path.join(b3, 'csv_files/test-arrays.csv'),
        "DATABASE_PATH": f'sqlite:
    }
    return b1
def fonk2():
    b2 = {
        "DB_TRAIN_FEATURE_TABLE": 'train_features_data',
        "DB_TEST_FEATURE_TABLE": 'test_features_data',
        "DB_OUTPUT_TABLE": 'output_features'
    }
    return b2
def fonk3():
    b3 = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    b1 = fonk1(b3)
    b2 = fonk2()
    b4 = 'xoxb-359976621911-4H0Z3pab9hsjqKzJVdFz9Kx0'
    print("Base Directory:", b3)
    for key, value in b1.items():
        print(f"{key}: {value}")
    for key, value in b2.items():
        print(f"{key}: {value}")
    print("Slack Token:", b4)
if b5 = = "__main__":
    fonk3()