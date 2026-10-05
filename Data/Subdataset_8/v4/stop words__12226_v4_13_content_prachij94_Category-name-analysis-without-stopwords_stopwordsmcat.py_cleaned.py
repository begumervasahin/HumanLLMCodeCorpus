import pandas as pd
df1 = pd.read_excel("C:/Users/IMART/Downloads/Working MCAT_subcat.xlsx", sheet_name="Sheet2")
df2 = pd.read_excel("C:/Users/IMART/Downloads/Subcat_super_PMCAT.xlsx", sheet_name="Export Worksheet")
df3 = pd.read_excel("C:/Users/IMART/Downloads/wordfrequencyfinal.xlsx", sheet_name="wordfrequencyfinal")
df3["HIGH FREQUENCY WORDS"] = df3["HIGH FREQUENCY WORDS"].str.lower()
df2["GLCAT_MCAT_NAME"] = df2["GLCAT_MCAT_NAME"].str.lower()
df1["GLCAT_MCAT_NAME"] = df1["GLCAT_MCAT_NAME"].str.lower()
mergedf1 = pd.DataFrame(columns=['MCAT_Name', 'Subcat_ID', 'MCAT_Name&HighFrequencyWords'])
mergedf2 = pd.DataFrame(columns=['MCAT_ID', 'PMCAT', 'MCAT_Name', 'Subcat_ID', 'Stopword', 'Attribute'])
highfreqdict = df3.set_index('SUBCAT ID').T.to_dict('list')
row = 0
for i in range(len(df2)):
    subcatid = df2.iloc[i]["SUBCAT_ID"]
    if subcatid in highfreqdict.keys():
        j = i
        concatstring = ""
        while i < len(df2) and df2.iloc[i]["SUBCAT_ID"] == subcatid:
            concatstring += df2.iloc[i]["GLCAT_MCAT_NAME"] + " "
            i += 1
        uniq = set(concatstring.split(' '))
        string1 = " ".join(uniq)
        mergedf1.loc[row, 'MCAT_Name'] = df2.iloc[j]["GLCAT_MCAT_NAME"]
        mergedf1.loc[row, 'Subcat_ID'] = df2.iloc[j]["SUBCAT_ID"]
        mergedf1.loc[row, 'MCAT_Name&HighFrequencyWords'] = string1 + " " + str(highfreqdict[subcatid][0])
        row += 1
    else:
        mergedf1.loc[row, 'MCAT_Name'] = df2.iloc[i]["GLCAT_MCAT_NAME"]
        mergedf1.loc[row, 'Subcat_ID'] = df2.iloc[i]["SUBCAT_ID"]
        mergedf1.loc[row, 'MCAT_Name&HighFrequencyWords'] = df2.iloc[i]["GLCAT_MCAT_NAME"]
        i += 1
        row += 1
mergedkwdict = mergedf1[['Subcat_ID', 'MCAT_Name&HighFrequencyWords']].set_index('Subcat_ID').T.to_dict('list')
row = 0
for i in range(len(df1)):
    subcatid = df1.iloc[i]["FK_GLCAT_CAT_ID"]
    if subcatid in mergedkwdict.keys():
        stopwords = mergedkwdict[subcatid][0]
    else:
        stopwords = ""
    string2 = ""
    mcatname = df1.iloc[i]["GLCAT_MCAT_NAME"]
    for x in mcatname.split(" "):
        if x not in stopwords.split(" "):
            string2 += " " + x
    mergedf2.loc[row, 'MCAT_ID'] = df1.iloc[i]["GLCAT_MCAT_ID"]
    mergedf2.loc[row, 'PMCAT'] = df1.iloc[i]["PMCAT"]
    mergedf2.loc[row, 'MCAT_Name'] = df1.iloc[i]["GLCAT_MCAT_NAME"]
    mergedf2.loc[row, 'Subcat_ID'] = subcatid
    mergedf2.loc[row, 'Stopword'] = stopwords
    mergedf2.loc[row, 'Attribute'] = string2.strip()
    row += 1
mergedf2['Attribute'] = mergedf2['Attribute'].str.lstrip()
mergedf2.to_csv("stopwordsremovedmcats.csv", index=False)