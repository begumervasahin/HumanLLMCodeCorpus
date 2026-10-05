
import dash
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import mysql.connector
from datetime import datetime as dt
import statistics
import csv
from dash.dependencies import Input, Output, State
import plotly
from goose3 import Goose
from b1 import Market
b1 = Market()
b2 = b1.ticker(start=0, limit=10)
b3 = []
b4 = []
b5 = []
for b13 in b2:
    b4.append(b13["b23"])
    b3.append(b13["market_cap_usd"])
b6 = b1.stats()
b7 = b6["bitcoin_percentage_of_market_cap"]
b8 = b1.ticker('bitcoin')
b9 = b8[0]["market_cap_usd"]
for a1 in range(len(b3)):
    b5.append((float(b3[a1]) * float(b7)) / float(b9))
b4.append("Others")
b5.append(100 - sum(b5))
b10 = Goose()
def fonk1(b38):
    b11 = False
    b12 = ""
    for b13 in b38:
        if b13 = = '[':
            b11 = True
            continue
        if b13 = = ']':
            b11 = False
            continue
        if b11:
            continue
        b12 = b12 + b13
    return b12
def fonk2(v):
    b14 = []
    for b13 in range(-1, -100, -1):
        b14.append(((v[b13] - v[b13 - 1]) / v[b13 - 1]) * 100)
    return b14
b15 = dash.Dash()
b16 = b15.b16
b17 = mysql.connector.connect(user='student', password='cs336student',
                              b18 = 'cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
                              b19 = 'CryptoNews')
def fonk3(elem):
    return elem[5]
def fonk4(elem):
    return int(elem[1])
b15.b20 = html.Div(b22={'backgroundImage': 'url("http:
                             'width': '96%', 'margin': '0% 0% 0% 2%', 'borderRadius': '10px'},
                      b21 = [
    html.H1(b22 = {'textAlign': 'center', 'font': 'bold 35px Castellar, serif', 'padding': '20px 0px 0px 0px'},
            b21 = 'Crypto Analysis'),
    html.Label(b22 = {'margin': '0% 0% 0% 1%', 'font': '20px Britannic, serif'}, b21='Select a currency:'),
    html.Br(),
    html.Div(b22 = {'width': '20%', 'font-size': '20px', 'margin': '0% 0% 0% 1%'}, b21=dcc.Dropdown(
        b23 = 'cryptos',
        b24 = [{'label': 'Bitcoin', 'b25': 'Bitcoin'},
                 {'label': 'Ethereum', 'b25': 'Ethereum'},
                 {'label': 'Ripple', 'b25': 'Ripple'},
                 {'label': 'Litecoin', 'b25': 'Litecoin'},
                 {'label': 'Monero', 'b25': 'Monero'}],
        b25 = 'Bitcoin'
    )),
    html.Hr(),
    html.Div(b22 = {'margin': '0% 0% 0% 1%'}, b21=[
        html.Div([
            html.H4(b22 = {'font-weight': 'bold', 'border': '2px solid black'}, b21='Price Chart'),
            html.Div(b23 = 'price', b21=[])
        ], b26 = "six columns"),
        html.Div([
            html.Div(b22 = {'width': '20%', 'margin': '0% 0% 0% 2%'}, b21=[
                html.H4(b22 = {'font-weight': 'bold', 'border': '2px solid black'}, b21='Facts'),
                html.Div(b22 = {'font-size': '15px', 'text-align': 'justify'}, b23='price_facts')
            ], b26 = "six columns"),
            html.Div(b22 = {'width': '26%', 'margin': '0% 0% 0% 2%'}, b21=[
                html.H4(b22 = {'font-weight': 'bold', 'border': '2px solid black'}, b21='About'),
                html.Div(b22 = {'font-size': '15px', 'text-align': 'justify', 'height': '400px', 'overflow': 'scroll'},
                         b23 = 'about')
            ], b26 = "six columns"),
        ], b26 = "row"),
    ], b26 = "row"),
    html.Hr(),
    html.Div([
        html.Div(b22 = {'width': '47%', 'margin': '0% 0% 0% 2%'}, b21=[
            html.H4(b22 = {'font-weight': 'bold', 'border': '2px solid black'}, b21='Relevant Domains'),
            html.Div(b22 = {'font-size': '15px'}, b23='rel_domains')
        ], b26 = "six columns"),
        html.Div(b22 = {'width': '47%', 'margin': '0% 0% 0% 2%'}, b21=[
            html.H4(b22 = {'font-weight': 'bold', 'border': '2px solid black'}, b21='Market Cap Distribution'),
            dcc.Graph(
                b23 = 'pi',
                b27 = {
                    'data': [
                        {'values': b5, 'labels': b4, 'type': 'pie'},
                    ],
                    'b20': {
                        'title': "Market Cap Distribution",
                    }
                }
            )
        ], b26 = "six columns"),
    ], b26 = "row"),
    html.Hr(),
    html.H1(b22 = {'textAlign': 'center', 'font': 'bold 35px Castellar, serif', 'padding': '20px 0px 0px 0px'},
            b21 = 'Outlier Analysis'),
    html.Div([
        html.Div(b22 = {'margin': '0% 0% 0% 1%', 'width': '45%'}, b21=[
            html.H4(b22 = {'font-weight': 'bold', 'border': '2px solid black'},
                    b21 = 'Outlier Feature Calculation'),
            dte.DataTable(
                b28 = outlier_df.to_dict('records'),
                b29 = True,
                b30 = True,
                b31 = True,
                b32 = [],
                b23 = 'outlier'
            ),
            html.Div(b21 = ['*All calculations are with respect to Bitcoin.']),
            html.Div(b22 = {'font-size': '15px'},
                     b21 = ['This is an interactive table. You can sort, search, and filter using any column in the table. The adjacent graphs will update accordingly.']),
        ], b26 = "six columns"),
        html.Div([
            html.Div(b23 = 'selected-indexes'),
            dcc.Graph(
                b23 = 'graph-outlier'
            )], b26 = "six columns"),
    ], b26 = "row"),
    html.Hr(),
    html.H1(b22 = {'textAlign': 'center', 'font': 'bold 35px Castellar, serif', 'padding': '20px 0px 0px 0px'},
            b21 = 'Pump and Dump Analysis'),
    html.Div(b22 = {'font-size': '15px'}, b21=['''
        Click on the below link to go to the pump and dump webpage
        ''']),
    html.Div(b22 = {'font-size': '20px'}, b21=html.A(b58="https:
                                                          b33 = "_blank", b21="Click here")),
    html.Div(b22 = {'width': '95%', 'margin': '1% 2.5% 1% 2.5%', 'borderRadius': '10px', 'opacity': '1'},
             b21 = html.Div(b23='output')),
])
@b15.callback(
    Output('about', 'b21'),
    [Input('cryptos', 'b25')])
