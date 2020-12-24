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
import numpy as np

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

base_dir = dirname(dirname(abspath(__file__)))
data_path = 'data/similarity.csv'

def get_data():
    with open(join(base_dir, data_path), 'rb') as fp:
        df_to_load = pd.read_csv(fp, index_col=0)
        return df_to_load


df = get_data()


def layout():
    return html.Div([
        html.Div(id='test', children=''),
        html.Div(id='dd-output-container-similarity'),
        html.Div([
            dcc.Graph(id='graph-similarity')
        ])
    ])


@app.callback(
    Output(component_id='graph-similarity', component_property='figure'),
    [Input(component_id="test", component_property="children")]
)
def update_graph(my_dropdown):
    dfc = df.sort_values(by='similarity', ascending=False)
    traces = []
    for i in range(len(dfc)):
        if not np.isnan(dfc.iloc[i].values[0]):
            trace = go.Bar(x=[dfc.iloc[i].name], y=[dfc.iloc[i].values[0]], name=df.iloc[i].name)
            traces.append(trace)

    graph_layout = go.Layout(
        yaxis=dict(
            range = [.8, .95],
            showgrid=False,
            ticks='',
            showticklabels=False,
        )
    )

    figure = go.Figure(data=traces,
                       layout=graph_layout
                       )
    
    return figure


@app.callback(
    Output('click-data', 'children'),
    [Input('graph-similarity', 'clickData')])
def display_click_data(clickData):
    print("clickData in markets", clickData)

