# Projet MI BOMBOOO

##Diagramme de cas d'utilisation

``` mermaid
usecase-beta
direction LR

actor Joueur("Joueur") 

systemBoundary "MI BOMBOOO" {
  usecase Deplacer("Déplacer")
  usecase Interagir("Interagir")
  usecase Combattre("Combattre")
  usecase Recuperer("Récupérer")
  usecase Fuir("Fuir")
}

Joueur --> Deplacer
Joueur --> Interagir
Joueur --> Combattre

Recuperer ..> Interagir : include
Fuir ..> Combattre : include
```

