import plotly.plotly as py
import plotly.graph_objs as go
import csv
import plotly
plotly.tools.set_credentials_file(username='YOUR_USERNAME', api_key='YOUR_API_KEY')
city_list = []
positive_list = []
negative_list = []
neutral_list = []
with open('sentimentValueList.csv', 'r') as cityData:
    csv_reader = csv.reader(cityData, delimiter=',')
    for row in csv_reader:
        city_list.append(row[0])
        positive_list.append(row[1])
        negative_list.append(row[2])
        neutral_list.append(row[3])
trace_positive = go.Scatter(
    x=city_list,
    y=positive_list,
    name='Positive Sentiment Values',
    line=dict(
        color=('rgb(205, 12, 24)'),
        width=2
    )
)
trace_negative = go.Scatter(
    x=city_list,
    y=negative_list,
    name='Negative Sentiment Values',
    line=dict(
        color=('rgb(22, 96, 167)'),
        width=2
    )
)
trace_neutral = go.Scatter(
    x=city_list,
    y=neutral_list,
    name='Neutral Sentiment Values',
    line=dict(
        color=('rgb(205, 12, 24)'),
        width=2,
        dash='dash'
    )
)
data = [trace_positive, trace_negative, trace_neutral]
layout = dict(
    title='Tweet Sentiment Analysis in New York',
    xaxis=dict(title='City'),
    yaxis=dict(title='Sentiment Score(%)'),
)
fig = dict(data=data, layout=layout)
py.iplot(fig, filename='styled-line')