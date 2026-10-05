import plotly.graph_objs as go
import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
app = dash.Dash(__name__)
colors = {
    'background': '
    'text': '
}
def load_stock_data():
    nsdq = pd.read_csv('nsdq.csv').set_index('Symbol')
    nyse = pd.read_csv('nyse.csv').set_index('Symbol')
    return nsdq, nyse
def generate_dropdown_options(nsdq, nyse):
    options = [{'label': f"{index} {row['Name']}", 'value': index} for index, row in nsdq.iterrows()]
    options += [{'label': f"{index} {row['Name']}", 'value': index} for index, row in nyse.iterrows()]
    return options
nsdq_data, nyse_data = load_stock_data()
stock_options = generate_dropdown_options(nsdq_data, nyse_data)
graph_options = [
    {'label': 'Daily', 'value': 'TIME_SERIES_DAILY'},
    {'label': 'Weekly', 'value': 'TIME_SERIES_WEEKLY'},
]
app.layout = html.Div([
    dcc.Dropdown(
        id='stock-symbol',
        options=stock_options,
        value='MSFT',
        multi=True,
        style={'width': '48%', 'display': 'inline-block'}
    ),
    dcc.Dropdown(
        id='graph-type',
        options=graph_options,
        value='TIME_SERIES_DAILY',
        style={'width': '48%', 'display': 'inline-block', 'marginLeft': '4%'}
    ),
    html.Button('Submit', id='submit-button', n_clicks=0, style={'marginTop': '20px'}),
    html.Div(id='graphs')
])
@app.callback(
    Output('graphs', 'children'),
    Input('submit-button', 'n_clicks'),
    State('stock-symbol', 'value'),
    State('graph-type', 'value')
)
def update_graphs(n_clicks, selected_symbols, graph_type):
    if n_clicks > 0:
        return [generate_graph(symbol, graph_type) for symbol in selected_symbols]
    return []
def generate_graph(symbol, graph_type):
    API_KEY = 'YOUR_API_KEY_HERE'
    API_URL = f"https:
    df = pd.read_csv(API_URL)
    if not df.empty:
        figure = go.Figure()
        figure.add_trace(go.Scatter(x=df['timestamp'], y=df['close'], mode='lines', name='close'))
        figure.update_layout(title=f"{symbol} Stock Prices", xaxis_title="Time", yaxis_title="Price")
        return dcc.Graph(figure=figure)
    else:
        return html.Div([f"No data available for {symbol}."])
if __name__ == '__main__':
    app.run_server(debug=True)