
import plotly.graph_objs as go
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
app = dash.Dash()
def get_stock_data():
    symbol = input('Enter the stock symbol: \n')
    datatype = 'datatype=csv'
    API_KEY = 'VW506K51LFXGUT1C'
    API_QUERY = f'https:
    print(f'API Query: {API_QUERY}')
    df = pd.read_csv(API_QUERY)
    return df
def create_stock_price_graph(df):
    graph = dcc.Graph(
        id='linegraph',
        figure={
            'data': [
                go.Scatter(
                    x=df['timestamp'],
                    y=df['close'],
                    mode='lines',
                    marker={'size': 12}
                )
            ],
            'layout': go.Layout(
                title='Stock Prices Over Time'
            )
        }
    )
    return graph
app.layout = html.Div([
    create_stock_price_graph(get_stock_data())
])
if __name__ == '__main__':
    app.run_server()