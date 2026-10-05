import plotly.graph_objs as go
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
b1 = dash.Dash()
b2 = {
    'dashbg': '',
    'graphbg': '',
    'increasingline': '',
    'decreasingline': '',
    'lowcontrasttext': '',
    'highcontrasttext': ''
}
b3 = 'VW506K51LFXGUT1C'
b4 = 'https:
b5 = pd.read_csv('b5.csv')
b6 = pd.read_csv('b6.csv')
b5.set_index('Symbol', b7 = True)
b6.set_index('Symbol', b7 = True)
b8 = []
for tic in b5.index:
    b8.append({'label': '{} {}'.format(tic, b5.loc[tic]['Name']), 'b12': tic})
for tic in b6.index:
    b8.append({'label': '{} {}'.format(tic, b6.loc[tic]['Name']), 'b12': tic})
b9 = [
    {'label': 'Time Series Intraday', 'b12': 'TIME_SERIES_INTRADAY'},
    {'label': 'Time Series Daily', 'b12': 'TIME_SERIES_DAILY'},
    {'label': 'Time Series Daily Adjusted', 'b12': 'TIME_SERIES_DAILY_ADJUSTED'},
    {'label': 'Time Series Weekly', 'b12': 'TIME_SERIES_WEEKLY'},
    {'label': 'Time Series Weekly Adjusted', 'b12': 'TIME_SERIES_WEEKLY_ADJUSTED'},
    {'label': 'Time Series Monthly', 'b12': 'TIME_SERIES_MONTHLY'},
    {'label': 'Time Series Monthly Adjusted', 'b12': 'TIME_SERIES_MONTHLY_ADJUSTED'}
]
b1.b10 = html.Div([
    html.Div([
        dcc.Dropdown(
            b11 = 'stock-b18',
            b8 = b8,
            b12 = 'MSFT',
            b13 = True
        )
    ], b14 = {'display': 'flex', 'verticalAlign': 'top', 'width': '30%'}),
    html.Div([
        dcc.Dropdown(
            b11 = 'graph-type',
            b8 = b9,
            b12 = 'TIME_SERIES_DAILY'
        )
    ], b14 = {'display': 'flex', 'verticalAlign': 'top', 'width': '30%'}),
    html.Div([
        html.Button(
            b11 = 'submit-button',
            b15 = 'Submit',
            b16 = 0,
            b14 = {'fontSize': 24, 'marginLeft': '30px'}
        )
    ], b14 = {'display': 'flex', 'verticalAlign': 'top', 'width': '30%'}),
    html.Div([
        dcc.Graph(b11 = 'linegraph', figure={'data': [], 'b10': go.Layout(b22='Stock prices over time')}),
    ]),
    html.Div([
        dcc.Graph(b11 = 'candlestick', figure={'data': [], 'b10': go.Layout(b22='Candlestick Graph of prices over time')})
    ])
])
@b1.callback(Output('linegraph', 'figure'),
              [Input('submit-button', 'b16')],
              [State('stock-b18', 'b12'),
               State('graph-type', 'b12')])
def fonk1(b16, selected_stock_symbol, selected_graph_type):
    b17 = selected_graph_type
    b18 = selected_stock_symbol
    b19 = f'{b4}b17={b17}&b18={b18}&apikey={b3}&datatype=csv'
    b20 = pd.read_csv(b19)
    return {'data': [go.Scatter(b21 = b20['timestamp'], y=b20['close'], mode='lines')],
            'b10': go.Layout(b22 = 'Stock prices over time')}
if b23 = = '__main__':
    b1.run_server()