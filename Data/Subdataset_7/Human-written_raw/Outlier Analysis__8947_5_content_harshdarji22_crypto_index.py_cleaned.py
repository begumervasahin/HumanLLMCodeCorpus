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
import re
import dash_table_experiments as dte
from dash.dependencies import Input, Output, State
import plotly
import urllib.request
from bs4 import BeautifulSoup
from goose3 import Goose
from b1 import Market
b1 = Market()
b2 = b1.ticker(start=0, limit=10)
b3 = []
b4 = []
b5 = []
for b13 in b2:
	b4.append(b13["b25"])
	b3.append(b13["market_cap_usd"])
b6 = b1.stats()
b7 = b6["bitcoin_percentage_of_market_cap"]
b8 = b1.ticker('bitcoin')
b9 = b8[0]["market_cap_usd"]
for a6 in range(len(b3)):
	b5.append((float(b3[a6])*float(b7))/float(b9))
b4.append("Others")
b5.append(100-sum(b5))
b10 = Goose()
def fonk1(b40):
	b11 = False
	b12 = ""
	for b13 in b40:
		if(b13 = ='['):
			b11 = True
			continue
		if(b13 = =']'):
			b11 = False
			continue
		if(b11):
			continue
		b12 = b12+b13
	return b12
def fonk2(v):
	b14 = []
	for b13 in range(-1,-100,-1):
		b14.append(((v[b13]-v[b13-1])/v[b13-1])*100)
	return b14
a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
b15 = pd.read_csv("outlier.csv")
b15.sort_values(b16 = ['Outlier Score'])
b17 = b15.iloc[61:161,:]
b18 = mysql.connector.connect(user='student', password='cs336student',
                              b19 = 'cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
                              b20 = 'CryptoNews')
def fonk3(elem):
	return elem[5]
def fonk4(elem):
    return int(elem[1])
