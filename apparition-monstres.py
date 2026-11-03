"""
apparition_monstres.py

Gère l'apparition aléatoire des monstres lorsque le joueur entre dans une pièce.

Fonctionnement :
- une seule probabilité d'apparition pour tout le château (ex : 30 %) ;
- si un monstre apparaît, il est tiré au hasard dans une liste globale,
  chaque monstre ayant la même chance d'être choisi ;
- la méthode verifier_apparition() renvoie un tuple (apparu, monstre)
  que l'UI peut utiliser directement.
"""

import copy
import random


class Monstre:
    """Version minimale d'un monstre.

    À remplacer (ou compléter) par la vraie classe Monstre du jeu
    quand elle sera développée.
    """

    def __init__(self, nom, points_de_vie, attaque):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.attaque = attaque

    def __str__(self):
        return f"{self.nom} (PV : {self.points_de_vie}, attaque : {self.attaque})"


class ApparitionMonstres:
    """Décide si un monstre apparaît quand le joueur entre dans une pièce."""

    def __init__(self, monstres_possibles, probabilite=0.3):
        """
        monstres_possibles : liste d'objets Monstre servant de modèles
        probabilite        : chance d'apparition, entre 0.0 (jamais) et 1.0 (toujours)
        """
        if not 0.0 <= probabilite <= 1.0:
            raise ValueError("La probabilité doit être comprise entre 0.0 et 1.0")

        self.monstres_possibles = monstres_possibles
        self.probabilite = probabilite

    def verifier_apparition(self):
        """À appeler à chaque fois que le joueur entre dans une pièce.

        Renvoie un tuple (apparu, monstre) :
        - (True, <Monstre>) si un monstre apparaît ;
        - (False, None) sinon.
        """
        # Pas de monstre si la liste est vide
        if not self.monstres_possibles:
            return False, None

        # random.random() renvoie un nombre entre 0.0 et 1.0 :
        # avec une probabilité de 0.3, il y a 30 % de chances qu'il soit inférieur.
        if random.random() >= self.probabilite:
            return False, None

        # Tirage équitable d'un monstre dans la liste
        modele = random.choice(self.monstres_possibles)

        # On renvoie une COPIE du modèle : ainsi, les dégâts subis pendant
        # un combat ne modifient pas le modèle, et le prochain monstre
        # du même type réapparaîtra avec tous ses points de vie.
        monstre = copy.copy(modele)
        return True, monstre


# --- Exemple d'utilisation (exécuté seulement si on lance ce fichier directement) ---
if __name__ == "__main__":
    liste_monstres = [
        Monstre("Squelette", 20, 4),
        Monstre("Rat géant", 10, 2),
        Monstre("Fantôme", 15, 5),
    ]

    apparition = ApparitionMonstres(liste_monstres, probabilite=0.3)

    # On simule 5 entrées dans une pièce
    for numero in range(1, 6):
        apparu, monstre = apparition.verifier_apparition()
        if apparu:
            print(f"Pièce {numero} : un {monstre.nom} surgit ! -> {monstre}")
        else:
            print(f"Pièce {numero} : la pièce est calme.")