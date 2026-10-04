import pandas as pd
b1 = pd.read_excel("C:/Users/IMART/Downloads/Subcat_super_PMCAT.xlsx", sheet_name="Export Worksheet")
b2 = pd.read_csv("C:/Users/IMART/Desktop/My_Data/Himanshu Stopwords/wordfrequencyfinal.csv")
b3 = pd.DataFrame(columns=['Subcat_ID', 'Stopwords'])
b4 = b1['SUBCAT_ID'].unique()
b2["HIGH FREQUENCY WORDS"] = b2["HIGH FREQUENCY WORDS"].str.lower()
b1["GLCAT_MCAT_NAME"] = b1["GLCAT_MCAT_NAME"].str.lower()
b5 = b2.set_index('SUBCAT ID').T.to_dict('list')
a1 = 0
a2 = 0
a3 = 0
def fonk1(df, b8, start_index):
    b6 = ""
    while start_index < len(df) and df.iloc[start_index]["SUBCAT_ID"] == b8:
        b6 += df.iloc[start_index]["GLCAT_MCAT_NAME"] + " "
        start_index += 1
    b7 = set(b6.split())
    return " ".join(b7), start_index
while a1 < len(b2):
    b8 = b2.iloc[a1]["SUBCAT ID"]
    if b8 in b4:
        unique_words_string, a2 = fonk1(b1, b8, a2)
        b9 = unique_words_string + " " + b5[b8][0]
    else:
        b9 = b2.iloc[a1]["HIGH FREQUENCY WORDS"]
    b3.loc[a3] = [b8, b9]
    a3 += 1
    a1 += 1
b3.to_csv("700subcatwisefinalstopwords.csv", b10 = False)