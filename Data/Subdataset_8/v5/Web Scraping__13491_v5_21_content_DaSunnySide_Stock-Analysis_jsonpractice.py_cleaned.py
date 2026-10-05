import plotly.graph_objs as go
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
app = dash.Dash()
symbol = input('Enter Stock Symbol: \n')
datatype = 'datatype=csv'
API_KEY = 'VW506K51LFXGUT1C'
API_QUERY = f'https:
print(f"API Query URL: {API_QUERY}")
df = pd.read_csv(API_QUERY)
app.layout = html.Div([
    dcc.Graph(
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
            'layout': go.Layout(title='Stock Prices Over Time')
        }
    )
])
if __name__ == '__main__':
    app.run_server()