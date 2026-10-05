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
i = 0
row = 0
while i < len(df2):
    if df2.iloc[i]["SUBCAT_ID"] in highfreqdict.keys():
        subcatid = df2.iloc[i]["SUBCAT_ID"]
        j = i
        concatstring = ""
        while df2.iloc[i]["SUBCAT_ID"] == subcatid and i <= len(df2) - 1:
            concatstring += df2.iloc[i]["GLCAT_MCAT_NAME"] + " "
            i += 1
            if i == len(df2):
                break
        uniq = set(concatstring.split(' '))
        string1 = ""
        for x in uniq:
            if x not in string1:
                string1 += x + " "
        mergedf1.loc[row, 'MCAT_Name'] = df2.iloc[j]["GLCAT_MCAT_NAME"]
        mergedf1.loc[row, 'Subcat_ID'] = df2.iloc[j]["SUBCAT_ID"]
        s = string1 + " " + str(highfreqdict[df2.iloc[j]["SUBCAT_ID"]][0])
        mergedf1.loc[row, 'MCAT_Name&HighFrequencyWords'] = s
        row += 1
    else:
        mergedf1.loc[row, 'MCAT_Name'] = df2.iloc[i]["GLCAT_MCAT_NAME"]
        mergedf1.loc[row, 'Subcat_ID'] = df2.iloc[i]["SUBCAT_ID"]
        mergedf1.loc[row, 'MCAT_Name&HighFrequencyWords'] = df2.iloc[i]["GLCAT_MCAT_NAME"]
        i += 1
        row += 1
mergedkwdict = mergedf1[['Subcat_ID', 'MCAT_Name&HighFrequencyWords']].set_index('Subcat_ID').T.to_dict('list')
i = 0
row = 0
while i < len(df1):
    if df1.iloc[i]["FK_GLCAT_CAT_ID"] in mergedkwdict.keys():
        subcatid = df1.iloc[i]["FK_GLCAT_CAT_ID"]
        string2 = ""
        stopwords = mergedkwdict[subcatid][0]
        mcatname = df1.iloc[i]["GLCAT_MCAT_NAME"]
        for x in mcatname.split(" "):
            if x not in stopwords.split(" "):
                string2 = string2 + " " + x
        mergedf2.loc[row, 'MCAT_ID'] = df1.iloc[i]["GLCAT_MCAT_ID"]
        mergedf2.loc[row, 'PMCAT'] = df1.iloc[i]["PMCAT"]
        mergedf2.loc[row, 'MCAT_Name'] = df1.iloc[i]["GLCAT_MCAT_NAME"]
        mergedf2.loc[row, 'Subcat_ID'] = subcatid
        mergedf2.loc[row, 'Stopword'] = stopwords
        mergedf2.loc[row, 'Attribute'] = string2.strip()
        i += 1
        row += 1
    else:
        subcatid = df1.iloc[i]["FK_GLCAT_CAT_ID"]
        mergedf2.loc[row, 'MCAT_ID'] = df1.iloc[i]["GLCAT_MCAT_ID"]
        mergedf2.loc[row, 'PMCAT'] = df1.iloc[i]["PMCAT"]
        mergedf2.loc[row, 'MCAT_Name'] = df1.iloc[i]["GLCAT_MCAT_NAME"]
        mergedf2.loc[row, 'Subcat_ID'] = subcatid
        string2 = ""
        if df1.iloc[i]["FK_GLCAT_CAT_ID"] in highfreqdict.keys():
            stopwords = highfreqdict[subcatid][0]
        else:
            stopwords = ""
        mcatname = df1.iloc[i]["GLCAT_MCAT_NAME"]
        for x in mcatname.split(" "):
            if x not in stopwords.split(" "):
                string2 = string2 + " " + x
        mergedf2.loc[row, 'Stopword'] = stopwords
        mergedf2.loc[row, 'Attribute'] = string2.strip()
        i += 1
        row += 1
mergedf2['Attribute'] = mergedf2['Attribute'].str.lstrip()
mergedf2.to_csv("stopwordsremovedmcats.csv", index=False)