import json
import threading
import time
from pprint import pprint

import dash
import dash_bootstrap_components as dbc
import pandas as pd
import redis
from dash import dcc, html
from dash_bootstrap_templates import load_figure_template
from utils.helper_functions import fetch_data_from_redis

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
r = redis.Redis(host='67.159.94.11', port=6379, db=0)

load_figure_template('bootstrap')

cpu_percent_history = None
cpu_percent_ma = None


def fetch():
    global r, cpu_percent_history, cpu_percent_ma
    data = fetch_data_from_redis(r)

    cpu_percent_history = pd.DataFrame(data['cpu_percent_history'], columns=[
        'cpu-{}'.format(i) for i in range(len(data['cpu_percent_history'][0]))])
    cpu_percent_ma = pd.DataFrame(data['cpu_percent_ma'], columns=[
        'cpu-{}'.format(i) for i in range(len(data['cpu_percent_ma'][0]))])

    time.sleep(4)


def fetch_task():
    while 1:
        fetch()


fetch()
task = threading.Thread(target=fetch_task)
task.start()

# make cpu graphs
cpu_graphs = []
for i in range(len(cpu_percent_history.columns)):
    cpu_graphs.append(
        dbc.Col(
            dcc.Graph(
                id='cpu-{}'.format(i),
                figure={
                    'data': [
                        {'x': cpu_percent_history.index, 'y': cpu_percent_history['cpu-{}'.format(
                            i)], 'type': 'line', 'name': 'Usage'},
                        {'x': cpu_percent_ma.index, 'y': cpu_percent_ma['cpu-{}'.format(
                            i)], 'type': 'line', 'name': 'MA'},
                    ],
                    'layout': {
                        'title': 'CPU-{}'.format(i),
                        'height': 250,
                        'xaxis': {'title': 'Time'},
                        'yaxis': {'title': 'percentage'},
                        'legend': {'orientation': 'h', 'yanchor': 'top'},
                        'margin': {'t': 30, 'b': 30, 'r': 30, 'l': 30},
                    },
                }
            )
        )
    )


# create a 3 rows, 5 columns grid from cpu_graphs, with no spacing between columns and rows.
cpu_graphs = [dbc.Row(cpu_graphs[0:5], className='g-4'),
              dbc.Row(cpu_graphs[5:10], className='g-4'),
              dbc.Row(cpu_graphs[10:15], className='g-4')]

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.H1("Dashboard", className="text-header")
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.H3("CPU History", className="text-header")
                )
            ]
        ),
        dbc.Row([
            dbc.Container(cpu_graphs)
        ]),
    ],
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(debug=True)
