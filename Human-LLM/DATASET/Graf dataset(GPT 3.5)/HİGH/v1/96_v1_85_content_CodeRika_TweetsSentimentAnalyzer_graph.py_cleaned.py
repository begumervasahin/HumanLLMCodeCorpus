import plotly.graph_objs as go
import plotly
import csv
plotly.tools.set_credentials_file(b1 = 'YOUR_USERNAME', api_key='YOUR_API_KEY')
b2 = []
b3 = []
b4 = []
b5 = []
with open('sentimentValueList.csv', 'r') as cityData:
    b6 = csv.reader(cityData, delimiter=',')
    next(b6)
    for row in b6:
        b2.append(row[0])
        b3.append(float(row[1]))
        b4.append(float(row[2]))
        b5.append(float(row[3]))
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
        b12 = ('rgb(0, 0, 0)'),
        b13 = 2,
        b16 = 'b16')
)
b17 = [b7, b14, b15]
b18 = dict(
    b19 = 'Tweet Sentiment Analysis',
    b20 = dict(b19='City'),
    b21 = dict(b19='Sentiment Score (%)')
)
b22 = dict(b17=b17, b18=b18)
plotly.offline.plot(b22, b23 = 'styled-b11.html')