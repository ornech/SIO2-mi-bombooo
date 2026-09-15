# Projet MI BOMBOOO

## Diagramme de cas d'utilisation

```mermaid
graph LR
    actor Joueur

    subgraph MI BOMBOOO
        Deplacer[Déplacer]
        Interagir[Interagir]
        Combattre[Combattre]
        Recuperer[Récupérer]
        Fuir[Fuir]
    end

    Joueur --> Deplacer
    Joueur --> Interagir
    Joueur --> Combattre

    Recuperer -.->|include| Interagir
    Fuir -.->|include| Combattre
```
