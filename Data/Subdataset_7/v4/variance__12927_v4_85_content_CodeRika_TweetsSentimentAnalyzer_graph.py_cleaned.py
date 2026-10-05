import plotly.plotly as py
import plotly.graph_objs as go
import csv
import plotly
plotly.tools.set_credentials_file(b1 = 'YOUR_USERNAME', api_key='YOUR_API_KEY')
b2 = []
b3 = []
b4 = []
b5 = []
with open('sentimentValueList.csv', 'r') as cityData:
    b6 = csv.reader(cityData, delimiter=',')
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
        a1 = 2
    )
)
b13 = go.Scatter(
    b8 = b2,
    b9 = b4,
    b10 = 'Negative Sentiment Values',
    b11 = dict(
        b12 = ('rgb(22, 96, 167)'),
        a1 = 2
    )
)
b14 = go.Scatter(
    b8 = b2,
    b9 = b5,
    b10 = 'Neutral Sentiment Values',
    b11 = dict(
        b12 = ('rgb(205, 12, 24)'),
        a1 = 2,
        b15 = 'b15'
    )
)
b16 = [b7, b13, b14]
b17 = dict(
    b18 = 'Tweet Sentiment Analysis in New York',
    b19 = dict(b18='City'),
    b20 = dict(b18='Sentiment Score(%)'),
)
b21 = dict(b16=b16, b17=b17)
py.iplot(b21, b22 = 'styled-b11')