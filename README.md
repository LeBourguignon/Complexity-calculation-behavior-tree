# Complexity calculation behavior tree

Programme en python permettant d'évaluer la complexité d'un arbre de comportement.

# Evaluation des ennemis dans Super Mario Bros.

## Goomba
```
Goomba :
        Analyse du graphe d'état :
                Ordre : 3
                Degré : 5
                Densité : 0.8333333333333334
                Rayon : 2
                Diamètre : 2
                Nombre d'états : 1
                Nombre de transitions : 4
                Ratio de transitions par état : 4.0
                Nombre de chemins : 4
                Longueur moyenne des chemins : 3.0
                Nombre de cycles : 0
                Longueur moyenne des cycles : 0
        Analyse des graphes de comportement des états :
                État : Goomba
                        Ordre : 3
                        Degré : 4
                        Densité : 0.6666666666666666
                        Rayon : 1
                        Diamètre : 1
                        Nombre d'actions : 2
                        Nombre de transitions : 3
                        Ratio de transitions par action : 1.5
                        Nombre de cycles : 2
                        Longueur moyenne des cycles : 1.5
                        Score de complexité de comportement : 3.0
Calcul du cumul des scores de complexité de comportement par chemin :
        Score cumulé : 12.0
        Score moyen : 3.0
Calcul du cumul des scores de complexité de comportement par cycle :
        Score cumulé : 0
        Score moyen : 0
Score de complexité du graphe d'état :
        Score : 1.5
```

## Piranha Plant
```
Piranha plant :
        Analyse du graphe d'état :
                Ordre : 4
                Degré : 5
                Densité : 0.4166666666666667
                Rayon : 2
                Diamètre : 3
                Nombre d'états : 2
                Nombre de transitions : 4
                Ratio de transitions par état : 2.0
                Nombre de chemins : 2
                Longueur moyenne des chemins : 4.0
                Nombre de cycles : 1
                Longueur moyenne des cycles : 2.0
        Analyse des graphes de comportement des états :
                État : Piranha Plant In
                        Ordre : 2
                        Degré : 2
                        Densité : 1.0
                        Rayon : 0
                        Diamètre : 0
                        Nombre d'actions : 1
                        Nombre de transitions : 1
                        Ratio de transitions par action : 1.0
                        Nombre de cycles : 1
                        Longueur moyenne des cycles : 1.0
                        Score de complexité de comportement : 1.0
                État : Piranha Plant Out
                        Ordre : 2
                        Degré : 2
                        Densité : 1.0
                        Rayon : 0
                        Diamètre : 0
                        Nombre d'actions : 1
                        Nombre de transitions : 1
                        Ratio de transitions par action : 1.0
                        Nombre de cycles : 1
                        Longueur moyenne des cycles : 1.0
                        Score de complexité de comportement : 1.0
Calcul du cumul des scores de complexité de comportement par chemin :
        Score cumulé : 4.0
        Score moyen : 2.0
Calcul du cumul des scores de complexité de comportement par cycle :
        Score cumulé : 2.0
        Score moyen : 2.0
Score de complexité du graphe d'état :
        Score : 1.0
```

## Koopa Troopa Vert
```
Koopa troopa vert :
        Analyse du graphe d'état :
                Ordre : 4
                Degré : 8
                Densité : 0.6666666666666666
                Rayon : 2
                Diamètre : 3
                Nombre d'états : 2
                Nombre de transitions : 7
                Ratio de transitions par état : 3.5
                Nombre de chemins : 5
                Longueur moyenne des chemins : 3.4
                Nombre de cycles : 1
                Longueur moyenne des cycles : 2.0
        Analyse des graphes de comportement des états :
                État : Koopa Troopa Vert
                        Ordre : 3
                        Degré : 4
                        Densité : 0.6666666666666666
                        Rayon : 1
                        Diamètre : 1
                        Nombre d'actions : 2
                        Nombre de transitions : 3
                        Ratio de transitions par action : 1.5
                        Nombre de cycles : 2
                        Longueur moyenne des cycles : 1.5
                        Score de complexité de comportement : 3.0
                État : Carapace
                        Ordre : 2
                        Degré : 2
                        Densité : 1.0
                        Rayon : 0
                        Diamètre : 0
                        Nombre d'actions : 1
                        Nombre de transitions : 1
                        Ratio de transitions par action : 1.0
                        Nombre de cycles : 1
                        Longueur moyenne des cycles : 1.0
                        Score de complexité de comportement : 1.0
Calcul du cumul des scores de complexité de comportement par chemin :
        Score cumulé : 17.0
        Score moyen : 3.4
Calcul du cumul des scores de complexité de comportement par cycle :
        Score cumulé : 4.0
        Score moyen : 4.0
Score de complexité du graphe d'état :
        Score : 1.75
```

## Koopa Paratroopa Vert
```
Koopa paratroopa vert :
        Analyse du graphe d'état :
                Ordre : 5
                Degré : 12
                Densité : 0.6
                Rayon : 2
                Diamètre : 4
                Nombre d'états : 3
                Nombre de transitions : 11
                Ratio de transitions par état : 3.6666666666666665
                Nombre de chemins : 8
                Longueur moyenne des chemins : 3.875
                Nombre de cycles : 1
                Longueur moyenne des cycles : 2.0
        Analyse des graphes de comportement des états :
                État : Koopa Paratroopa Vert
                        Ordre : 4
                        Degré : 6
                        Densité : 0.5
                        Rayon : 1
                        Diamètre : 2
                        Nombre d'actions : 3
                        Nombre de transitions : 5
                        Ratio de transitions par action : 1.6666666666666667
                        Nombre de cycles : 3
                        Score de complexité de comportement : 5.0      
                État : Koopa Troopa Vert
                        Ordre : 3
                        Degré : 4
                        Densité : 0.6666666666666666
                        Rayon : 1
                        Diamètre : 1
                        Nombre d'actions : 2
                        Nombre de transitions : 3
                        Ratio de transitions par action : 1.5
                        Nombre de cycles : 2
                        Longueur moyenne des cycles : 1.5
                        Score de complexité de comportement : 3.0      
                État : Carapace
                        Ordre : 2
                        Degré : 2
                        Densité : 1.0
                        Rayon : 0
                        Diamètre : 0
                        Nombre d'actions : 1
                        Nombre de transitions : 1
                        Ratio de transitions par action : 1.0
                        Nombre de cycles : 1
                        Longueur moyenne des cycles : 1.0
                        Score de complexité de comportement : 1.0      
Calcul du cumul des scores de complexité de comportement par chemin :  
        Score cumulé : 57.0
        Score moyen : 7.125
Calcul du cumul des scores de complexité de comportement par cycle :   
        Score cumulé : 4.0
        Score moyen : 4.0
Score de complexité du graphe d'état :
        Score : 3.388888888888889
```

# Auteurs

[Baptiste Andres](https://github.com/LeBourguignon)

[Benjamin Girod](https://github.com/Tebenj)
