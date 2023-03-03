import json
import threading
import time

import dash
import dash_bootstrap_components as dbc
import pandas as pd
import redis
from dash import dcc, html
from dash_bootstrap_templates import load_figure_template
from utils.helper_functions import fetch_data_from_redis

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
r = redis.Redis(host='67.159.94.11', port=6379, db=0)

load_figure_template('CYBORG')

data = fetch_data_from_redis(r)


def fetch_task():
    global r
    global data
    while 1:
        print('[INFO] Fetching data from redis...')
        data = fetch_data_from_redis(r)
        with open('data.json', 'w') as f:
            json.dump(data, f)
        time.sleep(1)


task = threading.Thread(target=fetch_task)
task.start()


cpu_percent_history = pd.DataFrame(data['cpu_percent_history'], columns=[
                                   'cpu-{}'.format(i) for i in range(len(data['cpu_percent_history'][0]))])
print(cpu_percent_history)
cpu_percent_ma = pd.DataFrame(data['cpu_percent_ma'], columns=[
                              'cpu-{}'.format(i) for i in range(len(data['cpu_percent_ma'][0]))])
print(cpu_percent_ma)

app.layout = dbc.Container(
    [
        dbc.Row([html.H1('Hello World')]),
        dbc.Row([
            dcc.Graph(id='example')
        ])
    ],
    fluid=True,
    className="dbc p-4 m-4"
)

if __name__ == "__main__":
    app.run_server()
