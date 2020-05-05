import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

df = pd.read_csv('generated_csv/' +
                 'CSC' +
                 '.csv',encoding='unicode_escape')

print(df)

print(df.columns)

import plotly.graph_objects as go

import networkx as nx
from networkx.drawing.nx_pydot import read_dot

G = nx.DiGraph(read_dot('generated.gv'))
print(list(G.nodes))
print(len(G.nodes))

'''
for desc in df['Description']:
    print(desc)'''

print(len(df['Description']))
node_x = []
node_y = []
descriptions = []
for node in G.nodes():
    print(node, '\t' ,(str(df[df['code'] == node]['Description'])))


print('\t' ,(str(df[df['code'] == 'node']['Description'])))

