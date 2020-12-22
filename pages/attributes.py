# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from os.path import abspath, dirname, join
from server import app


base_dir = dirname(dirname(abspath(__file__)))
data_path = 'data/cb_pb.csv'


def get_data():
    with open(join(base_dir, data_path), 'rb') as fp:
        df_to_load = pd.read_csv(fp, index_col=0)
        return df_to_load


df = get_data()


def layout():
    return html.Div([
        # html.H1(children='Scores of perfumes over claimed attributes'),
        # html.Div(children='''Scores of perfumes over claimed attributes'''),
        dcc.Dropdown(
            id='perfume-dropdown',
            options=[{'label': x, 'value': x} for x in df.index.unique()],
            value='My Burberry - Eau de Parfum'
        ),
        html.Div(id='dd-output-container'),
        html.Div([
            dcc.Graph(id='graph-attributes')
        ])
    ])

@app.callback(
    Output(component_id='graph-attributes', component_property='figure'),
    [Input(component_id="perfume-dropdown", component_property="value")]
)
def update_graph(my_dropdown):
    dfc = df.sort_values(by='perceived_benefit', ascending=False)
    traces = []
    for i in range(len(dfc)):
        if dfc.iloc[i].name == my_dropdown:
            trace_claimed = go.Bar(x=[dfc.iloc[i].values[0]], y=[dfc.iloc[i].values[2]],
                                   name= dfc.iloc[i].values[0] + ' Claimed')
            trace_perceived = go.Bar(x=[dfc.iloc[i].values[0]], y=[-dfc.iloc[i].values[1]],
                                     name= dfc.iloc[i].values[0] + 'Perceived')
            traces.append(trace_claimed)
            traces.append(trace_perceived)
    figure={
        'data': traces,
        'layout':
            go.Layout(title='Score des parfums sur les attributs', barmode='stack')
    }

    return figure



