import random
import os

number = random.randint(0, 2)
possible = ["feuille", "pierre", "ciseaux"]
choice = possible[number]

print()
print("Bienvenue dans le jeu du pierre, feuille, ciseaux")
print()
print("Vous allez choisir votre action et je vous dirais ensuite le resultats")
print("Pour commencez, ecrivez: 'Pierre', 'Feuille' ou 'Ciseaux'")
print("Si vous voulez retourner au menu taper 'Back'")
print()

def demander_action():
    while True:
        # Demander à l'utilisateur son choix et le mettre en minuscules
        entree_utilisateur = input("Votre choix : ").lower()
        # Vérifier si le choix de l'utilisateur est valide
        if entree_utilisateur in ["pierre", "feuille", "ciseaux", "back"]:
            return entree_utilisateur  # Retourner le choix de l'utilisateur
        else:
            print("Ce n'est pas une entrée valide. Veuillez réessayer.")  # Message d'erreur

repertoire_script = os.path.dirname(os.path.abspath(__file__))
nom_fichier = "Menu_Jeu.py"
chemin_fichier = os.path.join(repertoire_script, nom_fichier)
                                    
while True:
    entree_utilisateur = demander_action()
   
    if entree_utilisateur == choice:
        print("Égalité ! Nous avons tous les deux choisi", choice)
        print("Maintenant écrivez 'Back' pour retourner au menu")

    elif (entree_utilisateur == "pierre" and choice == "ciseaux") or \
        (entree_utilisateur == "feuille" and choice == "pierre") or \
        (entree_utilisateur == "ciseaux" and choice == "feuille"):
        print("Vous avez gagné ! Vous avez choisi", entree_utilisateur, "et j'ai choisi", choice)
        print("Maintenant écrivez 'Back' pour retourner au menu")

    elif entree_utilisateur == "back":
        os.system(f"python \"{chemin_fichier}\"")

    else:
        print("Vous avez perdu ! Vous avez choisi", entree_utilisateur, "et j'ai choisi", choice)
        print("Maintenant écrivez 'Back' pour retourner au menu")

   