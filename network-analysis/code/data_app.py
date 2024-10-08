"""
Author: Mohit Mayank

Idea: Plot Game of Thrones network using Visdcc in Dash.
"""
# imports
import dash
import visdcc
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


# Ref  https://github.com/imohitmayank/got_network_viz_python
# create app
app = dash.Dash()


# load data
ProjDir = "E:/PythonProj/AI_DH/network-analysis/"
df = pd.read_csv(ProjDir + "data/gameofthrones-master/got-s1-edges.csv")
df = df.loc[df['Weight']>10, :]
node_list = list(set(df['Source'].unique().tolist() + df['Target'].unique().tolist()))
nodes = [{'id': node_name, 'label': node_name, 'shape': 'dot', 'size': 7} for i, node_name in enumerate(node_list)]
# create edges from df
edges = []
for row in df.to_dict(orient='records'):
    source, target = row['Source'], row['Target']
    edges.append({
        'id': source + "__" + target,
        'from': source,
        'to': target,
        'width': 2,
    })

# define layout
app.layout = html.Div([
      visdcc.Network(id = 'net',
                     data = {'nodes': nodes, 'edges': edges},
                     options = dict(height= '600px', width= '100%')),
      dcc.RadioItems(id = 'color',
                     options=[{'label': 'Red'  , 'value': '#ff0000'},
                              {'label': 'Green', 'value': '#00ff00'},
                              {'label': 'Blue' , 'value': '#0000ff'} ],
                     value='Red'  )
])

# define callback
@app.callback(
    Output('net', 'options'),
    [Input('color', 'value')])
def myfun(x):
    return {'nodes':{'color': x}}

# define main calling
if __name__ == '__main__':
    app.run_server(debug=True)
