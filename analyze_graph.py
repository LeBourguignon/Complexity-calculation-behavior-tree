import networkx as nx

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

    # Calcul le nombre d'états
    num_states = graph.number_of_nodes() - 2 # -2 pour enlever les nœuds de début et de fin
    if debug : print(f"Nombre d'états : {num_states}")

    # Calcul du score de complexité de comportement pour chaque état
    if debug : print("Calcul du score de complexité de comportement pour chaque état :")
    for node in graph.nodes():
        if 'behavior' in graph.nodes[node]:
            behavior_graph = graph.nodes[node]['behavior']
            if debug : print(f"\tÉtat : {node}")

            # Calcul le nombre de nœuds
            num_nodes = behavior_graph.number_of_nodes() - 1 # -1 pour enlever le nœud de début
            if debug : print(f"\t\tNombre de nœuds : {num_nodes}")

            # Calcul le nombre de cycles
            cycles = list(nx.recursive_simple_cycles(behavior_graph))
            num_cycles = len(cycles)
            if debug : print(f"\t\tNombre de cycles : {num_cycles}")

            # Calcul la longueur moyen des cycles
            average_cycle_length = 0
            if num_cycles != 0 : average_cycle_length = sum([len(cycle) for cycle in cycles]) / num_cycles
            if debug : print(f"\t\tLongueur moyenne des cycles (score) : {average_cycle_length}")

            # Calcul le score de complexité de comportement
            graph.nodes[node]['score'] = average_cycle_length * num_nodes
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

    average_score_paths = 0
    if len(scores) != 0 : average_score_paths = sum(scores) / len(scores)
    if debug : print(f"\tScore moyen : {average_score_paths}")

    # Moyenne des sommes des scores de complexité de comportement par cycle
    if debug : print("Moyenne des sommes des scores de complexité de comportement par cycle :")
    cycles = list(nx.recursive_simple_cycles(graph))
    scores = []
    for cycle in cycles:
        score = 0
        for node in cycle:
            if 'score' in graph.nodes[node]:
                score += graph.nodes[node]['score']
        scores.append(score)

    average_score_cycles = 0
    if len(scores) != 0 : average_score_cycles = sum(scores) / len(scores)
    if debug : print(f"\tScore moyen : {average_score_cycles}")

    # Score de complexité du graphe d'état
    if debug : print("Score de complexité du graphe d'état :")
    # complexity_score = (average_score_paths + average_score_cycles) / 2
    # complexity_score = (average_score_paths + average_score_cycles) * num_states
    complexity_score = (average_score_paths + average_score_cycles) / 2 * num_states
    if debug : print(f"\tScore : {complexity_score}")

    return complexity_score


#################################################################

