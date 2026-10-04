import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd
import mysql.connector
from goose3 import Goose
import csv
b1 = mysql.connector.connect(
    b2 = 'student',
    b3 = 'cs336student',
    b4 = 'cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
    b5 = 'CryptoNews'
)
b6 = Goose()
def fonk1(b32):
    b7 = False
    b8 = ""
    for b9 in b32:
        if b9 = = '[':
            b7 = True
            continue
        if b9 = = ']':
            b7 = False
            continue
        if b7:
            continue
        b8 += b9
    return b8
b10 = pd.read_csv("outlier.csv")
b10.sort_values(b11 = ['Outlier Score'])
b12 = b10.iloc[61:161, :]
b13 = dash.Dash(b64)
b14 = b13.b14
b13.config['suppress_callback_exceptions'] = True
b13.b15 = html.Div(
    b16 = {
        'backgroundImage': 'url("http:
        'width': '96%',
        'b60': '0% 0% 0% 2%',
        'borderRadius': '10px'
    },
    b17 = [
        html.H1(
            b16 = {
                'textAlign': 'center',
                'font': 'bold 35px Castellar, serif',
                'padding': '20px 0px 0px 0px'
            },
            b17 = 'Crypto Analysis'
        ),
        html.Label(
            b16 = {'b60': '0% 0% 0% 1%', 'font': '20px Britannic, serif'},
            b17 = 'Select a currency:'
        ),
        html.Br(),
        html.Div(
            b16 = {'width': '20%', 'font-size': '20px', 'b60': '0% 0% 0% 1%'},
            b17 = dcc.Dropdown(
                b18 = 'cryptos',
                b19 = [
                    {'label': 'Bitcoin', 'b20': 'Bitcoin'},
                    {'label': 'Ethereum', 'b20': 'Ethereum'},
                    {'label': 'Ripple', 'b20': 'Ripple'},
                    {'label': 'Litecoin', 'b20': 'Litecoin'},
                    {'label': 'Monero', 'b20': 'Monero'}
                ],
                b20 = 'Bitcoin'
            )
        ),
        html.Hr(),
        html.Div(
            b16 = {'b60': '0% 0% 0% 1%'},
            b17 = [
                html.Div(
                    [
                        html.H4(
                            b16 = {'font-weight': 'bold', 'border': '2px solid black'},
                            b17 = 'Price Chart'
                        ),
                        html.Div(b18 = 'price', b17=[])
                    ],
                    b21 = "six b24"
                ),
                html.Div(
                    [
                        html.Div(
                            b16 = {'width': '20%', 'b60': '0% 0% 0% 2%'},
                            b17 = [
                                html.H4(
                                    b16 = {'font-weight': 'bold', 'border': '2px solid black'},
                                    b17 = 'Facts'
                                ),
                                html.Div(
                                    b16 = {'font-size': '15px', 'text-align': 'justify'},
                                    b18 = 'price_facts'
                                )
                            ],
                            b21 = "six b24"
                        ),
                        html.Div(
                            b16 = {'width': '26%', 'b60': '0% 0% 0% 2%'},
                            b17 = [
                                html.H4(
                                    b16 = {'font-weight': 'bold', 'border': '2px solid black'},
                                    b17 = 'About'
                                ),
                                html.Div(
                                    b16 = {'font-size': '15px', 'text-align': 'justify', 'b59': '400px', 'overflow': 'scroll'},
                                    b18 = 'about'
                                )
                            ],
                            b21 = "six b24"
                        ),
                    ],
                    b21 = "row"
                ),
            ],
            b21 = "row"
        ),
        html.Hr(),
        html.Div(
            [
                html.Div(
                    b16 = {'width': '47%', 'b60': '0% 0% 0% 2%'},
                    b17 = [
                        html.H4(
                            b16 = {'font-weight': 'bold', 'border': '2px solid black'},
                            b17 = 'Relevant Domains'
                        ),
                        html.Div(
                            b16 = {'font-size': '15px'},
                            b18 = 'rel_domains'
                        )
                    ],
                    b21 = "six b24"
                ),
                html.Div(
                    b16 = {'width': '47%', 'b60': '0% 0% 0% 2%'},
                    b17 = [
                        html.H4(
                            b16 = {'font-weight': 'bold', 'border': '2px solid black'},
                            b17 = 'Market Cap Distribution'
                        ),
                        dcc.Graph(
                            b18 = 'pi',
                            b22 = {
                                'b23': [
                                    {'values': [0], 'labels': [''], 'type': 'pie'},
                                ],
                                'b15': {
                                    'b57': "Market Cap Distribution",
                                }
                            }
                        )
                    ],
                    b21 = "six b24"
                ),
            ],
            b21 = "row"
        ),
        html.Hr(),
        html.H1(
            b16 = {'textAlign': 'center', 'font': 'bold 35px Castellar, serif', 'padding': '20px 0px 0px 0px'},
            b17 = 'Outlier Analysis'
        ),
        html.Div(
            [
                html.Div(
                    b16 = {'b60': '0% 0% 0% 1%', 'width': '45%'},
                    b17 = [
                        html.H4(
                            b16 = {'font-weight': 'bold', 'border': '2px solid black'},
                            b17 = 'Outlier Feature Calculation'
                        ),
                        dcc.DataTable(
                            b23 = b12.to_dict('records'),
                            b24 = [{"name": b9, "b18": b9} for b9 in b12.b24],
                            b25 = 'multi',
                            b18 = 'outlier'
                        ),
                        html.Div(
                            b17 = ['*All calculations are with respect to Bitcoin.']
                        ),
                        html.Div(
                            b16 = {'font-size': '15px'},
                            b17 = [
                                'This is an interactive table. You can sort, search and filter using any column in the table. The adjacent graphs will update accordingly.'
                            ]
                        ),
                    ],
                    b21 = "six b24"
                ),
                html.Div(
                    [
                        html.Div(b18 = 'selected-indexes'),
                        dcc.Graph(b18 = 'graph-outlier')
                    ],
                    b21 = "six b24"
                ),
            ],
            b21 = "row"
        ),
        html.Hr(),
        html.H1(
            b16 = {'textAlign': 'center', 'font': 'bold 35px Castellar, serif', 'padding': '20px 0px 0px 0px'},
            b17 = 'Pump and Dump Analysis'
        ),
        html.Div(
            b16 = {'font-size': '15px'},
            b17 = [
                'Click on the below link to go to the pump and dump webpage'
            ]
        ),
        html.Div(
            b16 = {'font-size': '20px'},
            b17 = html.A(
                b26 = "https:
                b27 = "_blank",
                b17 = "Click here"
            )
        ),
        html.Div(
            b16 = {'width': '95%', 'b60': '1% 2.5% 1% 2.5%', 'borderRadius': '10px', 'opacity': '1'},
            b17 = html.Div(b18='output')
        ),
    ]
)
@b13.callback(
    Output('about', 'b17'),
    [Input('cryptos', 'b20')]
)
def fonk2(b20):
    b28 = 'https:
    b29 = b20
    if b29 = = "Ripple":
        b29 = "Ripple_(payment_protocol)"
    elif b29 = = "EOS":
        b29 = "EOS.IO"
    elif b29 = = "Monero":
        b29 = "Monero_(cryptocurrency)"
    b30 = b28 + b29
    b7 = b6.extract(url=b30)
    b31 = b7.cleaned_text.split("\n")
    b32 = fonk1(b31[0] + b31[2])
    return b32
