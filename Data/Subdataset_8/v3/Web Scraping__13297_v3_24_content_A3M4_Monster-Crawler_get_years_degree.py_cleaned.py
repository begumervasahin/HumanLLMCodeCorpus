import re
import pandas as pd
def extract_experience_years(file_path):
    with open(file_path, encoding='utf-8') as file:
        content = file.read()
        years_list = [int(year.strip(" years")) for year in re.findall(r'\b\d+\s*years?\b', content) if int(year.strip(" years")) <= 10]
        return years_list
def extract_degrees(file_path):
    with open(file_path, encoding='utf-8') as file:
        content = file.read()
        diploma_count = len(re.findall(r'diploma', content, re.IGNORECASE))
        bachelor_count = len(re.findall(r'bachelor.{0,5}degree', content, re.IGNORECASE))
        master_count = len(re.findall(r'master.{0,5}degree', content, re.IGNORECASE))
        phd_count = len(re.findall(r'phd', content, re.IGNORECASE))
        print("Number of diploma:", diploma_count)
        print("Number of bachelor's degree:", bachelor_count)
        print("Number of master's degree:", master_count)
        print("Number of PhD:", phd_count)
def write_to_csv(data_list, filename):
    df = pd.DataFrame(data={"Experience Years": data_list})
    df.to_csv(filename, sep=',', index=False)
def main():
    file_path = input("Enter the path of the JSON file you want to parse: ")
    experience_years = extract_experience_years(file_path)
    extract_degrees(file_path)
    write_to_csv(experience_years, "experience_years.csv")
if __name__ == '__main__':
    main()