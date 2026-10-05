import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import statsmodels.api as sm
from dash.dependencies import Input, Output, State
b1 = dash.Dash(b29)
b2 = ['https:
b1 = dash.Dash(b29, b2=b2)
b3 = pd.read_excel("data/data.xlsx")
b4 = {'background': '
b1.b5 = html.Div(b8={'backgroundColor': b4['background']}, b7=[
    html.Div([
        html.Img(b6 = b1.get_asset_url('distr.png'), b8={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
        html.Div(b7 = [
            html.H1(b7 = 'Predictive analytics dashboards', b8={'textAlign': 'center', 'color': '
            html.Div(b7 = 'Distra web application for sales data visualization and time series forecasting',
                     b8 = {'textAlign': 'center', 'color': '
        ], b8 = {'width': '33%', 'display': 'inline-block'}),
        html.Div(b7 = [
            html.H5(b7 = 'Enter a product name:'),
            html.Div(b7 = [
                dcc.Input(b9 = 'input-box', type='text', b11='Article_32', b8={'float': 'left'}),
                html.Button('Submit', b9 = 'button')
            ]),
            html.H5(b7 = 'Select a distribution channel:'),
            dcc.Dropdown(
                b9 = 'canal-b9',
                b10 = [
                    {'label': 'Detail', 'b11': 'Détail'},
                    {'label': 'Distributor', 'b11': 'Distributeur'},
                    {'label': 'Wholesaler', 'b11': 'Grossiste'},
                    {'label': '1/2 Wholesaler', 'b11': '1/2 Gros'},
                    {'label': 'LMS', 'b11': 'GMS'}
                ],
                b11 = 'Détail', b8={'width': '91%'}
            ),
        ], b8 = {'width': '27%', 'float': 'right'})
    ]),
    html.Div([
        html.Div([
            dcc.Graph(b9 = 'graph-1'),
            dcc.Graph(b9 = 'graph-2'),
        ], b8 = {'width': '50%', 'float': 'left'}),
        html.Div([
            dcc.Graph(b9 = 'graph-3'),
            dcc.Graph(b9 = 'graph-4'),
            dcc.Slider(
                b9 = 'future-slider',
                b12 = 1,
                b13 = 7,
                b14 = 1,
                b15 = {i: str(i) for i in range(1, 8)},
                b11 = 5,
            )
        ], b8 = {'width': '48%', 'float': 'right'})
    ])
])
@b1.callback(
    Output('graph-1', 'figure'),
    [Input('button', 'n_clicks')],
    [State('canal-b9', 'b11'), State('input-box', 'b11')]
)
def fonk1(n_clicks, canal_id, input_box):
    b16 = b3.loc[(b3['code_article'] == input_box) & (b3['canal_principal'] == canal_id)]
    b17 = b16.groupby(['Order Date', 'code_article', 'canal_principal'])['CA_kMAD'].sum().reset_index()
    return {
        'data': [go.Scatter(b18 = b17['Order Date'], b21=b17['CA_kMAD'])],
        'b5': {'title': 'Visualization of sales turnover per Month:',
                   'xaxis': {'title': 'Date'}, 'yaxis': {'title': 'Turnover'}}
    }
@b1.callback(
    Output('graph-2', 'figure'),
    [Input('button', 'n_clicks')],
    [State('canal-b9', 'b11'), State('input-box', 'b11')]
)
def fonk2(n_clicks, canal_id, input_box):
    b16 = b3.loc[(b3['code_article'] == input_box) & (b3['canal_principal'] == canal_id)]
    b19 = b16.groupby(['Order Date', 'code_article', 'canal_principal'])['CA_kMAD'].sum().reset_index()
    return {
        'data': [go.Scatter(b18 = b19['Order Date'], b21=b19['CA_kMAD'], mode='lines')],
        'b5': {'title': 'Visualization of sales turnover per Day:',
                   'xaxis': {'title': 'Date'}, 'yaxis': {'title': 'Turnover'}}
    }
@b1.callback(
    Output('graph-3', 'figure'),
    [Input('button', 'n_clicks')],
    [State('canal-b9', 'b11'), State('input-box', 'b11')]
)
def fonk3(n_clicks, canal_id, input_box):
    b16 = b3.loc[(b3['code_article'] == input_box) & (b3['canal_principal'] == canal_id)]
    b19 = b16.groupby(['Order Date', 'code_article', 'canal_principal'])['CA_kMAD'].sum().reset_index()
    b19 = b19.groupby('Order Date')['CA_kMAD'].sum().reset_index()
    b19.set_index('Order Date', b20 = True)
    b21 = b19['CA_kMAD'].resample('MS').sum()
    b22 = sm.tsa.seasonal_decompose(b21, model='additive')
    b23 = sm.tsa.statespace.SARIMAX(b21, order=(1, 1, 1), seasonal_order=(1, 0, 0, 12),
                                    b24 = True, enforce_invertibility=True)
    b25 = b23.fit()
    b26 = b25.get_prediction(start=pd.to_datetime('2019-01-01'), dynamic=True)
    b27 = b26.conf_int()
    return {
        'data': [go.Scatter(b18 = b21['2018':].index, b21=b21['2018':], name='Actual'),
                 go.Scatter(b18 = b26.predicted_mean.index, b21=b26.predicted_mean, name='Predicted')],
        'b5': {'title': 'Sales turnover prediction per Month:',
                   'xaxis': {'title': 'Date'}, 'yaxis': {'title': 'Turnover'}}
    }
@b1.callback(
    Output('graph-4', 'figure'),
    [Input('button', 'n_clicks'), Input('canal-b9', 'b11'), Input('future-slider', 'b11')],
    [State('input-box', 'b11')]
)
def fonk4(n_clicks, canal_id, future_slider, input_box):
    b16 = b3.loc[(b3['code_article'] == input_box) & (b3['canal_principal'] == canal_id)]
    b19 = b16.groupby(['Order Date', 'code_article', 'canal_principal'])['CA_kMAD'].sum().reset_index()
    b19 = b19.groupby('Order Date')['CA_kMAD'].sum().reset_index()
    b19.set_index('Order Date', b20 = True)
    b21 = b19['CA_kMAD'].resample('MS').sum()
    b23 = sm.tsa.statespace.SARIMAX(b21, order=(1, 1, 1), seasonal_order=(1, 0, 0, 12),
                                    b24 = True, enforce_invertibility=True)
    b25 = b23.fit()
    b28 = b25.get_forecast(steps=future_slider)
    b27 = b28.conf_int()
    return {
        'data': [go.Scatter(b18 = b21.index, b21=b21, name='Actual'),
                 go.Scatter(b18 = b28.predicted_mean.index, b21=b28.predicted_mean, name='Predicted')],
        'b5': {'title': 'Sales turnover future prediction per Month:',
                   'xaxis': {'title': 'Date'}, 'yaxis': {'title': 'Turnover'}}
    }
if b29 = = '__main__':
    b1.run_server(b30 = True, host='127.0.0.1', port=8050)