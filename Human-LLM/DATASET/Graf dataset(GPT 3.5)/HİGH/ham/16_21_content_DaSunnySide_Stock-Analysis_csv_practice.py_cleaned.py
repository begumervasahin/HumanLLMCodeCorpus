import plotly.graph_objs as go
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
from pandas.io.json import json_normalize
import plotly.tools as tools
import dash
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
b1 = dash.Dash()
b2 = {
    'dashbg' : '
    'graphbg' : '
    'increasingline' : '
    'decreasingline' : '
    'lowcontrasttext' : '
    'highcontrasttext' : '
}
b3 = 'b3'
b4 = 'b4'
b5 = 'b5'
b6 = 'b6'
b7 = 'b7'
b8 = 'b8'
b9 = 'b9'
b10 = pd.read_csv('b10.csv')
b11 = pd.read_csv('b11.csv')
b10.set_index('Symbol', b12 = True)
b11.set_index('Symbol', b12 = True)
b13 = []
for tic in b10.index:
    b13.append({'label':'{} {}'.format(tic, b10.loc[tic]['Name']), 'b24':tic})
for tic in b11.index:
    b13.append({'label': '{} {}'.format(tic, b11.loc[tic]['Name']), 'b24':tic})
b14 = input('Stock Symbol: \n')
b15 = 'b15=csv'
b16 = input("Function: \n")
if b16 = = 'b3' :
    b17 = input('Time b17 in minutes: \n')
    b14 = b14 + '&b17=' + b17 + 'min'
b18 = 'VW506K51LFXGUT1C'
b19 = 'https:
if b16 = = 'b3' :
    b20 = pd.read_csv(b19)
else:
    b20 = pd.read_csv(b19)
b21 = [
            {'label': 'Time Series Intraday', 'b24' : 'b3'},
            {'label': 'Time Series Daily', 'b24' : 'b4'},
            {'label': 'Time Series Daily Adjusted', 'b24' : 'b5'},
            {'label': 'Time Series Weekly', 'b24' : 'b6'},
            {'label': 'Time Series Weekly Adjusted', 'b24' : 'b7'},
            {'label': 'Time Series Monthly', 'b24' : 'b8'},
            {'label': 'Time Series Monthly Adjusted', 'b24' : 'b9'}
        ]
b1.b22 = html.Div(([
    html.Div([
        dcc.Dropdown(
        b23 = 'stock-b14',
        b13 = b13,
        b24 = 'MSFT',
        b25 = True)
        ], b26 = {'display': 'flex', 'verticalAlign':'top', 'width':'30%'}),
    html.Div([
        dcc.Dropdown(
            b23 = 'graph-type',
            b13 = b21,
            b24 = 'b4'
    )
    ], b26 = {'display': 'flex', 'verticalAlign':'top', 'width':'30%'}),
    html.Div([
        html.Button(
            b23 = 'submit-button',
            b27 = 'Submit',
            b28 = 0,
            b26 = {'fontSize':24, 'marginLeft':'30px'}
        )
    ], b26 = {'display': 'flex', 'verticalAlign': 'top', 'width': '30%'}),
    html.Div([
        dcc.Graph(b23 = 'linegraph',
                  b29 = {
                      'data': [
                          go.Scatter(b30 = b20['timestamp'], y=b20['b36'],
                                     b31 = 'lines', marker={
                                  'size': 12,
                                  'color': '
                              })],
                      'b22': go.Layout(b32 = 'Stock prices over time')}),
    ]),
    html.Div([
        dcc.Graph(b23 = 'candlestick',
                      b29 = {
                          'data': [
                              go.Candlestick(b30 = b20['timestamp'],
                                             b33 = b20['b33'],
                                             b34 = b20['b34'],
                                             b35 = b20['b35'],
                                             b36 = b20['b36'],
                                             b37 = '
                                             b38 = '
                                             )
                          ],
                            'b22': go.Layout(b32 = 'Candlestick Graph of prices over time')
                      })
    ])
]
))
@b1.callback(Output('linegraph', 'b29'),
              [Input('submit-button', 'b28')],
              [State('stock-b14', 'b24'),
               State('graph-type', 'b24')])
def fonk1(b28, selected_graph_type, selected_stock_symbol):
    b16 = selected_graph_type
    b14 = selected_stock_symbol
    b19 = 'https:
    b39 = pd.read_csv(b19)
    return {'data': b39, 'b22': go.Layout(b32 = 'Stock prices over time')}
if b40 = = '__main__':
    b1.run_server()