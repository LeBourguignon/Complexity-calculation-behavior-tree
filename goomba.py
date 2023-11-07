import networkx as nx

def goomba_state_graph():
    # Crée un graphe d'état
    state_graph = nx.MultiDiGraph()

    # Ajoute des nœuds pour chaque état
    state_graph.add_nodes_from([
        ("Début", {"color": "green"}), 
        ("Goomba",  {"behavior": goomba_behavior_graph_goomba()}), 
        ("Fin", {"color": "red"})
    ])

    # Ajoute des transitions entre les états
    state_graph.add_edges_from([
        ("Début", "Goomba"),
        ("Goomba", "Fin", {"condition": "Collision chute"}),
        ("Goomba", "Fin", {"condition": "Collision attaque mario"})
    ])

    return state_graph

def goomba_behavior_graph_goomba():
    # Crée un sous-graphe pour le comportement de Goomba
    behavior_graph = nx.MultiDiGraph()

    # Ajoute des nœuds pour chaque action
    behavior_graph.add_nodes_from([
        ("Début", {"color": "green"}), 
        ("Avancer"), 
        ("Se retourner")
    ])

    # Ajoute des transitions entre les actions
    behavior_graph.add_edges_from([
        ("Début", "Avancer"),
        ("Avancer", "Avancer"),
        ("Avancer", "Se retourner", {"condition": "Collision obstacle"}),
        ("Se retourner", "Avancer")
    ])

    return behavior_graph