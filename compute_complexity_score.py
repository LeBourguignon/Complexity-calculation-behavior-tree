import networkx as nx

from analyze_graph import find_all_paths

# Premiere fonction permettant de calculer le score de complexité de compréhension d'un ennemi
def compute_complexity_score_1(graph, debug=False):

    # Calcul des scores de complexité de comportement des états
    if debug : print("\tCalcul des scores de complexité de comportement des états :")
    for node in graph.nodes():
        if 'behavior' in graph.nodes[node]:
            behavior_graph = graph.nodes[node]['behavior']
            if debug : print(f"\t\tÉtat : {node}")

            # Calcul le nombre de cycles
            cycles = list(nx.recursive_simple_cycles(behavior_graph))
            num_cycles = len(cycles)
            if debug : print(f"\t\t\tNombre de cycles : {num_cycles}")

            # Calcul la longueur moyenne des cycles
            average_cycle_length = 0
            if num_cycles != 0 : average_cycle_length = sum([len(cycle) for cycle in cycles]) / num_cycles
            if debug : print(f"\t\t\tLongueur moyenne des cycles : {average_cycle_length}")

            ### Calcul le score de complexité de comportement ###
            graph.nodes[node]['score'] = num_cycles * average_cycle_length
            if debug : print(f"\t\t\tScore de complexité de comportement : {graph.nodes[node]['score']}")

    # Calcul le nombre de chemins
    paths = find_all_paths(graph, 'Début', 'Fin')
    num_paths = len(paths)
    if debug : print(f"\tNombre de chemins : {num_paths}")

    # Calcul le nombre de cycles
    cycles = list(nx.recursive_simple_cycles(graph))
    num_cycles = len(cycles)
    if debug : print(f"\tNombre de cycles : {num_cycles}")

    # Calcul du cumul des scores de complexité de comportement par chemin  
    if debug : print("\tCalcul du cumul des scores de complexité de comportement par chemin :")
    cumul_score_paths = 0
    for path in paths:
        score = 0
        for node in path:
            if 'score' in graph.nodes[node]:
                score += graph.nodes[node]['score']
        cumul_score_paths += score

    if debug : print(f"\t\tScore cumulé : {cumul_score_paths}")

    # Calcul du cumul des scores de complexité de comportement par cycle
    if debug : print("\tCalcul du cumul des scores de complexité de comportement par cycle :")
    cumul_score_cycles = 0
    for cycle in cycles:
        score = 0
        for node in cycle:
            if 'score' in graph.nodes[node]:
                score += graph.nodes[node]['score']
        cumul_score_cycles += score

    if debug : print(f"\t\tScore cumulé : {cumul_score_cycles}")

    # Score de complexité du graphe d'état
    if debug : print("\tScore de complexité du graphe d'état :")
    complexity_score = (cumul_score_paths + cumul_score_cycles) / (num_paths + num_cycles)
    if debug : print(f"\t\tScore : {complexity_score}")

    return complexity_score


# Deuxieme fonction permettant de calculer le score de complexité de compréhension d'un ennemi
def compute_complexity_score_2(graph, debug=False):

    # Calcul des scores de complexité de comportement des états
    if debug : print("\tCalcul des scores de complexité de comportement des états :")
    for node in graph.nodes():
        if 'behavior' in graph.nodes[node]:
            behavior_graph = graph.nodes[node]['behavior']
            if debug : print(f"\t\tÉtat : {node}")

            # Calcul la complexité cyclomatique du graphe de comportement
            graph_copy = behavior_graph.copy()
            graph_copy.remove_node('Début')
            num_connected_components = nx.number_strongly_connected_components(graph_copy)
            cyclomatic_complexity = graph_copy.size() - graph_copy.order() + num_connected_components
            if debug : print(f"\t\t\tComplexité cyclomatique : {cyclomatic_complexity}")

            ### Calcul le score de complexité de comportement ###
            graph.nodes[node]['score'] = cyclomatic_complexity

    # Calcul la complexité cyclomatique du graphe d'état
    graph_copy = graph.copy()
    graph_copy.add_edge('Fin', 'Début')
    num_connected_components = nx.number_strongly_connected_components(graph_copy)
    cyclomatic_complexity = graph_copy.size() - graph_copy.order() + num_connected_components
    if debug : print(f"\tComplexité cyclomatique : {cyclomatic_complexity}")

    # Calcul le nombre de chemins
    paths = find_all_paths(graph, 'Début', 'Fin')
    num_paths = len(paths)
    if debug : print(f"\tNombre de chemins : {num_paths}")

    # Calcul le nombre de cycles
    cycles = list(nx.recursive_simple_cycles(graph))
    num_cycles = len(cycles)
    if debug : print(f"\tNombre de cycles : {num_cycles}")

    # Calcul du cumul des scores de complexité de comportement par chemin  
    if debug : print("\tCalcul du cumul des scores de complexité de comportement par chemin :")
    cumul_score_paths = 0
    for path in paths:
        score = 0
        for node in path:
            if 'score' in graph.nodes[node]:
                score += graph.nodes[node]['score']
        cumul_score_paths += score

    if debug : print(f"\t\tScore cumulé : {cumul_score_paths}")

    # Calcul du cumul des scores de complexité de comportement par cycle
    if debug : print("\tCalcul du cumul des scores de complexité de comportement par cycle :")
    cumul_score_cycles = 0
    for cycle in cycles:
        score = 0
        for node in cycle:
            if 'score' in graph.nodes[node]:
                score += graph.nodes[node]['score']
        cumul_score_cycles += score

    if debug : print(f"\t\tScore cumulé : {cumul_score_cycles}")

    # Score de complexité du graphe d'état
    if debug : print("\tScore de complexité du graphe d'état :")
    complexity_score = (cumul_score_paths + cumul_score_cycles) / (num_paths + num_cycles) + cyclomatic_complexity
    if debug : print(f"\t\tScore : {complexity_score}")

    return complexity_score