def demander_nombre_random(prompt='> ', min_val=1):
    try:
        # Tentez de convertir l'entrée en un nombre entier
        entree_utilisateur = int(input("Votre choix :"))
        return entree_utilisateur
        # Si la conversion est réussie, la boucle se termine
    
    except ValueError:
        # Si une exception ValueError est levée, cela signifie que l'entrée n'est pas un nombre
            print("Ce n'est pas un nombre valide. Veuillez réessayer.")
            return demander_nombre_random()
    
def demander_action_random():
    """Demander à l'utilisateur s'il veut rejouer ou revenir au menu."""
    while True:
        # Demander à l'utilisateur son choix et le mettre en minuscules
        entree_utilisateur = input("Votre choix: ").lower()
        # Vérifier si le choix de l'utilisateur est valide
        if entree_utilisateur in ["oui", "non"]:
            return entree_utilisateur  # Retourner le choix de l'utilisateur
        else:
            print("Ce n'est pas une entrée valide. Veuillez réessayer.")  # Message d'erreur
