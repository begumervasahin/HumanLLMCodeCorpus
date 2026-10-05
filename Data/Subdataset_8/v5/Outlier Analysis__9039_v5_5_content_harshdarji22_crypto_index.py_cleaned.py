
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd
import mysql.connector
import csv
from goose3 import Goose
from coinmarketcap import Market
app = dash.Dash(__name__)
server = app.server
cnx = mysql.connector.connect(user='student', password='cs336student',
                              host='cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
                              database='CryptoNews')
def fetch_coinmarketcap_data():
    coinmarketcap = Market()
    return coinmarketcap.ticker(start=0, limit=10)
def process_market_cap_data(stat):
    pl = [i["id"] for i in stat]
    pv = [float(i["market_cap_usd"]) for i in stat]
    stat1 = coinmarketcap.stats()
    bitcoin_per = stat1["bitcoin_percentage_of_market_cap"]
    bit = coinmarketcap.ticker('bitcoin')
    bit_p = bit[0]["market_cap_usd"]
    pv2 = [(float(p) * float(bitcoin_per)) / float(bit_p) for p in pv]
    pl.append("Others")
    pv2.append(100 - sum(pv2))
    return pl, pv2
g = Goose()
def clean_text(s):
    f = False
    s1 = ""
    for i in s:
        if i == '[':
            f = True
            continue
        if i == ']':
            f = False
            continue
        if f:
            continue
        s1 += i
    return s1
app.layout = html.Div(
    children=[
        html.H1(children='Crypto Analysis', style={'textAlign': 'center', 'font': 'bold 35px Castellar, serif', 'padding': '20px 0px 0px 0px'}),
        html.Label(children='Select a currency:', style={'margin': '0% 0% 0% 1%', 'font': '20px Britannic, serif'}),
        html.Br(),
        html.Div(
            children=dcc.Dropdown(
                id='cryptos',
                options=[
                    {'label': 'Bitcoin', 'value': 'Bitcoin'},
                    {'label': 'Ethereum', 'value': 'Ethereum'},
                    {'label': 'Ripple', 'value': 'Ripple'},
                    {'label': 'Litecoin', 'value': 'Litecoin'},
                    {'label': 'Monero', 'value': 'Monero'}
                ],
                value='Bitcoin'
            ),
            style={'width': '20%', 'font-size': '20px', 'margin': '0% 0% 0% 1%'}
        ),
        html.Hr(),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.H4(children='Price Chart', style={'font-weight': 'bold', 'border': '2px solid black'}),
                        html.Div(id='price')
                    ],
                    className="six columns"
                ),
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.H4(children='Facts', style={'font-weight': 'bold', 'border': '2px solid black'}),
                                html.Div(id='price_facts', style={'font-size': '15px', 'text-align': 'justify'})
                            ],
                            className="six columns"
                        ),
                        html.Div(
                            children=[
                                html.H4(children='About', style={'font-weight': 'bold', 'border': '2px solid black'}),
                                html.Div(id='about', style={'font-size': '15px', 'text-align': 'justify', 'height': '400px', 'overflow': 'scroll'})
                            ],
                            className="six columns"
                        ),
                    ],
                    className="row"
                ),
            ],
            className="row"
        ),
        html.Hr(),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.H4(children='Relevant Domains', style={'font-weight': 'bold', 'border': '2px solid black'}),
                        html.Div(id='rel_domains', style={'font-size': '15px'})
                    ],
                    className="six columns"
                ),
                html.Div(
                    children=[
                        html.H4(children='Market Cap Distribution', style={'font-weight': 'bold', 'border': '2px solid black'}),
                        dcc.Graph(id='pi')
                    ],
                    className="six columns"
                ),
            ],
            className="row"
        ),
        html.Hr(),
        html.H1(children='Outlier Analysis', style={'textAlign': 'center', 'font': 'bold 35px Castellar, serif', 'padding': '20px 0px 0px 0px'}),
    ],
    style={'backgroundImage': 'url("http:
)
@app.callback(
    Output('about', 'children'),
    [Input('cryptos', 'value')]
)
def update_about(value):
    BASE_URL = 'https:
    BACK_URL = '{}'.format(value)
    if BACK_URL == "Ripple":
        BACK_URL = "Ripple_(payment_protocol)"
    if BACK_URL == "EOS":
        BACK_URL = "EOS.IO"
    if BACK_URL == "Monero":
        BACK_URL = "Monero_(cryptocurrency)"
    LANDING_PAGE = BASE_URL + BACK_URL
    f = g.extract(url=LANDING_PAGE)
    c = f.cleaned_text.split("\n")
    s = clean_text(c[0] + c[2])
    return s
@app.callback(
    Output('price', 'children'),
    [Input('cryptos', 'value')]
)
def update_price(value):
    pass
@app.callback(
    Output('price_facts', 'children'),
    [Input('price', 'children')]
)
def update_price_facts(value):
    pass
@app.callback(
    Output('rel_domains', 'children'),
    [Input('cryptos', 'value')]
)
def update_rel_domains(value):
    pass
@app.callback(
    Output('top_news', 'children'),
    [Input('cryptos', 'value')]
)
def update_top_news(value):
    pass
@app.callback(
    Output('outlier', 'selected_row_indices'),
    [Input('graph-outlier', 'clickData')],
    [State('outlier', 'selected_row_indices')]
)
def update_selected_row_indices(clickData, selected_row_indices):
    pass
@app.callback(
    Output('graph-outlier', 'figure'),
    [Input('outlier', 'rows'),
     Input('outlier', 'selected_row_indices')]
)
def update_figure(rows, selected_row_indices):
    pass
if __name__ == '__main__':
    app.run_server(debug=True)