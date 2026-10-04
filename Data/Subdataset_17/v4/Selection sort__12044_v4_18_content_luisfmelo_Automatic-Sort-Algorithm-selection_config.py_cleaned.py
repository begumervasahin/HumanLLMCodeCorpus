import os
BASE_DIR = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
TRAIN_DATA_PATH = os.path.join(BASE_DIR, 'csv_files/train-arrays.csv')
TRAIN_TARGET_OUTPUT_PATH = os.path.join(BASE_DIR, 'csv_files/train-target.csv')
TEST_DATA_PATH = os.path.join(BASE_DIR, 'csv_files/test-arrays.csv')
DB_TRAIN_FEATURE_TABLE = 'train_features_data'
DB_TEST_FEATURE_TABLE = 'test_features_data'
DB_OUTPUT_TABLE = 'output_features'
DATABASE_PATH = 'sqlite:
SLACK_TOKEN = 'xoxb-359976621911-4H0Z3pab9hsjqKzJVdFz9Kx0'
print("Base Directory:", BASE_DIR)
print("Train Data Path:", TRAIN_DATA_PATH)
print("Train Target Output Path:", TRAIN_TARGET_OUTPUT_PATH)
print("Test Data Path:", TEST_DATA_PATH)
print("Database Path:", DATABASE_PATH)
print("Slack Token:", SLACK_TOKEN)