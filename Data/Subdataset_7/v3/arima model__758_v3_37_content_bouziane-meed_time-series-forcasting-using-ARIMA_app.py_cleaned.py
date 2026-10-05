import dash
from dash import dcc, html, Input, Output, State
import pandas as pd
import plotly.graph_objects as go
import statsmodels.api as sm
from statsmodels.tsa.statespace.sarimax import SARIMAX
import itertools
from datetime import datetime
import numpy as np
b1 = dash.Dash(b20)
b2 = pd.read_excel("data/data.xlsx")
b3 = ['https:
b1.css.append_css({'external_url': b3})
b1.b4 = html.Div(b7={'backgroundColor': '
    html.Div([
        html.Img(b5 = b1.get_asset_url('distr.png'), b7={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
        html.Div(b6 = [
            html.H1('Predictive Analytics Dashboards', b7 = {'textAlign': 'center', 'color': '
            html.Div('Distra web application for sales data visualization and time series forecasting', b7 = {'textAlign': 'center', 'color': '
        ], b7 = {'width': '33%', 'display': 'inline-block'}),
    ]),
    html.Div([
        html.H5('Enter a product name:'),
        html.Div([
            dcc.Input(b8 = 'input-box', type='text', b10='Article_32', b7={'float': 'left'}),
            html.Button('Submit', b8 = 'button', n_clicks=0)
        ]),
        html.H5('Select a distribution channel:'),
        dcc.Dropdown(
            b8 = 'canal-b8',
            b9 = [
                {'label': 'Detail', 'b10': 'Detail'},
                {'label': 'Distributor', 'b10': 'Distributor'},
                {'label': 'Wholesaler', 'b10': 'Wholesaler'},
                {'label': '1/2 Wholesaler', 'b10': 'HalfWholesaler'},
                {'label': 'LMS', 'b10': 'LMS'}
            ],
            b10 = 'Detail'
        ),
    ], b7 = {'width': '27%', 'float': 'right'}),
    html.Div([
        dcc.Graph(b8 = 'graph-1'),
        dcc.Graph(b8 = 'graph-2'),
        dcc.Graph(b8 = 'graph-3'),
        dcc.Graph(b8 = 'graph-4'),
        dcc.Slider(
            b8 = 'future-slider',
            b11 = 1,
            b12 = 7,
            b13 = 1,
            b10 = 5,
            b14 = {i: str(i) for i in range(1, 8)}
        )
    ])
])
@b1.callback(
    [Output('graph-1', 'figure'),
     Output('graph-2', 'figure'),
     Output('graph-3', 'figure'),
     Output('graph-4', 'figure')],
    [Input('button', 'n_clicks')],
    [State('input-box', 'b10'), State('canal-b8', 'b10'), State('future-slider', 'b10')]
)
def fonk1(n_clicks, art, cnl, stp):
    b15 = b2[(b2['code_article'] == art) & (b2['canal_principal'] == cnl)]
    b16 = go.Figure(data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])])
    b17 = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[3, 1, 6])])
    b18 = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[2, 3, 1])])
    b19 = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[5, 3, 4])])
    return b16, b17, b18, b19
if b20 = = '__main__':
    b1.run_server(b21 = True, host='127.0.0.1', port=8050)