import random
import os

def demander_action():
    while True:
        # Demander à l'utilisateur son choix et le mettre en minuscules
        entree_utilisateur = input("Votre choix : ").lower()
        # Vérifier si le choix de l'utilisateur est valide
        if entree_utilisateur in ["pierre", "feuille", "ciseaux", "back"]:
            return entree_utilisateur  # Retourner le choix de l'utilisateur
        else:
            print("Ce n'est pas une entrée valide. Veuillez réessayer.")  # Message d'erreur

def demander_action2():
    while True:
        # Demander à l'utilisateur son choix et le mettre en minuscules
        entree_utilisateur = input("Votre choix : ").lower()
        # Vérifier si le choix de l'utilisateur est valide
        if entree_utilisateur in ["replay", "back"]:
            return entree_utilisateur  # Retourner le choix de l'utilisateur
        else:
            print("Ce n'est pas une entrée valide. Veuillez réessayer.")  # Message d'erreur

def demander_nombre(prompt='> ', min_val=1, max_val=3):
    try:
        # Tentez de convertir l'entrée en un nombre entier
        entree_utilisateur = int(input("Votre choix : "))
        return entree_utilisateur
        # Si la conversion est réussie, la boucle se termine

    except ValueError:
        # Si une exception ValueError est levée, cela signifie que l'entrée n'est pas un nombre
        print("Ce n'est pas un nombre valide. Veuillez réessayer.")
        return demander_nombre()
    
possible = ["feuille", "pierre", "ciseaux"]
repertoire_script = os.path.dirname(os.path.abspath(__file__)) # Detecter ou le fichier se trouve
nom_fichier = "Menu_Jeu.py" # Une simple variable ^^
chemin_fichier = os.path.join(repertoire_script, nom_fichier) # On remplace le nom du fichier actuel (pierre) par celui que l'on veut
nom_fichier2 = "Pierre.py"
chemin_fichier2 = os.path.join(repertoire_script, nom_fichier2)

win = 0
win_bot = 0

print()
print("Bienvenue dans le jeu du pierre, feuille, ciseaux")
print("Pour commencez, ecrivez le nombre de manches voulue")
print()
                                    
manche = demander_nombre()

print()
print(f"Vous aller jouer durant {manche} manche(s)")
print("Maintenant vous pouvez ecrire 'Pierre', 'Feuille', 'Ciseaux'")
print("Je vous dirais le resultat ensuite")
print()
print("Pour revenir au menu ecrivez 'Back'")

for i in range(manche):
    entree_utilisateur = demander_action()
    number = random.randint(0, 2)
    choice = possible[number]


    if entree_utilisateur == choice:
        print()
        print("Égalité ! Nous avons tous les deux choisi", choice)
        win = win + 0 # Sa sers a rien mais c'est pour mieux visualiser
        print(f"Il y'a {win} point(s) pour toi et {win_bot} point(s) pour moi !")
        print()


    elif (entree_utilisateur == "pierre" and choice == "ciseaux") or \
        (entree_utilisateur == "feuille" and choice == "pierre") or \
        (entree_utilisateur == "ciseaux" and choice == "feuille"):
        print()
        print("Vous avez gagné ! Vous avez choisi", entree_utilisateur, "et j'ai choisi", choice)
        win = win + 1 # On ajoute 1 au taux de win
        print(f"Il y'a {win} point(s) pour toi et {win_bot} point(s) pour moi !")
        print()


    elif entree_utilisateur == "back":
        os.system(f"python \"{chemin_fichier}\"") # On lance le menu

    else:
        print()
        print("Vous avez perdu ! Vous avez choisi", entree_utilisateur, "et j'ai choisi", choice)
        win_bot = win_bot + 1 # Sa sers a rien mais c'est pour mieux visualiser
        print(f"Il y'a {win} point(s) pour toi et {win_bot} point(s) pour moi !")
        print()

if win > win_bot:
    print()
    print(f"Vous avez gagner, vous avez {win} point(s) et moi {win_bot} point(s)")
    print("Maintenant ecrivez 'back' pour retourner au menu ou 'replay' pour rejouer")
    print()

elif win == win_bot:
    print()
    print(f"Egalité nous avons tout les deux {win} point(s)")
    print("Maintenant ecrivez 'back' pour retourner au menu ou 'replay' pour rejouer")
    print()

else:
    print()
    print(f"Vous avez perdu, J'ai {win_bot} point(s) et vous {win} point(s)")
    print("Maintenant ecrivez 'back' pour retourner au menu ou 'replay' pour rejouer")
    print()
    
while True:
    final_shot = demander_action2()
    
    if final_shot == "back":
        os.system(f"python \"{chemin_fichier}\"") # On lance le menu
    
    elif final_shot == "replay":
        os.system(f"python \"{chemin_fichier2}\"")

    




   