import requests
from bs4 import BeautifulSoup
def get_all_links(web_page, file_names, file_common_names, file_symptoms):
    response = requests.get(web_page)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a")
    last_link_index = len(links) - 1
    for index, link in enumerate(links):
        href = link.get("href")
        if len(href) == 5:
            continue
        if href.endswith("index.htm"):
            find_exit = str(links[index])
            if ">H.I.<" in find_exit:
                return
            continue
        next_page = "http:
        remedy_response = requests.get(next_page)
        remedy_soup = BeautifulSoup(remedy_response.text, "html.parser")
        paragraphs = remedy_soup.find_all("p")
        name = paragraphs[2].get_text()
        file_names.write(name + "\n")
        common_names = paragraphs[3].get_text().replace("        ", "")
        common_names = common_names.replace("(", "").replace(")", "")
        common_names = common_names[1:].strip()
        formatted_common_names = convert_to_csv(common_names)
        file_common_names.write(formatted_common_names + "\n")
        diseases = extract_diseases(remedy_soup)
        file_symptoms.write(diseases + "\n")
        break
def extract_diseases(soup):
    info = str(soup)
    pass_clinical = 0
    start_diseases = 0
    stop_diseases = 0
    for index, char in enumerate(info):
        if info[index:index+8] == "Clinical":
            pass_clinical = 1
        if pass_clinical == 1 and info[index:index+4] == "</b>":
            start_diseases = index + 4
        if start_diseases > 0 and info[index:index+13] == "</blockquote>":
            stop_diseases = index
            break
    reformatted_diseases = info[start_diseases:stop_diseases]
    reformatted_diseases = reformatted_diseases.replace("<i>", "").replace("</i>", "")
    reformatted_diseases = reformatted_diseases.replace("<font color=", "")
    reformatted_diseases = reformatted_diseases.replace("</font>", "").replace("\n", "")
    reformatted_diseases = reformatted_diseases.replace("        ", "")
    out_rec = convert_to_csv(reformatted_diseases)
    return out_rec
def convert_to_csv(out_rec):
    csv_record = '"'
    upto = 0
    for index, char in enumerate(out_rec):
        if char == '.':
            if out_rec[index-1:index] == 'N' or out_rec[index-1:index] == 'O':
                continue
            csv_record += out_rec[upto:index] + '","'
            whitespace_count = 1
            while out_rec[index + whitespace_count:index + whitespace_count + 1] == ' ':
                whitespace_count += 1
            upto = index + whitespace_count
    csv_record = csv_record[:-2]
    for index, char in enumerate(csv_record):
        if char == '"' and ('A' <= csv_record[index+1:index+2] <= 'Z'):
            csv_record = csv_record[:index+1] + '1' + csv_record[index+1:]
    for index, char in enumerate(csv_record):
        if char == '"':
            if csv_record[index+1:index+2] == "1":
                csv_record = csv_record[:index+2] + '","' + csv_record[index+2:]
            if csv_record[index+1:index+2] == "2":
                csv_record = csv_record[:index+2] + '","' + csv_record[index+2:]
    return csv_record
def main():
    file_names = open("h-remedies", "w")
    file_common_names = open("commonRemedyNames", "w")
    file_symptoms = open("remedy-symptoms", "w")
    for x in range(26):
        web_page = "http:
        get_all_links(web_page, file_names, file_common_names, file_symptoms)
    file_names.close()
    file_common_names.close()
    file_symptoms.close()
main()