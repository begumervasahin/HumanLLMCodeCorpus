import os
def define_paths(base_dir):
    paths = {
        "TRAIN_DATA_PATH": os.path.join(base_dir, 'csv_files/train-arrays.csv'),
        "TRAIN_TARGET_OUTPUT_PATH": os.path.join(base_dir, 'csv_files/train-target.csv'),
        "TEST_DATA_PATH": os.path.join(base_dir, 'csv_files/test-arrays.csv'),
        "DATABASE_PATH": f'sqlite:
    }
    return paths
def define_db_table_names():
    table_names = {
        "DB_TRAIN_FEATURE_TABLE": 'train_features_data',
        "DB_TEST_FEATURE_TABLE": 'test_features_data',
        "DB_OUTPUT_TABLE": 'output_features'
    }
    return table_names
def main():
    base_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    paths = define_paths(base_dir)
    table_names = define_db_table_names()
    slack_token = 'xoxb-359976621911-4H0Z3pab9hsjqKzJVdFz9Kx0'
    print("Base Directory:", base_dir)
    for key, value in paths.items():
        print(f"{key}: {value}")
    for key, value in table_names.items():
        print(f"{key}: {value}")
    print("Slack Token:", slack_token)
if __name__ == "__main__":
    main()