import plotly.graph_objs as go
import plotly.offline as py_offline
import csv
plotly.tools.set_credentials_file(b1 = 'YOUR_USERNAME', api_key='YOUR_API_KEY')
city_list, positive_list, negative_list, b2 = [], [], [], []
with open('sentimentValueList.csv', 'r') as city_data:
    b3 = csv.reader(city_data, delimiter=',')
    next(b3)
    for row in b3:
        city_list.append(row[0])
        positive_list.append(float(row[1]))
        negative_list.append(float(row[2]))
        b2.append(float(row[3]))
b4 = go.Scatter(x=city_list, y=positive_list, name='Positive Sentiment Values',
                            b5 = dict(color='rgb(205, 12, 24)', width=2))
b6 = go.Scatter(x=city_list, y=negative_list, name='Negative Sentiment Values',
                            b5 = dict(color='rgb(22, 96, 167)', width=2))
b7 = go.Scatter(x=city_list, y=b2, name='Neutral Sentiment Values',
                           b5 = dict(color='rgb(0, 0, 0)', width=2, dash='dash'))
b8 = [b4, b6, b7]
b9 = dict(title='Tweet Sentiment Analysis', xaxis=dict(title='City'), yaxis=dict(title='Sentiment Score (%)'))
b10 = dict(b8=b8, b9=b9)
py_offline.plot(b10, b11 = 'tweet_sentiment_analysis.html')