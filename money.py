import os
from deflist_money import demander_nombre_money1
from deflist_money import demander_nombre_money2
from deflist_money import demander_action_money
import time
import sys

repertoire_script = os.path.dirname(os.path.abspath(__file__))
nom_fichier1 = "Menu_Jeu.py"
chemin_fichier1 = os.path.join(repertoire_script, nom_fichier1)

nom_fichier2 = "money.py"
chemin_fichier2 = os.path.join(repertoire_script, nom_fichier2)

print()
print("Bienvenue dans le jeu de la monnaie")
print("Vous aller me donner un prix et une somme que vous donner au vendeur et il vous feras le rendu")
print()

prix = demander_nombre_money1()

print()
print(f"Votre prix est de: {prix}€")
print("Maintenant ecrivez la somme que vous donnez au vendeur")
print()

paiement = demander_nombre_money2()
print()
print(f"Vous avez donné(e): {paiement}€ au vendeur")
print()

def money(prix, paiement):

    if prix >= paiement:
        return 0
    
    rendu = {}
    difference = paiement - prix
    monnaie = [100, 50, 20, 10, 5, 2, 1]

    for m in monnaie:
        if difference // m >0:
            rendu[m] = difference //m
            difference = difference % m
    
    return rendu

give_it = money(prix, paiement)

def print_change(rendu):
    if rendu:  # Vérifie si le rendu de monnaie n'est pas vide
        print("Voici le rendu de monnaie :")
        for billet, quantite in rendu.items():
            print(f"{quantite} billet(s) de {billet}€")
    else:
        print("...")
        time.sleep(1.5)
        print("t'es serieux ?!")
        time.sleep(1.5)
        print("Sale voleur, je te donne pas l'article pour la peine...")
        time.sleep(1.5)
        print("Bye bye sale voleur !")
        time.sleep(1.5)
        sys.exit()

if give_it is not None:
    print_change(give_it)
elif give_it == 0:
    print("Pas de monnaie à rendre.")


time.sleep(1)

print()
print("Voulez vous rejouez ? (Oui/Non)")
print()

choix = demander_action_money()

if choix == "oui":
    os.system(f"python \"{chemin_fichier2}\"")

elif choix == "non": 
    os.system(f"python \"{chemin_fichier1}\"")
