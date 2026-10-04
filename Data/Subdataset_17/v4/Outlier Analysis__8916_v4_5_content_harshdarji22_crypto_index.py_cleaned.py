import dash
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import mysql.connector
from goose3 import Goose
from coinmarketcap import Market
import dash_table_experiments as dte
from dash.dependencies import Input, Output, State
import csv
coinmarketcap = Market()
stat = coinmarketcap.ticker(start=0, limit=10)
crypto_names = [i["id"] for i in stat]
crypto_market_caps = [i["market_cap_usd"] for i in stat]
market_stats = coinmarketcap.stats()
bitcoin_percentage = market_stats["bitcoin_percentage_of_market_cap"]
bitcoin_data = coinmarketcap.ticker('bitcoin')
bitcoin_market_cap = bitcoin_data[0]["market_cap_usd"]
market_caps_percentage = [(float(mcap) * float(bitcoin_percentage)) / float(bitcoin_market_cap) for mcap in crypto_market_caps]
crypto_names.append("Others")
market_caps_percentage.append(100 - sum(market_caps_percentage))
g = Goose()
def remove_brackets(text):
    return re.sub(r'\[.*?\]', '', text)
def get_changes(values):
    return [((values[i] - values[i - 1]) / values[i - 1]) * 100 for i in range(-1, -100, -1)]
cnx = mysql.connector.connect(user='student', password='cs336student',
                              host='cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
                              database='CryptoNews')
