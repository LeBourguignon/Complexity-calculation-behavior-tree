from analyze_graph import analyze_state_graph

from goomba import goomba_state_graph
from piranha_plant import piranha_plant_state_graph
from koopa_troopa_vert import koopa_troopa_vert_state_graph
from koopa_paratroopa_vert import koopa_paratroopa_vert_state_graph

if __name__ == "__main__":
    main_graph = goomba_state_graph()
    print("Goomba :")
    analyze_state_graph(main_graph, True)

    main_graph = piranha_plant_state_graph()
    print("Piranha plant :")
    analyze_state_graph(main_graph, True)

    main_graph = koopa_troopa_vert_state_graph()
    print("Koopa troopa vert :")
    analyze_state_graph(main_graph, True)

    main_graph = koopa_paratroopa_vert_state_graph()
    print("Koopa paratroopa vert :")
    analyze_state_graph(main_graph, True)