import networkx as nx
import matplotlib.pyplot as plt

from goomba import goomba_state_graph

def draw_graphs(graph, title="Graphe d'État Principal"):
    # Dessine le graphe principal
    draw_graph(graph, title)

    # Récupère les sous-graphes associés aux nœuds comportementaux
    child_nodes = [n for n, data in graph.nodes(data=True) if 'behavior' in data]
    for node in child_nodes:
        child_graph = graph.nodes[node]['behavior']
        if has_node_with_behavior(child_graph):
            draw_graphs(child_graph, f"Graphe d'État pour {node}")
        else:
            draw_graph(child_graph, f"Graphe de Comportement pour {node}")

def draw_graph(graph, title):
    pos = nx.spring_layout(graph)
    node_colors = [data.get('color', 'skyblue') for node, data in graph.nodes(data=True)]
    edge_labels = {(n1, n2): d.get('condition', '') for n1, n2, d in graph.edges(data=True)}

    nx.draw(graph, pos, with_labels=True, node_size=800, node_color=node_colors, font_weight='bold', font_size=8)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.title(title)
    print(f"Affichage du {title}")
    plt.show()

def has_node_with_behavior(graph):
    for node in graph.nodes():
        if 'behavior' in graph.nodes[node]:
            return True  # Dès qu'un nœud avec behavior est trouvé, retourne True
    return False  # Si aucun nœud avec behavior n'est trouvé, retourne False

if __name__ == "__main__":
    draw_graphs(goomba_state_graph())