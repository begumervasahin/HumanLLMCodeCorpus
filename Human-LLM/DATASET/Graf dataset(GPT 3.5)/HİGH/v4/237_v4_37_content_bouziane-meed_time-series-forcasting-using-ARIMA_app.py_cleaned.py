import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import statsmodels.api as sm
from dash.dependencies import Input, Output, State
import itertools
b1 = dash.Dash(b30)
b2 = ['https:
b1 = dash.Dash(b30, b2=b2)
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
                html.Div(b7 = [dcc.Input(b9='input-box', type='text', b11='Article_32')],
                         b8 = {'float': 'left'}),
                html.Div(b7 = [html.Button('Submit', b9='button')])
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
def fonk1(n_clicks, cnl, art):
    b16 = b3
    b16['Order Date'] = pd.to_datetime({'year': b16['Annee'], 'month': b16['Mois'],
                                                  'day': b16['Jour']})
    b16['date_YearMonth'] = b16['Order Date'].dt.strftime('%Y-%m-%d')
    b17 = b3.loc[(b3['code_article'] == art) & (b3['canal_principal'] == cnl)]
    b18 = b17.groupby(['date_YearMonth', 'code_article', 'canal_principal'])['CA_kMAD'].sum().reset_index()
    return {
        'data': [go.Scatter(b19 = b18['date_YearMonth'], b22=b18['CA_kMAD'])],
        'b5': {'title': 'Visualization of sales turnover per Month:',
                   'xaxis': {'title': 'Date'}, 'yaxis': {'title': 'Turnover'}}
    }
@b1.callback(
    Output('graph-2', 'figure'),
    [Input('button', 'n_clicks')],
    [State('canal-b9', 'b11'), State('input-box', 'b11')]
)
def fonk2(n_clicks, cnl, art):
    b3['Order Date'] = pd.to_datetime({'year': b3['Annee'], 'month': b3['Mois'], 'day': b3['Jour']})
    b17 = b3.loc[(b3['code_article'] == art) & (b3['canal_principal'] == cnl)]
    b20 = b17.groupby(['Order Date', 'code_article', 'canal_principal'])['CA_kMAD'].sum().reset_index()
    return {
        'data': [go.Scatter(b19 = b20['Order Date'], b22=b20['CA_kMAD'], mode='lines')],
        'b5': {'title': 'Visualization of sales turnover per Day:',
                   'xaxis': {'title': 'Date'}, 'yaxis': {'title': 'Turnover'}}
    }
@b1.callback(
    Output('graph-3', 'figure'),
    [Input('button', 'n_clicks')],
    [State('canal-b9', 'b11'), State('input-box', 'b11')]
)
def fonk3(n_clicks, cnl, art):
    b3['Order Date'] = pd.to_datetime({'year': b3['Annee'], 'month': b3['Mois'], 'day': b3['Jour']})
    b17 = b3.loc[(b3['code_article'] == art) & (b3['canal_principal'] == cnl)]
    b20 = b17.groupby(['Order Date', 'code_article', 'canal_principal'])['CA_kMAD'].sum().reset_index()
    b20 = b20.groupby('Order Date')['CA_kMAD'].sum().reset_index()
    b20.set_index('Order Date', b21 = True)
    b22 = b20['CA_kMAD'].resample('MS').sum()
    b23 = sm.tsa.seasonal_decompose(b22, model='additive')
    b24 = sm.tsa.statespace.SARIMAX(b22, order=(1, 1, 1), seasonal_order=(1, 0, 0, 12),
                                    b25 = True, enforce_invertibility=True)
    b26 = b24.fit()
    b27 = b26.get_prediction(start=pd.to_datetime('2019-01-01'), dynamic=True)
    b28 = b27.conf_int()
    return {
        'data': [go.Scatter(b19 = b22['2018':].index, b22=b22['2018':], name='Actual'),
                 go.Scatter(b19 = b27.predicted_mean.index, b22=b27.predicted_mean, name='Predicted')],
        'b5': {'title': 'Sales turnover prediction per Month:',
                   'xaxis': {'title': 'Date'}, 'yaxis': {'title': 'Turnover'}}
    }
@b1.callback(
    Output('graph-4', 'figure'),
    [Input('button', 'n_clicks'), Input('canal-b9', 'b11'), Input('future-slider', 'b11')],
    [State('input-box', 'b11')]
)
def fonk4(n_clicks, cnl, stp, art):
    b3['Order Date'] = pd.to_datetime({'year': b3['Annee'], 'month': b3['Mois'], 'day': b3['Jour']})
    b17 = b3.loc[(b3['code_article'] == art) & (b3['canal_principal'] == cnl)]
    b20 = b17.groupby(['Order Date', 'code_article', 'canal_principal'])['CA_kMAD'].sum().reset_index()
    b20 = b20.groupby('Order Date')['CA_kMAD'].sum().reset_index()
    b20.set_index('Order Date', b21 = True)
    b22 = b20['CA_kMAD'].resample('MS').sum()
    b24 = sm.tsa.statespace.SARIMAX(b22, order=(1, 1, 1), seasonal_order=(1, 0, 0, 12),
                                    b25 = True, enforce_invertibility=True)
    b26 = b24.fit()
    b29 = b26.get_forecast(steps=stp)
    b28 = b29.conf_int()
    return {
        'data': [go.Scatter(b19 = b22.index, b22=b22, name='Actual'),
                 go.Scatter(b19 = b29.predicted_mean.index, b22=b29.predicted_mean, name='Predicted')],
        'b5': {'title': 'Sales turnover future prediction per Month:',
                   'xaxis': {'title': 'Date'}, 'yaxis': {'title': 'Turnover'}}
    }
if b30 = = '__main__':
    b1.run_server(b31 = True, host='127.0.0.1', port=8050)