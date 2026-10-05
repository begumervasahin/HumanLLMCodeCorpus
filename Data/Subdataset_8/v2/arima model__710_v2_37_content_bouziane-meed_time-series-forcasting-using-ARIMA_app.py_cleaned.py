import dash
from dash import dcc, html, Input, Output, State
import pandas as pd
import plotly.graph_objects as go
import statsmodels.api as sm
from statsmodels.tsa.statespace.sarimax import SARIMAX
import itertools
from datetime import datetime
import numpy as np
external_stylesheets = ['https:
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
df = pd.read_excel("data/data.xlsx")
app.layout = html.Div(style={'backgroundColor': '
    html.Div([
        html.Img(src=app.get_asset_url('distr.png'), style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
        html.Div(children=[
            html.H1(children='Predictive Analytics Dashboards', style={'textAlign': 'center', 'color': '
            html.Div(children='Distra web application for sales data visualization and time series forecasting', style={'textAlign': 'center', 'color': '
        ], style={'width': '33%', 'display': 'inline-block'}),
    ]),
    html.Div(children=[
        html.H5(children='Enter a product name:'),
        html.Div(children=[
            html.Div(children=[dcc.Input(id='input-box', type='text', value='Article_32')], style={'float': 'left'}),
            html.Button('Submit', id='button', n_clicks=0)
        ]),
        html.H5(children='Select a distribution channel:'),
        dcc.Dropdown(
            id='canal-id',
            options=[
                {'label': 'Detail', 'value': 'Detail'},
                {'label': 'Distributor', 'value': 'Distributor'},
                {'label': 'Wholesaler', 'value': 'Wholesaler'},
                {'label': '1/2 Wholesaler', 'value': 'HalfWholesaler'},
                {'label': 'LMS', 'value': 'LMS'}
            ],
            value='Detail'
        ),
    ], style={'width': '27%', 'float': 'right'}),
    html.Div([
        dcc.Graph(id='graph-1'),
        dcc.Graph(id='graph-2'),
        dcc.Graph(id='graph-3'),
        dcc.Graph(id='graph-4'),
        dcc.Slider(
            id='future-slider',
            min=1,
            max=7,
            step=1,
            value=5,
            marks={i: str(i) for i in range(1, 8)}
        )
    ])
])
@app.callback(
    [Output('graph-1', 'figure'),
     Output('graph-2', 'figure'),
     Output('graph-3', 'figure'),
     Output('graph-4', 'figure')],
    [Input('button', 'n_clicks')],
    [State('input-box', 'value'), State('canal-id', 'value'), State('future-slider', 'value')]
)
def update_output(n_clicks, art, cnl, stp):
    filtered_df = df[(df['code_article'] == art) & (df['canal_principal'] == cnl)]
    fig1 = go.Figure(data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])])
    fig2 = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[3, 1, 6])])
    fig3 = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[2, 3, 1])])
    fig4 = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[5, 3, 4])])
    return fig1, fig2, fig3, fig4
if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1', port=8050)