import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# load data
ProjDir = "E:/PythonProj/AI_DH/network-analysis/"
df = pd.read_csv(ProjDir + "data/gameofthrones-master/got-s1-edges.csv")
orginalDf = df

print(df.head)
print(df.columns)
# 数据表头
# Source,Target,Weight,Season
# pick only important weights (hard threshold)
df = df.loc[df['Weight']>10, :]
# print(df)


# load pandas df as networkx graph
G = nx.from_pandas_edgelist(df,
                            source='Source',
                            target='Target',
                            edge_attr='Weight')
# print("Number of unique characters:", len(G.nodes))
# print("Number of connections:", len(G.edges))
#
# # 度中心性
# # 度中心性是衡量网络中节点重要性的指标。它只是连接到节点的边的数量，由节点的最大可能度标准化。
# degree_centrality = nx.degree_centrality(G)
# print(degree_centrality)
#
# # 最短路径
# # 寻找两个节点之间的最短路径是图论中常见的问题。NetworkX 提供了几个用于计算最短路径的函数，例如 shortest_path() 和 shortest_path_length()：
# path = nx.shortest_path(G, source="LYSA", target="JEOR")
# length = nx.shortest_path_length(G, source="LYSA", target="LYSA")
# print(f"Shortest path: {path}, Length: {length}")
#
# # 聚类系数
# # 聚类系数是衡量图中节点形成簇或紧密结合的组的趋势的指标。它是连接到节点的三角形数量与可能连接到该节点的三角形数量的比率。可以使用
# # clustering()
# # 函数计算图中所有节点的聚类系数：
#
# clustering_coefficient = nx.clustering(G)
# print(clustering_coefficient)
#
# # 社区检测
# # 社区检测是在图中查找节点组的过程，这些节点组之间的连接比与网络其他部分的连接更紧密。NetworkX 提供了几种社区检测算法，例如 Louvain 方法和 Girvan-Newman 方法
# from networkx.algorithms import community
# communities = list(community.greedy_modularity_communities(G))
# print("There are {} communities.".format(len(communities) ))
# print(communities)

# # networkx可视化权利的游戏网络
# # 可视化权利的游戏网络
# plt.figure(figsize=(10, 10))
# pos = nx.spring_layout(G)
#
# nx.draw(G, pos, with_labels=False, node_color="blue", node_size=700, font_size=15)
# nx.draw_networkx_edge_labels(G, pos, edge_labels=G.edges, font_color='red')
# plt.title("权利的游戏网络图")
# plt.show()


# # # https://github.com/imohitmayank/got_network_viz_python
# #
# # # all graph options
# graphs_viz_options = [nx.draw, nx.draw_networkx, nx.draw_circular, nx.draw_kamada_kawai, nx.draw_random, nx.draw_shell, nx.draw_spring]
# #
# # plot graph option
# selected_graph_option = 3
# # plot
# plt.figure(figsize=(8,6), dpi=100)
# graphs_viz_options[selected_graph_option](G)
# plt.show()




# # https://pyvis.readthedocs.io/en/latest/
# # https://zhuanlan.zhihu.com/p/680750111
# import pyvis
# from pyvis.network import Network
# # create vis network
# net = Network(notebook=True, width=1000, height=600)
# # load the networkx graph
# net.from_nx(G)
# net.show("pyvisExample111.html",local=True)


# 教程 https://towardsdatascience.com/introducing-jaal-interacting-with-network-made-easy-124173bb4fa
# github：https://github.com/imohitmayank/jaal

from jaal import Jaal
from jaal.datasets import load_got
# # load the data
# edge_df, node_df = load_got()
# # init Jaal and run server
# Jaal(edge_df, node_df).plot()

edge_df = orginalDf
# print(edge_df.columns)
edge_df = edge_df.rename(columns={'Source': 'from','Target':'to'})
Jaal(edge_df).plot()
