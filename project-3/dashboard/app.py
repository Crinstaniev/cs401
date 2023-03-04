import dash
import dash_bootstrap_components as dbc
import pandas as pd
import redis
from dash import dcc, html
from utils.helper_functions import fetch_data_from_redis
from dash.dependencies import Input, Output
import plotly.graph_objects as go

app = dash.Dash(__name__)
r = redis.Redis(host='67.159.94.11', port=6379, db=0)

cpu_percent_history = None
cpu_percent_ma = None
cpu_freq = None


def fetch():
    global r, cpu_percent_history, cpu_percent_ma, cpu_freq
    data = fetch_data_from_redis(r)

    cpu_percent_history = pd.DataFrame(data['cpu_percent_history'], columns=[
        'cpu-{}'.format(i) for i in range(len(data['cpu_percent_history'][0]))])
    cpu_percent_ma = pd.DataFrame(data['cpu_percent_ma'], columns=[
        'cpu-{}'.format(i) for i in range(len(data['cpu_percent_ma'][0]))])
    cpu_freq = data['cpu_freq_current']


app.layout = dbc.Container(
    [
        dcc.Interval(
            id='interval-component',
            # interval=5*1000,  # in milliseconds
        ),
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
        dbc.Row(id='live-update-cpu-component'),
        dbc.Row([dbc.Col(html.H3("CPU Frequency", className="text-header"))]),
        dbc.Row(
            dcc.Graph(id='cpu-speed-meter', animate=True)
        )
    ],
    fluid=True,
)


@app.callback(
    Output('live-update-cpu-component', 'children'),
    Input('interval-component', 'n_intervals')
)
def update_cpu_graph(n):
    # make cpu graphs
    fetch()
    global cpu_percent_history, cpu_percent_ma
    cpu_graphs = []
    for i in range(len(cpu_percent_history.columns)):
        cpu_graphs.append(
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
                        'xaxis': {'title': 'Time'},
                        'yaxis': {'title': 'percentage'},
                        'height': 225,
                        'legend': {'orientation': 'h', 'yanchor': 'top'},
                        'margin': {'t': 30, 'b': 30, 'r': 30, 'l': 30},
                    },
                },
                style={'display': 'inline-block', 'width': '20%'},
            ),
        )

    # create a 3 rows, 5 columns grid from cpu_graphs
    cpu_grid = [dbc.Row(cpu_graphs[0:5], className='g-0'),
                dbc.Row(cpu_graphs[5:10], className='g-0'),
                dbc.Row(cpu_graphs[10:15], className='g-0')]

    return cpu_grid


# Define a callback function to update the gauge chart with the CPU frequency
@app.callback(
    dash.dependencies.Output('cpu-speed-meter', 'figure'),
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_gauge_chart(n):
    # Get the CPU frequency
    global cpu_freq
    freq = cpu_freq

    # Create the gauge chart
    fig = go.Figure(
        go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=freq,
            mode="gauge+number",
            title={'text': "CPU Frequency (MHz)"},
            gauge={
                'axis': {'range': [0, 4000]},
                'steps': [
                    {'range': [0, 1000], 'color': "lightgray"},
                    {'range': [1000, 2000], 'color': "gray"},
                    {'range': [2000, 3000], 'color': "lightgreen"},
                    {'range': [3000, 4000], 'color': "green"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 3900
                }
            }
        )
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
