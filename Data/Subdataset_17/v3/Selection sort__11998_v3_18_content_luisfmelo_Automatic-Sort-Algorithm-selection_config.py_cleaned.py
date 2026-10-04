import os
def get_base_dir():
    return os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + '/'
def get_file_path(base_dir, relative_path):
    return os.path.join(base_dir, relative_path)
BASE_DIR = get_base_dir()
TRAIN_DATA = get_file_path(BASE_DIR, 'csv_files/train-arrays.csv')
TRAIN_TARGET_OUTPUT = get_file_path(BASE_DIR, 'csv_files/train-target.csv')
TEST_DATA = get_file_path(BASE_DIR, 'csv_files/test-arrays.csv')
DB_TRAIN_FEATURE_TABLE = 'train_features_data'
DB_TEST_FEATURE_TABLE = 'test_features_data'
DB_OUTPUT_TABLE = 'output_features'
DB_PATH = f'sqlite:
SLACK_TOKEN = 'xoxb-359976621911-4H0Z3pab9hsjqKzJVdFz9Kx0'
def print_configurations():
    configurations = {
        "Base Directory": BASE_DIR,
        "Training Data Path": TRAIN_DATA,
        "Training Target Output Path": TRAIN_TARGET_OUTPUT,
        "Testing Data Path": TEST_DATA,
        "Database Path": DB_PATH,
        "Database Training Features Table": DB_TRAIN_FEATURE_TABLE,
        "Database Testing Features Table": DB_TEST_FEATURE_TABLE,
        "Database Output Features Table": DB_OUTPUT_TABLE,
        "Slack Token": SLACK_TOKEN
    }
    for key, value in configurations.items():
        print(f"{key}: {value}")
if __name__ == "__main__":
    print_configurations()