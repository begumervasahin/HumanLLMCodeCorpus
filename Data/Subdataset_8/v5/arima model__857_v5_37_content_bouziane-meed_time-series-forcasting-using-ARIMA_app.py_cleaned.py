import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import statsmodels.api as sm
from dash.dependencies import Input, Output, State
app = dash.Dash(__name__)
external_stylesheets = ['https:
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
df = pd.read_excel("data/data.xlsx")
colors = {'background': '
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.Div([
        html.Img(src=app.get_asset_url('distr.png'), style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
        html.Div(children=[
            html.H1(children='Predictive analytics dashboards', style={'textAlign': 'center', 'color': '
            html.Div(children='Distra web application for sales data visualization and time series forecasting',
                     style={'textAlign': 'center', 'color': '
        ], style={'width': '33%', 'display': 'inline-block'}),
        html.Div(children=[
            html.H5(children='Enter a product name:'),
            html.Div(children=[
                dcc.Input(id='input-box', type='text', value='Article_32', style={'float': 'left'}),
                html.Button('Submit', id='button')
            ]),
            html.H5(children='Select a distribution channel:'),
            dcc.Dropdown(
                id='canal-id',
                options=[
                    {'label': 'Detail', 'value': 'Détail'},
                    {'label': 'Distributor', 'value': 'Distributeur'},
                    {'label': 'Wholesaler', 'value': 'Grossiste'},
                    {'label': '1/2 Wholesaler', 'value': '1/2 Gros'},
                    {'label': 'LMS', 'value': 'GMS'}
                ],
                value='Détail', style={'width': '91%'}
            ),
        ], style={'width': '27%', 'float': 'right'})
    ]),
    html.Div([
        html.Div([
            dcc.Graph(id='graph-1'),
            dcc.Graph(id='graph-2'),
        ], style={'width': '50%', 'float': 'left'}),
        html.Div([
            dcc.Graph(id='graph-3'),
            dcc.Graph(id='graph-4'),
            dcc.Slider(
                id='future-slider',
                min=1,
                max=7,
                step=1,
                marks={i: str(i) for i in range(1, 8)},
                value=5,
            )
        ], style={'width': '48%', 'float': 'right'})
    ])
])
@app.callback(
    Output('graph-1', 'figure'),
    [Input('button', 'n_clicks')],
    [State('canal-id', 'value'), State('input-box', 'value')]
)
def update_graph_1(n_clicks, canal_id, input_box):
    filtered_df = df.loc[(df['code_article'] == input_box) & (df['canal_principal'] == canal_id)]
    monthly_sales = filtered_df.groupby(['Order Date', 'code_article', 'canal_principal'])['CA_kMAD'].sum().reset_index()
    return {
        'data': [go.Scatter(x=monthly_sales['Order Date'], y=monthly_sales['CA_kMAD'])],
        'layout': {'title': 'Visualization of sales turnover per Month:',
                   'xaxis': {'title': 'Date'}, 'yaxis': {'title': 'Turnover'}}
    }
@app.callback(
    Output('graph-2', 'figure'),
    [Input('button', 'n_clicks')],
    [State('canal-id', 'value'), State('input-box', 'value')]
)
def update_graph_2(n_clicks, canal_id, input_box):
    filtered_df = df.loc[(df['code_article'] == input_box) & (df['canal_principal'] == canal_id)]
    daily_sales = filtered_df.groupby(['Order Date', 'code_article', 'canal_principal'])['CA_kMAD'].sum().reset_index()
    return {
        'data': [go.Scatter(x=daily_sales['Order Date'], y=daily_sales['CA_kMAD'], mode='lines')],
        'layout': {'title': 'Visualization of sales turnover per Day:',
                   'xaxis': {'title': 'Date'}, 'yaxis': {'title': 'Turnover'}}
    }
@app.callback(
    Output('graph-3', 'figure'),
    [Input('button', 'n_clicks')],
    [State('canal-id', 'value'), State('input-box', 'value')]
)
def update_graph_3(n_clicks, canal_id, input_box):
    filtered_df = df.loc[(df['code_article'] == input_box) & (df['canal_principal'] == canal_id)]
    daily_sales = filtered_df.groupby(['Order Date', 'code_article', 'canal_principal'])['CA_kMAD'].sum().reset_index()
    daily_sales = daily_sales.groupby('Order Date')['CA_kMAD'].sum().reset_index()
    daily_sales.set_index('Order Date', inplace=True)
    y = daily_sales['CA_kMAD'].resample('MS').sum()
    decomposition = sm.tsa.seasonal_decompose(y, model='additive')
    mod = sm.tsa.statespace.SARIMAX(y, order=(1, 1, 1), seasonal_order=(1, 0, 0, 12),
                                    enforce_stationarity=True, enforce_invertibility=True)
    results = mod.fit()
    pred = results.get_prediction(start=pd.to_datetime('2019-01-01'), dynamic=True)
    pred_ci = pred.conf_int()
    return {
        'data': [go.Scatter(x=y['2018':].index, y=y['2018':], name='Actual'),
                 go.Scatter(x=pred.predicted_mean.index, y=pred.predicted_mean, name='Predicted')],
        'layout': {'title': 'Sales turnover prediction per Month:',
                   'xaxis': {'title': 'Date'}, 'yaxis': {'title': 'Turnover'}}
    }
@app.callback(
    Output('graph-4', 'figure'),
    [Input('button', 'n_clicks'), Input('canal-id', 'value'), Input('future-slider', 'value')],
    [State('input-box', 'value')]
)
def update_graph_4(n_clicks, canal_id, future_slider, input_box):
    filtered_df = df.loc[(df['code_article'] == input_box) & (df['canal_principal'] == canal_id)]
    daily_sales = filtered_df.groupby(['Order Date', 'code_article', 'canal_principal'])['CA_kMAD'].sum().reset_index()
    daily_sales = daily_sales.groupby('Order Date')['CA_kMAD'].sum().reset_index()
    daily_sales.set_index('Order Date', inplace=True)
    y = daily_sales['CA_kMAD'].resample('MS').sum()
    mod = sm.tsa.statespace.SARIMAX(y, order=(1, 1, 1), seasonal_order=(1, 0, 0, 12),
                                    enforce_stationarity=True, enforce_invertibility=True)
    results = mod.fit()
    pred_uc = results.get_forecast(steps=future_slider)
    pred_ci = pred_uc.conf_int()
    return {
        'data': [go.Scatter(x=y.index, y=y, name='Actual'),
                 go.Scatter(x=pred_uc.predicted_mean.index, y=pred_uc.predicted_mean, name='Predicted')],
        'layout': {'title': 'Sales turnover future prediction per Month:',
                   'xaxis': {'title': 'Date'}, 'yaxis': {'title': 'Turnover'}}
    }
if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1', port=8050)