b21 = dash.Dash()
b22 = b21.b22
b21.config['suppress_callback_exceptions']=True
b21.b23 = html.Div(b24={'backgroundImage':'url("http:
    html.H1(b24 = {'textAlign':'center','font':'bold 35px Castellar, serif','padding':'20px 0px 0px 0px'} ,b35='Crypto Analysis'),
	html.Label(b24 = {'margin': '0% 0% 0% 1%','font':'20px Britannic, serif'},b35='Select a currency:'),
	html.Br(),
	html.Div(b24 = {'width':'20%','font-size':'20px','margin':'0% 0% 0% 1%'},b35=dcc.Dropdown(
		b25 = 'cryptos',
		b26 = [{'label':'Bitcoin', 'b27':'Bitcoin',},
		{'label':'Ethereum', 'b27':'Ethereum'},
		{'label':'Ripple', 'b27':'Ripple',},
		{'label':'Litecoin', 'b27':'Litecoin'},
		{'label':'Monero', 'b27':'Monero'}],
		b27 = 'Bitcoin'
	)),
	html.Hr(),
	html.Div(b24 = {'margin':'0% 0% 0% 1%'},b35=[
        html.Div([
            html.H4(b24 = {'font-weight':'bold','border': '2px solid black',},b35='Price Chart'),
            html.Div(b25 = 'price',b35=[])
        ], b28 = "six columns"),
        html.Div([html.Div(b24 = {'width':'20%','margin':'0% 0% 0% 2%'} ,b35=[
            html.H4(b24 = {'font-weight':'bold','border': '2px solid black'},b35='Facts'),
            html.Div(b24 = {'font-size':'15px','text-align': 'justify'},b25='price_facts')
        ], b28 = "six columns"),
        html.Div(b24 = {'width':'26%','margin':'0% 0% 0% 2%'},b35=[
            html.H4(b24 = {'font-weight':'bold','border': '2px solid black',},b35='About'),
            html.Div(b24 = {'font-size':'15px','text-align': 'justify','height':'400px','overflow':'scroll'},b25='about')
        ], b28 = "six columns"),
    ], b28 = "row"),
    ], b28 = "row"),
	html.Hr(),
	html.Div([
        html.Div(b24 = {'width':'47%','margin':'0% 0% 0% 2%'} ,b35=[
            html.H4(b24 = {'font-weight':'bold','border': '2px solid black'},b35='Relevent Domains'),
            html.Div(b24 = {'font-size':'15px',},b25='rel_domains')
        ], b28 = "six columns"),
		html.Div(b24 = {'width':'47%','margin':'0% 0% 0% 2%'} ,b35=[
            html.H4(b24 = {'font-weight':'bold','border': '2px solid black'},b35='Market Cap Distribution'),
            dcc.Graph(
				b25 = 'pi',
				b29 = {
					'data': [
						{'values': b5, 'labels':b4 , 'type': 'pie'},
					],
					'b23': {
						'title': "Market Cap Distribution",
					}
				}
			)
        ], b28 = "six columns"),
    ], b28 = "row"),
	html.Hr(),
	html.H1(b24 = {'textAlign':'center','font':'bold 35px Castellar, serif','padding':'20px 0px 0px 0px'} ,b35='Outlier Analysis'),
	html.Div([
    		html.Div(b24 = {'margin':'0% 0% 0% 1%','width':'45%'},b35 = [
			html.H4(b24 = {'font-weight':'bold','border': '2px solid black'},b35='Outlier Feature Calculation'),
			dte.DataTable(
			b30 = b17.to_dict('records'),
			b31 = True,
			b32 = True,
			b33 = True,
			b34 = [],
			b25 = 'outlier'
		),
		html.Div(b35 = ['''
		*All calculations are with respect to Bitcoin.
		''']),
		html.Div(b24 = {'font-size':'15px',},b35=['''
		This is a interactive table. You can sort, search and filter using any column in the table. The adjacent graphs will update accordingly.
		''']),],b28 = "six columns"),
		html.Div([html.Div(b25 = 'selected-indexes'),
		dcc.Graph(
			b25 = 'graph-outlier'
		)],b28 = "six columns"),
	], b28 = "row"),
	html.Hr(),
	html.H1(b24 = {'textAlign':'center','font':'bold 35px Castellar, serif','padding':'20px 0px 0px 0px'} ,b35='Pump and Dump Analysis'),
	html.Div(b24 = {'font-size':'15px',},b35=['''
		Click on the below link to go to the pump and dump webpage
		''']),
	html.Div(b24 = {'font-size':'20px'},b35=html.A(b55="https:
	html.Div(b24 = {'width':'95%','margin':'1% 2.5% 1% 2.5%','borderRadius':'10px','opacity':'1'}, b35=html.Div(b25='output')),
])
@b21.callback(
    dash.dependencies.Output('about', 'b35'),
    [dash.dependencies.Input('cryptos', 'b27')])
def fonk5(b27):
	b36 = 'https:
	b37 = '{}'.format(b27)
	if b37 = ="Ripple":
		b37 = "Ripple_(payment_protocol)"
	if b37 = ="EOS":
		b37 = "EOS.IO"
	if b37 = ="Monero":
		b37 = "Monero_(cryptocurrency)"
	b38 = b36 + b37
	b11 = b10.extract(url = b38)
	b39 = b11.cleaned_text.split("\n")
	b40 = fonk1(b39[0]+b39[2])
	return b40
@b21.callback(
    dash.dependencies.Output('price', 'b35'),
    [dash.dependencies.Input('cryptos', 'b27')])
def fonk6(b27):
	b41 = '{}'.format(b27)
	b42 = pd.read_sql("select quote, time from CryptoNews.Value where currency_name like '"+b41+"'",b18)
	b43 = b42.iloc[:,1].tolist()
	b44 = b42.iloc[:,0].tolist()
	b45 = []
	b46 = []
	for b13 in range(0,len(b44)-7):
		b46.append(b43[b13+7])
		b47 = sum(b44[b13:b13+7])/7
		b45.append(b47)
	b48 = []
	b49 = []
	global a4
	a4 = ((b44[-1]-b44[-8])/b44[-8])*100
	global a5
	a5 = ((b44[-1]-b44[-31])/b44[-31])*100
	global a1
	a1 = b44[-1]
	global a2
	a2 = b45[-1]
	for b13 in range(0,len(b44)-30):
		b49.append(b43[b13+30])
		b47 = sum(b44[b13:b13+30])/30
		b48.append(b47)
	global a3
	a3 = b48[-1]
	b50 = html.Div(b35=[dcc.Graph(
				b25 = 'pi',
				b29 = {
					'data': [
						{'b50': b43 , 'b44': b44, 'type': 'line', 'name': 'Price','mode':'lines+markers'},
						{'b50': b46 , 'b44': b45, 'type': 'line', 'name': '7 Day moving Average','mode':'lines'},
						{'b50': b49 , 'b44': b48, 'type': 'line', 'name': '30 Day moving Average','mode':'lines'}
					],
					'b23': {
						'title': b41+' price',
					}
				}
			)])
	return b50
@b21.callback(
    dash.dependencies.Output('price_facts', 'b35'),
    [dash.dependencies.Input('price', 'b35')])
def fonk7(b27):
	b50 = html.Table(
		[
			html.Tr( [html.Td("Current Price"), html.Td(round(a1,2))] ),
			html.Tr( [html.Td("Past 7 days Average"), html.Td(round(a2,2))] ),
			html.Tr( [html.Td("Past 30 days Average"), html.Td(round(a3,2))] ),
			html.Tr( [html.Td("Past 7 days % Change"), html.Td(round(a4,2))] ),
			html.Tr( [html.Td("Past 30 days % Change"), html.Td(round(a5,2))] )
		]
)
	return b50
import csv
@b21.callback(
    dash.dependencies.Output('rel_domains', 'b35'),
    [dash.dependencies.Input('cryptos', 'b27')])
def fonk8(b27):
	b39 = '{}'.format(b27)
	b11 = "dom_"+b39+".csv"
	b51 = csv.b59(open(b11),delimiter=',')
	b52 = sorted(b51, key=takeSecond, reverse = True)
	b53 = list(b52)
	b54 = []
	for b13 in b53:
		b54.append("http:
	b50 = html.Table(
		[
			html.Tr( [html.Td(html.A(b55 = b54[0],target = "_blank", b35 = b53[0][0]))]),
			html.Tr( [html.Td(html.A(b55 = b54[1],target = "_blank", b35 = b53[1][0]))]),
			html.Tr( [html.Td(html.A(b55 = b54[2],target = "_blank", b35 = b53[2][0]))]),
			html.Tr( [html.Td(html.A(b55 = b54[3],target = "_blank", b35 = b53[3][0]))]),
			html.Tr( [html.Td(html.A(b55 = b54[4],target = "_blank", b35 = b53[4][0]))]),
		]
)
	return b50
@b21.callback(
    dash.dependencies.Output('top_news', 'b35'),
    [dash.dependencies.Input('cryptos', 'b27')])
def fonk9(b27):
	b39 = '{}'.format(b27)
	b11 = "dom_"+b39+".csv"
	b51 = csv.b59(open(b11),delimiter=',')
	b56 = []
	b52 = sorted(b51, key=takeSecond, reverse = True)
	b53 = list(b52)
	print(len(b53))
	b13 = 0
	a6 = 0
	while(b13<5):
		b57 = b53[a6][0]
		print(b57)
		b58 = []
		a6 = a6+1
		try:
			b59 = csv.b59(open("output.csv"),delimiter=',')
			b60 = filter(lambda b43:b43[0]==b39, b59)
			b61 = filter(lambda b43:b43[4]=="Y", fil)
			print("before")
			b62 = sorted(b61, key=takeSixth, reverse = True)
			print("after")
			b58 = list(b62)
			b56.append(b58[0])
			print(b58[0][2])
			b13 = b13+1
		except:
			continue
	b50 = html.Table(
		[
			html.Tr( [html.Td(html.A(b55 = b56[0][1],target = "_blank", b35 = b56[0][2]))]),
			html.Tr( [html.Td(html.A(b55 = b56[1][1],target = "_blank", b35 = b56[1][2]))]),
			html.Tr( [html.Td(html.A(b55 = b56[2][1],target = "_blank", b35 = b56[2][2]))]),
			html.Tr( [html.Td(html.A(b55 = b56[3][1],target = "_blank", b35 = b56[3][2]))]),
			html.Tr( [html.Td(html.A(b55 = b56[4][1],target = "_blank", b35 = b56[4][2]))]),
		])
	return b50
@b21.callback(
    Output('outlier', 'b34'),
    [Input('graph-outlier', 'clickData')],
    [State('outlier', 'b34')])
def fonk10(clickData, b34):
    if clickData:
        for point in clickData['points']:
            if point['pointNumber'] in b34:
                b34.remove(point['pointNumber'])
            else:
                b34.append(point['pointNumber'])
    return b34
@b21.callback(
    Output('graph-outlier', 'b29'),
    [Input('outlier', 'b30'),
     Input('outlier', 'b34')])
def fonk11(b30, b34):
    b63 = pd.DataFrame(b30)
    b64 = plotly.tools.make_subplots(
        b30 = 3, cols=1,
        b65 = ('Opposite Trends', 'Mean Square Error','Volatility', ),
        b66 = True)
    b67 = {'color': ['
    for b13 in (b34 or []):
        b67['color'][b13] = '
    b64.append_trace({
        'b50': b63['Crypto Currency'],
        'b44': b63['Opposite Trend %'],
        'type': 'bar',
        'b67': b67
    }, 1, 1)
    b64.append_trace({
        'b50': b63['Crypto Currency'],
        'b44': b63['Mean Square Error'],
        'type': 'bar',
        'b67': b67
    }, 2, 1)
    b64.append_trace({
        'b50': b63['Crypto Currency'],
        'b44': b63['Volatility'],
        'type': 'bar',
        'b67': b67
    }, 3, 1)
    b64['b23']['showlegend'] = False
    b64['b23']['height'] = 800
    b64['b23']['margin'] = {
        'l': 40,
        'r': 10,
        't': 60,
        'b': 200
    }
    b64['b23']['yaxis2']['type'] = 'log'
    b64['b23']['yaxis3']['type'] = 'log'
    return b64
b21.css.append_css({"external_url": "https:
b21.css.append_css({
    'external_url': 'https:
})
if b68 = = '__main__':
    b21.run_server(b69 = True)