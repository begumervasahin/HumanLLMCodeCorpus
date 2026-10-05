import re
import pandas as pd
def get_experience_years(file_path):
    years_list = []
    with open(file_path, encoding='utf-8') as file:
        content = file.read()
        pattern = re.compile(r'\d+ years')
        matches = pattern.findall(content)
        for match in matches:
            years = int(re.sub("\D", "", match))
            if years <= 10:
                years_list.append(years)
        print("Years of experience:", years_list)
        return years_list
def get_degree(file_path):
    diploma_count = 0
    bachelor_degree_count = 0
    master_degree_count = 0
    phd_count = 0
    with open(file_path, encoding='utf-8') as file:
        content = file.read()
        diploma_count = len(re.findall(r'diploma', content, flags=re.IGNORECASE))
        bachelor_degree_count = len(re.findall(r'bachelor.{0,5}degree', content, flags=re.IGNORECASE))
        master_degree_count = len(re.findall(r'master.{0,5}degree', content, flags=re.IGNORECASE))
        phd_count = len(re.findall(r'phd', content, flags=re.IGNORECASE))
    print("Number of diplomas:", diploma_count)
    print("Number of bachelor's degrees:", bachelor_degree_count)
    print("Number of master's degrees:", master_degree_count)
    print("Number of PhDs:", phd_count)
def list_to_csv(data_list):
    df = pd.DataFrame(data={"col1": data_list})
    df.to_csv("experience_years.csv", sep=',', index=False)
    print("Data saved to experience_years.csv")
def main():
    file_path = input("Enter the path of the JSON file you want to parse: ")
    get_experience_years(file_path)
    get_degree(file_path)
if __name__ == '__main__':
    main()