def fonk5(b25):
    b34 = 'https:
    b35 = '{}'.format(b25)
    if b35 = = "Ripple":
        b35 = "Ripple_(payment_protocol)"
    if b35 = = "EOS":
        b35 = "EOS.IO"
    if b35 = = "Monero":
        b35 = "Monero_(cryptocurrency)"
    b36 = b34 + b35
    b11 = b10.extract(url=b36)
    b37 = b11.cleaned_text.split("\n")
    b38 = fonk1(b37[0] + b37[2])
    return b38
@b15.callback(
    Output('price', 'b21'),
    [Input('cryptos', 'b25')])
def fonk6(b25):
    b39 = '{}'.format(b25)
    b40 = pd.read_sql("select quote, time from CryptoNews.Value where currency_name like '" + b39 + "'", b17)
    b41 = b40.iloc[:, 1].tolist()
    b42 = b40.iloc[:, 0].tolist()
    b43 = []
    b44 = []
    for b13 in range(0, len(b42) - 7):
        b44.append(b41[b13 + 7])
        b45 = sum(b42[b13:b13 + 7]) / 7
        b43.append(b45)
    b46 = []
    b47 = []
    for b13 in range(0, len(b42) - 30):
        b47.append(b41[b13 + 30])
        b45 = sum(b42[b13:b13 + 30]) / 30
        b46.append(b45)
    global b48
    b48 = ((b42[-1] - b42[-8]) / b42[-8]) * 100
    global b49
    b49 = ((b42[-1] - b42[-31]) / b42[-31]) * 100
    global b50
    b50 = b42[-1]
    global b51
    b51 = b43[-1]
    global b52
    b52 = b46[-1]
    b53 = html.Div(b21=[dcc.Graph(
        b23 = 'pi',
        b27 = {
            'data': [
                {'b53': b41, 'b42': b42, 'type': 'line', 'name': 'Price', 'mode': 'lines+markers'},
                {'b53': b44, 'b42': b43, 'type': 'line', 'name': '7 Day moving Average', 'mode': 'lines'},
                {'b53': b47, 'b42': b46, 'type': 'line', 'name': '30 Day moving Average', 'mode': 'lines'}
            ],
            'b20': {
                'title': b39 + ' price',
            }
        }
    )])
    return b53
@b15.callback(
    Output('price_facts', 'b21'),
    [Input('price', 'b21')])
def fonk7(b25):
    b53 = html.Table(
        [
            html.Tr([html.Td("Current Price"), html.Td(round(b50, 2))]),
            html.Tr([html.Td("Past 7 days Average"), html.Td(round(b51, 2))]),
            html.Tr([html.Td("Past 30 days Average"), html.Td(round(b52, 2))]),
            html.Tr([html.Td("Past 7 days % Change"), html.Td(round(b48, 2))]),
            html.Tr([html.Td("Past 30 days % Change"), html.Td(round(b49, 2))])
        ]
    )
    return b53
