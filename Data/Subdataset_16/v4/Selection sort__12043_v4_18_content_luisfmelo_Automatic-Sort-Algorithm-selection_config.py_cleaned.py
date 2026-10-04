import os
b1 = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
b2 = os.path.join(b1, 'csv_files/train-arrays.csv')
b3 = os.path.join(b1, 'csv_files/train-target.csv')
b4 = os.path.join(b1, 'csv_files/test-arrays.csv')
b5 = 'train_features_data'
b6 = 'test_features_data'
b7 = 'output_features'
b8 = 'sqlite:
b9 = 'xoxb-359976621911-4H0Z3pab9hsjqKzJVdFz9Kx0'
print("Base Directory:", b1)
print("Train Data Path:", b2)
print("Train Target Output Path:", b3)
print("Test Data Path:", b4)
print("Database Path:", b8)
print("Slack Token:", b9)