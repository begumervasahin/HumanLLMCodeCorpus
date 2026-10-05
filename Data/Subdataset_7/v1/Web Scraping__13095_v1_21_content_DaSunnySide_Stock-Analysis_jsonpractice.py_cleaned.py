import plotly.graph_objs as go
import pandas as pd
import plotly.offline as pyo
from pandas.io.json import json_normalize
import plotly.tools as tools
import dash
import dash_html_components as html
import dash_core_components as dcc
b1 = dash.Dash()
b2 = input('Stock Symbol: \n')
b3 = 'b3=csv'
b4 = 'VW506K51LFXGUT1C'
b5 = 'https:
print(b5)
b6 = pd.read_csv(b5)
b1.b7 = html.Div([
    dcc.Graph(b8 = 'linegraph',
              b9 = {
                  'data': [
                      go.Scatter(b10 = b6['timestamp'], y=b6['close'],
                                 b11 = 'lines', marker={'size': 12})],
                  'b7': go.Layout(b12 = 'Stock prices over time')
              })
])
if b13 = = '__main__':
    b1.run_server()