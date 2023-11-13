import networkx as nx

def piranha_plant_state_graph():
    # Crée un graphe d'état
    state_graph = nx.MultiDiGraph()

    # Ajoute des nœuds pour chaque état
    state_graph.add_nodes_from([
        ("Début", {"color": "green"}), 
        ("Piranha Plant In",  {"behavior": piranha_plant_behavior_graph_piranha_plant()}), 
        ("Piranha Plant Out",  {"behavior": piranha_plant_behavior_graph_piranha_plant()}), 
        ("Fin", {"color": "red"})
    ])

    # Ajoute des transitions entre les états
    state_graph.add_edges_from([
        ("Début", "Piranha Plant In"),

        ("Piranha Plant In", "Piranha Plant Out", {"condition": "Après X secondes si mario n'est pas au-dessus"}),
        ("Piranha Plant Out", "Piranha Plant In", {"condition": "Après X secondes"}),

        ("Piranha Plant Out", "Fin", {"condition": "Collision boule de feu mario"}),
        ("Piranha Plant Out", "Fin", {"condition": "Collision étoile mario"})
    ])

    return state_graph

def piranha_plant_behavior_graph_piranha_plant():
    # Crée un sous-graphe pour le comportement
    behavior_graph = nx.MultiDiGraph()

    # Ajoute des nœuds pour chaque action
    behavior_graph.add_nodes_from([
        ("Début", {"color": "green"}), 
        ("Attendre")
    ])

    # Ajoute des transitions entre les actions
    behavior_graph.add_edges_from([
        ("Début", "Attendre"),
        ("Attendre", "Attendre")
    ])

    return behavior_graph