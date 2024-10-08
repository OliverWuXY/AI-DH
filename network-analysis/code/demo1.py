import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# load data
ProjDir = "E:/PythonProj/AI_DH/network-analysis/"
df = pd.read_csv(ProjDir + "data/gameofthrones-master/got-s1-edges.csv")
orginalDf = df

# 数据表头
# Source,Target,Weight,Season
# pick only important weights (hard threshold)
df = df.loc[df['Weight']>20, :]
# print(df)


# load pandas df as networkx graph
G = nx.from_pandas_edgelist(df,
                            source='Source',
                            target='Target',
                            edge_attr='Weight')
print("Number of unique characters:", len(G.nodes))
print("Number of connections:", len(G.edges))

# # 可视化权利的游戏网络
# plt.figure(figsize=(10, 10))
# pos = nx.spring_layout(G)
#
# nx.draw(G, pos, with_labels=False, node_color="blue", node_size=700, font_size=15)
# nx.draw_networkx_edge_labels(G, pos, edge_labels=G.edges, font_color='red')
# plt.title("权利的游戏网络图")
# plt.show()


# https://github.com/imohitmayank/got_network_viz_python

# # all graph options
# graphs_viz_options = [nx.draw, nx.draw_networkx, nx.draw_circular, nx.draw_kamada_kawai, nx.draw_random, nx.draw_shell, nx.draw_spring]
#
# # plot graph option
# selected_graph_option = 3
#
# # plot
# plt.figure(figsize=(8,6), dpi=100)
# graphs_viz_options[selected_graph_option](G)
# plt.show()




# # https://pyvis.readthedocs.io/en/latest/
# # https://zhuanlan.zhihu.com/p/680750111
# # import pyvis
# from pyvis.network import Network
# # create vis network
# net = Network(notebook=True, width=1000, height=600)
# # load the networkx graph
# net.from_nx(G)
# net.show("pyvisExample.html",local=True)


# 教程 https://towardsdatascience.com/introducing-jaal-interacting-with-network-made-easy-124173bb4fa
# github：https://github.com/imohitmayank/jaal

from jaal import Jaal
# from jaal.datasets import load_got
# # load the data
# edge_df, node_df = load_got()
# init Jaal and run server
# Jaal(edge_df, node_df).plot()

edge_df = orginalDf
# print(edge_df.columns)
edge_df = edge_df.rename(columns={'Source': 'from','Target':'to'})
Jaal(edge_df).plot()
