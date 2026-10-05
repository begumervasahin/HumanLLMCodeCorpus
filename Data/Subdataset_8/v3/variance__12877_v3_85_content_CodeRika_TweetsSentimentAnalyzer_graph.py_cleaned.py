import plotly.graph_objs as go
import plotly.offline as py_offline
import csv
plotly.tools.set_credentials_file(username='YOUR_USERNAME', api_key='YOUR_API_KEY')
city_list, positive_list, negative_list, neutral_list = [], [], [], []
with open('sentimentValueList.csv', 'r') as city_data:
    csv_reader = csv.reader(city_data, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        city_list.append(row[0])
        positive_list.append(float(row[1]))
        negative_list.append(float(row[2]))
        neutral_list.append(float(row[3]))
trace_positive = go.Scatter(x=city_list, y=positive_list, name='Positive Sentiment Values',
                            line=dict(color='rgb(205, 12, 24)', width=2))
trace_negative = go.Scatter(x=city_list, y=negative_list, name='Negative Sentiment Values',
                            line=dict(color='rgb(22, 96, 167)', width=2))
trace_neutral = go.Scatter(x=city_list, y=neutral_list, name='Neutral Sentiment Values',
                           line=dict(color='rgb(0, 0, 0)', width=2, dash='dash'))
data = [trace_positive, trace_negative, trace_neutral]
layout = dict(title='Tweet Sentiment Analysis', xaxis=dict(title='City'), yaxis=dict(title='Sentiment Score (%)'))
fig = dict(data=data, layout=layout)
py_offline.plot(fig, filename='tweet_sentiment_analysis.html')