
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd
import mysql.connector
import csv
from goose3 import Goose
from b6 import Market
b1 = dash.Dash(b31)
b2 = b1.b2
b3 = mysql.connector.connect(user='student', password='cs336student',
                              b4 = 'cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
                              b5 = 'CryptoNews')
def fonk1():
    b6 = Market()
    return b6.ticker(b7 = 0, limit=10)
def fonk2(stat):
    b8 = [b18["b21"] for b18 in stat]
    b9 = [float(b18["market_cap_usd"]) for b18 in stat]
    b10 = b6.stats()
    b11 = b10["bitcoin_percentage_of_market_cap"]
    b12 = b6.ticker('bitcoin')
    b13 = b12[0]["market_cap_usd"]
    b14 = [(float(p) * float(b11)) / float(b13) for p in b9]
    b8.append("Others")
    b14.append(100 - sum(b14))
    return b8, b14
b15 = Goose()
def fonk3(b30):
    b16 = False
    b17 = ""
    for b18 in b30:
        if b18 = = '[':
            b16 = True
            continue
        if b18 = = ']':
            b16 = False
            continue
        if b16:
            continue
        b17 += b18
    return b17
b1.b19 = html.Div(
    b20 = [
        html.H1(b20 = 'Crypto Analysis', b24={'textAlign': 'center', 'font': 'bold 35px Castellar, serif', 'padding': '20px 0px 0px 0px'}),
        html.Label(b20 = 'Select a currency:', b24={'margin': '0% 0% 0% 1%', 'font': '20px Britannic, serif'}),
        html.Br(),
        html.Div(
            b20 = dcc.Dropdown(
                b21 = 'cryptos',
                b22 = [
                    {'label': 'Bitcoin', 'b23': 'Bitcoin'},
                    {'label': 'Ethereum', 'b23': 'Ethereum'},
                    {'label': 'Ripple', 'b23': 'Ripple'},
                    {'label': 'Litecoin', 'b23': 'Litecoin'},
                    {'label': 'Monero', 'b23': 'Monero'}
                ],
                b23 = 'Bitcoin'
            ),
            b24 = {'width': '20%', 'font-size': '20px', 'margin': '0% 0% 0% 1%'}
        ),
        html.Hr(),
        html.Div(
            b20 = [
                html.Div(
                    b20 = [
                        html.H4(b20 = 'Price Chart', b24={'font-weight': 'bold', 'border': '2px solid black'}),
                        html.Div(b21 = 'price')
                    ],
                    b25 = "six columns"
                ),
                html.Div(
                    b20 = [
                        html.Div(
                            b20 = [
                                html.H4(b20 = 'Facts', b24={'font-weight': 'bold', 'border': '2px solid black'}),
                                html.Div(b21 = 'price_facts', b24={'font-size': '15px', 'text-align': 'justify'})
                            ],
                            b25 = "six columns"
                        ),
                        html.Div(
                            b20 = [
                                html.H4(b20 = 'About', b24={'font-weight': 'bold', 'border': '2px solid black'}),
                                html.Div(b21 = 'about', b24={'font-size': '15px', 'text-align': 'justify', 'height': '400px', 'overflow': 'scroll'})
                            ],
                            b25 = "six columns"
                        ),
                    ],
                    b25 = "row"
                ),
            ],
            b25 = "row"
        ),
        html.Hr(),
        html.Div(
            b20 = [
                html.Div(
                    b20 = [
                        html.H4(b20 = 'Relevant Domains', b24={'font-weight': 'bold', 'border': '2px solid black'}),
                        html.Div(b21 = 'rel_domains', b24={'font-size': '15px'})
                    ],
                    b25 = "six columns"
                ),
                html.Div(
                    b20 = [
                        html.H4(b20 = 'Market Cap Distribution', b24={'font-weight': 'bold', 'border': '2px solid black'}),
                        dcc.Graph(b21 = 'pi')
                    ],
                    b25 = "six columns"
                ),
            ],
            b25 = "row"
        ),
        html.Hr(),
        html.H1(b20 = 'Outlier Analysis', b24={'textAlign': 'center', 'font': 'bold 35px Castellar, serif', 'padding': '20px 0px 0px 0px'}),
    ],
    b24 = {'backgroundImage': 'url("http:
)
@b1.callback(
    Output('about', 'b20'),
    [Input('cryptos', 'b23')]
)
def fonk4(b23):
    b26 = 'https:
    b27 = '{}'.format(b23)
    if b27 = = "Ripple":
        b27 = "Ripple_(payment_protocol)"
    if b27 = = "EOS":
        b27 = "EOS.IO"
    if b27 = = "Monero":
        b27 = "Monero_(cryptocurrency)"
    b28 = b26 + b27
    b16 = b15.extract(url=b28)
    b29 = b16.cleaned_text.split("\n")
    b30 = fonk3(b29[0] + b29[2])
    return b30
@b1.callback(
    Output('price', 'b20'),
    [Input('cryptos', 'b23')]
)
def fonk5(b23):
    pass
@b1.callback(
    Output('price_facts', 'b20'),
    [Input('price', 'b20')]
)
def fonk6(b23):
    pass
@b1.callback(
    Output('rel_domains', 'b20'),
    [Input('cryptos', 'b23')]
)
def fonk7(b23):
    pass
@b1.callback(
    Output('top_news', 'b20'),
    [Input('cryptos', 'b23')]
)
def fonk8(b23):
    pass
@b1.callback(
    Output('outlier', 'selected_row_indices'),
    [Input('graph-outlier', 'clickData')],
    [State('outlier', 'selected_row_indices')]
)
def fonk9(clickData, selected_row_indices):
    pass
@b1.callback(
    Output('graph-outlier', 'figure'),
    [Input('outlier', 'rows'),
     Input('outlier', 'selected_row_indices')]
)
def fonk10(rows, selected_row_indices):
    pass
if b31 = = '__main__':
    b1.run_server(b32 = True)