@b13.callback(
    Output('price', 'b17'),
    [Input('cryptos', 'b20')]
)
def fonk3(b20):
    b33 = b20
    b34 = b7"SELECT quote, time FROM CryptoNews.Value WHERE currency_name LIKE '{b33}'"
    b35 = pd.read_sql(b34, b1)
    b36 = b35['time'].tolist()
    b37 = b35['quote'].tolist()
    b38 = [sum(b37[b9:b9 + 7]) / 7 for b9 in range(len(b37) - 7)]
    b39 = [b36[b9 + 7] for b9 in range(len(b37) - 7)]
    b40 = [sum(b37[b9:b9 + 30]) / 30 for b9 in range(len(b37) - 30)]
    b41 = [b36[b9 + 30] for b9 in range(len(b37) - 30)]
    b42 = ((b37[-1] - b37[-8]) / b37[-8]) * 100
    b43 = ((b37[-1] - b37[-31]) / b37[-31]) * 100
    b44 = b37[-1]
    b45 = b38[-1]
    b46 = b40[-1]
    b47 = html.Div(
        b17 = [
            dcc.Graph(
                b18 = 'price_chart',
                b22 = {
                    'b23': [
                        {'b47': b36, 'b37': b37, 'type': 'line', 'name': 'Price', 'mode': 'lines+markers'},
                        {'b47': b39, 'b37': b38, 'type': 'line', 'name': '7 Day Moving Average', 'mode': 'lines'},
                        {'b47': b41, 'b37': b40, 'type': 'line', 'name': '30 Day Moving Average', 'mode': 'lines'}
                    ],
                    'b15': {
                        'b57': b7'{b33} price',
                    }
                }
            )
        ]
    )
    return b47
