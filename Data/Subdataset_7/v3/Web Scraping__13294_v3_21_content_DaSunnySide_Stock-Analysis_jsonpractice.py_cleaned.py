
import plotly.graph_objs as go
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
b1 = dash.Dash()
def fonk1():
    b2 = input('Enter the stock b2: \n')
    b3 = 'b3=csv'
    b4 = 'VW506K51LFXGUT1C'
    b5 = f'https:
    print(f'API Query: {b5}')
    b6 = pd.read_csv(b5)
    return b6
def fonk2(b6):
    b7 = dcc.Graph(
        b8 = 'linegraph',
        b9 = {
            'data': [
                go.Scatter(
                    b10 = b6['timestamp'],
                    b11 = b6['close'],
                    b12 = 'lines',
                    b13 = {'size': 12}
                )
            ],
            'b15': go.Layout(
                b14 = 'Stock Prices Over Time'
            )
        }
    )
    return b7
b1.b15 = html.Div([
    fonk2(fonk1())
])
if b16 = = '__main__':
    b1.run_server()