import pickle
from graph_tool.all import *


with open('Analytics/nba_analytics/singleGameGraph.pkl', 'rb') as f1:
    gs = pickle.load(f1)

home_nodes = set()
for e in gs.transition_graph['home']['Edges']:
    home_nodes.update(set([e['From'],e['To']]))
vert_lookup = {n:i for (n,i) in zip(home_nodes, range(len(home_nodes)))}


hg = Graph()
edge_list = []
for e in gs.transition_graph['home']['Edges']:
    edge_list.append(hg.add_edge(vert_lookup[e['From']],
                                 vert_lookup[e['To']]))

hg.num_edges()
hg.num_vertices()

graph_draw(hg,
           vertex_text=hg.vertex_index,
           vertex_font_size=18,
           output_size=(2000, 2000),
           output="Analytics/nba_analytics/bball_graph_ex.png")
