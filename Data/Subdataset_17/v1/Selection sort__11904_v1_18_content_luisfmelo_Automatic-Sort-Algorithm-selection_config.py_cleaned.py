import os
BASE_DIR = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + '/'
TRAIN_DATA = os.path.join(BASE_DIR, 'csv_files/train-arrays.csv')
TRAIN_TARGET_OUTPUT = os.path.join(BASE_DIR, 'csv_files/train-target.csv')
TEST_DATA = os.path.join(BASE_DIR, 'csv_files/test-arrays.csv')
DB_TRAIN_FEATURE_TABLE = 'train_features_data'
DB_TEST_FEATURE_TABLE = 'test_features_data'
DB_OUTPUT_TABLE = 'output_features'
DB_PATH = 'sqlite:
SLACK_TOKEN = 'xoxb-359976621911-4H0Z3pab9hsjqKzJVdFz9Kx0'
def print_configurations():
    print(f"Base Directory: {BASE_DIR}")
    print(f"Training Data Path: {TRAIN_DATA}")
    print(f"Training Target Output Path: {TRAIN_TARGET_OUTPUT}")
    print(f"Testing Data Path: {TEST_DATA}")
    print(f"Database Path: {DB_PATH}")
    print(f"Database Training Features Table: {DB_TRAIN_FEATURE_TABLE}")
    print(f"Database Testing Features Table: {DB_TEST_FEATURE_TABLE}")
    print(f"Database Output Features Table: {DB_OUTPUT_TABLE}")
    print(f"Slack Token: {SLACK_TOKEN}")
if __name__ == "__main__":
    print_configurations()