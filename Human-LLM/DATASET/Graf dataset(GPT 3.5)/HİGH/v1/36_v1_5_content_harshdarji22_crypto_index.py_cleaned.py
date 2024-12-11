import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import mysql.connector
import csv
from bs4 import BeautifulSoup
from goose3 import Goose
from b6 import Market
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import plotly
b1 = dash.Dash(b61)
b2 = b1.b2
b3 = mysql.connector.connect(user='student', password='cs336student',
                              b4 = 'cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
                              b5 = 'CryptoNews')
b6 = Market()
b7 = b6.ticker(start=0, limit=10)
b8 = []
b9 = []
b10 = []
for b18 in b7:
    b9.append(b18["b22"])
    b8.append(b18["market_cap_usd"])
b11 = b6.stats()
b12 = b11["bitcoin_percentage_of_market_cap"]
b13 = b6.ticker('bitcoin')
b14 = b13[0]["market_cap_usd"]
for a1 in range(len(b8)):
    b10.append((float(b8[a1]) * float(b12)) / float(b14))
b9.append("Others")
b10.append(100 - sum(b10))
b15 = Goose()
def fonk1(b32):
    b16 = False
    b17 = ""
    for b18 in b32:
        if b18 = = '[':
            b16 = True
            continue
        if b18 = = ']':
            b16 = False
            continue
        if b16:
            continue
        b17 = b17 + b18
    return b17
def fonk2(v):
    b19 = []
    for b18 in range(-1, -100, -1):
        b19.append(((v[b18] - v[b18 - 1]) / v[b18 - 1]) * 100)
    return b19
