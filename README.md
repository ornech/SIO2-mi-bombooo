# Projet MI BOMBOOO

## Diagramme de cas d'utilisation

```mermaid
graph LR
    Joueur["Joueur"]

## Diagramme de séquence 
![Uploading image.png…]()

    Joueur --> Deplacer
    Joueur --> Interagir
    Joueur --> Combattre

    Recuperer -.->|include| Interagir
    Fuir -.->|include| Combattre
```