# Fonction permettant d'analyser un graphe d'état
def analyze_state_graph(graph, debug=False):
    if debug : print("\tAnalyse du graphe d'état :")

    ### Analyse généraliste d'un graphe ###
    # Calcul l'order du graphe d'état
    order = graph.order()
    if debug : print(f"\t\tOrdre : {order}")

    # Calcul le degré du graphe d'état
    degree = graph.size()
    if debug : print(f"\t\tDegré : {degree}")

    # Calcul la densité du graphe d'état
    density = nx.density(graph)
    if debug : print(f"\t\tDensité : {density}")

    # Calcul le rayon du graphe d'état
    graph_copy = graph.copy()
    graph_copy.add_edge('Fin', 'Début')
    radius = nx.radius(graph_copy)
    if debug : print(f"\t\tRayon : {radius}")

    # Calcul le diamètre du graphe d'état
    graph_copy = graph.copy()
    graph_copy.add_edge('Fin', 'Début')
    diameter = nx.diameter(graph_copy)
    if debug : print(f"\t\tDiamètre : {diameter}")


    ### Analyse du graphe d'état ###
    # Calcul le nombre d'états
    num_states = graph.number_of_nodes() - 2 # -2 pour enlever les nœuds de début et de fin
    if debug : print(f"\t\tNombre d'états : {num_states}")

    # Calcul le nombre de transitions
    num_transitions = graph.number_of_edges() - 1 # -1 pour enlever la transition de début
    if debug : print(f"\t\tNombre de transitions : {num_transitions}")

    # Calcul le ratio de transitions par état
    ratio_transitions = num_transitions / num_states
    if debug : print(f"\t\tRatio de transitions par état : {ratio_transitions}")

    # Calcul le nombre de chemins
    paths = find_all_paths(graph, 'Début', 'Fin')
    num_paths = len(paths)
    if debug : print(f"\t\tNombre de chemins : {num_paths}")

    # Calcul la longueur moyenne des chemins
    average_path_length = 0
    if num_paths != 0 : average_path_length = sum([len(path) for path in paths]) / num_paths
    if debug : print(f"\t\tLongueur moyenne des chemins : {average_path_length}")

    # Calcul le nombre de cycles
    cycles = list(nx.recursive_simple_cycles(graph))
    num_cycles = len(cycles)
    if debug : print(f"\t\tNombre de cycles : {num_cycles}")

    # Calcul la longueur moyenne des cycles
    average_cycle_length = 0
    if num_cycles != 0 : average_cycle_length = sum([len(cycle) for cycle in cycles]) / num_cycles
    if debug : print(f"\t\tLongueur moyenne des cycles : {average_cycle_length}")

    # Analyse des graphes de comportement des états
    if debug : print("\tAnalyse des graphes de comportement des états :")
    for node in graph.nodes():
        if 'behavior' in graph.nodes[node]:
            behavior_graph = graph.nodes[node]['behavior']
            if debug : print(f"\t\tÉtat : {node}")

            # Analyse le graphe de comportement
            analyze_behavior_graph(behavior_graph, debug)



# Fonction permettant d'analyser un graphe de comportement
def analyze_behavior_graph(graph, debug=False):

    ### Analyse généraliste d'un graphe ###
    # Calcul l'order du graphe de comportement
    order = graph.order()
    if debug : print(f"\t\t\tOrdre : {order}")

    # Calcul le degré du graphe de comportement
    degree = graph.size()
    if debug : print(f"\t\t\tDegré : {degree}")

    # Calcul la densité du graphe de comportement
    density = nx.density(graph)
    if debug : print(f"\t\t\tDensité : {density}")

    # Calcul le rayon du graphe de comportement
    graph_copy = graph.copy()
    graph_copy.remove_node('Début')
    radius = nx.radius(graph_copy)
    if debug : print(f"\t\t\tRayon : {radius}")

    # Calcul le diamètre du graphe de comportement
    graph_copy = graph.copy()
    graph_copy.remove_node('Début')
    diameter = nx.diameter(graph_copy)
    if debug : print(f"\t\t\tDiamètre : {diameter}")


    ### Analyse du graphe de comportement ###
    # Calcul le nombre d'action
    num_actions = graph.number_of_nodes() - 1 # -1 pour enlever le nœud de début
    if debug : print(f"\t\t\tNombre d'actions : {num_actions}")

    # Calcul le nombre de transitions
    num_transitions = graph.number_of_edges() - 1 # -1 pour enlever la transition de début
    if debug : print(f"\t\t\tNombre de transitions : {num_transitions}")

    # Calcul le ratio de transitions par action
    ratio_transitions = num_transitions / num_actions
    if debug : print(f"\t\t\tRatio de transitions par action : {ratio_transitions}")

    # Calcul le nombre de cycles
    cycles = list(nx.recursive_simple_cycles(graph))
    num_cycles = len(cycles)
    if debug : print(f"\t\t\tNombre de cycles : {num_cycles}")

    # Calcul la longueur moyenne des cycles
    average_cycle_length = 0
    if num_cycles != 0 : average_cycle_length = sum([len(cycle) for cycle in cycles]) / num_cycles
    if debug : print(f"\t\t\tLongueur moyenne des cycles : {average_cycle_length}")