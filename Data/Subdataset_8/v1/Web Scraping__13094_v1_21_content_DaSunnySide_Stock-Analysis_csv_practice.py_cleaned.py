import plotly.graph_objs as go
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
app = dash.Dash(__name__)
colors = {
    'dashbg': '
    'graphbg': '
    'increasingline': '
    'decreasingline': '
    'lowcontrasttext': '
    'highcontrasttext': '
}
nsdq = pd.read_csv('nsdq.csv')
nyse = pd.read_csv('nyse.csv')
nsdq.set_index('Symbol', inplace=True)
nyse.set_index('Symbol', inplace=True)
options = [{'label': f"{tic} {nsdq.loc[tic]['Name']}", 'value': tic} for tic in nsdq.index]
options += [{'label': f"{tic} {nyse.loc[tic]['Name']}", 'value': tic} for tic in nyse.index]
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
        dcc.Dropdown(
            id='stock-symbol',
            options=options,
            value='MSFT',
            multi=True
        )
    ], style={'display': 'inline-block', 'width': '30%'}),
    html.Div([
        dcc.Dropdown(
            id='graph-type',
            options=graph_options,
            value='TIME_SERIES_DAILY'
        )
    ], style={'display': 'inline-block', 'width': '30%'}),
    html.Div([
        html.Button(
            id='submit-button',
            children='Submit',
            n_clicks=0,
            style={'fontSize': 24}
        )
    ], style={'display': 'inline-block', 'marginLeft': '30px'}),
    html.Div(id='graphs')
])
@app.callback(
    Output('graphs', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('stock-symbol', 'value'),
     State('graph-type', 'value')]
)
def update_graphs(n_clicks, selected_stock_symbols, selected_graph_type):
    if n_clicks == 0:
        return []
    API_KEY = 'VW506K51LFXGUT1C'
    datatype = 'datatype=csv'
    graphs = []
    for symbol in selected_stock_symbols:
        function = selected_graph_type
        API_QUERY = f'https:
        df = pd.read_csv(API_QUERY)
        line_graph = dcc.Graph(
            figure={
                'data': [go.Scatter(x=df['timestamp'], y=df['close'], mode='lines')],
                'layout': go.Layout(title=f'Stock prices over time for {symbol}')
            }
        )
        candlestick_graph = dcc.Graph(
            figure={
                'data': [go.Candlestick(x=df['timestamp'],
                                         open=df['open'],
                                         high=df['high'],
                                         low=df['low'],
                                         close=df['close'])],
                'layout': go.Layout(title=f'Candlestick Graph of prices over time for {symbol}')
            }
        )
        graphs.append(html.Div([line_graph, candlestick_graph]))
    return graphs
if __name__ == '__main__':
    app.run_server(debug=True)