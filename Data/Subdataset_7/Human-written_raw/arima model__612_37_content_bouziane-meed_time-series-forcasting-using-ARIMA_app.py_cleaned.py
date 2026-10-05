import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.offline as py
import plotly.tools as tls
import plotly.graph_objects as go
import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from dash.dependencies import Input, Output, State
b1 = ['https:
b2 = dash.Dash(b40, b1=b1)
b3 = go.Figure()
b4 = pd.read_excel("data/data.xlsx")
b5 = {
    'background': '
    'text': '
}
b2.b6 = html.Div(b9={'backgroundColor': b5['background']}, b8=[
    html.Div([ html.Img(b7 = b2.get_asset_url('distr.png'), b9={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
    html.Div(b8 = [
    html.H1(
        b8 = 'Predictive analytics dashboards',
        b9 = {
            'textAlign': 'center',
            'color': '
        }
    ),
    html.Div(b8 = 'Distra web application for sales data visualization and time series forecasting', b9={
        'textAlign': 'center',
        'color': '
    })
    ], b9 = {'width': '33%', 'display': 'inline-block', 'background': '
    html.Div(b8 = [
    html.H5(b8 = 'Enter a product b35 :'),
    html.Div(b8 = [html.Div(b8=[dcc.Input(b10='input-box', type='text', b12= 'Article_32')], b9={'float': 'left'}),
    html.Div(b8 = [html.Button('Submit', b10='button')])]),
    html.H5(b8 = 'Select a distribution channel :'),
    dcc.Dropdown(
            b10 = 'canal-b10',
            b11 = [
            {'label': 'Detail', 'b12': 'DÃ©tail'},
            {'label': 'Distributor', 'b12': 'Distributeur'},
            {'label': 'Wholesaler', 'b12': 'Grossiste'},
            {'label': '1/2 Wholesaler', 'b12': '1/2 Gros'},
            {'label': 'LMS', 'b12': 'GMS'}
            ],
            b12 = 'DÃ©tail', b9={'width': '91%'}
        ),
        ], b9 = {'width': '27%', 'float': 'right'}
        )
        ]),
        html.Div(b8 = [
        html.H3(b8 = ' .')
        ], b9 = {'background': '
    html.Div([
    html.Div([
    dcc.Graph(b10 = 'graph-1'),
    dcc.Graph(b10 = 'graph-2'),
    ], b9 = {'width': '50%', 'float': 'left'}),
    html.Div([
    dcc.Graph(b10 = 'graph-3'),
    dcc.Graph(b10 = 'graph-4'),
    dcc.Slider(
        b10 = 'future-slider',
        b13 = 1,
        b14 = 7,
        b15 = 1,
        b16 = {
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7'
    },
        b12 = 5,
    )
    ], b9 = {'width': '48%', 'float': 'right'})
    ])
])
@b2.callback(
    Output('graph-1', 'figure'),
    [Input('button', 'n_clicks'),Input('canal-b10', 'b12')], [State('input-box', 'b12')])
def fonk1(n_clicks,cnl,art):
    b17 = b4
    b17['Order Date'] = pd.to_datetime({'year':b17['Annee'],'month':b17['Mois'],'day':b17['Jour']})
    b17['date_YearMonth'] = b17['Order Date'].dt.year.astype('str') + '-' + b17['Order Date'].dt.month.astype('str') + '-01'
    b17['date_YearMonth'] = pd.to_datetime(b17['date_YearMonth'])
    b18 = b4.loc[b4['code_article'] == art]
    b18 = b18.loc[b4['canal_principal'] == cnl]
    b19 = b18.groupby(['date_YearMonth','code_article', 'canal_principal'])['CA_kMAD'].sum().reset_index()
    return {
        'data': [
                     go.Scatter(
            b20 = b19['date_YearMonth'],
            b21 = b19['CA_kMAD'],
         )
         ],
        'b6': {
            'title': 'Visualization of sales turnover per Month :',
            'xaxis' : {'title': 'Date'},
            'yaxis' : {'title': 'Turnover'}
        }
    }
@b2.callback(
    Output('graph-2', 'figure'),
    [Input('button', 'n_clicks'),Input('canal-b10', 'b12')], [State('input-box', 'b12')])
def fonk2(n_clicks,cnl,art):
    b4['Order Date'] = pd.to_datetime({'year':b4['Annee'],'month':b4['Mois'],'day':b4['Jour']})
    b18 = b4.loc[b4['code_article'] == art]
    b18 = b18.loc[b4['canal_principal'] == cnl]
    b22 = b18.groupby(['Order Date','code_article', 'canal_principal'])['CA_kMAD'].sum().reset_index()
    return {
        'data': [
            {'b20': b22['Order Date'], 'b21': b22['CA_kMAD'], 'type': 'category'},
        ],
        'b6': {
            'title': 'Visualization of sales turnover per Day :',
                'xaxis' : {'title': 'Date'},
            'yaxis' : {'title': 'Turnover'}
        }
    }
@b2.callback(
    Output('graph-3', 'figure'),
   [Input('button', 'n_clicks'),Input('canal-b10', 'b12')], [State('input-box', 'b12')])
def fonk3(n_clicks,cnl,art):
    b4['Order Date'] = pd.to_datetime({'year':b4['Annee'],'month':b4['Mois'],'day':b4['Jour']})
    b18 = b4.loc[b4['code_article'] == art]
    b18 = b18.loc[b4['canal_principal'] == cnl]
    b22 = b18.groupby(['Order Date','code_article', 'canal_principal'])['CA_kMAD'].sum().reset_index()
    b22 = b22.groupby('Order Date')['CA_kMAD'].sum().reset_index()
    b22 = b22.set_index('Order Date')
    b22.index
    b21 = b22['CA_kMAD'].resample('MS').sum()
    from pylab import rcParams
    rcParams['figure.figsize'] = 5, 5
    b23 = sm.tsa.seasonal_decompose(b21, model='additive')
    b24 = d = q = range(0, 2)
    b25 = list(itertools.product(b24, d, q))
    b26 = [(b20[0], b20[1], b20[2], 12) for b20 in list(itertools.product(b24, d, q))]
    for param in b25:
        for param_seasonal in b26:
            try:
                b27 = sm.tsa.statespace.SARIMAX(b21,
                                                b28 = param,
                                                b29 = param_seasonal,
                                                b30 = False,
                                                b31 = True)
                b32 = b27.fit()
            except:
                continue
    b27 = sm.tsa.statespace.SARIMAX(b21,
                                b28 = (1, 1, 1),
                                b29 = (1, 0, 0, 12),
                                b30 = True,
                                b31 = True)
    b32 = b27.fit()
    b32.summary().tables[1]
    b33 = b32.get_prediction(start=pd.to_datetime('2019-01-01'), dynamic=True)
    b34 = b33.conf_int()
    return {
        'data': [go.Scatter(
            b20 = b21['2018':].index,
            b21 = b21['2018':],
            b35 = 'Actual'
        ),
        go.Scatter(
            b20 = b33.predicted_mean.index,
            b21 = b33.predicted_mean,
            b35 = 'Predicted'
        )],
        'b6': {
                'title': 'Sales turnover prediction per Month :',
                'xaxis' : {'title': 'Date'},
            'yaxis' : {'title': 'Turnover'}
            }
        }
@b2.callback(
    Output('graph-4', 'figure'),
   [Input('button', 'n_clicks'),Input('canal-b10', 'b12'),Input('future-slider', 'b12')], [State('input-box', 'b12')])
def fonk4(n_clicks,cnl,stp,art):
    b4['Order Date'] = pd.to_datetime({'year':b4['Annee'],'month':b4['Mois'],'day':b4['Jour']})
    b18 = b4.loc[b4['code_article'] == art]
    b18 = b18.loc[b4['canal_principal'] == cnl]
    b22 = b18.groupby(['Order Date','code_article', 'canal_principal'])['CA_kMAD'].sum().reset_index()
    b22 = b22.groupby('Order Date')['CA_kMAD'].sum().reset_index()
    b22 = b22.set_index('Order Date')
    b22.index
    b21 = b22['CA_kMAD'].resample('MS').sum()
    from pylab import rcParams
    rcParams['figure.figsize'] = 5, 5
    b23 = sm.tsa.seasonal_decompose(b21, model='additive')
    b24 = d = q = range(0, 2)
    b25 = list(itertools.product(b24, d, q))
    b26 = [(b20[0], b20[1], b20[2], 12) for b20 in list(itertools.product(b24, d, q))]
    for param in b25:
        for param_seasonal in b26:
            try:
                b27 = sm.tsa.statespace.SARIMAX(b21,
                                                b28 = param,
                                                b29 = param_seasonal,
                                                b30 = False,
                                                b31 = True)
                b32 = b27.fit()
            except:
                continue
    b27 = sm.tsa.statespace.SARIMAX(b21,
                                b28 = (1, 1, 1),
                                b29 = (1, 0, 0, 12),
                                b30 = True,
                                b31 = True)
    b32 = b27.fit()
    b32.summary().tables[1]
    b33 = b32.get_prediction(start=pd.to_datetime('2019-01-01'), dynamic=True)
    b34 = b33.conf_int()
    b36 = b33.predicted_mean
    b37 = b21['2019-01-01':]
    b38 = ((b36 - b37) ** 2).mean()
    b39 = b32.get_forecast(steps=stp)
    b34 = b39.conf_int()
    return {
        'data': [go.Scatter(
        b20 = b21.index,
        b21 = b21,
        b35 = 'Actual'
    ),
    go.Scatter(
        b20 = b39.predicted_mean.index,
        b21 = b39.predicted_mean,
        b35 = 'Predicted'
    )],
        'b6': {
                'title': 'Sales turnover future prediction per Month :',
                'xaxis' : {'title': 'Date'},
            'yaxis' : {'title': 'Turnover'}
            }
        }
if b40 = = '__main__':
    b2.run_server(b41 = True, host='127.0.0.1', port=8050)