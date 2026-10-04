import os
b1 = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + '/'
b2 = os.path.join(b1, 'csv_files/train-arrays.csv')
b3 = os.path.join(b1, 'csv_files/train-target.csv')
b4 = os.path.join(b1, 'csv_files/test-arrays.csv')
b5 = 'train_features_data'
b6 = 'test_features_data'
b7 = 'output_features'
b8 = 'sqlite:
b9 = 'xoxb-359976621911-4H0Z3pab9hsjqKzJVdFz9Kx0'
def fonk1():
    print(f"Base Directory: {b1}")
    print(f"Training Data Path: {b2}")
    print(f"Training Target Output Path: {b3}")
    print(f"Testing Data Path: {b4}")
    print(f"Database Path: {b8}")
    print(f"Database Training Features Table: {b5}")
    print(f"Database Testing Features Table: {b6}")
    print(f"Database Output Features Table: {b7}")
    print(f"Slack Token: {b9}")
if b10 = = "__main__":
    fonk1()