import functions1
import show_network

import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output, State
import pandas as pd
course_df = pd.DataFrame(
    columns=[
        'department',  # 0
        'code',  # 1
        'level',  # 2
        'name',  # 3
        'Credit Hours',  #
        'Prerequisites',  #
        'Description',  #
    ]
)

import dash_table as dt



app = dash.Dash()
# application = app.server

app.layout = html.Div(
    children=[
        # html.H1(children='Hello Dash'),
        html.I(
            "enter department code   :"
        ),

        html.Div(),  # br
        dcc.Textarea(
            id='department',
            #value='this is where you specify department',
            value='CSC',
            style={'width': '50%', 'height': 30},
        ),
        html.Div(),  # br
        html.Div(id='textarea-example-output', style={'whiteSpace': 'pre-line'}),

        html.Div(
            [

                html.Button('Submit', id='submit_raw_text', n_clicks=0),
            ]
        ),

        html.Div(
            [
                dcc.Graph(id='example')  # or something other than Graph?...
            ],
        ),

        dcc.Slider(
            id='n_points',
            min=10,
            max=100,
            step=1,
            value=50,
        ),

        html.Div(id="table1")
    ]
)


@app.callback(
    Output('table1', 'children'),
    [Input('submit_raw_text', 'n_clicks')],
     [State('department', 'value')]
)
def update_output(n_clicks,  department_value):
    functions1.iniate_gv_file_from_txt_import_data_write_to_dataset_then_add_node_n_edge(department_value)


if __name__ == "__main__":
    app.run_server(debug=True)
