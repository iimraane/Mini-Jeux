# En gros faut faire un menu pour le P, F, C et le c+ c-
import os
from def_list import demander_nombre_menu

repertoire_script = os.path.dirname(os.path.abspath(__file__))
nom_fichier1 = "Pierre.py"
chemin_fichier1 = os.path.join(repertoire_script, nom_fichier1)

nom_fichier2 = "import_random.py"
chemin_fichier2 = os.path.join(repertoire_script, nom_fichier2)
current_user = os.getlogin()

print()
print("Bienvenue dans le menu des jeu !")
print(f"A quoi voulez-vous jouer aujourd'hui, {current_user} ?")
print()
print("Pour jouer a 'Pierre, Feuille, Ciseaux' taper 1")
print("Pour jouer a 'C'est plus, C'est moins' taper 2")
print("Pour quitter tapez 3")
print()

while True:
    entree_utilisateur = demander_nombre_menu()

    if entree_utilisateur == 1:
        os.system(f"python \"{chemin_fichier1}\"")
    
    elif entree_utilisateur == 2:
        os.system(f"python \"{chemin_fichier2}\"")
    
    elif entree_utilisateur == 3:
         os.system(f"python \"{chemin_fichier1}\"")