b1.b20 = html.Div(b21={'backgroundImage': 'url("http:
    html.H1(b21 = {'textAlign': 'center', 'font': 'bold 35px Castellar, serif', 'padding': '20px 0px 0px 0px'}, b27='Crypto Analysis'),
    html.Label(b21 = {'margin': '0% 0% 0% 1%', 'font': '20px Britannic, serif'}, b27='Select a currency:'),
    html.Br(),
    html.Div(b21 = {'width': '20%', 'font-size': '20px', 'margin': '0% 0% 0% 1%'}, b27=dcc.Dropdown(
        b22 = 'cryptos',
        b23 = [{'label': 'Bitcoin', 'b24': 'Bitcoin'},
                 {'label': 'Ethereum', 'b24': 'Ethereum'},
                 {'label': 'Ripple', 'b24': 'Ripple'},
                 {'label': 'Litecoin', 'b24': 'Litecoin'},
                 {'label': 'Monero', 'b24': 'Monero'}],
        b24 = 'Bitcoin'
    )),
    html.Hr(),
    html.Div(b21 = {'margin': '0% 0% 0% 1%'}, b27=[
        html.Div([
            html.H4(b21 = {'font-weight': 'bold', 'border': '2px solid black'}, b27='Price Chart'),
            html.Div(b22 = 'price', b27=[])
        ], b25 = "six columns"),
        html.Div([html.Div(b21 = {'width': '20%', 'margin': '0% 0% 0% 2%'}, b27=[
            html.H4(b21 = {'font-weight': 'bold', 'border': '2px solid black'}, b27='Facts'),
            html.Div(b21 = {'font-size': '15px', 'text-align': 'justify'}, b22='price_facts')
        ], b25 = "six columns"),
            html.Div(b21 = {'width': '26%', 'margin': '0% 0% 0% 2%'}, b27=[
                html.H4(b21 = {'font-weight': 'bold', 'border': '2px solid black'}, b27='About'),
                html.Div(b21 = {'font-size': '15px', 'text-align': 'justify', 'height': '400px', 'overflow': 'scroll'}, b22='about')
            ], b25 = "six columns"),
        ], b25 = "row"),
    ], b25 = "row"),
    html.Hr(),
    html.Div([
        html.Div(b21 = {'width': '47%', 'margin': '0% 0% 0% 2%'}, b27=[
            html.H4(b21 = {'font-weight': 'bold', 'border': '2px solid black'}, b27='Relevant Domains'),
            html.Div(b21 = {'font-size': '15px'}, b22='rel_domains')
        ], b25 = "six columns"),
        html.Div(b21 = {'width': '47%', 'margin': '0% 0% 0% 2%'}, b27=[
            html.H4(b21 = {'font-weight': 'bold', 'border': '2px solid black'}, b27='Market Cap Distribution'),
            dcc.Graph(
                b22 = 'pi',
                b26 = {
                    'data': [
                        {'values': b10, 'labels': b9, 'type': 'pie'},
                    ],
                    'b20': {
                        'title': "Market Cap Distribution",
                    }
                }
            )
        ], b25 = "six columns"),
    ], b25 = "row"),
    html.Hr(),
    html.H1(b21 = {'textAlign': 'center', 'font': 'bold 35px Castellar, serif', 'padding': '20px 0px 0px 0px'}, b27='Outlier Analysis'),
    html.Div([
        html.Div(b21 = {'margin': '0% 0% 0% 1%', 'width': '45%'}, b27=[
            html.H4(b21 = {'font-weight': 'bold', 'border': '2px solid black'}, b27='Outlier Feature Calculation'),
            html.Div(b21 = {'font-size': '15px'}, b22='outlier')
        ]),
        html.Div([html.Div(b22 = 'selected-indexes'),
                  dcc.Graph(
                      b22 = 'graph-outlier'
                  )], b25 = "six columns"),
    ], b25 = "row"),
    html.Hr(),
    html.H1(b21 = {'textAlign': 'center', 'font': 'bold 35px Castellar, serif', 'padding': '20px 0px 0px 0px'},
            b27 = 'Pump and Dump Analysis'),
    html.Div(b21 = {'font-size': '15px'}, b27=['''
            Click on the below link to go to the pump and dump webpage
            ''']),
    html.Div(b21 = {'font-size': '20px'}, b27=html.A(b47="https:
    html.Div(b21 = {'width': '95%', 'margin': '1% 2.5% 1% 2.5%', 'borderRadius': '10px', 'opacity': '1'},
             b27 = html.Div(b22='output')),
])
@b1.callback(
    Output('about', 'b27'),
    [Input('cryptos', 'b24')])
def fonk3(b24):
    b28 = 'https:
    b29 = '{}'.format(b24)
    if b29 = = "Ripple":
        b29 = "Ripple_(payment_protocol)"
    if b29 = = "EOS":
        b29 = "EOS.IO"
    if b29 = = "Monero":
        b29 = "Monero_(cryptocurrency)"
    b30 = b28 + b29
    b16 = b15.extract(url=b30)
    b31 = b16.cleaned_text.split("\n")
    b32 = fonk1(b31[0] + b31[2])
    return b32
@b1.callback(
    Output('price', 'b27'),
    [Input('cryptos', 'b24')])
def fonk4(b24):
    b33 = '{}'.format(b24)
    b34 = pd.read_sql("select quote, time from CryptoNews.Value where currency_name like '" + b33 + "'", b3)
    b35 = b34.iloc[:, 1].tolist()
    b36 = b34.iloc[:, 0].tolist()
    b37 = []
    b38 = []
    for b18 in range(0, len(b36) - 7):
        b38.append(b35[b18 + 7])
        b39 = sum(b36[b18:b18 + 7]) / 7
        b37.append(b39)
    b40 = []
    b41 = []
    for b18 in range(0, len(b36) - 30):
        b41.append(b35[b18 + 30])
        b39 = sum(b36[b18:b18 + 30]) / 30
        b40.append(b39)
    return html.Div(b27 = [dcc.Graph(
        b22 = 'pi',
        b26 = {
            'data': [
                {'b42': b35, 'b36': b36, 'type': 'line', 'name': 'Price', 'mode': 'lines+markers'},
                {'b42': b38, 'b36': b37, 'type': 'line', 'name': '7 Day moving Average', 'mode': 'lines'},
                {'b42': b41, 'b36': b40, 'type': 'line', 'name': '30 Day moving Average', 'mode': 'lines'}
            ],
            'b20': {
                'title': b33 + ' price',
            }
        }
    )])
@b1.callback(
    Output('price_facts', 'b27'),
    [Input('price', 'b27')])
def fonk5(b24):
    b42 = html.Table(
        [
            html.Tr([html.Td("Current Price"), html.Td(round(curr_price, 2))]),
            html.Tr([html.Td("Past 7 days Average"), html.Td(round(curr_7_avg, 2))]),
            html.Tr([html.Td("Past 30 days Average"), html.Td(round(curr_30_avg, 2))]),
            html.Tr([html.Td("Past 7 days % Change"), html.Td(round(change_7, 2))]),
            html.Tr([html.Td("Past 30 days % Change"), html.Td(round(change_30, 2))])
        ]
    )
    return b42
@b1.callback(
    Output('rel_domains', 'b27'),
    [Input('cryptos', 'b24')])
def fonk6(b24):
    b31 = '{}'.format(b24)
    b16 = "dom_" + b31 + ".csv"
    b43 = csv.b51(open(b16), delimiter=',')
    b44 = sorted(b43, key=takeSecond, reverse=True)
    b45 = list(b44)
    b46 = []
    for b18 in b45:
        b46.append("http:
    b42 = html.Table(
        [
            html.Tr([html.Td(html.A(b47 = b46[0], target="_blank", b27=b45[0][0]))]),
            html.Tr([html.Td(html.A(b47 = b46[1], target="_blank", b27=b45[1][0]))]),
            html.Tr([html.Td(html.A(b47 = b46[2], target="_blank", b27=b45[2][0]))]),
            html.Tr([html.Td(html.A(b47 = b46[3], target="_blank", b27=b45[3][0]))]),
            html.Tr([html.Td(html.A(b47 = b46[4], target="_blank", b27=b45[4][0]))]),
        ]
    )
    return b42
@b1.callback(
    Output('outlier', 'b27'),
    [Input('cryptos', 'b24')])
def fonk7(b24):
    b31 = '{}'.format(b24)
    b16 = "dom_" + b31 + ".csv"
    b43 = csv.b51(open(b16), delimiter=',')
    b48 = []
    b44 = sorted(b43, key=takeSecond, reverse=True)
    b45 = list(b44)
    b18 = 0
    a1 = 0
    while b18 < 5:
        b49 = b45[a1][0]
        b50 = []
        a1 = a1 + 1
        try:
            b51 = csv.b51(open("output.csv"), delimiter=',')
            b52 = filter(lambda b35: b35[0] == b31, b51)
            b53 = filter(lambda b35: b35[4] == "Y", fil)
            b54 = sorted(b53, key=takeSixth, reverse=True)
            b50 = list(b54)
            b48.append(b50[0])
            b18 = b18 + 1
        except:
            continue
    b42 = html.Table(
        [
            html.Tr([html.Td(html.A(b47 = b48[0][1], target="_blank", b27=b48[0][2]))]),
            html.Tr([html.Td(html.A(b47 = b48[1][1], target="_blank", b27=b48[1][2]))]),
            html.Tr([html.Td(html.A(b47 = b48[2][1], target="_blank", b27=b48[2][2]))]),
            html.Tr([html.Td(html.A(b47 = b48[3][1], target="_blank", b27=b48[3][2]))]),
            html.Tr([html.Td(html.A(b47 = b48[4][1], target="_blank", b27=b48[4][2]))]),
        ])
    return b42
@b1.callback(
    Output('outlier', 'selected_row_indices'),
    [Input('graph-outlier', 'clickData')],
    [State('outlier', 'selected_row_indices')])
def fonk8(clickData, selected_row_indices):
    if clickData:
        for point in clickData['points']:
            if point['pointNumber'] in selected_row_indices:
                selected_row_indices.remove(point['pointNumber'])
            else:
                selected_row_indices.append(point['pointNumber'])
    return selected_row_indices
@b1.callback(
    Output('graph-outlier', 'b26'),
    [Input('outlier', 'b57'),
     Input('outlier', 'selected_row_indices')])
def fonk9(b57, selected_row_indices):
    b55 = pd.DataFrame(b57)
    b56 = plotly.tools.make_subplots(
        b57 = 3, cols=1,
        b58 = ('Opposite Trends', 'Mean Square Error', 'Volatility',),
        b59 = True)
    b60 = {'color': []}
    for b18 in range(len(b55)):
        if b18 in selected_row_indices:
            b60['color'].append('red')
        else:
            b60['color'].append('blue')
    b56.append_trace({
        'b42': b55['Crypto Currency'],
        'b36': b55['Opposite Trend %'],
        'type': 'bar',
        'b60': b60
    }, 1, 1)
    b56.append_trace({
        'b42': b55['Crypto Currency'],
        'b36': b55['Mean Square Error'],
        'type': 'bar',
        'b60': b60
    }, 2, 1)
    b56.append_trace({
        'b42': b55['Crypto Currency'],
        'b36': b55['Volatility'],
        'type': 'bar',
        'b60': b60
    }, 3, 1)
    b56['b20']['showlegend'] = False
    b56['b20']['height'] = 800
    b56['b20']['margin'] = {
        'l': 40,
        'r': 10,
        't': 60,
        'b': 200
    }
    b56['b20']['yaxis2']['type'] = 'log'
    b56['b20']['yaxis3']['type'] = 'log'
    return b56
b1.css.append_css({"external_url": "https:
b1.css.append_css({
    'external_url': 'https:
})
if b61 = = '__main__':
    b1.run_server(b62 = True)