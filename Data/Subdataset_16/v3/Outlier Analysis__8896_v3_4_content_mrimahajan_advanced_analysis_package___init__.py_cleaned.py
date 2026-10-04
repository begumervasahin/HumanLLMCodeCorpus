
import pandas as pd
import numpy as np
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = self.fonk2()
    def fonk2(self):
        try:
            b2 = pd.read_csv(self.b1)
            print("Data loaded successfully.")
            return b2
        except FileNotFoundError:
            print(f"File '{self.b1}' not found.")
            return None
    def fonk3(self):
        if self.b2 is not None:
            b3 = self.b2.describe()
            print("Summary statistics calculated.")
            return b3
        else:
            print("Data not loaded.")
            return None
    def fonk4(self):
        if self.b2 is not None:
            b4 = self.b2.isnull().sum()
            print("Missing values counted.")
            return b4
        else:
            print("Data not loaded.")
            return None
    def fonk5(self, b5 = 'mean'):
        if self.b2 is not None:
            if b5 = = 'mean':
                self.b2.fillna(self.b2.mean(), b6 = True)
            elif b5 = = 'median':
                self.b2.fillna(self.b2.median(), b6 = True)
            elif b5 = = 'mode':
                self.b2.fillna(self.b2.mode().iloc[0], b6 = True)
            else:
                print("Invalid b5. Choose from 'mean', 'median', or 'mode'.")
                return
            print(f"Missing values filled using {b5} b5.")
        else:
            print("Data not loaded.")
    def fonk6(self):
        if self.b2 is not None:
            b7 = self.b2.corr()
            print("Correlation matrix calculated.")
            return b7
        else:
            print("Data not loaded.")
            return None
    def fonk7(self, output_file):
        if self.b2 is not None:
            self.b2.to_csv(output_file, b8 = False)
            print(f"Data exported to '{output_file}'.")
        else:
            print("Data not loaded.")
if b9 = = "__main__":
    b10 = class1('b2.csv')
    print("Summary Statistics:\n", b10.fonk3())
    print("Missing Values:\n", b10.fonk4())
    b10.fonk5(b5 = 'mean')
    print("Missing Values After Filling:\n", b10.fonk4())
    print("Correlation Matrix:\n", b10.fonk6())
    b10.fonk7('processed_data.csv')