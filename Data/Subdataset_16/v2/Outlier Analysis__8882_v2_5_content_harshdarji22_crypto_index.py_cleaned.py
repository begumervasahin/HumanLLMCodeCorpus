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
b13 = dash.Dash(b63)
b14 = b13.b14
b13.config['suppress_callback_exceptions'] = True
b13.b15 = html.Div(
    b16 = {
        'backgroundImage': 'url("http:
        'width': '96%',
        'b59': '0% 0% 0% 2%',
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
            b16 = {'b59': '0% 0% 0% 1%', 'font': '20px Britannic, serif'},
            b17 = 'Select a currency:'
        ),
        html.Br(),
        html.Div(
            b16 = {'width': '20%', 'font-size': '20px', 'b59': '0% 0% 0% 1%'},
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
            b16 = {'b59': '0% 0% 0% 1%'},
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
                            b16 = {'width': '20%', 'b59': '0% 0% 0% 2%'},
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
                            b16 = {'width': '26%', 'b59': '0% 0% 0% 2%'},
                            b17 = [
                                html.H4(
                                    b16 = {'font-weight': 'bold', 'border': '2px solid black'},
                                    b17 = 'About'
                                ),
                                html.Div(
                                    b16 = {'font-size': '15px', 'text-align': 'justify', 'b58': '400px', 'overflow': 'scroll'},
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
                    b16 = {'width': '47%', 'b59': '0% 0% 0% 2%'},
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
                    b16 = {'width': '47%', 'b59': '0% 0% 0% 2%'},
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
                                    'b56': "Market Cap Distribution",
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
                    b16 = {'b59': '0% 0% 0% 1%', 'width': '45%'},
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
            b16 = {'width': '95%', 'b59': '1% 2.5% 1% 2.5%', 'borderRadius': '10px', 'opacity': '1'},
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
    if b29 = = "EOS":
        b29 = "EOS.IO"
    if b29 = = "Monero":
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
    b34 = pd.read_sql(b7"SELECT quote, time FROM CryptoNews.Value WHERE currency_name LIKE '{b33}'", b1)
    b35 = b34['time'].tolist()
    b36 = b34['quote'].tolist()
    b37 = [sum(b36[b9:b9 + 7]) / 7 for b9 in range(len(b36) - 7)]
    b38 = [b35[b9 + 7] for b9 in range(len(b36) - 7)]
    b39 = [sum(b36[b9:b9 + 30]) / 30 for b9 in range(len(b36) - 30)]
    b40 = [b35[b9 + 30] for b9 in range(len(b36) - 30)]
    b41 = ((b36[-1] - b36[-8]) / b36[-8]) * 100
    b42 = ((b36[-1] - b36[-31]) / b36[-31]) * 100
    b43 = b36[-1]
    b44 = b37[-1]
    b45 = b39[-1]
    b46 = html.Div(
        b17 = [
            dcc.Graph(
                b18 = 'price_chart',
                b22 = {
                    'b23': [
                        {'b46': b35, 'b36': b36, 'type': 'line', 'name': 'Price', 'mode': 'lines+markers'},
                        {'b46': b38, 'b36': b37, 'type': 'line', 'name': '7 Day Moving Average', 'mode': 'lines'},
                        {'b46': b40, 'b36': b39, 'type': 'line', 'name': '30 Day Moving Average', 'mode': 'lines'}
                    ],
                    'b15': {
                        'b56': b7'{b33} price',
                    }
                }
            )
        ]
    )
    return b46
@b13.callback(
    Output('price_facts', 'b17'),
    [Input('price', 'b17')]
)
def fonk4(b20):
    b47 = html.Table([
        html.Tr([html.Td("Current Price"), html.Td(round(b43, 2))]),
        html.Tr([html.Td("Past 7 days Average"), html.Td(round(b44, 2))]),
        html.Tr([html.Td("Past 30 days Average"), html.Td(round(b45, 2))]),
        html.Tr([html.Td("Past 7 days % Change"), html.Td(round(b41, 2))]),
        html.Tr([html.Td("Past 30 days % Change"), html.Td(round(b42, 2))])
    ])
    return b47
@b13.callback(
    Output('rel_domains', 'b17'),
    [Input('cryptos', 'b20')]
)
def fonk5(b20):
    b31 = b20
    b7 = b7"dom_{b31}.csv"
    b48 = csv.reader(open(b7), delimiter=',')
    b49 = sorted(b48, key=lambda b46: int(b46[1]), reverse=True)
    b50 = list(b49)
    b51 = [b7"http:
    b52 = html.Table([
        html.Tr([html.Td(html.A(b26 = b51[0], b27="_blank", b17=b50[0][0]))]),
        html.Tr([html.Td(html.A(b26 = b51[1], b27="_blank", b17=b50[1][0]))]),
        html.Tr([html.Td(html.A(b26 = b51[2], b27="_blank", b17=b50[2][0]))]),
        html.Tr([html.Td(html.A(b26 = b51[3], b27="_blank", b17=b50[3][0]))]),
        html.Tr([html.Td(html.A(b26 = b51[4], b27="_blank", b17=b50[4][0]))]),
    ])
    return b52
@b13.callback(
    Output('graph-outlier', 'b22'),
    [Input('outlier', 'b23'), Input('outlier', 'selected_rows')]
)
def fonk6(rows, selected_rows):
    b53 = pd.DataFrame(rows)
    b54 = {'color': ['
    for b9 in (selected_rows or []):
        b54['color'][b9] = '
    b55 = go.Figure(
        b23 = [
            go.Bar(b46 = b53['Crypto Currency'], b36=b53['Opposite Trend %'], b54=b54, name='Opposite Trends'),
            go.Bar(b46 = b53['Crypto Currency'], b36=b53['Mean Square Error'], b54=b54, name='Mean Square Error', b60='y2'),
            go.Bar(b46 = b53['Crypto Currency'], b36=b53['Volatility'], b54=b54, name='Volatility', b60='y3')
        ],
        b15 = go.Layout(
            b56 = 'Outlier Analysis',
            b57 = False,
            b58 = 800,
            b59 = {'l': 40, 'r': 10, 't': 60, 'b': 200},
            b60 = {'b56': 'Opposite Trend %'},
            b61 = {'b56': 'Mean Square Error', 'overlaying': 'b36', 'side': 'right', 'type': 'log'},
            b62 = {'b56': 'Volatility', 'overlaying': 'b36', 'side': 'right', 'type': 'log'}
        )
    )
    return b55
if b63 = = '__main__':
    b13.run_server(b64 = True)