import plotly.graph_objs as go
import pandas as pd
import dash
from dash import html, dcc, Input, Output
app = dash.Dash()
API_KEY = 'VW506K51LFXGUT1C'
API_BASE_URL = 'https:
nsdq = pd.read_csv('nsdq.csv').set_index('Symbol')
nyse = pd.read_csv('nyse.csv').set_index('Symbol')
options = [{'label': f'{tic} {nsdq.loc[tic]["Name"]}', 'value': tic} for tic in nsdq.index]
options += [{'label': f'{tic} {nyse.loc[tic]["Name"]}', 'value': tic} for tic in nyse.index]
graph_options = [
    {'label': 'Time Series Intraday', 'value': 'TIME_SERIES_INTRADAY'},
    {'label': 'Time Series Daily', 'value': 'TIME_SERIES_DAILY'},
    {'label': 'Time Series Daily Adjusted', 'value': 'TIME_SERIES_DAILY_ADJUSTED'},
    {'label': 'Time Series Weekly', 'value': 'TIME_SERIES_WEEKLY'},
    {'label': 'Time Series Weekly Adjusted', 'value': 'TIME_SERIES_WEEKLY_ADJUSTED'},
    {'label': 'Time Series Monthly', 'value': 'TIME_SERIES_MONTHLY'},
    {'label': 'Time Series Monthly Adjusted', 'value': 'TIME_SERIES_MONTHLY_ADJUSTED'}
]
app.layout = html.Div([
    html.Div([
        dcc.Dropdown(id='stock-symbol', options=options, value='MSFT', multi=True)
    ], style={'display': 'flex', 'verticalAlign': 'top', 'width': '30%'}),
    html.Div([
        dcc.Dropdown(id='graph-type', options=graph_options, value='TIME_SERIES_DAILY')
    ], style={'display': 'flex', 'verticalAlign': 'top', 'width': '30%'}),
    html.Div([
        html.Button(id='submit-button', children='Submit', n_clicks=0,
                    style={'fontSize': 24, 'marginLeft': '30px'})
    ], style={'display': 'flex', 'verticalAlign': 'top', 'width': '30%'}),
    html.Div([
        dcc.Graph(id='linegraph', figure={'data': [], 'layout': go.Layout(title='Stock prices over time')}),
    ]),
    html.Div([
        dcc.Graph(id='candlestick', figure={'data': [], 'layout': go.Layout(title='Candlestick Graph of prices over time')})
    ])
])
@app.callback(Output('linegraph', 'figure'),
              [Input('submit-button', 'n_clicks')],
              [State('stock-symbol', 'value'), State('graph-type', 'value')])
def update_line_graph(n_clicks, selected_stock_symbol, selected_graph_type):
    function = selected_graph_type
    symbol = selected_stock_symbol
    API_QUERY = f'{API_BASE_URL}function={function}&symbol={symbol}&apikey={API_KEY}&datatype=csv'
    df = pd.read_csv(API_QUERY)
    return {'data': [go.Scatter(x=df['timestamp'], y=df['close'], mode='lines')],
            'layout': go.Layout(title='Stock prices over time')}
if __name__ == '__main__':
    app.run_server()