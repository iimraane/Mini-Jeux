import random
import sys  # Importez le module sys
import os
number = random.randint(1, 1000)
repertoire_script = os.path.dirname(os.path.abspath(__file__))
nom_fichier = "Menu_Jeu.py"
chemin_fichier = os.path.join(repertoire_script, nom_fichier)

def demander_nombre(prompt='> ', min_val=1):
    try:
        # Tentez de convertir l'entrée en un nombre entier
        entree_utilisateur = int(input("Votre choix :"))
        return entree_utilisateur
        # Si la conversion est réussie, la boucle se termine
    
    except ValueError:
        # Si une exception ValueError est levée, cela signifie que l'entrée n'est pas un nombre
            print("Ce n'est pas un nombre valide. Veuillez réessayer.")
            return demander_nombre()

print("Bienvenue dans le jeu des nombres")
print()
print("Je vais choisir un nombre entre 1 et 1000, tu devras le trouver en utilisant les indices a ta disposition")
print("Entrez le nombre d'essais maximum souhaités ou '200484' pour revenir au menu principale")
print()

essais = demander_nombre()

if essais == 200484:
        os.system(f"python \"{chemin_fichier}\"")

while True: 

    if essais < 1:
        print("Ce n'est pas un nombre valide. Veuillez réessayer.")
        essais = demander_nombre()
    
    elif essais >= 1:
        break

essais_print = essais
print()
if essais == 1:
    print(f"Vous avez {essais} essai.")
else:
    print(f"Vous avez {essais} essais.")
print("Entrez un chiffre entre 1 et 1000 pour commencer")
print()

for i in range(0, essais): # Boucle infini
    
    guess = demander_nombre("Devinez le nombre: ")


    if guess == 190684: # Si l'input est 190684, donner le nombre choisis. (Pour debug)
     print(f"Le nombre est:", (number))
     pass

    elif guess == 160463:
     sys.exit() 


    elif guess < 0 or guess > 1000:
        print("Ce n'est pas un nombre valide. Veuillez réessayer.")
        print()
    elif guess < number:
        print("C'est plus !")
        essais_print -= 1
        print(f"Il vous reste {essais_print} essais.")
        print()
    elif guess > number:
        print("C'est moins !")
        essais_print -= 1
        print(f"Il vous reste {essais_print} essais.")
        print()
    

    else:
     print("C'est la bonne réponse !")
     print(f"Vous avez reussis en {essais - essais_print} essais !")
     print("Entrez ~160463~ pour terminer le jeu")
     break

if essais_print == 0:
    print("Vous n'avez plus d'essais !")
    print(f"Le nombre etait: {number}...")