@b15.callback(
    Output('rel_domains', 'b21'),
    [Input('cryptos', 'b25')])
def fonk8(b25):
    b37 = '{}'.format(b25)
    b11 = "dom_" + b37 + ".csv"
    b54 = csv.b62(open(b11), delimiter=',')
    b55 = sorted(b54, key=takeSecond, reverse=True)
    b56 = list(b55)
    b57 = []
    for b13 in b56:
        b57.append("http:
    b53 = html.Table(
        [
            html.Tr([html.Td(html.A(b58 = b57[0], b33="_blank", b21=b56[0][0]))]),
            html.Tr([html.Td(html.A(b58 = b57[1], b33="_blank", b21=b56[1][0]))]),
            html.Tr([html.Td(html.A(b58 = b57[2], b33="_blank", b21=b56[2][0]))]),
            html.Tr([html.Td(html.A(b58 = b57[3], b33="_blank", b21=b56[3][0]))]),
            html.Tr([html.Td(html.A(b58 = b57[4], b33="_blank", b21=b56[4][0]))]),
        ]
    )
    return b53
@b15.callback(
    Output('top_news', 'b21'),
    [Input('cryptos', 'b25')])
def fonk9(b25):
    b37 = '{}'.format(b25)
    b11 = "dom_" + b37 + ".csv"
    b54 = csv.b62(open(b11), delimiter=',')
    b59 = []
    b55 = sorted(b54, key=takeSecond, reverse=True)
    b56 = list(b55)
    b13 = 0
    a1 = 0
    while (b13 < 5):
        b60 = b56[a1][0]
        b61 = []
        a1 = a1 + 1
        try:
            b62 = csv.b62(open("output.csv"), delimiter=',')
            b63 = filter(lambda b41: b41[0] == b37, b62)
            b64 = filter(lambda b41: b41[4] == "Y", fil)
            b65 = sorted(b64, key=takeSixth, reverse=True)
            b61 = list(b65)
            b59.append(b61[0])
            b13 = b13 + 1
        except:
            continue
    b53 = html.Table(
        [
            html.Tr([html.Td(html.A(b58 = b59[0][1], b33="_blank", b21=b59[0][2]))]),
            html.Tr([html.Td(html.A(b58 = b59[1][1], b33="_blank", b21=b59[1][2]))]),
            html.Tr([html.Td(html.A(b58 = b59[2][1], b33="_blank", b21=b59[2][2]))]),
            html.Tr([html.Td(html.A(b58 = b59[3][1], b33="_blank", b21=b59[3][2]))]),
            html.Tr([html.Td(html.A(b58 = b59[4][1], b33="_blank", b21=b59[4][2]))]),
        ])
    return b53
@b15.callback(
    Output('outlier', 'b32'),
    [Input('graph-outlier', 'clickData')],
    [State('outlier', 'b32')])
def fonk10(clickData, b32):
    if clickData:
        for point in clickData['points']:
            if point['pointNumber'] in b32:
                b32.remove(point['pointNumber'])
            else:
                b32.append(point['pointNumber'])
    return b32
@b15.callback(
    Output('graph-outlier', 'b27'),
    [Input('outlier', 'b28'),
     Input('outlier', 'b32')])
def fonk11(b28, b32):
    b66 = pd.DataFrame(b28)
    b67 = plotly.tools.make_subplots(
        b28 = 3, cols=1,
        b68 = ('Opposite Trends', 'Mean Square Error', 'Volatility',),
        b69 = True)
    b70 = {'color': ['' for _ in range(len(b28))]}
    for b13 in (b32 or []):
        b70['color'][b13] = ''
    b67.append_trace({
        'b53': b66['Crypto Currency'],
        'b42': b66['Opposite Trend %'],
        'type': 'bar',
        'b70': b70
    }, 1, 1)
    b67.append_trace({
        'b53': b66['Crypto Currency'],
        'b42': b66['Mean Square Error'],
        'type': 'bar',
        'b70': b70
    }, 2, 1)
    b67.append_trace({
        'b53': b66['Crypto Currency'],
        'b42': b66['Volatility'],
        'type': 'bar',
        'b70': b70
    }, 3, 1)
    b67['b20']['showlegend'] = False
    b67['b20']['height'] = 800
    b67['b20']['margin'] = {
        'l': 40,
        'r': 10,
        't': 60,
        'b': 200
    }
    b67['b20']['yaxis2']['type'] = 'log'
    b67['b20']['yaxis3']['type'] = 'log'
    return b67
b15.css.append_css({"external_url": "https:
b15.css.append_css({
    'external_url': 'https:
})
if b71 = = '__main__':
    b15.run_server(b72 = True)