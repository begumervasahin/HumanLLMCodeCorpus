import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import csv
plotly.tools.set_credentials_file(b1 = 'XXXXXXXX', api_key='XXXXXXXXXXXXXXXXXXXX')
b2 = list()
b3 = list()
b4 = list()
b5 = list()
with open('sentimentValueList.csv','r') as cityData:
	b6 = csv.reader(cityData, delimiter=',')
	a1 = 0
	for row in b6:
		b2.append(row[0])
		b3.append(row[1])
		b4.append(row[2])
		b5.append(row[3])
b7 = go.Scatter(
	b8 = b2,
	b9 = b3,
	b10 = 'Positive Sentiment Values',
	b11 = dict(
		b12 = ('rgb(205, 12, 24)'),
		b13 = 2)
)
b14 = go.Scatter(
	b8 = b2,
	b9 = b4,
	b10 = 'Negative Sentiment Values',
	b11 = dict(
		b12 = ('rgb(22, 96, 167)'),
		b13 = 2)
)
b15 = go.Scatter(
	b8 = b2,
	b9 = b5,
	b10 = 'Neutral Sentiment Values',
	b11 = dict(
		b12 = ('rgb(205, 12, 24)'),
		b13 = 2,
		b16 = 'b16')
)
b17 = [b7, b14, b15]
b18 = dict(title = 'Tweet Sentiment Analysis in New York',
              b19 = dict(title = 'City'),
              b20 = dict(title = 'Sentiment Score(%)'),
              )
b21 = dict(b17=b17, b18=b18)
py.iplot(b21, b22 = 'styled-b11')