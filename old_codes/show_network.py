import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
from dash.dependencies import State, Input, Output

import functions1



app = dash.Dash()

app.layout = html.Div(children=[
    # html.H1(children='Hello Dash'),

    # html.H1(children='Hello Dash'),
    html.I(
        "instruction: FIRST select department code, THEN, CLICK SUBMIT. if nothing happens, drag the slide under submit button to refresh page   :"
    ),

    html.Div(),  # br
    dcc.Dropdown(
        id='department',
        options=[
            {'label': 'ACCOUNTING', 'value': 'ACCT'},
            {'label': 'CHEMISTRY', 'value': 'CHEM'},
            {'label': 'PHYSICS', 'value': 'PHYS'},
            {'label': 'COMPUTER SCIENCE', 'value': 'CSC'},
            {'label': 'MATHMETHICS', 'value': 'MATH'},
            {'label': 'BIOLOGY', 'value': 'BIOL'}
        ],
        value='CSC'
    ),
    html.Div(),  # br
    html.Div(id='textarea-example-output', style={'whiteSpace': 'pre-line'}),

    html.Div(
        [

            html.Button('Submit', id='submit_raw_text', n_clicks=0),
        ]
    ),

    dcc.Slider(
        id='n_points',
        min=10,
        max=100,
        step=1,
        value=50,
    ),
    html.Div(
        [
            dcc.Graph(id='example')  # or something other than Graph?...
        ],
    ),


    html.Div(id="table1")
])



def add_br_to_long_string(long_string):
    character_index = 0
    formatted_string = ''
    how_many_lines = len(long_string) / 50
    long_string = long_string.replace('Name: Description, dtype: object', '')
    for i in range(0, int(how_many_lines) + 1):
        # print(i)
        formatted_string += long_string[(character_index + i * 4):(character_index + 4 * i + 50)] + '<br>'
        character_index += 46
    return formatted_string


'''
print(('If the index pos_i is very small (too negative), the insert string gets prepended. If too long, the insert string gets appended. If pos_i is between -len(string_s) and +len(string_s) - 1, the insert string gets inserted into the correct place.'))
print(add_br_to_long_string('If the index pos_i is very small (too negative), the insert string gets prepended. If too long, the insert string gets appended. If pos_i is between -len(string_s) and +len(string_s) - 1, the insert string gets inserted into the correct place.'))
'''

pd.options.display.max_colwidth = 500
df = pd.read_csv('old_generated_csv/' +
                 'CSC' 
                 '.csv', encoding='unicode_escape')
for description in df['Description']:
    description = add_br_to_long_string(str(description))

@app.callback(
    dash.dependencies.Output('example', 'figure'),
    [dash.dependencies.Input('n_points', 'value')]
)
def update_figure(n_points):
    # This example shows how to draw a NetworkX graph in Plotly.

    import plotly.graph_objects as go

    import networkx as nx
    from networkx.drawing.nx_pydot import read_dot

    G = nx.DiGraph(read_dot('generated.gv'))

    # pos = nx.nx_pydot.graphviz_layout(G)

    '''
    pos = nx.nx_pydot.pydot_layout(G, prog='neato')
    pos = nx.circular_layout(G)
    pos = nx.planar_layout(G)       #nice
    pos = nx.spiral_layout(G)       #nice
    '''
    pos = nx.nx_pydot.graphviz_layout(G, prog='dot')  # nice

    # Retrieve the coordinates of the nodes and store them
    # in two separate edge lists: one for X coordinates
    # and one for Y coordinates.
    edge_x = []
    edge_y = []
    for edge in G.edges():
        # Get the X and Y coordinates from pos.
        x0 = pos[edge[0]][0]
        y0 = pos[edge[0]][1]
        x1 = pos[edge[1]][0]
        y1 = pos[edge[1]][1]
        edge_x.append(x0)
        edge_x.append(x1)
        # Plotly will connect every node on the edge list in sequence.
        # Inserting a "None" node to prevent Plotly from connecting nodes
        # that should not be connected.
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    # Create a line plot to draw all the edges.
    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        mode='lines',
        line=dict(width=0.7))

    # Create a node list
    node_x = []
    node_y = []
    descriptions = []
    for node in G.nodes():
        # Saving node coordinates to the node list.
        x = pos[node][0]
        y = pos[node][1]
        node_x.append(x)
        node_y.append(y)
        descriptions.append(
            str(df[df['code'] == node]['name'].values)[2:-2] +
            '<br>Departement:' +
            str(df[df['code'] == node]['department'].values)[2:-2] +
            '<br>Code:' +
            str(node) +
            '<br>Credit Hour:' +
            str(df[df['code'] == node]['Credit Hours'].values)[2:-2] +
            '<br>Prerequistite:' +
            add_br_to_long_string(str(df[df['code'] == node]['Prerequisites'].values))[2:-2] +
            '<br>Description:<br>' +
            add_br_to_long_string(str(df[df['code'] == node]['Description'].values))[2:-2]
        )

    # print(list(G.nodes))

    # Create a scatter plot to draw all the nodes.
    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers+text",  # Show both markers and labels
        text=list(G.nodes),  # The texts will be the labels of the nodes

        textposition="middle left",  # Place the text to the left of the node

        hovertext=list(descriptions),
        hoverinfo='text',  # Tooltip will be from the "text" argument

        marker=dict(
            size=10,
            color="white",
            line_width=2)
    )

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        # title="A NetworkX Graph Rendered with Plotly",
                        titlefont_size=16,
                        showlegend=False,
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )
    fig.update_layout(
        autosize=False,
        width=1900,
        height=1000
    )
    return fig


@app.callback(
    Output('table1', 'children'),
    [Input('submit_raw_text', 'n_clicks')],
     [State('department', 'value')]
)
def update_output(n_clicks,  department_value):
    if n_clicks <1:
        functions1.iniate_gv_file_from_txt_import_data_write_to_dataset_then_add_node_n_edge(department_value)
    else:
        functions1.append_gv_file_from_txt_import_data_write_to_dataset_then_add_node_n_edge(department_value)


if __name__ == "__main__":
    app.run_server(debug=True)
