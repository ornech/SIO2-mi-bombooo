def choisir_porte():
    """
    Gère le Sprint 2 : Le choix des portes.
    Affiche les options, sécurise l'entrée utilisateur et retourne le choix effectué.
    """
    print("\n--- CHOIX DES PORTES ---")
    print("Vous vous trouvez face à un couloir sombre. Trois portes s'offrent à vous :")
    print("1. La porte en bois vermoulu")
    print("2. La porte en fer forgé")
    print("3. La porte mystérieuse gravée de runes")
    
    # Boucle de sécurité : tant que le joueur ne fait pas un choix valide, on redemande
    while True:
        choix = input("\nQuel est votre choix ? (Entrez 1, 2 ou 3) : ")
        
        # On vérifie si l'entrée correspond aux choix possibles
        if choix in ['1', '2', '3']:
            porte_choisie = int(choix)
            print(f"\n-> Vous poussez la porte numéro {porte_choisie}...")
            return porte_choisie  # Renvoie un entier (1, 2 ou 3) pour la suite
        else:
            print("❌ Choix invalide. Veuillez entrer uniquement 1, 2 ou 3.")

# C'est cette partie qui permet d'afficher le résultat du test dans ta console :
if __name__ == "__main__":
    resultat = choisir_porte()
    print(f"✅ Résultat affiché avec succès ! Valeur retournée : {resultat}")