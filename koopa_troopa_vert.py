import networkx as nx

def koopa_troopa_vert_state_graph():
    # Crée un graphe d'état
    state_graph = nx.MultiDiGraph()

    # Ajoute des nœuds pour chaque état
    state_graph.add_nodes_from([
        ("Début", {"color": "green"}), 
        ("Koopa Troopa Vert",  {"behavior": koopa_troopa_vert_behavior_graph_koopa_troopa_vert()}), 
        ("Carapace",  {"behavior": koopa_troopa_vert_behavior_graph_carapace()}), 
        ("Fin", {"color": "red"})
    ])

    # Ajoute des transitions entre les états
    state_graph.add_edges_from([
        ("Début", "Koopa Troopa Vert"),

        ("Koopa Troopa Vert", "Fin", {"condition": "Collision chute"}),
        ("Koopa Troopa Vert", "Fin", {"condition": "Collision boule de feu mario"}),
        ("Koopa Troopa Vert", "Fin", {"condition": "Collision étoile mario"}),

        ("Koopa Troopa Vert", "Carapace", {"condition": "Collision saut mario"}),
        ("Carapace", "Koopa Troopa Vert", {"condition": "Aprés X secondes"}),
        
        ("Carapace", "Fin", {"condition": "Collision mario"}),
        ("Carapace", "Fin", {"condition": "Collision boule de feu mario"})
        
    ])

    return state_graph

def koopa_troopa_vert_behavior_graph_koopa_troopa_vert():
    # Crée un sous-graphe pour le comportement
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

def koopa_troopa_vert_behavior_graph_carapace():
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