# Projet MI BOMBOOO

## Diagramme de cas d'utilisation

```mermaid
graph LR
    %% Définition explicite de l'acteur avec un alias
    actor Joueur as J

    subgraph MI BOMBOOO
        Deplacer["Déplacer"]
        Interagir["Interagir"]
        Combattre["Combattre"]
        Recuperer["Récupérer"]
        Fuir["Fuir"]
    end

    %% Relations entre l'acteur et les cas d'utilisation
    J --> Deplacer
    J --> Interagir
    J --> Combattre

    %% Relations entre les cas d'utilisation (include)
    Recuperer -.->|include| Interagir
    Fuir -.->|include| Combattre
```
