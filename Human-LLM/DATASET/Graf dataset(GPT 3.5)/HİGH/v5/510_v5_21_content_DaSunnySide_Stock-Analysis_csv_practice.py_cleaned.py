import plotly.graph_objs as go
import pandas as pd
import dash
from dash import html, dcc, Input, Output
b1 = dash.Dash()
b2 = 'VW506K51LFXGUT1C'
b3 = 'https:
b4 = pd.read_csv('b4.csv').set_index('Symbol')
b5 = pd.read_csv('b5.csv').set_index('Symbol')
b6 = [{'label': f'{tic} {b4.loc[tic]["Name"]}', 'value': tic} for tic in b4.index]
b6 += [{'label': f'{tic} {b5.loc[tic]["Name"]}', 'value': tic} for tic in b5.index]
b7 = [
    {'label': 'Time Series Intraday', 'value': 'TIME_SERIES_INTRADAY'},
    {'label': 'Time Series Daily', 'value': 'TIME_SERIES_DAILY'},
    {'label': 'Time Series Daily Adjusted', 'value': 'TIME_SERIES_DAILY_ADJUSTED'},
    {'label': 'Time Series Weekly', 'value': 'TIME_SERIES_WEEKLY'},
    {'label': 'Time Series Weekly Adjusted', 'value': 'TIME_SERIES_WEEKLY_ADJUSTED'},
    {'label': 'Time Series Monthly', 'value': 'TIME_SERIES_MONTHLY'},
    {'label': 'Time Series Monthly Adjusted', 'value': 'TIME_SERIES_MONTHLY_ADJUSTED'}
]
b1.b8 = html.Div([
    html.Div([
        dcc.Dropdown(b9 = 'stock-b12', b6=b6, value='MSFT', multi=True)
    ], b10 = {'display': 'flex', 'verticalAlign': 'top', 'width': '30%'}),
    html.Div([
        dcc.Dropdown(b9 = 'graph-type', b6=b7, value='TIME_SERIES_DAILY')
    ], b10 = {'display': 'flex', 'verticalAlign': 'top', 'width': '30%'}),
    html.Div([
        html.Button(b9 = 'submit-button', children='Submit', n_clicks=0,
                    b10 = {'fontSize': 24, 'marginLeft': '30px'})
    ], b10 = {'display': 'flex', 'verticalAlign': 'top', 'width': '30%'}),
    html.Div([
        dcc.Graph(b9 = 'linegraph', figure={'data': [], 'b8': go.Layout(b16='Stock prices over time')}),
    ]),
    html.Div([
        dcc.Graph(b9 = 'candlestick', figure={'data': [], 'b8': go.Layout(b16='Candlestick Graph of prices over time')})
    ])
])
@b1.callback(Output('linegraph', 'figure'),
              [Input('submit-button', 'n_clicks')],
              [State('stock-b12', 'value'), State('graph-type', 'value')])
def fonk1(n_clicks, selected_stock_symbol, selected_graph_type):
    b11 = selected_graph_type
    b12 = selected_stock_symbol
    b13 = f'{b3}b11={b11}&b12={b12}&apikey={b2}&datatype=csv'
    b14 = pd.read_csv(b13)
    return {'data': [go.Scatter(b15 = b14['timestamp'], y=b14['close'], mode='lines')],
            'b8': go.Layout(b16 = 'Stock prices over time')}
if b17 = = '__main__':
    b1.run_server()