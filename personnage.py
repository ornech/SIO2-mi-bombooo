class Personnage:
    def __init__(self, nom, pv):
        self.nom = nom
        self.pv = pv

    def attaque(self, cible, degats):
        cible.pv = max(0, cible.pv - degats)
