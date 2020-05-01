import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

df = pd.read_csv('generated_csv/' +
                 'CSC' +
                 '.csv',encoding='unicode_escape')
pd.options.display.width = 1200
pd.options.display.max_colwidth = 1000
pd.options.display.max_columns = 100
print(str(df[df['code']=='CSC_4520']['Description']))

app = dash.Dash()

app.layout = html.Div(children=[
    # html.H1(children='Hello Dash'),

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

])


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
        descriptions.append(str(df[df['code']==node]['Description']))


    print(list(G.nodes))
    # Create a scatter plot to draw all the nodes.
    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers + text",  # Show both markers and labels
        text=list(G.nodes),  # The texts will be the labels of the nodes

        textposition="middle left",  # Place the text to the left of the node

        hovertext =list(descriptions),
        #hoverinfo= 'name',  # Tooltip will be from the "text" argument

        marker=dict(
            size=10,
            color="Red",
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


if __name__ == '__main__':
    app.run_server(debug=True)
