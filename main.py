import networkx as nx
import matplotlib.pyplot as plt

from goomba import goomba_state_graph



# Fonction pour dessiner les graphes
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



# Fonction pour trouver les tous les chemins entre deux nœuds en doublant pour les liens en double où chaque noeud apparait une seule fois dans le chemin
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]

    paths = []  # Liste des chemins
    for link in graph.out_edges(start):
        node = link[1]
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths



# Fonction pour calculer le score de complexité d'un graphe d'état
def calculate_complexity_score(graph, debug=False):

    # Calcul du score de complexité de comportement pour chaque état
    if debug : print("Calcul du score de complexité de comportement pour chaque état :")
    for node in graph.nodes():
        if 'behavior' in graph.nodes[node]:
            behavior_graph = graph.nodes[node]['behavior']
            if debug : print(f"\tÉtat : {node}")

            # Calcul le nombre de nœuds
            number_of_nodes = behavior_graph.number_of_nodes() - 1  # -1 pour enlever le nœud de début
            if debug : print(f"\t\tNombre de nœuds : {number_of_nodes}")

            # Calcul du degré moyen entrant
            in_degree = behavior_graph.in_degree()
            average_in_degree = sum(dict(in_degree).values()) / number_of_nodes
            if debug : print(f"\t\tDegré moyen entrant : {average_in_degree}")          

            # Calcul le nombre de cycles
            cycles = list(nx.simple_cycles(behavior_graph))
            num_cycles = len(cycles)
            if debug : print(f"\t\tNombre de cycles : {num_cycles}")

            graph.nodes[node]['score'] = average_in_degree * num_cycles
            if debug : print(f"\t\tScore : {graph.nodes[node]['score']}")

    # Moyenne des sommes des scores de complexité de comportement par chemin
    if debug : print("Moyenne des sommes des scores de complexité de comportement par chemin :")
    paths = find_all_paths(graph, 'Début', 'Fin')
    scores = []
    for path in paths:
        score = 0
        for node in path:
            if 'score' in graph.nodes[node]:
                score += graph.nodes[node]['score']
        scores.append(score)
        if debug : print(f"\tChemin : {path}")
        if debug : print(f"\t\tScore : {score}")

    average_score_paths = 0
    if len(scores) != 0 : average_score_paths = sum(scores) / len(scores)
    if debug : print(f"\tScore moyen : {average_score_paths}")

    # Moyenne des sommes des scores de complexité de comportement par cycle
    if debug : print("Moyenne des sommes des scores de complexité de comportement par cycle :")
    cycles = list(nx.simple_cycles(graph))
    scores = []
    for cycle in cycles:
        score = 0
        for node in cycle:
            if 'score' in graph.nodes[node]:
                score += graph.nodes[node]['score']
        scores.append(score)
        if debug : print(f"\tCycle : {cycle}")
        if debug : print(f"\t\tScore : {score}")

    average_score_cycles = 0
    if len(scores) != 0 : average_score_cycles = sum(scores) / len(scores)
    if debug : print(f"\tScore moyen : {average_score_cycles}")

    # Score de complexité du graphe d'état
    if debug : print("Score de complexité du graphe d'état :")
    complexity_score = (average_score_paths + average_score_cycles) * (graph.number_of_nodes() - 2) # -2 pour enlever les nœuds de début et de fin
    if debug : print(f"\tScore : {complexity_score}")

    return complexity_score



if __name__ == "__main__":
    # draw_graphs(goomba_state_graph())

    main_graph = goomba_state_graph()
    calculate_complexity_score(main_graph, True)