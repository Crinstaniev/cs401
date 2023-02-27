import dash
from dash import html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

app = dash.Dash(external_stylesheets=[dbc.themes.LUX])

load_figure_template('LUX')


app.layout = html.Div(children=[
    dbc.Row(dbc.Col(html.Div("Column 1 – width 12 by default"))),
    dbc.Row(
        [
            dbc.Col(html.Div("Column 1 – width 6 by default")),
            dbc.Col(html.Div("Column 2 – width 6 by default")),
        ]
    ),
], style={
    "margin-left": "7px",
    "margin-top": "7px"
})




if __name__ == "__main__":
    app.run_server()
