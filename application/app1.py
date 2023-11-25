import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash import callback
from dash.dependencies import Input, Output, State
import pandas as pd

app = dash.Dash(__name__,  external_stylesheets=[dbc.themes.BOOTSTRAP]
                )

# app = Dash(__name__)

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output'),

])


@callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'

if __name__ == "__main__":
    # app.run_server(debug=True)
    app.run_server(debug=False, host='0.0.0.0', port = 8080)
    # app.run_server(debug=False, host='192.168.0.32', port = 8080)



