22. Repository: ayush-garg341/skill_recommendation
   File: preprocess.py
   URL: https:
   Code Content:
import nltk
import pandas as pd
import re
def fonk1(frame):
	b1 = ['c
	b2 = []
	a1 = 0
	for _, b3 in frame.iteritems():
		a1 = a1 + 1
		b3 = b3.replace('>','')
		b3 = b3.replace('<','')
		b3 = b3.replace('...','')
		b4 = b3.split(',')
		b5 = []
		b6 = re.compile(r'([a-z].*[0-9])')
		b7 = re.compile(r'([a-z].*[a-z])')
		for b9 in b4:
			b8 = b9.split(' ')
			if len(b8) <= 4:
				b9 = b9.lower()
				b9 = b9.strip()
				if (b6.match(b9) or b7.match(b9) or b9 in b1):
					if '?' in b9:
						b9 = b9.replace('?', '')
					if '&amp;' in b9:
						b9 = b9.replace('&amp;', '')
					if b9.endswith('.'):
						b9 = b9.replace('.', '')
					if '&' in b9:
						b9 = b9.replace('&', '')
					if '
						b9 = b9.replace('
						b9 = b9.replace('
					if b9.startswith('.') and not b9.startswith('.net'):
						b9 = b9.replace('.', '')
					if b9 not in b5:
						b5.append(b9.strip())
		b2.append(b5)
	return b2
   README Content:
This is skill recommendation using apriori algorithm (association mining)<br />
**Description** :- We make a list of list of skills and pre-process them. After that we apply apriori algorithm on this list to get
frequent patterns and skills which are related to each other or have high probability of occuring together. There are two parameters to adjust
_support_ and _confidence_ .<br />
**get_skills.py** :- this file read the skills coming from various sources but as for now I have data stored in csv file.<br />
**http_api.py** :- This contains the code if one wants to post the data at any URL.<br />
**preprocess.py** :- this is to pre-process the data we have and remove unwanted characters.<br />
**machine_learning.py** :- this is the main file as it generates the dataframe of antecedants and consequents of skill-set.<br />
**file_handle.py** :- to save the datframe into csv so that we can look up afterwards the frequent patterns.<br />
**skill_recom.py** :- this code recommend the related skills of a particular skill by looking into the csv file that we made earlier.<br />
**suggesting_api.py**:- this is Flask api to make the code live.<br />
**database.py** :- this is if we were to connect to database and fetch data directly from there instead of storing it in csv. (still to implement)