outlier_df = pd.read_csv("outlier.csv")
outlier_df.sort_values(by=['Outlier Score'], inplace=True)
outlier_df = outlier_df.iloc[61:161, :]
app = dash.Dash()
server = app.server
app.config['suppress_callback_exceptions'] = True
app.layout = html.Div(style={
    'backgroundImage': 'url("http:
    'width': '96%', 'margin': '0% 0% 0% 2%', 'borderRadius': '10px'
}, children=[
    html.H1('Crypto Analysis', style={'textAlign': 'center', 'font': 'bold 35px Castellar, serif', 'padding': '20px 0px 0px 0px'}),
    html.Label('Select a currency:', style={'margin': '0% 0% 0% 1%', 'font': '20px Britannic, serif'}),
    html.Br(),
    html.Div(style={'width': '20%', 'font-size': '20px', 'margin': '0% 0% 0% 1%'}, children=[
        dcc.Dropdown(
            id='cryptos',
            options=[{'label': crypto.capitalize(), 'value': crypto.capitalize()} for crypto in crypto_names],
            value='Bitcoin'
        )
    ]),
    html.Hr(),
    html.Div(style={'margin': '0% 0% 0% 1%'}, children=[
        html.Div([
            html.H4('Price Chart', style={'font-weight': 'bold', 'border': '2px solid black'}),
            html.Div(id='price', children=[])
        ], className="six columns"),
        html.Div([
            html.Div(style={'width': '20%', 'margin': '0% 0% 0% 2%'}, children=[
                html.H4('Facts', style={'font-weight': 'bold', 'border': '2px solid black'}),
                html.Div(id='price_facts', style={'font-size': '15px', 'text-align': 'justify'})
            ], className="six columns"),
            html.Div(style={'width': '26%', 'margin': '0% 0% 0% 2%'}, children=[
                html.H4('About', style={'font-weight': 'bold', 'border': '2px solid black'}),
                html.Div(id='about', style={'font-size': '15px', 'text-align': 'justify', 'height': '400px', 'overflow': 'scroll'})
            ], className="six columns")
        ], className="row"),
    ]),
    html.Hr(),
    html.Div([
        html.Div(style={'width': '47%', 'margin': '0% 0% 0% 2%'}, children=[
            html.H4('Relevant Domains', style={'font-weight': 'bold', 'border': '2px solid black'}),
            html.Div(id='rel_domains', style={'font-size': '15px'})
        ], className="six columns"),
        html.Div(style={'width': '47%', 'margin': '0% 0% 0% 2%'}, children=[
            html.H4('Market Cap Distribution', style={'font-weight': 'bold', 'border': '2px solid black'}),
            dcc.Graph(
                id='pi',
                figure={
                    'data': [{'values': market_caps_percentage, 'labels': crypto_names, 'type': 'pie'}],
                    'layout': {'title': "Market Cap Distribution"}
                }
            )
        ], className="six columns")
    ], className="row"),
    html.Hr(),
    html.H1('Outlier Analysis', style={'textAlign': 'center', 'font': 'bold 35px Castellar, serif', 'padding': '20px 0px 0px 0px'}),
    html.Div([
        html.Div(style={'margin': '0% 0% 0% 1%', 'width': '45%'}, children=[
            html.H4('Outlier Feature Calculation', style={'font-weight': 'bold', 'border': '2px solid black'}),
            dte.DataTable(
                rows=outlier_df.to_dict('records'),
                row_selectable=True,
                filterable=True,
                sortable=True,
                selected_row_indices=[],
                id='outlier'
            ),
            html.Div(children=['*All calculations are with respect to Bitcoin.']),
            html.Div(style={'font-size': '15px'}, children=[
                'This is an interactive table. You can sort, search, and filter using any column in the table. The adjacent graphs will update accordingly.'
            ])
        ], className="six columns"),
        html.Div([
            html.Div(id='selected-indexes'),
            dcc.Graph(id='graph-outlier')
        ], className="six columns")
    ], className="row"),
    html.Hr(),
    html.H1('Pump and Dump Analysis', style={'textAlign': 'center', 'font': 'bold 35px Castellar, serif', 'padding': '20px 0px 0px 0px'}),
    html.Div('Click on the below link to go to the pump and dump webpage', style={'font-size': '15px'}),
    html.Div(html.A(href="https:
    html.Div(id='output', style={'width': '95%', 'margin': '1% 2.5% 1% 2.5%', 'borderRadius': '10px', 'opacity': '1'})
])
@app.callback(
    Output('about', 'children'),
    [Input('cryptos', 'value')]
)
def update_about_section(crypto_name):
    BASE_URL = 'https:
    if crypto_name == "Ripple":
        crypto_name = "Ripple_(payment_protocol)"
    elif crypto_name == "EOS":
        crypto_name = "EOS.IO"
    elif crypto_name == "Monero":
        crypto_name = "Monero_(cryptocurrency)"
    url = BASE_URL + crypto_name
    article = g.extract(url=url)
    cleaned_text = article.cleaned_text.split("\n")
    summary = remove_brackets(cleaned_text[0] + cleaned_text[2])
    return summary
@app.callback(
    Output('price', 'children'),
    [Input('cryptos', 'value')]
)
def update_price_chart(crypto_name):
    query = f"SELECT quote, time FROM CryptoNews.Value WHERE currency_name LIKE '{crypto_name}'"
    hist = pd.read_sql(query, cnx)
    dates = hist['time'].tolist()
    prices = hist['quote'].tolist()
    moving_avg_7 = [sum(prices[i:i+7])/7 for i in range(len(prices)-7)]
    moving_avg_30 = [sum(prices[i:i+30])/30 for i in range(len(prices)-30)]
    global curr_price, curr_7_avg, curr_30_avg, change_7, change_30
    curr_price = prices[-1]
    curr_7_avg = moving_avg_7[-1]
    curr_30_avg = moving_avg_30[-1]
    change_7 = ((prices[-1] - prices[-8]) / prices[-8]) * 100
    change_30 = ((prices[-1] - prices[-31]) / prices[-31]) * 100
    return dcc.Graph(
        id='price_chart',
        figure={
            'data': [
                {'x': dates, 'y': prices, 'type': 'line', 'name': 'Price', 'mode': 'lines+markers'},
                {'x': dates[7:], 'y': moving_avg_7, 'type': 'line', 'name': '7 Day Moving Average', 'mode': 'lines'},
                {'x': dates[30:], 'y': moving_avg_30, 'type': 'line', 'name': '30 Day Moving Average', 'mode': 'lines'}
            ],
            'layout': {'title': f'{crypto_name} Price'}
        }
    )
@app.callback(
    Output('price_facts', 'children'),
    [Input('price', 'children')]
)
def update_price_facts(_):
    return html.Table([
        html.Tr([html.Td("Current Price"), html.Td(round(curr_price, 2))]),
        html.Tr([html.Td("Past 7 Days Average"), html.Td(round(curr_7_avg, 2))]),
        html.Tr([html.Td("Past 30 Days Average"), html.Td(round(curr_30_avg, 2))]),
        html.Tr([html.Td("Past 7 Days % Change"), html.Td(round(change_7, 2))]),
        html.Tr([html.Td("Past 30 Days % Change"), html.Td(round(change_30, 2))])
    ])
@app.callback(
    Output('rel_domains', 'children'),
    [Input('cryptos', 'value')]
)
def update_relevant_domains(crypto_name):
    file_name = f"dom_{crypto_name}.csv"
    with open(file_name) as f:
        reader = csv.reader(f)
        domains = sorted(reader, key=lambda x: int(x[1]), reverse=True)
    domain_links = ["http:
    return html.Table([
        html.Tr([html.Td(html.A(href=link, target="_blank", children=domain[0]))]) for link, domain in zip(domain_links, domains)
    ])
@app.callback(
    Output('outlier', 'selected_row_indices'),
    [Input('graph-outlier', 'clickData')],
    [State('outlier', 'selected_row_indices')]
)
def update_selected_row_indices(click_data, selected_row_indices):
    if click_data:
        for point in click_data['points']:
            if point['pointNumber'] in selected_row_indices:
                selected_row_indices.remove(point['pointNumber'])
            else:
                selected_row_indices.append(point['pointNumber'])
    return selected_row_indices
@app.callback(
    Output('graph-outlier', 'figure'),
    [Input('outlier', 'rows'), Input('outlier', 'selected_row_indices')]
)
def update_outlier_graph(rows, selected_row_indices):
    dff = pd.DataFrame(rows)
    fig = plotly.tools.make_subplots(
        rows=3, cols=1,
        subplot_titles=('Opposite Trends', 'Mean Square Error', 'Volatility'),
        shared_xaxes=True
    )
    marker = {'color': ['
    for i in selected_row_indices or []:
        marker['color'][i] = '
    fig.append_trace({
        'x': dff['Crypto Currency'],
        'y': dff['Opposite Trend %'],
        'type': 'bar',
        'marker': marker
    }, 1, 1)
    fig.append_trace({
        'x': dff['Crypto Currency'],
        'y': dff['Mean Square Error'],
        'type': 'bar',
        'marker': marker
    }, 2, 1)
    fig.append_trace({
        'x': dff['Crypto Currency'],
        'y': dff['Volatility'],
        'type': 'bar',
        'marker': marker
    }, 3, 1)
    fig['layout']['showlegend'] = False
    fig['layout']['height'] = 800
    fig['layout']['margin'] = {'l': 40, 'r': 10, 't': 60, 'b': 200}
    fig['layout']['yaxis2']['type'] = 'log'
    fig['layout']['yaxis3']['type'] = 'log'
    return fig
app.css.append_css({"external_url": "https:
app.css.append_css({'external_url': 'https:
if __name__ == '__main__':
    app.run_server(debug=True)