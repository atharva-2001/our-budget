import flask
import dash
import dash_auth
import dash_core_components as dcc
from dash.dependencies import Input, State, Output
import dash_html_components as html
from dash_html_components.Div import Div
import dash_gif_component as Gif
import requests
import dash_bootstrap_components as dbc

from .config import username, password

external_stylesheets = [
    "https://codepen.io/chriddyp/pen/bWLwgP.css",
    dbc.themes.BOOTSTRAP,
]


app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
)

server = app.server

app.layout = html.Div([])


def run(host="127.0.0.1", debug=True):
    app.run_server(debug=debug, host=host, port=3004)


if __name__ == "__main__":
    run()
