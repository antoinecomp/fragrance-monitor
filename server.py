from flask import Flask
from dash import Dash
#import dash_auth

server = Flask('dashboard')

app = Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width"}],
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
)

app.config['suppress_callback_exceptions'] = True