import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import mysql.connector
from goose3 import Goose
from b1 import Market
import dash_table_experiments as dte
from dash.dependencies import Input, Output, State
import re
import csv
b1 = Market()
b2 = b1.ticker(start=0, limit=10)
b3 = [i["b21"] for i in b2]
b4 = [i["market_cap_usd"] for i in b2]
b5 = b1.stats()
b6 = b5["bitcoin_percentage_of_market_cap"]
b7 = b1.ticker('bitcoin')
b8 = b7[0]["market_cap_usd"]
b9 = [(float(mcap) * float(b6)) / float(b8) for mcap in b4]
b3.append("Others")
b9.append(100 - sum(b9))
b10 = Goose()
def fonk1(text):
    return re.sub(r'\[.*?\]', '', text)
def fonk2(values):
    return [((values[i] - values[i - 1]) / values[i - 1]) * 100 for i in range(-1, -100, -1)]
b11 = mysql.connector.connect(user='student', password='cs336student',
                              b12 = 'cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
                              b13 = 'CryptoNews')
b14 = pd.read_csv("outlier.csv")
b14.sort_values(b15 = ['Outlier Score'], inplace=True)
b14 = b14.iloc[61:161, :]
b16 = dash.Dash()
b17 = b16.b17
b16.config['suppress_callback_exceptions'] = True
b16.b18 = html.Div(b20={
    'backgroundImage': 'b34("http:
    'width': '96%', 'b60': '0% 0% 0% 2%', 'borderRadius': '10px'
}, b19 = [
    html.H1('Crypto Analysis', b20 = {'textAlign': 'center', 'font': 'bold 35px Castellar, serif', 'padding': '20px 0px 0px 0px'}),
    html.Label('Select a currency:', b20 = {'b60': '0% 0% 0% 1%', 'font': '20px Britannic, serif'}),
    html.Br(),
    html.Div(b20 = {'width': '20%', 'font-size': '20px', 'b60': '0% 0% 0% 1%'}, b19=[
        dcc.Dropdown(
            b21 = 'cryptos',
            b22 = [{'label': crypto.capitalize(), 'b23': crypto.capitalize()} for crypto in b3],
            b23 = 'Bitcoin'
        )
    ]),
    html.Hr(),
    html.Div(b20 = {'b60': '0% 0% 0% 1%'}, b19=[
        html.Div([
            html.H4('Price Chart', b20 = {'font-weight': 'bold', 'border': '2px solid black'}),
            html.Div(b21 = 'price', b19=[])
        ], b24 = "six columns"),
        html.Div([
            html.Div(b20 = {'width': '20%', 'b60': '0% 0% 0% 2%'}, b19=[
                html.H4('Facts', b20 = {'font-weight': 'bold', 'border': '2px solid black'}),
                html.Div(b21 = 'price_facts', b20={'font-size': '15px', 'text-align': 'justify'})
            ], b24 = "six columns"),
            html.Div(b20 = {'width': '26%', 'b60': '0% 0% 0% 2%'}, b19=[
                html.H4('About', b20 = {'font-weight': 'bold', 'border': '2px solid black'}),
                html.Div(b21 = 'about', b20={'font-size': '15px', 'text-align': 'justify', 'b59': '400px', 'overflow': 'scroll'})
            ], b24 = "six columns")
        ], b24 = "row"),
    ]),
    html.Hr(),
    html.Div([
        html.Div(b20 = {'width': '47%', 'b60': '0% 0% 0% 2%'}, b19=[
            html.H4('Relevant Domains', b20 = {'font-weight': 'bold', 'border': '2px solid black'}),
            html.Div(b21 = 'rel_domains', b20={'font-size': '15px'})
        ], b24 = "six columns"),
        html.Div(b20 = {'width': '47%', 'b60': '0% 0% 0% 2%'}, b19=[
            html.H4('Market Cap Distribution', b20 = {'font-weight': 'bold', 'border': '2px solid black'}),
            dcc.Graph(
                b21 = 'pi',
                b25 = {
                    'data': [{'values': b9, 'labels': b3, 'type': 'pie'}],
                    'b18': {'b57': "Market Cap Distribution"}
                }
            )
        ], b24 = "six columns")
    ], b24 = "row"),
    html.Hr(),
    html.H1('Outlier Analysis', b20 = {'textAlign': 'center', 'font': 'bold 35px Castellar, serif', 'padding': '20px 0px 0px 0px'}),
    html.Div([
        html.Div(b20 = {'b60': '0% 0% 0% 1%', 'width': '45%'}, b19=[
            html.H4('Outlier Feature Calculation', b20 = {'font-weight': 'bold', 'border': '2px solid black'}),
            dte.DataTable(
                b26 = b14.to_dict('records'),
                b27 = True,
                b28 = True,
                b29 = True,
                b30 = [],
                b21 = 'outlier'
            ),
            html.Div(b19 = ['*All calculations are with respect to Bitcoin.']),
            html.Div(b20 = {'font-size': '15px'}, b19=[
                'This is an interactive table. You can sort, search, and filter using any column in the table. The adjacent graphs will update accordingly.'
            ])
        ], b24 = "six columns"),
        html.Div([
            html.Div(b21 = 'selected-indexes'),
            dcc.Graph(b21 = 'graph-outlier')
        ], b24 = "six columns")
    ], b24 = "row"),
    html.Hr(),
    html.H1('Pump and Dump Analysis', b20 = {'textAlign': 'center', 'font': 'bold 35px Castellar, serif', 'padding': '20px 0px 0px 0px'}),
    html.Div('Click on the below link to go to the pump and dump webpage', b20 = {'font-size': '15px'}),
    html.Div(html.A(b31 = "https:
    html.Div(b21 = 'output', b20={'width': '95%', 'b60': '1% 2.5% 1% 2.5%', 'borderRadius': '10px', 'opacity': '1'})
])
@b16.callback(
    Output('about', 'b19'),
    [Input('cryptos', 'b23')]
)
def fonk3(crypto_name):
    b32 = 'https:
    b33 = {
        "Ripple": "Ripple_(payment_protocol)",
        "EOS": "EOS.IO",
        "Monero": "Monero_(cryptocurrency)"
    }
    b34 = b32 + b33.get(crypto_name, crypto_name)
    b35 = b10.extract(b34=b34)
    b36 = b35.b36.split("\n")
    b37 = fonk1(b36[0] + b36[2])
    return b37
@b16.callback(
    Output('price', 'b19'),
    [Input('cryptos', 'b23')]
)
def fonk4(crypto_name):
    b38 = f"SELECT quote, time FROM CryptoNews.Value WHERE currency_name LIKE '{crypto_name}'"
    b39 = pd.read_sql(b38, b11)
    b40 = b39['time'].tolist()
    b41 = b39['quote'].tolist()
    b42 = [sum(b41[i:i+7]) / 7 for i in range(len(b41) - 7)]
    b43 = [sum(b41[i:i+30]) / 30 for i in range(len(b41) - 30)]
    global b44, b45, b46, b47, b48
    b44 = b41[-1]
    b45 = b42[-1]
    b46 = b43[-1]
    b47 = ((b41[-1] - b41[-8]) / b41[-8]) * 100
    b48 = ((b41[-1] - b41[-31]) / b41[-31]) * 100
    return dcc.Graph(
        b21 = 'price_chart',
        b25 = {
            'data': [
                {'b56': b40, 'y': b41, 'type': 'line', 'name': 'Price', 'mode': 'lines+markers'},
                {'b56': b40[7:], 'y': b42, 'type': 'line', 'name': '7 Day Moving Average', 'mode': 'lines'},
                {'b56': b40[30:], 'y': b43, 'type': 'line', 'name': '30 Day Moving Average', 'mode': 'lines'}
            ],
            'b18': {'b57': f'{crypto_name} Price'}
        }
    )
@b16.callback(
    Output('price_facts', 'b19'),
    [Input('price', 'b19')]
)
def fonk5(_):
    return html.Table([
        html.Tr([html.Td("Current Price"), html.Td(round(b44, 2))]),
        html.Tr([html.Td("Past 7 Days Average"), html.Td(round(b45, 2))]),
        html.Tr([html.Td("Past 30 Days Average"), html.Td(round(b46, 2))]),
        html.Tr([html.Td("Past 7 Days % Change"), html.Td(round(b47, 2))]),
        html.Tr([html.Td("Past 30 Days % Change"), html.Td(round(b48, 2))])
    ])
@b16.callback(
    Output('rel_domains', 'b19'),
    [Input('cryptos', 'b23')]
)
def fonk6(crypto_name):
    b49 = f"dom_{crypto_name}.csv"
    with open(b49) as f:
        b50 = csv.b50(f)
        b51 = sorted(b50, key=lambda b56: int(b56[1]), reverse=True)
    b52 = ["http:
    return html.Table([
        html.Tr([html.Td(html.A(b31 = link, target="_blank", b19=domain[0]))]) for link, domain in zip(b52, b51)
    ])
@b16.callback(
    Output('outlier', 'b30'),
    [Input('graph-outlier', 'clickData')],
    [State('outlier', 'b30')]
)
def fonk7(click_data, b30):
    if click_data:
        for point in click_data['points']:
            if point['pointNumber'] in b30:
                b30.remove(point['pointNumber'])
            else:
                b30.append(point['pointNumber'])
    return b30
@b16.callback(
    Output('graph-outlier', 'b25'),
    [Input('outlier', 'b26'), Input('outlier', 'b30')]
)
def fonk8(b26, b30):
    b53 = pd.DataFrame(b26)
    b54 = go.Figure()
    b55 = {'color': ['
    for i in b30 or []:
        b55['color'][i] = '
    b54.add_trace(go.Bar(b56 = b53['Crypto Currency'], y=b53['Opposite Trend %'], b55=b55, name='Opposite Trends'))
    b54.add_trace(go.Bar(b56 = b53['Crypto Currency'], y=b53['Mean Square Error'], b55=b55, name='Mean Square Error'))
    b54.add_trace(go.Bar(b56 = b53['Crypto Currency'], y=b53['Volatility'], b55=b55, name='Volatility'))
    b54.update_layout(
        b57 = 'Outlier Analysis',
        b58 = False,
        b59 = 800,
        b60 = dict(l=40, r=10, t=60, b=200),
        b61 = dict(type='log'),
        b62 = dict(type='log')
    )
    return b54
b16.css.append_css({"external_url": "https:
b16.css.append_css({'external_url': 'https:
if b63 = = '__main__':
    b16.run_server(b64 = True)