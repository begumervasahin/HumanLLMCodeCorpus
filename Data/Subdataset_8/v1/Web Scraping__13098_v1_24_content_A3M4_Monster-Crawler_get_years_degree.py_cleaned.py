import re
import pandas as pd
def get_experience_years(file):
    with open(file, encoding='utf-8') as f:
        years_list = []
        content = f.read()
        pattern = re.compile(r'\b\d+\s*years?\b')
        matches = pattern.findall(content)
        for match in matches:
            match = re.sub("\D", "", match)
            years = int(match)
            if years <= 10:
                years_list.append(years)
        return years_list
def get_degree(file):
    with open(file, encoding='utf-8') as f:
        content = f.read()
        diploma_count = len(re.findall(r'diploma', content, re.IGNORECASE))
        bachelor_count = len(re.findall(r'bachelor.{0,5}degree', content, re.IGNORECASE))
        master_count = len(re.findall(r'master.{0,5}degree', content, re.IGNORECASE))
        phd_count = len(re.findall(r'phd', content, re.IGNORECASE))
        print("Number of diploma:", diploma_count)
        print("Number of bachelor's degree:", bachelor_count)
        print("Number of master's degree:", master_count)
        print("Number of PhD:", phd_count)
def list_to_csv(data_list, filename):
    df = pd.DataFrame(data={"col1": data_list})
    df.to_csv(filename, sep=',', index=False)
def main():
    path = input("Enter the path of the JSON file you want to parse: ")
    experience_years = get_experience_years(path)
    degree_data = get_degree(path)
    list_to_csv(experience_years, "experience_years.csv")
if __name__ == '__main__':
    main()