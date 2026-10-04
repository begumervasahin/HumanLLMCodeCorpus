import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd
import mysql.connector
from goose3 import Goose
import csv
b1 = mysql.connector.connect(user='student', password='cs336student',
                              b2 = 'cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
                              b3 = 'CryptoNews')
b4 = Goose()
def fonk1(b28):
    b5 = False
    b6 = ""
    for b7 in b28:
        if b7 = = '[':
            b5 = True
            continue
        if b7 = = ']':
            b5 = False
            continue
        if b5:
            continue
        b6 = b6 + b7
    return b6
b8 = pd.read_csv("outlier.csv")
b8.sort_values(b9 = ['Outlier Score'])
b10 = b8.iloc[61:161, :]
b11 = dash.Dash(b61)
b12 = b11.b12
b11.config['suppress_callback_exceptions'] = True
b11.b13 = html.Div(b14={'backgroundImage': 'url("http:
    html.H1(b14 = {'textAlign': 'center', 'font': 'bold 35px Castellar, serif', 'padding': '20px 0px 0px 0px'}, b23='Crypto Analysis'),
    html.Label(b14 = {'b57': '0% 0% 0% 1%', 'font': '20px Britannic, serif'}, b23='Select a currency:'),
    html.Br(),
    html.Div(b14 = {'width': '20%', 'font-size': '20px', 'b57': '0% 0% 0% 1%'}, b23=dcc.Dropdown(
        b15 = 'cryptos',
        b16 = [
            {'label': 'Bitcoin', 'b17': 'Bitcoin'},
            {'label': 'Ethereum', 'b17': 'Ethereum'},
            {'label': 'Ripple', 'b17': 'Ripple'},
            {'label': 'Litecoin', 'b17': 'Litecoin'},
            {'label': 'Monero', 'b17': 'Monero'}
        ],
        b17 = 'Bitcoin'
    )),
    html.Hr(),
    html.Div(b14 = {'b57': '0% 0% 0% 1%'}, b23=[
        html.Div([
            html.H4(b14 = {'font-weight': 'bold', 'border': '2px solid black'}, b23='Price Chart'),
            html.Div(b15 = 'price', b23=[])
        ], b18 = "six b21"),
        html.Div([
            html.Div(b14 = {'width': '20%', 'b57': '0% 0% 0% 2%'}, b23=[
                html.H4(b14 = {'font-weight': 'bold', 'border': '2px solid black'}, b23='Facts'),
                html.Div(b14 = {'font-size': '15px', 'text-align': 'justify'}, b15='price_facts')
            ], b18 = "six b21"),
            html.Div(b14 = {'width': '26%', 'b57': '0% 0% 0% 2%'}, b23=[
                html.H4(b14 = {'font-weight': 'bold', 'border': '2px solid black'}, b23='About'),
                html.Div(b14 = {'font-size': '15px', 'text-align': 'justify', 'b56': '400px', 'overflow': 'scroll'}, b15='about')
            ], b18 = "six b21"),
        ], b18 = "row"),
    ], b18 = "row"),
    html.Hr(),
    html.Div([
        html.Div(b14 = {'width': '47%', 'b57': '0% 0% 0% 2%'}, b23=[
            html.H4(b14 = {'font-weight': 'bold', 'border': '2px solid black'}, b23='Relevant Domains'),
            html.Div(b14 = {'font-size': '15px'}, b15='rel_domains')
        ], b18 = "six b21"),
        html.Div(b14 = {'width': '47%', 'b57': '0% 0% 0% 2%'}, b23=[
            html.H4(b14 = {'font-weight': 'bold', 'border': '2px solid black'}, b23='Market Cap Distribution'),
            dcc.Graph(
                b15 = 'pi',
                b19 = {
                    'b20': [
                        {'values': [0], 'labels': [''], 'type': 'pie'},
                    ],
                    'b13': {
                        'b54': "Market Cap Distribution",
                    }
                }
            )
        ], b18 = "six b21"),
    ], b18 = "row"),
    html.Hr(),
    html.H1(b14 = {'textAlign': 'center', 'font': 'bold 35px Castellar, serif', 'padding': '20px 0px 0px 0px'}, b23='Outlier Analysis'),
    html.Div([
        html.Div(b14 = {'b57': '0% 0% 0% 1%', 'width': '45%'}, b23=[
            html.H4(b14 = {'font-weight': 'bold', 'border': '2px solid black'}, b23='Outlier Feature Calculation'),
            dcc.DataTable(
                b20 = b10.to_dict('records'),
                b21 = [{"name": b7, "b15": b7} for b7 in b10.b21],
                b22 = 'multi',
                b15 = 'outlier'
            ),
            html.Div(b23 = [
                '*All calculations are with respect to Bitcoin.'
            ]),
            html.Div(b14 = {'font-size': '15px'}, b23=[
                'This is an interactive table. You can sort, search and filter using any column in the table. The adjacent graphs will update accordingly.'
            ]),
        ], b18 = "six b21"),
        html.Div([
            html.Div(b15 = 'selected-indexes'),
            dcc.Graph(b15 = 'graph-outlier')
        ], b18 = "six b21"),
    ], b18 = "row"),
    html.Hr(),
    html.H1(b14 = {'textAlign': 'center', 'font': 'bold 35px Castellar, serif', 'padding': '20px 0px 0px 0px'}, b23='Pump and Dump Analysis'),
    html.Div(b14 = {'font-size': '15px'}, b23=[
        'Click on the below link to go to the pump and dump webpage'
    ]),
    html.Div(b14 = {'font-size': '20px'}, b23=html.A(b50="https:
    html.Div(b14 = {'width': '95%', 'b57': '1% 2.5% 1% 2.5%', 'borderRadius': '10px', 'opacity': '1'}, b23=html.Div(b15='output')),
])
@b11.callback(
    Output('about', 'b23'),
    [Input('cryptos', 'b17')]
)
def fonk2(b17):
    b24 = 'https:
    b25 = '{}'.format(b17)
    if b25 = = "Ripple":
        b25 = "Ripple_(payment_protocol)"
    if b25 = = "EOS":
        b25 = "EOS.IO"
    if b25 = = "Monero":
        b25 = "Monero_(cryptocurrency)"
    b26 = b24 + b25
    b5 = b4.extract(url=b26)
    b27 = b5.cleaned_text.split("\n")
    b28 = fonk1(b27[0] + b27[2])
    return b28
@b11.callback(
    Output('price', 'b23'),
    [Input('cryptos', 'b17')]
)
def fonk3(b17):
    b29 = '{}'.format(b17)
    b30 = pd.read_sql("SELECT quote, time FROM CryptoNews.Value WHERE currency_name LIKE '" + b29 + "'", b1)
    b31 = b30['time'].tolist()
    b32 = b30['quote'].tolist()
    b33 = []
    b34 = []
    for b7 in range(0, len(b32) - 7):
        b34.append(b31[b7 + 7])
        b35 = sum(b32[b7:b7 + 7]) / 7
        b33.append(b35)
    b36 = []
    b37 = []
    b38 = ((b32[-1] - b32[-8]) / b32[-8]) * 100
    b39 = ((b32[-1] - b32[-31]) / b32[-31]) * 100
    b40 = b32[-1]
    b41 = b33[-1]
    for b7 in range(0, len(b32) - 30):
        b37.append(b31[b7 + 30])
        b35 = sum(b32[b7:b7 + 30]) / 30
        b36.append(b35)
    b42 = b36[-1]
    b43 = html.Div(b23=[
        dcc.Graph(
            b15 = 'price_chart',
            b19 = {
                'b20': [
                    {'b43': b31, 'b32': b32, 'type': 'line', 'name': 'Price', 'mode': 'lines+markers'},
                    {'b43': b34, 'b32': b33, 'type': 'line', 'name': '7 Day Moving Average', 'mode': 'lines'},
                    {'b43': b37, 'b32': b36, 'type': 'line', 'name': '30 Day Moving Average', 'mode': 'lines'}
                ],
                'b13': {
                    'b54': b29 + ' price',
                }
            }
        )
    ])
    return b43
@b11.callback(
    Output('price_facts', 'b23'),
    [Input('price', 'b23')]
)
def fonk4(b17):
    b44 = html.Table([
        html.Tr([html.Td("Current Price"), html.Td(round(b40, 2))]),
        html.Tr([html.Td("Past 7 days Average"), html.Td(round(b41, 2))]),
        html.Tr([html.Td("Past 30 days Average"), html.Td(round(b42, 2))]),
        html.Tr([html.Td("Past 7 days % Change"), html.Td(round(b38, 2))]),
        html.Tr([html.Td("Past 30 days % Change"), html.Td(round(b39, 2))])
    ])
    return b44
@b11.callback(
    Output('rel_domains', 'b23'),
    [Input('cryptos', 'b17')]
)
def fonk5(b17):
    b27 = '{}'.format(b17)
    b5 = "dom_" + b27 + ".csv"
    b45 = csv.reader(open(b5), delimiter=',')
    b46 = sorted(b45, key=lambda b43: int(b43[1]), reverse=True)
    b47 = list(b46)
    b48 = ["http:
    b49 = html.Table([
        html.Tr([html.Td(html.A(b50 = b48[0], target="_blank", b23=b47[0][0]))]),
        html.Tr([html.Td(html.A(b50 = b48[1], target="_blank", b23=b47[1][0]))]),
        html.Tr([html.Td(html.A(b50 = b48[2], target="_blank", b23=b47[2][0]))]),
        html.Tr([html.Td(html.A(b50 = b48[3], target="_blank", b23=b47[3][0]))]),
        html.Tr([html.Td(html.A(b50 = b48[4], target="_blank", b23=b47[4][0]))]),
    ])
    return b49
@b11.callback(
    Output('graph-outlier', 'b19'),
    [Input('outlier', 'b20'), Input('outlier', 'selected_rows')]
)
def fonk6(rows, selected_rows):
    b51 = pd.DataFrame(rows)
    b52 = {'color': ['
    for b7 in (selected_rows or []):
        b52['color'][b7] = '
    b53 = go.Figure(
        b20 = [
            go.Bar(b43 = b51['Crypto Currency'], b32=b51['Opposite Trend %'], b52=b52, name='Opposite Trends'),
            go.Bar(b43 = b51['Crypto Currency'], b32=b51['Mean Square Error'], b52=b52, name='Mean Square Error', b58='y2'),
            go.Bar(b43 = b51['Crypto Currency'], b32=b51['Volatility'], b52=b52, name='Volatility', b58='y3')
        ],
        b13 = go.Layout(
            b54 = 'Outlier Analysis',
            b55 = False,
            b56 = 800,
            b57 = {'l': 40, 'r': 10, 't': 60, 'b': 200},
            b58 = {'b54': 'Opposite Trend %'},
            b59 = {'b54': 'Mean Square Error', 'overlaying': 'b32', 'side': 'right', 'type': 'log'},
            b60 = {'b54': 'Volatility', 'overlaying': 'b32', 'side': 'right', 'type': 'log'}
        )
    )
    return b53
if b61 = = '__main__':
    b11.run_server(b62 = True)