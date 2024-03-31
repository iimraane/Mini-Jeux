import random
import os
from deflist_pierre import demander_action2_pierre 
from deflist_pierre import demander_action_pierre
from deflist_pierre import demander_nombre_pierre

possible = ["feuille", "pierre", "ciseaux"]
repertoire_script = os.path.dirname(os.path.abspath(__file__)) # Detecter ou le fichier se trouve
nom_fichier = "Menu_Jeu.py" # Une simple variable ^^
chemin_fichier = os.path.join(repertoire_script, nom_fichier) # On remplace le nom du fichier actuel (pierre) par celui que l'on veut
nom_fichier2 = "Pierre.py"
chemin_fichier2 = os.path.join(repertoire_script, nom_fichier2)

points_user = 0
points_bot = 0

print()
print("Bienvenue dans le jeu du pierre, feuille, ciseaux")
print("Pour commencez, ecrivez le nombre de point(s) maximum voulu(s)")
print()
                                    
points_max = demander_nombre_pierre()

print()
print(f"Le premier arrivé a {points_max} point(s) gagne !")
print("Maintenant vous pouvez ecrire 'Pierre', 'Feuille', 'Ciseaux'")
print("Je vous dirais le resultat ensuite")
print()
print("Pour revenir au menu ecrivez 'Back'")

while True:
    entree_utilisateur = demander_action_pierre()
    number = random.randint(0, 2)
    choice = possible[number]


    if entree_utilisateur == choice:
        print()
        print("Égalité ! Nous avons tous les deux choisi", choice)
        points_user = points_user + 0 # Sa sers a rien mais c'est pour mieux visualiser
        print(f"Il y'a {points_user} point(s) pour toi et {points_bot} point(s) pour moi !")
        print()


    elif (entree_utilisateur == "pierre" and choice == "ciseaux") or \
        (entree_utilisateur == "feuille" and choice == "pierre") or \
        (entree_utilisateur == "ciseaux" and choice == "feuille"):
        print()
        print("Vous avez gagné ! Vous avez choisi", entree_utilisateur, "et j'ai choisi", choice)
        points_user = points_user + 1 # On ajoute 1 au taux de win de l'user
        print(f"Il y'a {points_user} point(s) pour toi et {points_bot} point(s) pour moi !")
        print()

    elif entree_utilisateur == "back":
        os.system(f"python \"{chemin_fichier}\"") # On lance le menu

    else:
        print()
        print("Vous avez perdu ! Vous avez choisi", entree_utilisateur, "et j'ai choisi", choice)
        points_bot = points_bot + 1 # on ajoute 1 win au bot
        print(f"Il y'a {points_user} point(s) pour toi et {points_bot} point(s) pour moi !")
        print()

    if points_bot == points_max or points_user == points_max:
        break  # Sortir de la boucle principale si l'un des joueurs atteint le score maximum

if points_user > points_bot:
    print()
    print(f"Vous avez gagner, vous avez {points_user} point(s) et moi {points_bot} point(s)")
    print("Maintenant ecrivez 'back' pour retourner au menu ou 'replay' pour rejouer")
    print()

else:
    print()
    print(f"Vous avez perdu, J'ai {points_bot} point(s) et vous {points_user} point(s)")
    print("Maintenant ecrivez 'back' pour retourner au menu ou 'replay' pour rejouer")
    print()

while True:
    final_shot = demander_action2_pierre()
    
    if final_shot == "back":
        os.system(f"python \"{chemin_fichier}\"") # On lance le menu
    
    elif final_shot == "replay":
        os.system(f"python \"{chemin_fichier2}\"")



   