@b13.callback(
    Output('price_facts', 'b17'),
    [Input('price', 'b17')]
)
def fonk4(b20):
    b48 = html.Table([
        html.Tr([html.Td("Current Price"), html.Td(round(b44, 2))]),
        html.Tr([html.Td("Past 7 days Average"), html.Td(round(b45, 2))]),
        html.Tr([html.Td("Past 30 days Average"), html.Td(round(b46, 2))]),
        html.Tr([html.Td("Past 7 days % Change"), html.Td(round(b42, 2))]),
        html.Tr([html.Td("Past 30 days % Change"), html.Td(round(b43, 2))])
    ])
    return b48
@b13.callback(
    Output('rel_domains', 'b17'),
    [Input('cryptos', 'b20')]
)
def fonk5(b20):
    b31 = b20
    b7 = b7"dom_{b31}.csv"
    with open(b7) as file:
        b49 = csv.reader(file, delimiter=',')
        b50 = sorted(b49, key=lambda b47: int(b47[1]), reverse=True)
        b51 = list(b50)
        b52 = [b7"http:
        b53 = html.Table([
            html.Tr([html.Td(html.A(b26 = b52[0], b27="_blank", b17=b51[0][0]))]),
            html.Tr([html.Td(html.A(b26 = b52[1], b27="_blank", b17=b51[1][0]))]),
            html.Tr([html.Td(html.A(b26 = b52[2], b27="_blank", b17=b51[2][0]))]),
            html.Tr([html.Td(html.A(b26 = b52[3], b27="_blank", b17=b51[3][0]))]),
            html.Tr([html.Td(html.A(b26 = b52[4], b27="_blank", b17=b51[4][0]))]),
        ])
    return b53
@b13.callback(
    Output('graph-outlier', 'b22'),
    [Input('outlier', 'b23'), Input('outlier', 'selected_rows')]
)
def fonk6(rows, selected_rows):
    b54 = pd.DataFrame(rows)
    b55 = {'color': ['
    for b9 in (selected_rows or []):
        b55['color'][b9] = '
    b56 = go.Figure(
        b23 = [
            go.Bar(b47 = b54['Crypto Currency'], b37=b54['Opposite Trend %'], b55=b55, name='Opposite Trends'),
            go.Bar(b47 = b54['Crypto Currency'], b37=b54['Mean Square Error'], b55=b55, name='Mean Square Error', b61='y2'),
            go.Bar(b47 = b54['Crypto Currency'], b37=b54['Volatility'], b55=b55, name='Volatility', b61='y3')
        ],
        b15 = go.Layout(
            b57 = 'Outlier Analysis',
            b58 = False,
            b59 = 800,
            b60 = {'l': 40, 'r': 10, 't': 60, 'b': 200},
            b61 = {'b57': 'Opposite Trend %'},
            b62 = {'b57': 'Mean Square Error', 'overlaying': 'b37', 'side': 'right', 'type': 'log'},
            b63 = {'b57': 'Volatility', 'overlaying': 'b37', 'side': 'right', 'type': 'log'}
        )
    )
    return b56
if b64 = = '__main__':
    b13.run_server(b65 = True)